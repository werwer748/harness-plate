"""plate의 푸시 훅(plugins/plate/hooks/push_guard.py)을 시험한다.

시험마다 임시 폴더에 프로젝트를 만들고, Claude Code가 Bash의 PreToolUse 훅에 넘기는
JSON을 훅에 주어 돌린다. 종료 코드 2가 막음, 0이 통과다. 막을 때의 글은 stderr다.
원격은 설정과 원격 추적 브랜치만 두고 실제로 푸시하지 않는다.
"""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_edit_guard import GIT_ENV, Project

PLUGIN_ROOT = Path(__file__).resolve().parent.parent / "plugins" / "plate"
HOOK = PLUGIN_ROOT / "hooks" / "push_guard.py"
HOOKS_JSON = PLUGIN_ROOT / "hooks" / "hooks.json"

BLOCKED = "기본 브랜치"

# 따옴표가 든 명령 치환 뒤에 이은 push. 치환 안의 따옴표, 주석, heredoc을 따로 세어야 뒤의 push를 읽는다
SUBSTITUTION_PUSHES = (
    "git commit -m \"$(cat <<'EOF'\nKeep \"don't\" wording\nEOF\n)\" && git push origin main",
    "git commit -m \"$(cat <<'EOF'\nClose \"issue #12\" properly\nEOF\n)\" && git push origin main",
    "git commit -m \"$(echo \"fix #1\")\" && git push origin main",
    "echo \"$(echo \"fix #1\")\" && git push origin main",
    "echo \"$(git log -1 --format=\"%h #%s\")\"; git push origin main",
    "echo \"`echo \"it's\"`\" && git push origin main",
)

# 따옴표의 짝을 맞추지 못해 명령을 나누지 못하는 꼴. 셸은 `$'…'` 안의 `\'`를 따옴표로 읽지 않는다
UNSPLIT_PUSHES = (
    "echo $'it\\'s' && git push origin main",
    "git commit -m \"don't && git push origin main",
)


def with_origin(p, head="main"):
    """origin 원격을 더하고, 원격의 HEAD가 `head` 브랜치를 가리키게 한다."""
    p.git("remote", "add", "origin", "https://example.invalid/origin.git")
    p.git("update-ref", "refs/remotes/origin/" + head, "HEAD")
    p.git("symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/" + head)
    return p


def payload(command, cwd):
    return json.dumps({
        "session_id": "test",
        "transcript_path": "/dev/null",
        "cwd": str(cwd),
        "hook_event_name": "PreToolUse",
        "tool_name": "Bash",
        "tool_input": {"command": command, "description": "시험"},
    })


def bash(command, cwd):
    """Bash 호출을 훅에 준다. (종료 코드, stderr)를 돌려준다."""
    done = subprocess.run(
        [sys.executable, str(HOOK)], input=payload(command, cwd), env=GIT_ENV,
        capture_output=True, text=True,
    )
    return done.returncode, done.stderr


class PushGuardTestCase(unittest.TestCase):
    def setUp(self):
        self.base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.base)

    def project(self, head="main", **kwargs):
        return with_origin(Project(self.base, **kwargs), head)

    def assertPassed(self, result):
        code, err = result
        self.assertEqual(code, 0, "통과해야 하는데 막았다: " + err)

    def assertBlocked(self, result, *phrases):
        code, err = result
        self.assertEqual(code, 2, "막아야 하는데 통과시켰다 (종료 코드 %d): %s" % (code, err))
        for phrase in (BLOCKED,) + phrases:
            self.assertIn(phrase, err)
        return err


class BlockTest(PushGuardTestCase):
    def test_push_without_target_on_default_branch(self):
        p = self.project()
        for command in (
            "git push",
            "git push origin",
            "git push -u origin",
            "git push --force",
            "git push 2>&1 | tail -5",
        ):
            with self.subTest(command=command):
                self.assertBlocked(bash(command, p.root), "`main`")

    def test_push_to_default_branch(self):
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        for command in (
            "git push origin main",
            "git push origin HEAD:main",
            "git push origin tasks/x:main",
            "git push origin +tasks/x:main",
            "git push origin tasks/x:refs/heads/main",
            "git push --force origin main",
            "git push -u origin main",
            "git push origin tasks/x main",
        ):
            with self.subTest(command=command):
                self.assertBlocked(bash(command, p.root), "`main`")

    def test_push_head_while_on_default_branch(self):
        p = self.project()
        self.assertBlocked(bash("git push origin HEAD", p.root))
        self.assertBlocked(bash("git push -u origin HEAD", p.root))

    def test_delete_default_branch(self):
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        for command in (
            "git push origin --delete main",
            "git push --delete origin main",
            "git push -d origin main",
            "git push origin :main",
            "git push origin :refs/heads/main",
        ):
            with self.subTest(command=command):
                self.assertBlocked(bash(command, p.root), "`main`")

    def test_push_without_naming_default_branch(self):
        """기본 브랜치를 이름으로 적지 않아도 로컬의 기본 브랜치를 origin의 기본 브랜치로 보내는 꼴."""
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        for command in (
            "git push --all origin",
            "git push origin --all",
            "git push --all",
            "git push --branches origin",
            "git push --mirror origin",
            "git push --mirror",
            "git push origin 'refs/heads/*:refs/heads/*'",
            "git push origin '+refs/heads/*:refs/heads/*'",
            "git push origin 'refs/heads/*'",
            "git push origin '*:*'",
            "git push origin :",
            "git push origin +:",
        ):
            with self.subTest(command=command):
                self.assertBlocked(bash(command, p.root), "`main`")

    def test_push_after_heredoc(self):
        """heredoc의 본문이 끝난 뒤의 줄과 `<<`가 있는 줄의 나머지는 명령이다."""
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        for command in (
            "cat > notes.md <<'EOF'\nhello\nEOF\ngit push origin main",
            "cat > notes.md <<'EOF'\ndon't\nEOF\ngit push origin main",
            "cat > notes.md <<'EOF' && git push origin main\nhello\nEOF",
            "cat <<< 'x'\ngit push origin main",
            "grep -n '<<' notes.md\ngit push origin main",
        ):
            with self.subTest(command=command):
                self.assertBlocked(bash(command, p.root), "`main`")

    def test_push_across_line_continuation(self):
        """셸은 `\\`+줄바꿈을 지우고 앞뒤를 한 명령으로 잇는다."""
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        for command in (
            "git push \\\n  origin main",
            "git push origin \\\n  main",
            "git add -A && \\\n  git push origin main",
        ):
            with self.subTest(command=command):
                self.assertBlocked(bash(command, p.root), "`main`")

    def test_push_after_comment(self):
        """`#` 주석은 그 줄 끝까지다. 다음 줄, 따옴표 안의 `#`, 낱말 가운데의 `#` 뒤는 명령이다."""
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        for command in (
            "# push it (it's ready)\ngit push origin main",
            "echo \"it's\" # don't\ngit push origin main",
            "git status # check\ngit push origin main",
            "echo '# x'; git push origin main",
            "echo a#b; git push origin main",
            "echo $#; git push origin main",
        ):
            with self.subTest(command=command):
                self.assertBlocked(bash(command, p.root), "`main`")

    def test_push_inside_chained_command(self):
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        for command in (
            "git add -A && git commit -m 'x' && git push origin main",
            "git status; git push origin main",
            "git status;git push origin main",
            "git fetch || git push origin main",
            "git status\ngit push origin main",
        ):
            with self.subTest(command=command):
                self.assertBlocked(bash(command, p.root), "`main`")

    def test_push_after_substitution_with_quotes(self):
        """명령 치환 안의 따옴표, 주석, heredoc은 따로 세므로 치환 뒤에 이은 push를 나눠 읽고 그 까닭으로 막는다."""
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        for command in SUBSTITUTION_PUSHES:
            with self.subTest(command=command):
                err = self.assertBlocked(bash(command, p.root), "`main`", "git push origin main")
                self.assertNotIn("나누지 못했", err)

    def test_unsplit_command_with_push(self):
        """따옴표가 어긋나 명령을 나누지 못하면, 글에 push가 있을 때 막고 따로 하라고 알린다."""
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        for command in UNSPLIT_PUSHES:
            with self.subTest(command=command):
                self.assertBlocked(bash(command, p.root), "따로")

    def test_push_inside_git_c_uses_that_folder(self):
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        elsewhere = tempfile.mkdtemp(dir=self.base)  # git 레포가 아닌 폴더에서 부른다
        self.assertBlocked(bash("git -C %s push origin main" % p.root, elsewhere), "`main`")
        self.assertBlocked(bash("cd /tmp && git -C '%s' push origin :main" % p.root, elsewhere))
        self.assertPassed(bash("git -C %s push origin tasks/x" % p.root, elsewhere))

    def test_git_c_folder_has_its_own_default_branch(self):
        here = self.project()  # 기본 브랜치가 main
        there = self.project(head="trunk")  # 기본 브랜치가 trunk
        self.assertPassed(bash("git -C %s push origin main" % there.root, here.root))
        self.assertBlocked(bash("git -C %s push origin trunk" % there.root, here.root), "`trunk`")

    def test_default_branch_is_origin_head(self):
        p = self.project(head="develop")
        p.git("switch", "-q", "-c", "tasks/x")
        self.assertBlocked(bash("git push origin develop", p.root), "`develop`")
        self.assertPassed(bash("git push origin main", p.root))

    def test_default_branch_without_origin_head(self):
        p = Project(self.base)  # 브랜치 main, origin 없음
        p.git("remote", "add", "origin", "https://example.invalid/origin.git")
        p.git("switch", "-q", "-c", "tasks/x")
        self.assertBlocked(bash("git push origin main", p.root), "`main`")
        self.assertPassed(bash("git push origin master", p.root))

    def test_master_when_no_main(self):
        p = Project(self.base)
        p.git("branch", "-q", "-m", "main", "master")
        p.git("remote", "add", "origin", "https://example.invalid/origin.git")
        self.assertBlocked(bash("git push", p.root), "`master`")
        self.assertBlocked(bash("git push origin master", p.root), "`master`")

    def test_message_names_command(self):
        p = self.project()
        err = self.assertBlocked(bash("git push origin main", p.root))
        self.assertIn("git push origin main", err)


class PassTest(PushGuardTestCase):
    def test_push_to_other_branch(self):
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        for command in (
            "git push",
            "git push origin",
            "git push -u origin HEAD",
            "git push -u origin tasks/x",
            "git push origin tasks/x:tasks/y",
            "git push origin --delete tasks/old",
            "git push origin main:tasks/x",
            "git push origin v1.0",
            "git push --tags origin",
            "git push origin 'refs/heads/tasks/*:refs/heads/tasks/*'",
        ):
            with self.subTest(command=command):
                self.assertPassed(bash(command, p.root))

    def test_push_only_tags_on_default_branch(self):
        """기본 브랜치에 있어도 태그만 보내는 push는 기본 브랜치로 가지 않는다."""
        p = self.project()
        for command in (
            "git push --tags",
            "git push --tags origin",
            "git push origin --tags",
            "git push -u origin --tags",
            "git push origin 'refs/tags/*:refs/tags/*'",
        ):
            with self.subTest(command=command):
                self.assertPassed(bash(command, p.root))

    def test_push_to_remote_other_than_origin(self):
        p = self.project()
        p.git("remote", "add", "fork", "https://example.invalid/fork.git")
        self.assertPassed(bash("git push fork main", p.root))
        self.assertPassed(bash("git push fork", p.root))
        self.assertPassed(bash("git push fork --delete main", p.root))
        self.assertPassed(bash("git push --all fork", p.root))
        self.assertPassed(bash("git push --mirror fork", p.root))

    def test_heredoc_body_is_not_a_command(self):
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        for command in (
            "cat > notes.md <<'EOF'\ngit push origin main\nEOF",
            "git commit -F - <<'EOF'\ngit push origin main\nEOF",
            "cat <<EOF > notes.md\ngit push origin main\nEOF\ngit status",
            "cat <<-EOF\n\tgit push origin main\n\tEOF",
            "cat <<'A' <<'B'\ngit push origin main\nA\ngit push origin main\nB",
            "git commit -m \"$(cat <<'EOF'\ngit push origin main\nEOF\n)\"",
        ):
            with self.subTest(command=command):
                self.assertPassed(bash(command, p.root))

    def test_line_continuation_is_one_command(self):
        """기본 브랜치에 있어도 줄 잇기로 다른 브랜치를 적은 push는 기본 브랜치로 가지 않는다."""
        p = self.project()
        for command in (
            "git push \\\n  origin tasks/x",
            "git push -u \\\n  origin HEAD:tasks/x",
        ):
            with self.subTest(command=command):
                self.assertPassed(bash(command, p.root))

    def test_comment_is_not_a_command(self):
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        for command in (
            "echo hi # ; git push origin main",
            "# git push origin main",
            "git status # && git push origin main",
            "git status\n  # git push origin main\ngit log",
        ):
            with self.subTest(command=command):
                self.assertPassed(bash(command, p.root))

    def test_project_not_set_up(self):
        p = self.project(setup=False)
        self.assertPassed(bash("git push", p.root))
        self.assertPassed(bash("git push origin main", p.root))
        self.assertPassed(bash("git push origin :main", p.root))

    def test_unsplit_command_in_project_not_set_up(self):
        p = self.project(setup=False)
        p.git("switch", "-q", "-c", "tasks/x")
        for command in UNSPLIT_PUSHES:
            with self.subTest(command=command):
                self.assertPassed(bash(command, p.root))

    def test_unsplit_command_without_push(self):
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        self.assertPassed(bash("echo $'it\\'s' && git status", p.root))

    def test_substitution_with_quotes_without_push(self):
        """명령 치환 안의 따옴표를 따로 세므로, push 없는 명령은 글에 push가 있어도 막지 않는다."""
        p = self.project()
        p.git("switch", "-q", "-c", "tasks/x")
        for command in (
            "git commit -m \"$(cat <<'EOF'\nKeep \"don't\" wording\nEOF\n)\"",
            "git commit -m \"$(cat <<'EOF'\nKeep \"don't\" push wording\nEOF\n)\"",
            "git commit -m \"$(echo \"fix #1\")\" && git push origin tasks/x",
            "echo \"`echo \"it's\"`\" && git push origin tasks/x",
        ):
            with self.subTest(command=command):
                self.assertPassed(bash(command, p.root))

    def test_commands_that_are_not_push(self):
        p = self.project()
        for command in (
            "git status",
            "git log --grep push",
            "echo 'git push origin main'",
            "git commit -m 'git push origin main'",
            "ls && git fetch origin main",
        ):
            with self.subTest(command=command):
                self.assertPassed(bash(command, p.root))

    def test_outside_git(self):
        folder = tempfile.mkdtemp(dir=self.base)
        self.assertPassed(bash("git push origin main", folder))

    def test_call_without_command(self):
        p = self.project()
        done = subprocess.run(
            [sys.executable, str(HOOK)], env=GIT_ENV, capture_output=True, text=True,
            input=json.dumps({"cwd": str(p.root), "tool_name": "Bash", "tool_input": {}}),
        )
        self.assertEqual(done.returncode, 0, done.stderr)


class HooksJsonTest(PushGuardTestCase):
    """hooks.json에서 Bash에 건 명령 글을 Claude Code처럼 `sh -c`로 돌린다."""

    def bash_command(self):
        with open(HOOKS_JSON, encoding="utf-8") as f:
            entries = json.load(f)["hooks"]["PreToolUse"]
        matched = [e for e in entries if "Bash" in e["matcher"].split("|")]
        self.assertEqual(len(matched), 1, "Bash의 PreToolUse에 건 훅이 하나여야 한다")
        return matched[0]["hooks"][0]["command"]

    def run_command(self, plugin_root, stdin):
        done = subprocess.run(
            ["sh", "-c", self.bash_command().replace("${CLAUDE_PLUGIN_ROOT}", str(plugin_root))],
            input=stdin, env=dict(GIT_ENV, CLAUDE_PLUGIN_ROOT=str(plugin_root)),
            capture_output=True, text=True,
        )
        return done.returncode, done.stderr

    def test_command_runs_push_guard(self):
        self.assertIn("push_guard.py", self.bash_command())

    def test_missing_script_exits_zero(self):
        p = self.project()
        missing = Path(self.base) / "no-such-plugin"
        self.assertPassed(self.run_command(missing, payload("git push origin main", p.root)))

    def test_existing_script_exit_code_passes_through(self):
        p = self.project()
        self.assertBlocked(self.run_command(PLUGIN_ROOT, payload("git push origin main", p.root)))
        self.assertPassed(self.run_command(PLUGIN_ROOT, payload("git status", p.root)))


if __name__ == "__main__":
    unittest.main()
