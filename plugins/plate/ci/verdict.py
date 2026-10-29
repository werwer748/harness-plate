#!/usr/bin/env python3
"""plate의 판정 스크립트. CI의 워크플로가 PR 모드 review의 등급 묶음으로 PR을 어떻게 할지 고른다.

입력: stdin으로 등급 묶음 JSON 하나. 꼴은 review 스킬의 PR 모드 절에 있다.
    {"build": "pass", "lint": "none", "test": "pass", "coverage": 85.5,
     "reliability": "A", "security": "A", "maintainability": "B"}
    build, lint, test: "pass" | "fail" | "none" | "unmeasured"
    coverage: 0~100의 수 | "skipped" | "unmeasured"
    reliability, security, maintainability: "A"~"E" | "unjudged"
선택 인자: --changed-files <파일>. PR이 바꾼 파일의 경로를 한 줄에 하나씩 적은 파일이다.
    `.github/workflows/`로 시작하는 줄이 있으면 merge를 request로 내린다. close와 request는
    그대로다. 인자가 없으면 목록 없이 판정한다.

출력: stdout에 판정 한 줄. 종료 코드는 0이다.
    close    닫기. 빌드·린트·테스트 가운데 "fail"이 있거나 보안이 C 이하다
    merge    자동 머지. 빌드·린트·테스트가 모두 "pass"나 "none", 커버리지가 80 이상이나
             "skipped", 신뢰성·보안·유지보수성이 모두 "A"이고, 바뀐 파일 목록에 워크플로
             경로가 없다
    request  머지 요청. 그 밖이다. 모름("unmeasured", "unjudged")과 워크플로를 바꾼 PR의
             merge는 여기로 온다
    stdin을 JSON 객체로 읽지 못하면(빈 입력, 깨진 JSON, 객체가 아닌 JSON), 또는
    `--changed-files`의 파일을 읽지 못하면 판정하지 않고 request를 낸다. 이때도 종료 코드는 0이다

예: echo "$BUNDLE" | python3 verdict.py
    echo "$BUNDLE" | python3 verdict.py --changed-files changed.txt
"""

import argparse
import json
import sys

COMMANDS = ("build", "lint", "test")
GRADES = ("reliability", "security", "maintainability")
WORKFLOW_PREFIX = ".github/workflows/"


def coverage_ok(value):
    if value == "skipped":
        return True
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value >= 80


def verdict(bundle):
    if any(bundle.get(key) == "fail" for key in COMMANDS) or bundle.get("security") in ("C", "D", "E"):
        return "close"
    if (
        all(bundle.get(key) in ("pass", "none") for key in COMMANDS)
        and coverage_ok(bundle.get("coverage"))
        and all(bundle.get(key) == "A" for key in GRADES)
    ):
        return "merge"
    return "request"


def touches_workflow(paths):
    return any(path.strip().startswith(WORKFLOW_PREFIX) for path in paths)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed-files")
    args = parser.parse_args()
    print(decide(args.changed_files))
    return 0


def decide(changed_files):
    """읽지 못한 입력은 머지 요청으로 보낸다(fail-closed)."""
    try:
        bundle = json.load(sys.stdin)
    except ValueError:
        return "request"
    if not isinstance(bundle, dict):
        return "request"
    result = verdict(bundle)
    if changed_files is not None:
        try:
            with open(changed_files, encoding="utf-8") as listing:
                paths = listing.readlines()
        except (OSError, ValueError):
            return "request"
        if result == "merge" and touches_workflow(paths):
            result = "request"
    return result


if __name__ == "__main__":
    sys.exit(main())
