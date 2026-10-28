# Phase 2: review가 테스트 파일을 빼고 테스트 적절성의 표를 고른다 (#70)

**목표**: 완료 조건 2가 참이 되고, 그 글의 테스트와 review의 헤드리스 시험 기록이 있다.

**테스트 먼저**: 아니오 — 고치는 것은 스킬 본문과 ADR(`.md`)이고, 더하는 테스트는 그 글이 있는지를 볼 뿐 코드의 동작을 바꾸지 않는다

**읽을 것**
- `gh issue view 70 --repo werwer748/harness-plate` (원인과 해결책)
- `plugins/plate/skills/review/SKILL.md`의 "낱말"(실행 경로 없는 파일, 바뀐 코드 파일), "4. 판단한다"의 범주 표, "5. 등급을 매긴다"의 표 고르기 줄과 "결과물인 마크다운만 바뀐 경우의 테스트 적절성" 표, "PR 모드"의 등급을 매기는 줄, "기록의 양식"의 테스트 적절성 자리
- `plugins/plate/skills/run/SKILL.md`의 낱말 "테스트가 있는 프로젝트" (옮길 테스트 파일의 정의)
- `docs/ADR.md`의 ADR-024 트레이드오프
- `tests/test_skill_rules.py`의 모듈 docstring과 도우미 (테스트의 꼴)
- `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"
- `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄

**TODO**
- [ ] review 낱말에 `**테스트 파일**`이 완료 조건 2의 정의 글(run의 정의와 같다)로 더해진다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] 4번 범주 표, 5번 표 고르기 줄, PR 모드의 등급을 매기는 줄의 `결과물인 마크다운과 실행 경로 없는 파일뿐이면`이 `결과물인 마크다운, 실행 경로 없는 파일, 테스트 파일뿐이면`으로 바뀐다. 5번에 `테스트 파일은 바뀐 동작이 아니라 그 근거라 표를 고를 때 세지 않는다`와 `테스트 적절성의 근거 첫 줄에 어느 표로 매겼는지 적는다`가 더해지고, "기록의 양식"의 테스트 적절성 자리에도 그 첫 줄이 든다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] ADR-024 트레이드오프의 괄호 안 글이 "결과물인 마크다운, 실행 경로 없는 파일(매니페스트의 버전 줄 같은 것), 테스트 파일뿐이면"으로 바뀐다 (`docs/ADR.md`)
- [ ] 새 `ReviewRulesTest.test_70_test_files_do_not_pick_default_table`이 더해진다. 완료 조건 2의 review 글들이 그 절에 있고 옛 글이 없는지 본다. 모듈 docstring의 review 목록에 `#70`이 더해진다 (`tests/test_skill_rules.py`)
- [ ] 디렉터리 구조의 `test_skill_rules.py` 줄의 규칙 목록에 "review가 테스트 파일도 빼고 표를 고름, 근거 첫 줄에 쓴 표를 적음"이 더해진다 (`docs/ARCHITECTURE.md`)
- [ ] review의 헤드리스 시험을 두 갈래로 돌리고 이 phase의 "한 일"에 기록한다. 차림(갈래마다 따로 만든 `mktemp -d` 시험 저장소): `main`에 문서 지도에 `docs/ARCHITECTURE.md` 행이 있는 `AGENTS.md`, 결과물인 마크다운 절에 `skills/*/SKILL.md`와 명령 절의 테스트 `python3 -m unittest discover -s tests`가 있는 `docs/ARCHITECTURE.md`, `skills/x/SKILL.md`, 그 글을 보는 `tests/test_x.py`를 커밋한다. `tasks/x` 브랜치에서 `skills/x/SKILL.md`와 `tests/test_x.py`를 바꾸고, 완료 조건 하나에 읽기만 하는 확인(`grep`) 하나와 `돌리지 않음` 줄 하나만 있는 `docs/tasks/plan.md`를 두고, 갈래 2에서만 `tool.py`와 그것을 시험하는 `tests/test_tool.py`를 더해 커밋한다. `claude -p`로 `/plate:review`를 맡기는 글 `부른 쪽: plate:run`과 함께 부르고, `--plugin-dir`에 작업 트리의 `plugins/plate`를, `--permission-mode bypassPermissions`를 준다. 기대: 갈래 1에서 `docs/tasks/review.md`의 테스트 적절성 근거 첫 줄이 결과물인 마크다운만 바뀐 경우의 표로 매겼다고 적고 등급이 A가 아니다. 갈래 2에서 근거 첫 줄이 기본 등급표로 매겼다고 적는다. 기록: 갈래마다 차림, 돌린 명령, 돌려받은 줄, 테스트 적절성 절 전문, 돌릴 때의 `git hash-object plugins/plate/skills/review/SKILL.md` 값

**통과 조건**
- 완료 조건 2가 참이다
  - 확인: `grep -cF -e '결과물인 마크다운, 실행 경로 없는 파일, 테스트 파일뿐이면' plugins/plate/skills/review/SKILL.md`가 `3`, `grep -cF -e '결과물인 마크다운과 실행 경로 없는 파일뿐이면' plugins/plate/skills/review/SKILL.md`가 `0`이다. 정의 글, `**테스트 파일**`, 5번의 두 글은 `grep -cF -e`로 저마다 `1`이다. `grep -cF -e '테스트 파일뿐이면' docs/ADR.md`가 `1`이다
  - 확인: 이 phase의 "한 일"에 적힌 두 갈래의 테스트 적절성 절이 TODO의 기대대로다. 적힌 해시가 지금 작업 트리의 `git hash-object plugins/plate/skills/review/SKILL.md`와 같다
- 테스트가 모두 통과하고, 고친 글이 빠지면 실패한다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: 새 사본(`mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한 것)에서 review 본문의 `테스트 파일은 바뀐 동작이 아니라 그 근거라 표를 고를 때 세지 않는다`가 한 번 있는지 보고, 빈 글로 바꿔 `python3 -m unittest discover -s tests`를 돌리면 출력에 `FAIL: test_70_test_files_do_not_pick_default_table (test_skill_rules.ReviewRulesTest`로 시작하는 줄이 있다
- 문서가 맞는다
  - 확인: `grep -F -e '테스트 파일도 빼고 표를 고름' docs/ARCHITECTURE.md`가 낸 줄이 `test_skill_rules.py`를 담는다. `sed -n '1,8p' tests/test_skill_rules.py`의 review 목록에 `#70`이 있다
