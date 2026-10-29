# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리거나 BACKLOG로 미루고 plate 저장소에서 고친다

## 완료 조건
1. plan 6번·**조건**의 세 경우 규칙과 run 8번의 고칠 쪽 계획에서의 멈춤에 돌려 보는 확인이 없고, grep·단위 시험과 `돌리지 않음` 줄만 있다 (`plugins/plate/skills/plan/SKILL.md:115`, `plugins/plate/skills/run/SKILL.md:209`)
   - 확인: 헤드리스 시험(작업 트리의 `--plugin-dir`)으로 두 규칙을 돌린다. run은 tasks 일괄의 `RUNLOG.md`와 고칠 쪽이 계획인 문제가 든 `retro.md`를 둔 시험 레포에서 `/plate:run`을 돌려, `phase-M.md`를 만들지 않고 멈추는 글이 나오는지 본다. plan은 합쳐지지 않은 다른 브랜치에 같은 이름이 있는 시험 레포에서 이름을 고르는 요청으로 `/plate:plan`을 돌려, 초안 점검이나 첫 물음이 그 브랜치의 같은 이름을 드는지 본다
2. tasks 완료 조건 1, 2, 3, 4, 5, 6이 참이다.
   - tasks 완료 조건 1: 테스트 묶음이 모두 통과한다.
     - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
   - tasks 완료 조건 2: plan의 초안 점검("6. 초안을 보여 주고 승인받는다")과 "적는 규칙"의 **조건**, retro의 "4. task의 변경을 점검한다"가 이름이나 번호로 고르거나 찾는 동작마다 세 경우를 확인 하나씩으로 덮게 한다: 지난 tasks의 같은 이름, 합쳐지지 않은 다른 브랜치(로컬과 origin)의 같은 이름, 한 동작이 만드는 이름마다. 테스트가 그 글을 지킨다.
     - 확인: `grep -n '합쳐지지 않은 다른 브랜치' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan의 6번과 **조건**, retro 4번에 저마다 한 줄 이상
     - 확인: 그 글을 지키는 `tests/test_skill_rules.py`의 시험이 있고, 그 줄을 지운 `cp -R` 사본에서 돌리면 그 시험이 실패한다
   - tasks 완료 조건 3: retro의 "task의 커밋"이 그 task 머리 `plan.md`를 마지막으로 더한 커밋 뒤의 커밋만 센다. 그래서 지난 tasks에 남은 같은 task 이름의 커밋이 들지 않는다.
     - 확인: 헤드리스 시험(작업 트리의 `--plugin-dir`)에서 지난 tasks의 `001-x: phase 1` 커밋이 남은 시험 레포의 이번 task `001-x`에 retro를 돌린다. 기대: 회고 절이 지난 커밋이 바꾼 파일을 점검 대상으로 적지 않는다
   - tasks 완료 조건 4: retro는 결정이나 완료 조건이 정한 동작이 2의 세 경우에서 목표를 해치면 회고 절의 "문제"에 적고(기준: 계획, 고칠 쪽: 계획) 판정을 "문제 있음"으로 낸다. run 8번은 고칠 쪽이 계획인 문제를 계획이 틀린 것으로 보고 고칠 phase를 더하지 않고 멈춘다.
     - 확인: 헤드리스 시험에서 결정대로 지난 tasks의 같은 이름 커밋을 집는 꼴을 둔 시험 레포에 retro를 돌린다. 기대: `판정: 문제 있음`이 나오고 문제 줄에 `기준: 계획`이 있다
     - 확인: `grep -n '고칠 쪽' plugins/plate/skills/run/SKILL.md` → 8번 "고칠 phase를 더한다"와 "멈춘다"에 저마다 한 줄 이상. 그 글을 지키는 시험이 있다
   - tasks 완료 조건 5: 맥락 문서가 바뀐 동작과 맞다: PRD 핵심 기능 7(멈추는 자리), ARCHITECTURE의 run 문단, 데이터 흐름의 실행, 그 아래 멈춤 문단, 디렉터리 구조의 `test_skill_rules.py` 줄.
     - 확인: `grep -n '고칠 쪽' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 7, ARCHITECTURE의 run 문단, 데이터 흐름의 실행, 멈춤 문단에 저마다 한 줄 이상
   - tasks 완료 조건 6: 두 매니페스트의 버전이 1.0.0이고, PRD의 1.0.0 줄이 낸 것으로 맞다.
     - 확인: `grep -n '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "1.0.0"`
     - 확인: `grep -n '1.0.0' docs/PRD.md` → 핵심 기능 아래의 줄이 1.0.0을 냈다고 적는다

## 결정
- 없음
