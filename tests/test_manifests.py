"""plate의 두 매니페스트(Claude Code용, Codex용)를 시험한다.

두 매니페스트는 같은 플러그인을 가리켜서 버전과 description이 늘 같아야 한다. 한쪽만 바꾸면 실패한다.
"""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAUDE = ROOT / "plugins" / "plate" / ".claude-plugin" / "plugin.json"
CODEX = ROOT / "plugins" / "plate" / ".codex-plugin" / "plugin.json"


def field(path, key):
    return json.loads(path.read_text(encoding="utf-8"))[key]


def version(path):
    return field(path, "version")


class VersionTest(unittest.TestCase):
    def test_both_manifests_have_version(self):
        for path in (CLAUDE, CODEX):
            with self.subTest(manifest=path.parent.name):
                self.assertRegex(version(path), r"^\d+\.\d+\.\d+$")

    def test_versions_match(self):
        self.assertEqual(version(CLAUDE), version(CODEX))


class DescriptionTest(unittest.TestCase):
    def test_descriptions_match(self):
        self.assertTrue(field(CLAUDE, "description"))
        self.assertEqual(field(CLAUDE, "description"), field(CODEX, "description"))


if __name__ == "__main__":
    unittest.main()
