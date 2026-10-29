# plan·retro·run이 되풀이되는 이름을 덮고 결정의 빈틈에서 멈춘다

## 목표
plan의 초안 점검과 조건 규칙, retro 4번이 이름이나 번호로 고르거나 찾는 동작마다 지난 tasks의 같은 이름, 합쳐지지 않은 다른 브랜치(로컬과 origin)의 같은 이름, 한 동작이 만드는 이름마다를 확인 하나씩으로 덮게 한다. retro의 "task의 커밋"은 그 task 머리를 마지막으로 더한 커밋 뒤의 것만 세고, 결정이나 완료 조건이 정한 동작이 그 경우에 목표를 해치면 문제(기준: 계획, 고칠 쪽: 계획)로 판정한다. run 8번은 고칠 쪽이 계획인 문제에서 고칠 phase를 더하지 않고 멈춘다. 바뀐 동작은 PRD와 ARCHITECTURE에 맞춘다.

## 범위 밖
- plan을 헤드리스로 끝까지 돌리는 것
- run을 헤드리스로 끝까지 돌리는 것
- 편집 훅의 커밋 범위(이미 task 머리를 더한 커밋 뒤를 본다)

## 완료 조건
1. plan의 "6. 초안을 보여 주고 승인받는다"(초안 전의 점검), "적는 규칙"의 **조건**, retro의 "4. task의 변경을 점검한다"가 저마다 세 경우를 든다: 지난 tasks의 같은 이름, 합쳐지지 않은 다른 브랜치(로컬과 origin)의 같은 이름, 한 동작이 만드는 이름마다.
   - 확인: `grep -n '합쳐지지 않은 다른 브랜치' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan의 6번과 **조건**, retro 4번에 저마다 한 줄 이상이고, 그 줄마다 `지난 tasks의 같은 이름`과 `이름마다`가 함께 있다
   - 확인: `cp -R` 사본에서 `sed -i '' '/합쳐지지 않은 다른 브랜치/d'`로 그 줄들을 지우고 `python3 -m unittest tests.test_skill_rules.PlanRulesTest.test_80_names_left_anywhere_covered tests.test_skill_rules.RetroRulesTest.test_80_retro_names_left_anywhere` → `FAILED`
   - 돌리지 않음: plan은 초안마다 사용자에게 묻는 스킬이라 헤드리스로 끝까지 돌리지 않는다
2. retro의 "task의 커밋"이 그 task 머리 `plan.md`를 마지막으로 더한 커밋 뒤의 커밋만 센다.
   - 확인: `grep -n -F '**task의 커밋**' plugins/plate/skills/retro/SKILL.md` → 낱말 절의 그 줄에 `마지막으로 더한 커밋` 이 있다
   - 확인: 헤드리스 시험(작업 트리의 `--plugin-dir`, `--permission-mode bypassPermissions`)으로 시험 레포 A에 retro를 돌린다. 레포 A의 차림: 셋업된 꼴(`AGENTS.md` 문서 지도, `docs/ARCHITECTURE.md` 명령 절). 지난 tasks에서 `docs/tasks/001-x/plan.md`를 더한 뒤 `001-x: phase 1` 커밋이 `old.txt`를 바꾸고 비움 커밋이 `docs/tasks/`를 지운다. 이번 tasks는 `plan: …` 커밋으로 `001-x/plan.md`를 다시 더하고, `001-x: phase 1` 커밋이 `new.txt`를 바꾸고 `done-phase-1.md`를 둔다. 기대: 시험 레포의 `docs/tasks/001-x/retro.md`에서 `grep -c 'old.txt'`가 `0`이고 `grep -c 'new.txt'`가 1 이상이다
3. retro는 결정이나 완료 조건이 정한 동작이 1의 세 경우에서 목표를 해치면 회고 절의 "문제"에 기준 "계획", 고칠 쪽 "계획"으로 적고 판정을 "문제 있음"으로 낸다. 그 꼴을 `FRICTION.md`의 경계 밖으로만 적지 않는다.
   - 확인: 헤드리스 시험으로 시험 레포 B에 retro를 돌린다. 레포 B의 차림: 셋업된 꼴. task 머리의 목표는 "새 보고서 이름이 다른 브랜치의 보고서와 겹치지 않는다"이고, 결정은 "`new_report.sh`는 작업 트리의 `reports/`만 보고 없는 번호를 고른다"이다. 그 스크립트를 둔 `done-phase-1.md`가 있다. 합쳐지지 않은 로컬 브랜치 `report/a`에 `reports/1.md`가 있고, 작업 트리의 `reports/`는 비어 있다. 기대: 결과의 첫 줄이 `판정: 문제 있음`이고, 시험 레포 `retro.md`의 "문제"에 `기준: 계획`과 `고칠 쪽: 계획`이 든 줄이 있다
   - 확인: 두 헤드리스 시험 전후로 이 저장소의 `git status --porcelain`이 `docs/tasks/RUNLOG.md`와 이 phase가 고친 파일을 빼면 같고, `git rev-parse HEAD`가 같다
   - 확인: 그 동작을 돌릴 때의 retro 본문 해시(`git hash-object plugins/plate/skills/retro/SKILL.md`)를 phase 기록에 적고, 회고 때 작업 트리에서 다시 낸 해시와 같다. 다르면 두 헤드리스 시험을 다시 돌린다
4. run 8번 "고칠 phase를 더한다"와 "멈춘다"는 마지막 회고 절에 고칠 쪽이 "계획"인 문제가 있으면 고칠 phase를 더하지 않고, 실행 방식과 상관없이 멈춘다(물은 자리 `멈춤`).
   - 확인: `grep -n '고칠 쪽' plugins/plate/skills/run/SKILL.md` → 8번과 "멈춘다"에 저마다 한 줄 이상
   - 확인: 그 글을 지키는 `tests/test_skill_rules.py`의 시험 `RunRulesTest.test_80_plan_side_problem_stops`가 있고, `cp -R` 사본에서 `sed -i '' '/고칠 쪽/d' plugins/plate/skills/run/SKILL.md` 뒤 그 시험이 `FAILED`
   - 돌리지 않음: run은 에이전트를 띄우고 묻는 스킬이라 헤드리스로 끝까지 돌리지 않는다
5. 맥락 문서가 바뀐 동작과 맞다(tasks 완료 조건 5).
   - PRD 핵심 기능 7: 멈추는 자리에 고칠 쪽이 계획인 회고의 문제가 든다
   - ARCHITECTURE: run 문단, 데이터 흐름의 실행("회고의 문제는 고칠 phase를 더해 고친다" 줄), 데이터 흐름 아래의 멈춤 문단, 디렉터리 구조의 `test_skill_rules.py` 줄(이 task가 더한 세 시험의 규칙)
   - 확인: `grep -n '고칠 쪽' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 7, ARCHITECTURE의 run 문단, 데이터 흐름의 실행, 멈춤 문단에 저마다 한 줄 이상
   - 확인: `grep -n -F 'test_skill_rules.py' docs/ARCHITECTURE.md` → 디렉터리 구조의 그 줄에 `합쳐지지 않은 다른 브랜치`, `task 머리를 마지막으로 더한 커밋`, `고칠 쪽이 계획`이 있다
6. 테스트 묶음이 모두 통과한다(tasks 완료 조건 1).
   - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 결정
- retro의 "task의 커밋"은 그 task 머리 `plan.md`를 마지막으로 더한 커밋 뒤의 것만 센다. 이유: 편집 훅이 이미 같은 기준을 쓰고, 브랜치나 원격이 없어도 돈다
- 결정이 정한 동작이 목표를 해치면 retro는 경계 밖이 아니라 문제로 판정한다(기준: 계획, 고칠 쪽: 계획). run은 그것을 계획이 틀린 것으로 보고 멈춘다. 이유: 목표를 해치는 결함이 회고 판정을 통과하지 않게 한다
- phase의 수행과 확인은 run이 넘긴 판의 본문을 따르고, 고친 retro의 동작은 헤드리스 시험(작업 트리의 `--plugin-dir`)으로 본다. 헤드리스 시험의 저장소 불변 확인은 `docs/tasks/RUNLOG.md`와 그 phase가 고친 파일을 빼고 본다. 이유: AGENTS.md의 작업 규칙과 `docs/TOOLS.md`의 "세션 도중의 스킬 본문 고침" (추천안으로 정함)
- retro 본문은 phase 1과 phase 2만 고치고, 헤드리스 시험은 phase 2에서 그 본문으로 돌린다. 뒤 phase는 retro 본문을 고치지 않는다. 이유: 본문 해시로 보는 완료 조건 3을 다시 참으로 둘 길을 남긴다 (추천안으로 정함)
