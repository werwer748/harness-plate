#!/usr/bin/env python3
"""plate의 판정 스크립트. CI의 워크플로가 PR 모드 review의 등급 묶음으로 PR을 어떻게 할지 고른다.

입력: stdin으로 등급 묶음 JSON 하나. 꼴은 review 스킬의 PR 모드 절에 있다.
    {"build": "pass", "lint": "none", "test": "pass", "coverage": 85.5,
     "reliability": "A", "security": "A", "maintainability": "B"}
    build, lint, test: "pass" | "fail" | "none" | "unmeasured"
    coverage: 0~100의 수 | "skipped" | "unmeasured"
    reliability, security, maintainability: "A"~"E" | "unjudged"

출력: stdout에 판정 한 줄. 종료 코드는 0이다.
    close    닫기. 빌드·린트·테스트 가운데 "fail"이 있거나 보안이 C 이하다
    merge    자동 머지. 빌드·린트·테스트가 모두 "pass"나 "none", 커버리지가 80 이상이나
             "skipped", 신뢰성·보안·유지보수성이 모두 "A"다
    request  머지 요청. 그 밖이다. 모름("unmeasured", "unjudged")은 여기로 온다

예: echo "$BUNDLE" | python3 verdict.py
"""

import json
import sys

COMMANDS = ("build", "lint", "test")
GRADES = ("reliability", "security", "maintainability")


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


def main():
    print(verdict(json.load(sys.stdin)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
