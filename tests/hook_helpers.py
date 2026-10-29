"""plate의 두 훅 시험(test_edit_guard, test_push_guard)이 함께 쓰는 도우미.

이름이 `test_`로 시작하지 않아 시험 찾기가 이 모듈을 시험으로 돌리지 않는다.
hooks.json에서 도구 이름이 든 matcher로 명령 글을 골라 Claude Code처럼 `sh -c`로 돌리는 것과,
훅의 막음(종료 코드 2)·통과(종료 코드 0)를 보는 assert를 둔다.
"""

import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent / "plugins" / "plate"
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


def hook_command(tool, hooks_json=HOOKS_JSON):
    """hooks.json의 PreToolUse에서 matcher에 `tool`이 든 항목 하나의 명령 글을 돌려준다.
    항목의 차례에 기대지 않는다. 그런 항목이 하나가 아니면 실패한다."""
    with open(hooks_json, encoding="utf-8") as f:
        entries = json.load(f)["hooks"]["PreToolUse"]
    matched = [e for e in entries if tool in e["matcher"].split("|")]
    if len(matched) != 1:
        raise AssertionError("%s의 PreToolUse에 건 훅이 하나여야 한다: %d개" % (tool, len(matched)))
    return matched[0]["hooks"][0]["command"]


def run_hook_command(tool, plugin_root, stdin):
    """`tool`에 건 hooks.json의 명령 글을 Claude Code처럼 `sh -c`로 돌린다. (종료 코드, stderr)를 돌려준다.

    `${CLAUDE_PLUGIN_ROOT}`는 명령 글에 그대로 바뀌어 들어가고 같은 이름의 환경 변수로도 넘어간다.
    """
    command = hook_command(tool).replace("${CLAUDE_PLUGIN_ROOT}", str(plugin_root))
    done = subprocess.run(
        ["sh", "-c", command],
        input=stdin, env=dict(GIT_ENV, CLAUDE_PLUGIN_ROOT=str(plugin_root)),
        capture_output=True, text=True,
    )
    return done.returncode, done.stderr


class HookTestCase(unittest.TestCase):
    """시험마다 임시 폴더(`self.base`)를 두고, 훅의 막음·통과를 본다.
    `BLOCK_PHRASES`는 막을 때의 글에 늘 들어야 하는 말이다."""

    BLOCK_PHRASES = ()

    def setUp(self):
        self.base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.base)

    def assertPassed(self, result):
        code, err = result
        self.assertEqual(code, 0, "통과해야 하는데 막았다: " + err)

    def assertBlocked(self, result, *phrases):
        code, err = result
        self.assertEqual(code, 2, "막아야 하는데 통과시켰다 (종료 코드 %d): %s" % (code, err))
        for phrase in tuple(self.BLOCK_PHRASES) + phrases:
            self.assertIn(phrase, err)
        return err
