# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리거나 BACKLOG로 미루고 plate 저장소에서 고친다

## 완료 조건
1. 다시 수행의 테스트 셈이 전체 역사에서 같은 제목의 커밋을 찾아, 지난 tasks의 같은 이름 phase 커밋이 테스트를 바꿨으면 이번 phase가 테스트를 바꾸지 않았어도 구현 편집을 통과시킨다. 갈라진 곳 뒤나 이 tasks의 계획 커밋 뒤의 커밋으로 좁혀야 한다 (`plugins/plate/hooks/edit_guard.py:146-150`)
   - 확인: 시험 레포에서 지난 tasks의 `001-a: phase 1` 커밋(테스트를 바꿈)과 비운 뒤 이번 tasks의 `001-a: phase 1` 커밋(구현만 바꿈), `## 확인 1` 절이 있는 phase 파일을 두고 구현 파일 편집 JSON을 훅에 넣으면 종료 2이고, 이번 tasks의 그 커밋이 테스트를 바꿨으면 종료 0이다
2. phase 본문의 새 구현 파일 옮기기가 파일이 여럿일 때 임시 자리를 잃거나 같은 이름끼리 덮이고, `git status --porcelain`이 다를 때 되살리는 법을 적지 않는다 (`plugins/plate/skills/phase/SKILL.md:59`)
   - 확인: 시험 레포에서 그 phase가 새로 만든 같은 이름의 구현 파일 둘(`pkg/a/__init__.py`, `pkg/b/__init__.py`)에 본문의 명령을 적힌 대로 돌려 옮겼다 되살리면 `git status --porcelain`이 시작할 때와 같고, 본문에 다를 때 되살리는 명령이 있다
3. `STOP`의 글이 "세 번째"를 손으로 적어 `STOP_COUNT`와 따로 논다 (`plugins/plate/hooks/edit_guard.py:30,45`)
   - 확인: `STOP_COUNT`를 바꾼 사본에서 세 번째 막음의 글이 그 수를 따른다
4. phase 커밋에서 테스트 파일을 지우기만 한 경우를 다시 수행의 셈에서 빼는지 보는 시험이 없다 (`plugins/plate/hooks/edit_guard.py:153-154`, `tests/test_edit_guard.py`)
   - 확인: `tests/test_edit_guard.py`에 그 시험이 있고, `--diff-filter=d`를 뺀 사본에서 그 시험이 실패한다
5. tasks 완료 조건 1, 2, 4, 6이 참이다.
   - tasks 완료 조건 1: 테스트 묶음이 모두 통과한다.
     - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
   - tasks 완료 조건 2: 편집 훅과 푸시 훅이 결정대로 돈다: 다시 수행하는 테스트 먼저 phase는 그 phase 커밋의 테스트 변경을 세고, 훅 안의 예외에서 편집 훅은 막고 푸시 훅은 글에 `push`가 있을 때만 막으며, 테스트 파일 삭제만은 테스트 변경으로 세지 않고, `.md` 편집은 git을 부르기 전에 통과한다(신뢰성-1·4·5·10, 성능-5·6, 유지보수성-5).
     - 확인: `docs/tasks/001-hook-fixes/plan.md`의 완료 조건 확인(임시 레포에서 훅에 JSON을 넣어 종료 코드를 보는 것)을 이 tasks의 마지막 커밋에서 다시 돌려 모두 기대대로다
   - tasks 완료 조건 4: run, phase, cleanup, review 본문이 발견대로 고쳐지고 PRD·ARCHITECTURE의 같은 동작 줄과 맞는다(신뢰성-2·3·8, 기존 작업 정합성-5·7·8, 성능-2·4).
     - 확인: `docs/tasks/003-skill-fixes/plan.md`의 완료 조건 확인을 이 tasks의 마지막 커밋에서 다시 돌려 모두 기대대로다
   - tasks 완료 조건 6: 스킬 description 열 개가 저마다 400자 이하이고 테스트가 그 상한을 지키며, 테스트 도우미의 중복과 낡은 글이 정리된다(성능-7, 유지보수성-2·3·4·6).
     - 확인: `python3 -m unittest tests.test_skill_rules tests.test_manifests tests.test_cleanup_skill tests.test_edit_guard tests.test_push_guard` → `OK`
     - 확인: `grep -n '^def section' tests/test_cleanup_skill.py` → 아무것도 나오지 않음

## 결정
- 없음
