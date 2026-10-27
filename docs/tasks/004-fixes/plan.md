# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리고 plate 저장소에서 고친다

## 완료 조건
1. retro 5번 "멈춤"의 `권한`을 보는 테스트가 `test_49_stop_list_includes_permission`으로 이름 붙고 모듈 docstring의 retro 목록에도 #50이 없어, tasks 머리가 #50의 해결로 적은 규칙의 시험을 이슈 번호로 찾을 수 없다 (`tests/test_skill_rules.py:296`)
   - 확인: `tests/test_skill_rules.py`를 읽어 retro 5번 "멈춤"의 `권한`을 보는 테스트 이름에 `50`이 들고, 모듈 docstring의 retro 목록에 #50이 있다
2. tasks 완료 조건 4, 5가 참이다.
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `mktemp -d`에 `git archive HEAD`를 풀어, run 본문의 맡기는 글 하나에서 `부른 쪽: plate:run` 줄을 지우고 돌리면 실패한다. 다시 풀어 retro 5번의 #49 해결 글을 지우고 돌리면 실패한다
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.18.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `docs/PRD.md`의 7, `docs/ARCHITECTURE.md`의 "패턴과 규칙"(맡기는 글의 문단과 run 문단)과 디렉터리 구조의 `test_skill_rules.py` 줄, `README.md`의 `run` 행을 문서마다 따로 읽어, run의 바뀐 동작(해시로 보는 파일을 고칠 때의 멈춤, 계획 수정의 결정 줄, 맡기는 글의 표지)과 `test_skill_rules.py`가 시험하는 규칙 목록에 어긋나는 줄이 없다. 하나라도 있으면 실패

## 결정
- 없음
