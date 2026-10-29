#!/usr/bin/env python3
"""plate의 편집 훅. Claude Code의 PreToolUse(Edit|Write|MultiEdit|NotebookEdit)에서 돈다.

막는 실패: 남은 phase가 있는 task 없이 코드를 고치는 것, 테스트 먼저인 phase에서
실패하는 테스트 없이 구현부터 하는 것. 막을 때는 종료 코드 2로 끝나고 stderr의 글이
에이전트에게 간다. 파일 편집 도구의 호출만 보고 Bash 명령은 보지 않는다.
"""

import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

DOCS_MAP_START = "<!-- plate:docs-map:start -->"
TASKS_DIR = "docs/tasks"
TEST_DIRS = {"tests", "test", "__tests__"}
TEST_NAMES = ("test_*", "*_test.*", "*.test.*", "*.spec.*")
MARKER = re.compile(r"^\*\*테스트 먼저\*\*:\s*(.*)$")
PHASE_FILE = re.compile(r"^phase-(\d+)\.md$")
CHECK_SECTION = re.compile(r"^## 확인 \d+\s*$")  # 확인하는 쪽이 phase 파일 끝에 더하는 절
FENCE = re.compile(r"^\s*(```|~~~)")
CI_WORKFLOW = ".github/workflows/plate-review.yml"  # setup이 쓰는 CI 워크플로
CODEOWNERS = ".github/CODEOWNERS"  # setup이 쓰는 코드 소유자 파일
SETUP_FILES = (CI_WORKFLOW, CODEOWNERS)  # setup이 처음 쓸 때 막지 않는 파일
COUNT_FILE = "plate-test-first.json"  # git 폴더 안에 둔다. 작업 트리에 변경을 만들지 않는다
STOP_COUNT = 3  # 같은 파일을 테스트 먼저 때문에 이만큼 막으면 STOP의 글을 낸다

PLAN_FIRST = (
    "plate: 남은 phase가 있는 task가 없어서 코드 파일을 고치지 않는다: `{rel}`\n"
    "계획부터 세운다. plate의 plan 스킬(`plate:plan`)로 계획을 세우고, "
    "plate의 run 스킬(`plate:run`)로 실행한다.\n"
)
TEST_FIRST = (
    "plate: 지금 phase(`{phase}`)는 테스트 먼저다. 커밋되지 않은 변경에 테스트 파일이 없어서 "
    "테스트 파일이 아닌 코드 파일을 고치지 않는다: `{rel}`\n"
    "실패하는 테스트부터 쓴다. 테스트를 돌려 실패 출력을 기록에 남기고, 그 뒤에 구현한다.\n"
    "테스트 파일은 " + ", ".join("`%s/`" % d for d in sorted(TEST_DIRS)) + " 아래이거나 이름이 "
    + ", ".join("`%s`" % n for n in TEST_NAMES) + " 꼴인 파일이다.\n"
)
ORDINALS = ("첫", "두", "세", "네", "다섯", "여섯", "일곱", "여덟", "아홉", "열")


def ordinal(n):
    """`n`번째를 글로 적는다(3 → `세 번째`). 열을 넘으면 숫자로 적는다."""
    return "%s 번째" % (ORDINALS[n - 1] if 1 <= n <= len(ORDINALS) else n)


STOP = (
    "plate: 테스트 먼저 때문에 같은 파일을 " + ordinal(STOP_COUNT) + " 막았다: `{rel}` (지금 phase: `{phase}`)\n"
    "더 시도하지 않는다. 상태를 막힘으로 하고 멈춘다. 막힌 까닭과 원하는 해결책을 "
    "`{phase}`의 \"남은 것\"과 \"하네스에서 걸린 것\"에 적는다.\n"
)


def git(root, *args):
    done = subprocess.run(
        ["git", "-C", root, *args], capture_output=True, text=True,
        encoding="utf-8", errors="replace",
    )
    return done.stdout if done.returncode == 0 else None


def is_code_file(rel):
    return (
        not rel.lower().endswith(".md")
        and not rel.startswith(TASKS_DIR + "/")
    )


def is_test_file(rel):
    parts = rel.split("/")
    if TEST_DIRS.intersection(parts[:-1]):
        return True
    return any(fnmatch.fnmatchcase(parts[-1], name) for name in TEST_NAMES)


def is_bytecode(rel):
    """테스트를 돌리기만 해도 생기는 Python 파일. 테스트 변경으로 세지 않는다."""
    return "__pycache__" in rel.split("/") or rel.endswith(".pyc")


def is_setup(root):
    try:
        with open(os.path.join(root, "AGENTS.md"), encoding="utf-8") as f:
            return DOCS_MAP_START in f.read()
    except OSError:
        return False


def unfinished_tasks(root):
    """끝나지 않은 task의 폴더 이름마다 남은 phase(`phase-N.md`)의 번호를 작은 것부터 돌려준다.
    `done-phase-N.md`만 있는 task는 끝난 task다."""
    tasks = {}
    base = os.path.join(root, TASKS_DIR)
    try:
        names = os.listdir(base)
    except OSError:
        return tasks
    for name in names:
        try:
            files = os.listdir(os.path.join(base, name))
        except OSError:
            continue
        numbers = sorted(int(m.group(1)) for m in map(PHASE_FILE.match, files) if m)
        if numbers:
            tasks[name] = numbers
    return tasks


def task_number(name):
    m = re.match(r"\d+", name)
    return (int(m.group()) if m else float("inf"), name)


def current_task(tasks):
    """끝나지 않은 task 가운데 번호가 가장 작은 것."""
    return min(tasks, key=task_number)


def plan_lines(text):
    """phase 파일에서 기록 절(`## `로 시작하는 절) 위의 계획 줄."""
    lines = []
    for line in text.splitlines():
        if line.startswith("## "):
            break
        lines.append(line)
    return lines


def is_test_first(lines):
    for line in lines:
        m = MARKER.match(line)
        if m:
            return m.group(1).startswith("예")
    return False


def has_check_section(text):
    """phase 파일에 코드 블록 밖의 확인 절(`## 확인 N`)이 있으면 고칠 문제를 받은 다시 수행이다."""
    fenced = False
    for line in text.splitlines():
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced and CHECK_SECTION.match(line):
            return True
    return False


def phase_commit_has_test_change(root, task, number):
    """이번 tasks에서 제목이 `NNN-slug: phase N`인 커밋이 테스트 파일을 더하거나 바꿨는가.
    지우기만 한 것은 세지 않는다.

    tasks가 끝나면 `docs/tasks/`를 비우고 다음 tasks가 같은 task 이름을 다시 쓰므로, 그 task 머리
    (`plan.md`)를 마지막으로 더한 커밋(이번 tasks의 계획 커밋) 뒤의 커밋만 본다."""
    subject = "%s: phase %d" % (task, number)
    plan = "/".join([TASKS_DIR, task, "plan.md"])
    added = (git(root, "log", "-1", "--diff-filter=A", "--format=%H", "--", plan) or "").strip()
    if not added:
        return False
    log = git(root, "log", "--format=%H %s", added + "..HEAD") or ""
    for line in log.splitlines():
        sha, _, title = line.partition(" ")
        if title != subject:
            continue
        files = git(root, "diff-tree", "--root", "--no-commit-id", "-r", "-z", "--name-only",
                    "--diff-filter=d", sha) or ""
        if any(is_code_file(f) and is_test_file(f) and not is_bytecode(f)
               for f in files.split("\0") if f):
            return True
    return False


def has_tests(root):
    files = git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard") or ""
    if any(is_code_file(f) and is_test_file(f) for f in files.split("\0") if f):
        return True
    return manifest_has_test_command(root)


def manifest_has_test_command(root):
    try:
        with open(os.path.join(root, "package.json"), encoding="utf-8") as f:
            script = json.load(f).get("scripts", {}).get("test")
        if isinstance(script, str) and "no test specified" not in script:
            return True
    except Exception:
        pass
    for name in ("Makefile", "makefile", "GNUmakefile"):
        try:
            with open(os.path.join(root, name), encoding="utf-8") as f:
                if re.search(r"^test\s*:(?!=)", f.read(), re.M):
                    return True
        except OSError:
            pass
    return False


def has_uncommitted_test_change(root):
    items = (git(root, "status", "--porcelain", "-z", "--untracked-files=all") or "").split("\0")
    paths = []
    i = 0
    while i < len(items):
        item = items[i]
        i += 1
        if len(item) < 4:
            continue
        if item[:2].strip() != "D":  # 지우기만 한 항목은 테스트 변경으로 세지 않는다
            paths.append(item[3:])
        if "R" in item[:2] or "C" in item[:2]:  # 이름을 바꾼 항목은 다음 칸이 옛 경로다
            paths.append(items[i])
            i += 1
    return any(is_code_file(p) and is_test_file(p) and not is_bytecode(p) for p in paths)


def count_block(root, phase, lines, rel):
    """같은 phase의 계획 줄과 plan.md가 바뀌지 않은 동안 이 파일을 테스트 먼저 때문에 막은 횟수를
    하나 늘려 돌려준다."""
    plan = "\n".join(re.sub(r"^(\s*- )\[[xX]\]", r"\1[ ]", line) for line in lines).rstrip()
    try:
        with open(os.path.join(root, os.path.dirname(phase), "plan.md"), encoding="utf-8") as f:
            plan += "\n" + f.read()
    except OSError:
        pass
    digest = hashlib.sha256(plan.encode("utf-8")).hexdigest()
    store = os.path.join(git(root, "rev-parse", "--absolute-git-dir").strip(), COUNT_FILE)
    try:
        with open(store, encoding="utf-8") as f:
            counts = json.load(f)
    except (OSError, ValueError):
        counts = {}
    entry = counts.get(phase)
    if not isinstance(entry, dict) or entry.get("plan") != digest:
        entry = {"plan": digest, "files": {}}
    entry["files"][rel] = entry["files"].get(rel, 0) + 1
    counts[phase] = entry
    if not write_counts(store, counts):
        # 셈을 남기지 못하면 세 번째 막음에 닿지 못한다. 셈을 잃는 대신 STOP으로 보낸다
        return STOP_COUNT
    return entry["files"][rel]


def write_counts(store, counts):
    """세는 파일을 같은 폴더의 임시 파일에 쓰고 바꿔 넣는다. 쓰지 못하면 False를 돌려준다."""
    tmp = None
    try:
        fd, tmp = tempfile.mkstemp(dir=os.path.dirname(store), prefix=COUNT_FILE + ".")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(counts, f, ensure_ascii=False)
        os.replace(tmp, store)
        return True
    except OSError:
        if tmp:
            try:
                os.remove(tmp)
            except OSError:
                pass
        return False


def check(data):
    """막으면 에이전트에게 줄 글을, 통과시키면 None을 돌려준다."""
    tool_input = data.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not path:
        return None
    if str(path).lower().endswith(".md"):
        # 코드 파일이 아니다. git을 부르기 전에 통과시킨다
        return None
    cwd = data.get("cwd") or os.getcwd()
    top = git(cwd, "rev-parse", "--show-toplevel")
    root = os.path.realpath(top.strip() if top else cwd)
    rel = os.path.relpath(os.path.realpath(os.path.join(cwd, path)), root).replace(os.sep, "/")
    if rel == ".." or rel.startswith("../"):
        return None
    if not is_code_file(rel) or not is_setup(root):
        return None
    if rel in SETUP_FILES and not os.path.exists(os.path.join(root, rel)):
        # setup이 승인받아 처음 쓰는 것. 남은 phase가 있든 없든, 테스트 먼저든 아니든 통과시킨다.
        # 이미 있으면 아래의 막음을 그대로 받는다
        return None

    tasks = unfinished_tasks(root)
    if not tasks:
        return PLAN_FIRST.format(rel=rel)

    if not top or is_test_file(rel):
        return None
    name = current_task(tasks)
    number = tasks[name][0]
    phase = "/".join(["docs", "tasks", name, "phase-%d.md" % number])
    with open(os.path.join(root, phase), encoding="utf-8") as f:
        text = f.read()
    lines = plan_lines(text)
    if not is_test_first(lines):
        return None
    # 싼 `git status`를 먼저 보고, 저장소 전체를 훑는 `git ls-files`는 그 뒤에 본다
    if has_uncommitted_test_change(root):
        return None
    # 다시 수행에서는 첫 수행이 그 phase 커밋에 남긴 테스트 변경도 센다
    if has_check_section(text) and phase_commit_has_test_change(root, name, number):
        return None
    if not has_tests(root):
        return None
    if count_block(root, phase, lines, rel) >= STOP_COUNT:
        return STOP.format(rel=rel, phase=phase)
    return TEST_FIRST.format(rel=rel, phase=phase)


ERROR = (
    "plate: 편집 훅 안에서 예외가 나서 이 편집을 막는다: {error}\n"
    "막아야 할 편집을 조용히 통과시키지 않으려고 막는다. 까닭(깨진 입력, UTF-8이 아닌 phase 파일, "
    "git의 오류)을 찾아 고친 뒤 다시 시도하고, 풀 수 없으면 막힘으로 멈춰 보고한다.\n"
)


def main():
    try:
        message = check(json.load(sys.stdin))
    except Exception as e:  # 예외로 종료 1이 되면 도구는 막지 않는다(fail-open). 정한 대로 막는다
        message = ERROR.format(error="%s: %s" % (type(e).__name__, e))
    if message:
        sys.stderr.write(message)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
