"""plate의 편집 훅(plugins/plate/hooks/edit_guard.py)을 시험한다.

시험마다 임시 폴더에 프로젝트를 만들고, Claude Code가 PreToolUse 훅에 넘기는
JSON을 훅에 주어 돌린다. 종료 코드 2가 막음, 0이 통과다. 막을 때의 글은 stderr다.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent / "plugins" / "plate"
HOOK = PLUGIN_ROOT / "hooks" / "edit_guard.py"
HOOKS_JSON = PLUGIN_ROOT / "hooks" / "hooks.json"

GIT_ENV = dict(
    os.environ,
    GIT_CONFIG_GLOBAL=os.devnull,
    GIT_CONFIG_NOSYSTEM="1",
    GIT_AUTHOR_NAME="t",
    GIT_AUTHOR_EMAIL="t@t",
    GIT_COMMITTER_NAME="t",
    GIT_COMMITTER_EMAIL="t@t",
)

DOCS_MAP = (
    "<!-- plate:docs-map:start -->\n"
    "## 문서 지도\n"
    "| 위치 | 내용 | 읽을 때 |\n"
    "|---|---|---|\n"
    "| `docs/tasks/NNN-slug/` | 작업 하나의 기록 | 그 작업을 이어 갈 때 |\n"
    "<!-- plate:docs-map:end -->\n"
)

PLAN_FIRST = "계획부터"
TEST_FIRST = "실패하는 테스트부터"
STOP = "더 시도하지 않는다"


def phase_text(n, marker):
    lines = ["# Phase %d: 시험" % n, "", "**목표**: 시험한다."]
    if marker == "예":
        lines.append("**테스트 먼저**: 예")
    elif marker == "아니오":
        lines.append("**테스트 먼저**: 아니오 — 문서만 고친다")
    lines += [
        "",
        "**읽을 것**",
        "- 없음",
        "",
        "**TODO**",
        "- [ ] 앱이 바뀐다 (`src/app.py`)",
        "",
        "**통과 조건**",
        "- 앱이 바뀌었다.",
        "  - 확인: 본다",
        "",
    ]
    return "\n".join(lines)


class Project:
    """시험용 프로젝트 하나. git 레포이고 첫 커밋이 돼 있다."""

    def __init__(self, base, setup=True, tests=True, git=True):
        self.root = Path(tempfile.mkdtemp(dir=base))
        self.is_git = git
        if git:
            self.git("init", "-q", "-b", "main")
        self.write("AGENTS.md", DOCS_MAP if setup else "# 지침\n")
        self.write("CLAUDE.md", "@AGENTS.md\n")
        self.write("src/app.py", "print('app')\n")
        if tests:
            self.write("tests/test_app.py", "import unittest\n")
        self.commit("시작")

    def git(self, *args):
        return subprocess.run(
            ["git", *args], cwd=self.root, env=GIT_ENV, check=True,
            capture_output=True, text=True,
        ).stdout

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def commit(self, message="커밋"):
        if self.is_git:
            self.git("add", "-A")
            self.git("commit", "-q", "--allow-empty", "-m", message)

    def add_task(self, name, phases):
        """phases: {번호: "예" | "아니오" | None}. 계획 파일을 쓰고 커밋한다."""
        self.write("docs/tasks/%s/plan.md" % name, "# 시험 작업\n")
        for n, marker in phases.items():
            self.write("docs/tasks/%s/phase-%d.md" % (name, n), phase_text(n, marker))
        self.commit("plan: " + name)

    def payload(self, rel, tool="Edit"):
        """rel을 고치는 편집 도구의 호출을 Claude Code가 훅에 넘기는 JSON 글로 만든다."""
        path = str(rel) if os.path.isabs(str(rel)) else str(self.root / rel)
        key = "notebook_path" if tool == "NotebookEdit" else "file_path"
        return json.dumps({
            "session_id": "test",
            "transcript_path": "/dev/null",
            "cwd": str(self.root),
            "hook_event_name": "PreToolUse",
            "tool_name": tool,
            "tool_input": {key: path},
        })

    def edit(self, rel, tool="Edit"):
        """rel을 고치는 편집 도구의 호출을 훅에 준다. (종료 코드, stderr)를 돌려준다."""
        done = subprocess.run(
            [sys.executable, str(HOOK)], input=self.payload(rel, tool), env=GIT_ENV,
            capture_output=True, text=True,
        )
        return done.returncode, done.stderr


class GuardTestCase(unittest.TestCase):
    def setUp(self):
        self.base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.base)

    def project(self, **kwargs):
        return Project(self.base, **kwargs)

    def assertPassed(self, result):
        code, err = result
        self.assertEqual(code, 0, "통과해야 하는데 막았다: " + err)

    def assertBlocked(self, result, *phrases):
        code, err = result
        self.assertEqual(code, 2, "막아야 하는데 통과시켰다 (종료 코드 %d): %s" % (code, err))
        for phrase in phrases:
            self.assertIn(phrase, err)
        return err


class SetupAndCodeFileTest(GuardTestCase):
    def test_setup_not_done_passes(self):
        p = self.project(setup=False)
        self.assertPassed(p.edit("src/app.py"))
        self.assertPassed(p.edit("src/new.py", tool="Write"))

    def test_non_code_files_pass(self):
        p = self.project()  # 남은 phase가 없다: 코드 파일이면 막히는 상태다
        self.assertBlocked(p.edit("src/app.py"), PLAN_FIRST)
        self.assertPassed(p.edit("docs/notes.md"))
        self.assertPassed(p.edit("README.MD", tool="Write"))
        # `.worktrees/` 아래도 코드 파일이다
        self.assertBlocked(p.edit(".worktrees/009-x/src/app.py"), PLAN_FIRST)

    def test_docs_tasks_files_are_not_code(self):
        p = self.project()  # 문서 지도가 있고 남은 phase가 없다
        self.assertBlocked(p.edit("src/app.py"), PLAN_FIRST)
        self.assertPassed(p.edit("docs/tasks/.gitkeep", tool="Write"))
        p.add_task("001-a", {1: "예"})  # 테스트 먼저인 phase에서도 같다
        self.assertBlocked(p.edit("src/app.py"), TEST_FIRST)
        self.assertPassed(p.edit("docs/tasks/001-a/notes.txt", tool="Write"))

    def test_file_outside_project_passes(self):
        p = self.project()
        outside = Path(tempfile.mkdtemp(dir=self.base)) / "app.py"
        self.assertPassed(p.edit(str(outside)))


class PlanFirstTest(GuardTestCase):
    def test_no_remaining_phase_blocks_code_file(self):
        p = self.project(tests=True)
        err = self.assertBlocked(p.edit("src/app.py"), PLAN_FIRST, "plate:plan")
        self.assertNotIn(STOP, err)
        self.assertBlocked(p.edit("src/new.py", tool="Write"), PLAN_FIRST, "plate:plan")
        self.assertBlocked(p.edit("nb/x.ipynb", tool="NotebookEdit"), PLAN_FIRST)
        # 테스트 파일도 코드 파일이다
        self.assertBlocked(p.edit("tests/test_app.py"), PLAN_FIRST)

    def test_plan_first_message_says_task(self):
        p = self.project()
        err = self.assertBlocked(p.edit("src/app.py"), "남은 phase가 있는 task가 없어서")
        self.assertNotIn("작업", err)

    def test_done_phase_only_task_is_finished(self):
        p = self.project()
        p.add_task("001-a", {})  # 통과한 phase가 모두 done-phase-N.md로 바뀐 task
        p.write("docs/tasks/001-a/done-phase-1.md", phase_text(1, "예"))
        p.write("docs/tasks/001-a/done-phase-2.md", phase_text(2, None))
        p.write("docs/tasks/001-a/retro.md", "## 회고 1\n")
        p.commit()
        self.assertBlocked(p.edit("src/app.py"), PLAN_FIRST, "plate:plan")

    def test_tasks_files_are_not_tasks(self):
        p = self.project()
        p.write("docs/tasks/plan.md", "# 시험 tasks\n")
        p.write("docs/tasks/FRICTION.md", "- 001-a: 없음\n")
        p.write("docs/tasks/RUNLOG.md", "- 수행 001-a phase 1\n")
        p.commit()
        self.assertBlocked(p.edit("src/app.py"), PLAN_FIRST, "plate:plan")
        p.add_task("001-a", {1: "예"})
        self.assertBlocked(p.edit("src/app.py"), TEST_FIRST, "001-a")

    def test_finished_task_does_not_count(self):
        p = self.project()
        p.add_task("001-done", {})  # phase 파일이 모두 지워진 작업
        p.write("docs/tasks/001-done/verify.md", "## 검증 1\n")
        p.commit()
        self.assertBlocked(p.edit("src/app.py"), PLAN_FIRST, "plate:plan")

    def test_no_remaining_phase_blocks_in_project_without_tests(self):
        p = self.project(tests=False)
        self.assertBlocked(p.edit("src/app.py"), PLAN_FIRST, "plate:plan")

    def test_no_remaining_phase_blocks_outside_git(self):
        p = self.project(git=False)
        self.assertBlocked(p.edit("src/app.py"), PLAN_FIRST, "plate:plan")

    def test_plan_first_blocks_are_not_counted(self):
        p = self.project()
        for _ in range(4):
            err = self.assertBlocked(p.edit("src/app.py"), PLAN_FIRST)
            self.assertNotIn(STOP, err)

    def test_remaining_phase_lets_code_through(self):
        p = self.project()
        p.add_task("001-a", {1: None})
        self.assertPassed(p.edit("src/app.py"))

    def test_setup_writes_new_ci_workflow(self):
        # 이미 셋업된 프로젝트에서 setup을 다시 불러 CI 에이전트를 승인한 경우: 남은 phase가 없다
        p = self.project()
        self.assertPassed(p.edit(".github/workflows/plate-review.yml", tool="Write"))
        self.assertBlocked(p.edit(".github/workflows/other.yml", tool="Write"), PLAN_FIRST)
        # 이미 있는 워크플로를 고치는 것은 막는다
        p.write(".github/workflows/plate-review.yml", "name: plate review\n")
        p.commit()
        self.assertBlocked(p.edit(".github/workflows/plate-review.yml"), PLAN_FIRST)
        self.assertBlocked(p.edit(".github/workflows/plate-review.yml", tool="Write"), PLAN_FIRST)

    def test_setup_writes_new_codeowners(self):
        # 이미 셋업된 프로젝트에서 setup을 다시 불러 CODEOWNERS를 쓰는 경우: 남은 phase가 없다
        p = self.project()
        self.assertPassed(p.edit(".github/CODEOWNERS", tool="Write"))
        # 이미 있는 CODEOWNERS를 고치는 것은 막는다
        p.write(".github/CODEOWNERS", "/.github/workflows/ @someone\n")
        p.commit()
        self.assertBlocked(p.edit(".github/CODEOWNERS"), PLAN_FIRST)
        self.assertBlocked(p.edit(".github/CODEOWNERS", tool="Write"), PLAN_FIRST)


class TestFirstTest(GuardTestCase):
    def test_blocks_code_without_test_change(self):
        p = self.project()
        p.add_task("001-a", {1: "예"})
        err = self.assertBlocked(p.edit("src/app.py"), TEST_FIRST)
        self.assertNotIn(STOP, err)
        self.assertNotIn(PLAN_FIRST, err)
        self.assertBlocked(p.edit("src/new.py", tool="Write"), TEST_FIRST)
        self.assertBlocked(p.edit("package.json"), TEST_FIRST)

    def test_setup_writes_new_ci_workflow_in_test_first_phase(self):
        # 이미 셋업된 프로젝트에서 남은 phase가 테스트 먼저일 때 setup을 다시 불러 CI 에이전트를 승인한 경우
        p = self.project()
        p.add_task("001-a", {1: "예"})
        self.assertPassed(p.edit(".github/workflows/plate-review.yml", tool="Write"))
        self.assertBlocked(p.edit(".github/workflows/other.yml", tool="Write"), TEST_FIRST)
        # 이미 있는 워크플로를 고치는 것은 막는다
        p.write(".github/workflows/plate-review.yml", "name: plate review\n")
        p.commit()
        self.assertBlocked(p.edit(".github/workflows/plate-review.yml"), TEST_FIRST)
        self.assertBlocked(p.edit(".github/workflows/plate-review.yml", tool="Write"), TEST_FIRST)

    def test_setup_writes_new_codeowners_in_test_first_phase(self):
        # 이미 셋업된 프로젝트에서 남은 phase가 테스트 먼저일 때 setup을 다시 불러 CODEOWNERS를 쓰는 경우
        p = self.project()
        p.add_task("001-a", {1: "예"})
        self.assertPassed(p.edit(".github/CODEOWNERS", tool="Write"))
        # 이미 있는 CODEOWNERS를 고치는 것은 막는다
        p.write(".github/CODEOWNERS", "/.github/workflows/ @someone\n")
        p.commit()
        self.assertBlocked(p.edit(".github/CODEOWNERS"), TEST_FIRST)
        self.assertBlocked(p.edit(".github/CODEOWNERS", tool="Write"), TEST_FIRST)

    def test_setup_writes_new_ci_workflow_in_phase_without_test_first(self):
        p = self.project()
        p.add_task("001-a", {1: "아니오"})
        self.assertPassed(p.edit(".github/workflows/plate-review.yml", tool="Write"))

    def test_other_uncommitted_change_does_not_count(self):
        p = self.project()
        p.add_task("001-a", {1: "예"})
        p.write("src/other.py", "x = 1\n")
        p.write("docs/tasks/001-a/phase-1.md", phase_text(1, "예") + "\n## 한 일\n- 없음\n")
        self.assertBlocked(p.edit("src/app.py"), TEST_FIRST)

    def test_modified_test_file_passes(self):
        p = self.project()
        p.add_task("001-a", {1: "예"})
        p.write("tests/test_app.py", "import unittest\n# 바뀜\n")
        self.assertPassed(p.edit("src/app.py"))

    def test_new_untracked_test_file_passes(self):
        p = self.project()
        p.add_task("001-a", {1: "예"})
        p.write("tests/unit/test_new.py", "import unittest\n")
        self.assertPassed(p.edit("src/app.py"))

    def test_staged_test_file_passes(self):
        p = self.project()
        p.add_task("001-a", {1: "예"})
        p.write("web/app.test.ts", "test('a', () => {})\n")
        p.git("add", "web/app.test.ts")
        self.assertPassed(p.edit("src/app.py"))

    def test_python_bytecode_is_not_a_test_change(self):
        # .gitignore가 없는 Python 프로젝트에서 테스트를 돌리기만 하면 생기는 파일
        p = self.project()
        p.add_task("001-a", {1: "예"})
        p.write("tests/__pycache__/test_app.cpython-313.pyc", "bytecode")
        p.write("tests/test_app.pyc", "bytecode")
        p.write("src/__pycache__/app.cpython-313.pyc", "bytecode")
        self.assertBlocked(p.edit("src/app.py"), TEST_FIRST)
        p.write("tests/test_app.py", "import unittest\n# 바뀜\n")
        self.assertPassed(p.edit("src/app.py"))

    def test_test_change_committed_already_does_not_count(self):
        p = self.project()
        p.add_task("001-a", {1: "예"})
        p.write("tests/test_app.py", "import unittest\n# 바뀜\n")
        p.commit("앞 phase")
        self.assertBlocked(p.edit("src/app.py"), TEST_FIRST)

    def test_marker_no_passes(self):
        p = self.project()
        p.add_task("001-a", {1: "아니오"})
        self.assertPassed(p.edit("src/app.py"))

    def test_no_marker_passes(self):
        p = self.project()
        p.add_task("001-a", {1: None})
        self.assertPassed(p.edit("src/app.py"))

    def test_project_without_tests_passes(self):
        p = self.project(tests=False)
        p.add_task("001-a", {1: "예"})
        self.assertPassed(p.edit("src/app.py"))

    def test_outside_git_passes(self):
        p = self.project(git=False)
        p.add_task("001-a", {1: "예"})
        self.assertPassed(p.edit("src/app.py"))

    def test_editing_test_file_passes(self):
        p = self.project()
        p.add_task("001-a", {1: "예"})
        for rel in [
            "tests/test_app.py",
            "tests/helpers.py",
            "test/app.js",
            "src/__tests__/app.js",
            "src/test_util.py",
            "pkg/app_test.go",
            "web/app.test.ts",
            "web/app.spec.ts",
        ]:
            with self.subTest(rel=rel):
                self.assertPassed(p.edit(rel))
        self.assertBlocked(p.edit("src/testutil.py"), TEST_FIRST)
        self.assertBlocked(p.edit("src/contest.py"), TEST_FIRST)


class TestProjectDetectionTest(GuardTestCase):
    def test_package_json_test_script_counts(self):
        p = self.project(tests=False)
        p.write("package.json", json.dumps({"scripts": {"test": "node --test"}}))
        p.add_task("001-a", {1: "예"})
        self.assertBlocked(p.edit("src/app.py"), TEST_FIRST)

    def test_npm_placeholder_test_script_does_not_count(self):
        p = self.project(tests=False)
        placeholder = 'echo "Error: no test specified" && exit 1'
        p.write("package.json", json.dumps({"scripts": {"test": placeholder}}))
        p.add_task("001-a", {1: "예"})
        self.assertPassed(p.edit("src/app.py"))

    def test_makefile_test_target_counts(self):
        p = self.project(tests=False)
        p.write("Makefile", "build:\n\tcc app.c\n\ntest:\n\t./run-tests\n")
        p.add_task("001-a", {1: "예"})
        self.assertBlocked(p.edit("src/app.py"), TEST_FIRST)


class CurrentPhaseTest(GuardTestCase):
    def test_smallest_unfinished_task_off_task_branch(self):
        p = self.project()
        p.add_task("001-a", {1: "아니오"})
        p.add_task("002-b", {1: "예"})
        self.assertPassed(p.edit("src/app.py"))

    def test_branch_does_not_pick_task(self):
        p = self.project()
        p.add_task("001-a", {1: "아니오"})
        p.add_task("002-b", {1: "예"})
        for branch in ("task/002-b", "tasks/x"):
            with self.subTest(branch=branch):
                p.git("switch", "-q", "-c", branch)
                self.assertPassed(p.edit("src/app.py"))
        p.add_task("000-z", {1: "예"})  # 번호가 더 작은 끝나지 않은 task
        self.assertBlocked(p.edit("src/app.py"), TEST_FIRST, "000-z")

    def test_finished_task_is_skipped(self):
        p = self.project()
        p.add_task("001-done", {})
        p.add_task("002-b", {1: "예"})
        self.assertBlocked(p.edit("src/app.py"), TEST_FIRST, "002-b")

    def test_first_remaining_phase_is_smallest_number(self):
        p = self.project()
        p.add_task("001-a", {2: "예", 10: "아니오"})
        self.assertBlocked(p.edit("src/app.py"), TEST_FIRST, "phase-2.md")


class ThirdBlockTest(GuardTestCase):
    def setUp(self):
        super().setUp()
        self.p = self.project()
        self.p.add_task("001-a", {1: "예"})

    def test_third_block_of_same_file_says_stop(self):
        for _ in range(2):
            err = self.assertBlocked(self.p.edit("src/app.py"), TEST_FIRST)
            self.assertNotIn(STOP, err)
        for _ in range(2):  # 세 번째와 그 뒤
            self.assertBlocked(self.p.edit("src/app.py"), STOP, "막힘", "까닭", "해결책", "phase-1.md")

    def test_count_is_per_file(self):
        self.p.edit("src/app.py")
        self.p.edit("src/app.py")
        err = self.assertBlocked(self.p.edit("src/other.py"), TEST_FIRST)
        self.assertNotIn(STOP, err)
        self.assertBlocked(self.p.edit("src/app.py"), STOP)

    def test_plan_change_resets_count(self):
        self.p.edit("src/app.py")
        self.p.edit("src/app.py")
        changed = phase_text(1, "예").replace("앱이 바뀐다", "앱이 다르게 바뀐다")
        self.p.write("docs/tasks/001-a/phase-1.md", changed)
        self.p.commit("plan: 001-a 수정")
        err = self.assertBlocked(self.p.edit("src/app.py"), TEST_FIRST)
        self.assertNotIn(STOP, err)

    def test_plan_md_change_resets_count(self):
        self.p.edit("src/app.py")
        self.p.edit("src/app.py")
        # 논의로 정한 해결책을 결정에 한 줄 더한다. phase 파일의 계획 줄은 그대로다
        self.p.write("docs/tasks/001-a/plan.md", "# 시험 작업\n\n## 결정\n- 해결책을 따른다. 이유: 논의\n")
        self.p.commit("plan: 001-a 결정 더함")
        err = self.assertBlocked(self.p.edit("src/app.py"), TEST_FIRST)
        self.assertNotIn(STOP, err)

    def test_checkbox_and_record_do_not_reset_count(self):
        self.p.edit("src/app.py")
        self.p.edit("src/app.py")
        checked = phase_text(1, "예").replace("- [ ]", "- [x]") + "\n## 한 일\n- 없음\n"
        self.p.write("docs/tasks/001-a/phase-1.md", checked)
        self.assertBlocked(self.p.edit("src/app.py"), STOP)


class HooksJsonCommandTest(GuardTestCase):
    """hooks.json의 명령 글을 Claude Code처럼 `sh -c`로 돌린다.

    `${CLAUDE_PLUGIN_ROOT}`는 명령 글에 그대로 바뀌어 들어가고 같은 이름의 환경 변수로도 넘어간다.
    """

    def run_command(self, plugin_root, stdin):
        with open(HOOKS_JSON, encoding="utf-8") as f:
            command = json.load(f)["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
        done = subprocess.run(
            ["sh", "-c", command.replace("${CLAUDE_PLUGIN_ROOT}", str(plugin_root))],
            input=stdin, env=dict(GIT_ENV, CLAUDE_PLUGIN_ROOT=str(plugin_root)),
            capture_output=True, text=True,
        )
        return done.returncode, done.stderr

    def test_missing_script_exits_zero(self):
        p = self.project()  # 남은 phase가 없다: 스크립트가 있으면 막는 호출이다
        missing = Path(self.base) / "no-such-plugin"
        self.assertPassed(self.run_command(missing, p.payload("src/app.py")))
        self.assertPassed(self.run_command(missing, p.payload("docs/notes.md")))

    def test_existing_script_exit_code_passes_through(self):
        p = self.project()
        self.assertBlocked(self.run_command(PLUGIN_ROOT, p.payload("src/app.py")), PLAN_FIRST)
        self.assertPassed(self.run_command(PLUGIN_ROOT, p.payload("docs/notes.md")))


if __name__ == "__main__":
    unittest.main()
