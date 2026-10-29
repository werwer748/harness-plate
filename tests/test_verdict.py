"""plate의 판정 스크립트(plugins/plate/ci/verdict.py)를 시험한다.

CI의 워크플로가 부르듯 등급 묶음 JSON을 stdin으로 주어 스크립트를 돌리고, stdout의 판정
(`merge` 자동 머지, `request` 머지 요청, `close` 닫기)을 본다.
"""

import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "plugins" / "plate" / "ci" / "verdict.py"
SETUP = ROOT / "plugins" / "plate" / "skills" / "setup" / "SKILL.md"
REVIEW = ROOT / "plugins" / "plate" / "skills" / "review" / "SKILL.md"

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


def setup_shape():
    """setup의 CI 워크플로 양식에서 `--json-schema`의 JSON을 뽑아 {키: 값의 집합}으로 돌려준다.

    수 값은 "number"로 센다. required가 키 전부가 아니거나 다른 키를 받으면 실패한다.
    """
    found = re.findall(r"--json-schema '([^']*)'", SETUP.read_text(encoding="utf-8"))
    if len(found) != 1:
        raise AssertionError("setup 양식의 --json-schema 줄이 %d개다" % len(found))
    schema = json.loads(found[0])
    properties = schema["properties"]
    if sorted(schema["required"]) != sorted(properties):
        raise AssertionError("setup 양식의 required가 키 전부가 아니다: %s" % schema["required"])
    if schema.get("additionalProperties") is not False:
        raise AssertionError("setup 양식이 다른 키를 받는다")
    shape = {}
    for key, spec in properties.items():
        values = set()
        for branch in spec.get("anyOf", [spec]):
            if branch["type"] == "number":
                values.add("number")
            elif branch["type"] == "string":
                values.update(branch["enum"])
            else:
                raise AssertionError("setup 양식의 %s에 모르는 type이 있다: %s" % (key, branch))
        shape[key] = values
    return shape


def review_shape():
    """review의 PR 모드 절의 등급 묶음 표를 {키: 값의 집합}으로 돌려준다.

    `"A"`~`"E"`는 A부터 E까지로 펴고, "0~100의 수"는 "number"로 센다.
    """
    lines = REVIEW.read_text(encoding="utf-8").splitlines()
    start = lines.index("## PR 모드")
    header = lines.index("| 키 | 값 | 뜻 |", start)
    shape = {}
    for line in lines[header + 2:]:
        if not line.startswith("|"):
            break
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        keys = re.findall(r"`([^`]+)`", cells[0])
        values = set()
        for low, high in re.findall(r'`"([A-Z])"`~`"([A-Z])"`', cells[1]):
            values.update(chr(code) for code in range(ord(low), ord(high) + 1))
        values.update(re.findall(r'`"([^"`]+)"`', cells[1]))
        if "0~100의 수" in cells[1]:
            values.add("number")
        for key in keys:
            shape[key] = values
    return shape


def verdict_module():
    spec = importlib.util.spec_from_file_location("plate_verdict", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BundleShapeTest(unittest.TestCase):
    """등급 묶음의 꼴(키 일곱 개와 값의 열거)이 setup 양식, review 표, 판정 스크립트에서 같다."""

    COMMAND_VALUES = {"pass", "fail", "none", "unmeasured"}
    GRADE_VALUES = {"A", "B", "C", "D", "E", "unjudged"}
    COVERAGE_VALUES = {"number", "skipped", "unmeasured"}

    def test_setup_schema_matches_review_table(self):
        self.assertEqual(setup_shape(), review_shape())

    def test_keys_match_verdict_script(self):
        module = verdict_module()
        keys = set(module.COMMANDS) | set(module.GRADES) | {"coverage"}
        self.assertEqual(len(keys), 7)
        self.assertEqual(set(setup_shape()), keys)
        self.assertEqual(set(review_shape()), keys)

    def test_values_match_verdict_script(self):
        module = verdict_module()
        for name, shape in (("setup", setup_shape()), ("review", review_shape())):
            for key in module.COMMANDS:
                with self.subTest(source=name, key=key):
                    self.assertEqual(shape[key], self.COMMAND_VALUES)
            for key in module.GRADES:
                with self.subTest(source=name, key=key):
                    self.assertEqual(shape[key], self.GRADE_VALUES)
            with self.subTest(source=name, key="coverage"):
                self.assertEqual(shape["coverage"], self.COVERAGE_VALUES)


if __name__ == "__main__":
    unittest.main()
