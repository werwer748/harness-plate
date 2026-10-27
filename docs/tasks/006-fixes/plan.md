# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리고 plate 저장소에서 고친다
- 바뀐 동작(버전 줄, 스킬 규칙)을 시험하는 테스트가 `tests/`에 없다

## 완료 조건
1. check 5번이 계획의 `- 돌리지 않음: {까닭}` 줄로 돌리지 않기로 정한 동작에 대한 "돌려 보지 않은 위험" 줄까지 실패로 해, 수행이 고칠 길 없는 실패와 세 번 실패의 멈춤으로 이어질 수 있다 (`plugins/plate/skills/check/SKILL.md:56`)
   - 확인: check 5번을 다시 읽어, 계획의 `돌리지 않음` 줄로 돌리지 않기로 정한 동작의 "돌려 보지 않은 위험" 줄은 실패로 하지 않는다고 적혀 있다
2. 결과물인 마크다운만 바뀐 경우의 테스트 적절성 표가 실행 경로 없는 파일(매니페스트 버전 줄)이 함께 바뀌면 쓰이지 않아, tasks마다 버전을 올리는 이 레포에서는 새 표가 쓰일 일이 없다 (`plugins/plate/skills/review/SKILL.md:121`)
   - 확인: review의 그 표가 쓰이는 조건을 다시 읽어, 실행 경로 없는 파일(매니페스트 버전 줄)이 함께 바뀌어도 그 표를 쓴다고 적혀 있다
3. "기능 적합성은 돌린 확인으로 매긴다" 줄이 새 표 뒤에 붙어 일반 등급표의 줄인지 새 표의 줄인지 흐려진다 (`plugins/plate/skills/review/SKILL.md:132`)
   - 확인: review 5번을 다시 읽어 그 줄이 일반 등급표에 딸린 목록 안에 있다
4. tasks 완료 조건 1, 2, 3, 4, 5, 6, 7이 참이다.
   - 확인: `plugins/plate/skills/plan/SKILL.md`의 "phase의 파일", "조건", 6번을 하나씩 읽어 세 곳이 저마다 위의 것을 적는다. 한 곳이라도 없으면 실패
   - 확인: plan의 "조건", 6번, 양식의 tasks 머리 완료 조건, task 머리 완료 조건을 하나씩 읽어 네 곳이 저마다 위의 것과 맞는다. 한 곳이라도 없으면 실패
   - 확인: `plugins/plate/skills/check/SKILL.md`의 절대 규칙 3, 절차, 확인 절의 양식, 적는 규칙을 읽어 위의 것이 서로 어긋나지 않게 적혀 있다
   - 확인: `plugins/plate/skills/retro/SKILL.md`의 4번과 회고 절의 양식을 읽어 위의 것이 적혀 있다
   - 확인: eval의 낱말 `done-phase-N.md`와 `retro.md`를 읽어 바뀐 확인 절과 회고 절의 꼴과 어긋나지 않는다
   - 확인: `mktemp -d` 안에 bare 원격과 그 복제본을 만들고, 복제본의 기본 브랜치에 원격에 없는 커밋 하나를 더한 뒤 run 1번에 적힌 브랜치 만들기, 앞선 커밋 알아보기, 되돌리기 명령을 적힌 그대로 돌린다. 되돌리기 전에는 알아보기가 커밋 1개를, 되돌린 뒤에는 0개를 내고, 되돌린 뒤 `git merge-base <기본 브랜치> tasks/<이름>`이 원격 기본 브랜치의 끝이고, tasks 브랜치에 그 커밋이 남는다. 하나라도 다르면 실패. 임시 디렉터리는 지운다
   - 확인: run의 낱말 "작업 트리의 스킬 줄"과 review의 낱말 "갈라진 곳"을 읽어 둘 다 로컬 기본 브랜치의 merge-base라고 적는다
   - 확인: run의 `RUNLOG.md` 절의 물은 자리 목록에 `기본 브랜치`가 있다
   - 확인: `plugins/plate/skills/review/SKILL.md`의 4번, 5번의 등급표와 그 아래 줄, PR 모드 절을 하나씩 읽어 위의 것이 적혀 있다
   - 확인: run의 `RUNLOG.md` 절의 물은 자리 목록과 eval의 낱말 "정해 둔 물음"을 견줘, `멈춤`을 뺀 목록이 같다. 다르면 실패
   - 확인: retro 5번의 "멈춤" 줄을 읽어 eval의 낱말과 어긋나지 않는다
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.15.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어, 이 tasks가 바꾼 동작(완료 조건 1~6)과 어긋나는 줄이 없다

## 결정
- 없음
