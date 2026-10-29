# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리거나 BACKLOG로 미루고 plate 저장소에서 고친다

## 완료 조건
1. 보고서 경로를 작업 트리의 `docs/cleanup/`만 보고 정해, 같은 날 합쳐지지 않은 cleanup 브랜치가 있을 때 기본 브랜치에서 다시 부르면 브랜치는 `-2`가 붙지만 보고서 파일 이름은 같아 두 브랜치를 기본 브랜치에 합칠 때 add/add 충돌이 나고, 지난 보고서 읽기도 그 보고서를 놓친다 (plugins/plate/skills/cleanup/SKILL.md:68)
   - 확인: `mktemp -d` 시험 레포에서 `docs/cleanup/2026-10-29.md`를 커밋한 `cleanup/2026-10-29`를 합치지 않은 채 기본 브랜치로 돌아가, 본문 1번의 보고서 경로 고르기와 5번의 브랜치 고르기를 적힌 차례대로 돌린다. 기대: 새 보고서 경로가 `docs/cleanup/2026-10-29.md`가 아니고, 두 cleanup 브랜치를 차례로 기본 브랜치에 합쳐도 충돌하지 않는다. 본문 2번이 합쳐지지 않은 cleanup 브랜치의 보고서를 지난 보고서로 보는지 본문에서 읽는다
2. cleanup에 복사한 "기본 브랜치"·"GitHub 원격" 정의(run에서)와 plan·cleanup의 "cleanup 브랜치" 정의가 같은지 지키는 시험이 없다 (plugins/plate/skills/cleanup/SKILL.md:52)
   - 확인: `tests/`에 cleanup과 run의 "기본 브랜치"·"GitHub 원격" 줄이 같은지, plan과 cleanup의 "cleanup 브랜치" 정의가 같은 브랜치 이름 규칙(`cleanup/<보고서 이름>`, 번호를 붙인 이름)을 적는지 보는 시험이 있다. `cp -R` 사본에서 cleanup의 그 정의 한 줄을 바꾸면 그 시험이 실패한다
3. cleanup "고른 발견이 없을 때"의 합침 갈래와 run "보낼 곳으로 합친다"의 충돌 뒤 되돌림, #80의 plan·retro 규칙에 돌려 보는 확인이 없다 (plugins/plate/skills/cleanup/SKILL.md:159)
   - 확인: `mktemp -d` 시험 레포에서 cleanup "고른 발견이 없을 때"의 합침 갈래 명령을 적힌 차례대로 두 갈래로 돌린다. 충돌 없을 때: 기본 브랜치가 cleanup 브랜치의 끝 커밋을 품고 cleanup 브랜치가 지워진다. 충돌할 때: `git merge --abort` 뒤 기본 브랜치의 해시가 전과 같다
   - 확인: `mktemp -d` 시험 레포에서 run "보낼 곳으로 합친다"를 충돌하는 갈래로 적힌 차례대로 돌린다. 기대: 되돌린 뒤 보낼 곳 브랜치의 해시가 전과 같고 `tasks/<이름>`이 남는다
   - 확인: 헤드리스 시험(작업 트리의 `--plugin-dir`)으로 retro를, 지난 tasks의 같은 task 이름 커밋이 남은 시험 레포의 task 하나에 돌린다. 기대: 그 경우를 회고 절의 문제나 `FRICTION.md`의 경계 밖으로 적는다. 저장소 불변 확인은 `docs/tasks/RUNLOG.md`와 그 phase가 고치는 파일을 빼고 본다
   - 돌리지 않음: plan은 초안마다 사용자에게 묻는 스킬이라 헤드리스로 끝까지 돌리지 않는다
4. tasks 완료 조건 1, 2, 3, 4, 5, 6이 참이다.
   - tasks 완료 조건 1: 테스트 묶음이 모두 통과한다.
     - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
   - tasks 완료 조건 2: plan의 초안 점검과 조건 규칙이 이렇게 확인을 두게 한다(#80). 동작이 이름이나 번호로 커밋이나 파일을 찾으면, 지난 tasks의 같은 이름이 남은 경우를 확인 하나로 덮는다. 동작이 입력(파일, 줄, 항목)을 받으면, 둘 이상인 경우를 확인 하나로 덮는다. retro 4번은 결정이 정한 동작이라도 그런 경우에 목표를 해치면 "문제 아님"으로 닫지 않고 `FRICTION.md`에 경계 밖으로 적는다. 테스트가 그 글들을 지킨다.
     - 확인: `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan의 "6. 초안을 보여 주고 승인받는다"와 "적는 규칙"의 **조건**, retro의 "4. task의 변경을 점검한다"에 저마다 한 줄 이상
     - 확인: 그 글을 지키는 `tests/test_skill_rules.py`의 시험이 있고, 그 글을 지운 사본(`cp -R`)에서 돌리면 그 시험이 실패한다
     - 돌리지 않음: plan은 사용자에게 묻고 retro는 task 전체를 읽는 스킬이라 헤드리스로 끝까지 돌리지 않는다
   - tasks 완료 조건 3: cleanup은 지금 브랜치의 HEAD에서 `cleanup/<보고서 이름>`을 묻지 않고 만들어 바꾼 뒤 보고서와 미룸을 커밋한다. 같은 이름의 브랜치가 이미 있으면 없는 번호를 붙인다. 고른 발견이 없으면 그 브랜치를 푸시해 기본 브랜치로 가는 PR을 열지(GitHub 원격이 없으면 기본 브랜치에 합칠지) 묻는다.
     - 확인: `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 절대 규칙, 보고서를 커밋하는 절, 고른 발견이 없을 때의 절에 저마다 한 줄 이상
     - 확인: `mktemp -d` 시험 레포에서 본문의 브랜치 명령을 적힌 차례대로 세 갈래로 돌린다. 기본 브랜치에서 돌리면: 새 `cleanup/…` 브랜치가 그 HEAD에서 생기고 기본 브랜치의 해시(`git rev-parse main`)는 돌리기 전과 같다. `tasks/x`에서 돌리면: 새 `cleanup/…` 브랜치가 `tasks/x`의 HEAD에서 생기고 기본 브랜치의 해시는 돌리기 전과 같다. 같은 이름의 `cleanup/…`가 이미 있을 때 돌리면: 번호를 붙인 새 이름의 브랜치가 생기고 옛 브랜치의 해시는 그대로다.
     - 돌리지 않음: cleanup은 에이전트 열두 개를 띄우고 묻는 스킬이라 헤드리스로 끝까지 돌리지 않는다
   - tasks 완료 조건 4: plan이 `cleanup/…` 브랜치에서 불리면 묻지 않고 그 HEAD에서 `tasks/<이름>`을 만들고, tasks 머리의 이름 줄 아래에 `**보낼 곳**: cleanup/<…>` 줄을 적는다. 기본 브랜치와 그 밖의 브랜치에서는 지금과 같다.
     - 확인: `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 1번, 7번, 계획 파일의 양식에 저마다 한 줄 이상
     - 확인: `mktemp -d` 시험 레포의 `cleanup/x` 브랜치에서 본문 7번의 브랜치 명령을 적힌 차례대로 돌린다. 기대: `tasks/<이름>`이 `cleanup/x`의 커밋을 품고(`git merge-base --is-ancestor cleanup/x tasks/<이름>`이 0), 기본 브랜치의 해시가 돌리기 전과 같다
     - 돌리지 않음: plan은 초안마다 사용자에게 묻는 스킬이라 헤드리스로 끝까지 돌리지 않는다
   - tasks 완료 조건 5: run은 tasks 머리에 `**보낼 곳**:` 줄이 있으면 `docs/tasks/`를 비운 뒤 `tasks/<이름>`을 그 브랜치에 로컬로 합칠지 묻는다(squash하지 않는다). 합친 뒤, origin이 GitHub이면 그 브랜치를 푸시해 기본 브랜치로 가는 PR을 열지 묻고 plate 워크플로가 없으면 코드 평가를 PR 댓글로 단다. GitHub이 아니면 그 브랜치를 기본 브랜치에 합칠지 묻는다. 보낼 곳 브랜치가 로컬에 없으면 합치지도 PR을 열지도 않고 알리고 10번으로 간다. 비운 뒤의 재개도 같은 자리로 간다. 그 줄이 없는 tasks는 지금과 같다.
     - 확인: `grep -n '보낼 곳' plugins/plate/skills/run/SKILL.md` → 0번, "비운다", "PR을 연다", "합친다"에 저마다 한 줄 이상
     - 확인: `mktemp -d` 시험 레포에서 본문의 명령을 적힌 차례대로 두 갈래로 돌린다. `cleanup/x`가 로컬에 있을 때: `cleanup/x`에서 갈라진 `tasks/y`를 합친다. 기대: `cleanup/x`가 `tasks/y`의 끝 커밋을 품고(`git merge-base --is-ancestor tasks/y cleanup/x`가 0), 기본 브랜치의 해시가 그대로다. `cleanup/x`를 지운 레포에서: 본문의 있는지 보는 명령(`git rev-parse --verify --quiet refs/heads/cleanup/x`)이 아무것도 내지 않는다. 기대: 그 갈래가 합치기 명령에 닿지 않는다.
     - 돌리지 않음: run은 에이전트를 띄우고 묻는 스킬이고 PR은 GitHub이 있어야 해 헤드리스로 끝까지 돌리지 않는다
   - tasks 완료 조건 6: 맥락 문서가 바뀐 동작과 맞다. PRD 핵심 기능 9: cleanup 브랜치와 고른 발견이 없을 때의 PR. PRD 핵심 기능 8: 보낼 곳으로 합침. ARCHITECTURE: plan 문단과 run 문단, 데이터 흐름의 계획·tasks 끝·정리 점검, 디렉터리 구조의 cleanup 줄, 테스트 목록 줄.
     - 확인: `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 9, ARCHITECTURE의 plan 문단과 데이터 흐름의 정리 점검에 저마다 한 줄 이상
     - 확인: `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 8, ARCHITECTURE의 run 문단과 데이터 흐름의 tasks 끝에 저마다 한 줄 이상

## 결정
- 없음
