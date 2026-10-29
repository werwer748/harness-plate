"""plate의 판정 스크립트(plugins/plate/ci/verdict.py)를 시험한다.

CI의 워크플로가 부르듯 등급 묶음 JSON을 stdin으로 주어 스크립트를 돌리고, stdout의 판정
(`merge` 자동 머지, `request` 머지 요청, `close` 닫기)을 본다.
"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "plugins" / "plate" / "ci" / "verdict.py"

# 자동 머지의 조건이 모두 맞는 등급 묶음
GOOD = {
    "build": "pass",
    "lint": "pass",
    "test": "pass",
    "coverage": 85.5,
    "reliability": "A",
    "security": "A",
    "maintainability": "A",
}


def verdict(changed_files=None, **changes):
    """changed_files가 경로 목록이면 한 줄에 하나씩 적은 파일을 `--changed-files`로 넘긴다."""
    bundle = dict(GOOD, **changes)
    command = [sys.executable, str(SCRIPT)]
    with tempfile.TemporaryDirectory() as folder:
        if changed_files is not None:
            listing = Path(folder) / "changed.txt"
            listing.write_text("".join(path + "\n" for path in changed_files))
            command += ["--changed-files", str(listing)]
        done = subprocess.run(
            command, input=json.dumps(bundle), capture_output=True, text=True,
        )
    if done.returncode != 0:
        raise AssertionError("종료 코드 %d: %s" % (done.returncode, done.stderr))
    return done.stdout


class OutputTest(unittest.TestCase):
    def test_prints_one_line(self):
        self.assertEqual(verdict(), "merge\n")


class MergeTest(unittest.TestCase):
    def test_all_conditions_met_merges(self):
        self.assertEqual(verdict().strip(), "merge")

    def test_none_command_is_not_failure_or_unknown(self):
        for key in ("build", "lint", "test"):
            with self.subTest(key=key):
                self.assertEqual(verdict(**{key: "none"}).strip(), "merge")

    def test_coverage_skipped_does_not_block_merge(self):
        self.assertEqual(verdict(coverage="skipped").strip(), "merge")


class CoverageTest(unittest.TestCase):
    def test_boundary_79_and_80(self):
        self.assertEqual(verdict(coverage=79).strip(), "request")
        self.assertEqual(verdict(coverage=79.9).strip(), "request")
        self.assertEqual(verdict(coverage=80).strip(), "merge")
        self.assertEqual(verdict(coverage=80.0).strip(), "merge")

    def test_coverage_unmeasured_requests(self):
        self.assertEqual(verdict(coverage="unmeasured").strip(), "request")

    def test_coverage_skipped_with_other_condition_missing_requests(self):
        self.assertEqual(verdict(coverage="skipped", reliability="B").strip(), "request")


class GradeTest(unittest.TestCase):
    def test_a_merges_b_requests(self):
        for key in ("reliability", "security", "maintainability"):
            with self.subTest(key=key):
                self.assertEqual(verdict(**{key: "A"}).strip(), "merge")
                self.assertEqual(verdict(**{key: "B"}).strip(), "request")

    def test_security_b_requests_c_and_below_close(self):
        self.assertEqual(verdict(security="B").strip(), "request")
        for grade in ("C", "D", "E"):
            with self.subTest(grade=grade):
                self.assertEqual(verdict(security=grade).strip(), "close")

    def test_low_reliability_or_maintainability_requests(self):
        for key in ("reliability", "maintainability"):
            for grade in ("C", "E"):
                with self.subTest(key=key, grade=grade):
                    self.assertEqual(verdict(**{key: grade}).strip(), "request")


class UnknownTest(unittest.TestCase):
    def test_unmeasured_command_requests(self):
        for key in ("build", "lint", "test"):
            with self.subTest(key=key):
                self.assertEqual(verdict(**{key: "unmeasured"}).strip(), "request")

    def test_unjudged_grade_requests(self):
        for key in ("reliability", "security", "maintainability"):
            with self.subTest(key=key):
                self.assertEqual(verdict(**{key: "unjudged"}).strip(), "request")


class CloseTest(unittest.TestCase):
    def test_failed_command_closes(self):
        for key in ("build", "lint", "test"):
            with self.subTest(key=key):
                self.assertEqual(verdict(**{key: "fail"}).strip(), "close")

    def test_close_wins_over_unknown(self):
        self.assertEqual(verdict(test="fail", coverage="unmeasured").strip(), "close")
        self.assertEqual(verdict(security="C", reliability="unjudged").strip(), "close")


class ChangedFilesTest(unittest.TestCase):
    WORKFLOW = [".github/workflows/plate-review.yml", "src/app.py"]

    def test_workflow_path_turns_merge_into_request(self):
        self.assertEqual(verdict(changed_files=self.WORKFLOW).strip(), "request")
        self.assertEqual(
            verdict(changed_files=[".github/workflows/other.yaml"]).strip(), "request"
        )

    def test_workflow_path_keeps_close_and_request(self):
        self.assertEqual(verdict(changed_files=self.WORKFLOW, test="fail").strip(), "close")
        self.assertEqual(verdict(changed_files=self.WORKFLOW, security="C").strip(), "close")
        self.assertEqual(verdict(changed_files=self.WORKFLOW, reliability="B").strip(), "request")

    def test_no_list_or_no_workflow_path_is_unchanged(self):
        self.assertEqual(verdict().strip(), "merge")
        self.assertEqual(verdict(changed_files=[]).strip(), "merge")
        self.assertEqual(
            verdict(changed_files=["src/app.py", ".github/CODEOWNERS", "docs/.github/workflows/x.yml"]).strip(),
            "merge",
        )
        self.assertEqual(verdict(changed_files=["src/app.py"], test="fail").strip(), "close")


def run_raw(stdin, *args):
    """stdin의 글을 그대로 넘겨 스크립트를 돌리고 (종료 코드, stdout)을 돌려준다."""
    done = subprocess.run(
        [sys.executable, str(SCRIPT), *args], input=stdin, capture_output=True, text=True,
    )
    return done.returncode, done.stdout


class UnreadableInputTest(unittest.TestCase):
    def test_broken_json_requests(self):
        self.assertEqual(run_raw("not json"), (0, "request\n"))

    def test_non_object_json_requests(self):
        for stdin in ("[]", "null", "3", '"merge"'):
            with self.subTest(stdin=stdin):
                self.assertEqual(run_raw(stdin), (0, "request\n"))

    def test_empty_input_requests(self):
        self.assertEqual(run_raw(""), (0, "request\n"))

    def test_unreadable_changed_files_requests(self):
        with tempfile.TemporaryDirectory() as folder:
            missing = str(Path(folder) / "missing.txt")
            self.assertEqual(
                run_raw(json.dumps(GOOD), "--changed-files", missing), (0, "request\n")
            )


if __name__ == "__main__":
    unittest.main()
