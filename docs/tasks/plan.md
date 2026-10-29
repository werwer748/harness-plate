# 이슈 #80과 cleanup 브랜치 문제를 고친다

**이름**: cleanup-branch

## 요청
#80(plan과 retro가 되풀이되는 이름과 여러 입력의 경우를 확인하지 않아 결함이 코드 평가까지 간다)과 cleanup이 기본 브랜치에 보고서를 커밋해 이어지는 plan→tasks의 run이 로컬 기본 브랜치를 되돌릴지 묻게 되는 문제를 함께 고친다

## 목표
plan과 retro가 tasks를 넘어 되풀이되는 이름과 여러 입력의 경우를 확인하고 회고하게 한다. cleanup은 어느 브랜치에서 부르든 `cleanup/<보고서 이름>` 브랜치에서만 커밋하고, 그 브랜치에서 갈라진 tasks는 끝에서 그 브랜치로 돌아와 PR 하나로 기본 브랜치에 들어가게 한다. 바뀐 동작은 맥락 문서와 맞춘다.

## 범위 밖
- setup과 context의 브랜치. 둘 다 커밋하지 않는다.
- run 1번의 "로컬 기본 브랜치에 앞선 커밋이 있으면 되돌릴지 묻는다"를 지우는 것. 손으로 넣은 커밋을 위해 남긴다.
- 버전을 1.0.0으로 올리는 것. 별도 릴리스 tasks의 일이다.
- 이 tasks의 cleanup 브랜치 흐름을 이 저장소에서 실제로 끝까지 돌리는 것(cleanup과 run은 에이전트를 띄우고 사용자에게 묻는다).

## 완료 조건
1. 테스트 묶음이 모두 통과한다.
   - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
2. plan의 초안 점검과 조건 규칙이 이렇게 확인을 두게 한다(#80).
   - 동작이 이름이나 번호로 커밋이나 파일을 찾으면, 지난 tasks의 같은 이름이 남은 경우를 확인 하나로 덮는다.
   - 동작이 입력(파일, 줄, 항목)을 받으면, 둘 이상인 경우를 확인 하나로 덮는다.
   retro 4번은 결정이 정한 동작이라도 그런 경우에 목표를 해치면 "문제 아님"으로 닫지 않고 `FRICTION.md`에 경계 밖으로 적는다. 테스트가 그 글들을 지킨다.
   - 확인: `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan의 "6. 초안을 보여 주고 승인받는다"와 "적는 규칙"의 **조건**, retro의 "4. task의 변경을 점검한다"에 저마다 한 줄 이상
   - 확인: 그 글을 지키는 `tests/test_skill_rules.py`의 시험이 있고, 그 글을 지운 사본(`cp -R`)에서 돌리면 그 시험이 실패한다
   - 돌리지 않음: plan은 사용자에게 묻고 retro는 task 전체를 읽는 스킬이라 헤드리스로 끝까지 돌리지 않는다
3. cleanup은 지금 브랜치의 HEAD에서 `cleanup/<보고서 이름>`을 묻지 않고 만들어 바꾼 뒤 보고서와 미룸을 커밋한다. 같은 이름의 브랜치가 이미 있으면 없는 번호를 붙인다. 고른 발견이 없으면 그 브랜치를 푸시해 기본 브랜치로 가는 PR을 열지(GitHub 원격이 없으면 기본 브랜치에 합칠지) 묻는다.
   - 확인: `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 절대 규칙, 보고서를 커밋하는 절, 고른 발견이 없을 때의 절에 저마다 한 줄 이상
   - 확인: `mktemp -d` 시험 레포에서 본문의 브랜치 명령을 적힌 차례대로 세 갈래로 돌린다. 기대는 갈래마다 다음과 같다.
     - 기본 브랜치에서 돌리면: 새 `cleanup/…` 브랜치가 그 HEAD에서 생긴다. 기본 브랜치의 해시(`git rev-parse main`)는 돌리기 전과 같다.
     - `tasks/x`에서 돌리면: 새 `cleanup/…` 브랜치가 `tasks/x`의 HEAD에서 생긴다. 기본 브랜치의 해시는 돌리기 전과 같다.
     - 같은 이름의 `cleanup/…`가 이미 있을 때 돌리면: 번호를 붙인 새 이름의 브랜치가 생기고, 옛 브랜치의 해시는 그대로다.
   - 돌리지 않음: cleanup은 에이전트 열두 개를 띄우고 묻는 스킬이라 헤드리스로 끝까지 돌리지 않는다
4. plan이 `cleanup/…` 브랜치에서 불리면 묻지 않고 그 HEAD에서 `tasks/<이름>`을 만들고, tasks 머리의 이름 줄 아래에 `**보낼 곳**: cleanup/<…>` 줄을 적는다. 기본 브랜치와 그 밖의 브랜치에서는 지금과 같다.
   - 확인: `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 1번, 7번, 계획 파일의 양식에 저마다 한 줄 이상
   - 확인: `mktemp -d` 시험 레포의 `cleanup/x` 브랜치에서 본문 7번의 브랜치 명령을 적힌 차례대로 돌린다. 기대: `tasks/<이름>`이 `cleanup/x`의 커밋을 품고(`git merge-base --is-ancestor cleanup/x tasks/<이름>`이 0), 기본 브랜치의 해시가 돌리기 전과 같다
   - 돌리지 않음: plan은 초안마다 사용자에게 묻는 스킬이라 헤드리스로 끝까지 돌리지 않는다
5. run은 tasks 머리에 `**보낼 곳**:` 줄이 있으면 `docs/tasks/`를 비운 뒤 이렇게 간다.
   - `tasks/<이름>`을 그 브랜치에 로컬로 합칠지 묻는다. squash하지 않는다.
   - 합친 뒤, origin이 GitHub이면 그 브랜치를 푸시해 기본 브랜치로 가는 PR을 열지 묻는다. plate 워크플로가 없으면 코드 평가를 PR 댓글로 단다. GitHub이 아니면 그 브랜치를 기본 브랜치에 합칠지 묻는다.
   - 보낼 곳 브랜치가 로컬에 없으면 합치지도 PR을 열지도 않고 알리고 10번으로 간다.
   - 비운 뒤의 재개도 같은 자리로 간다.
   - 그 줄이 없는 tasks는 지금과 같다.
   - 확인: `grep -n '보낼 곳' plugins/plate/skills/run/SKILL.md` → 0번, "비운다", "PR을 연다", "합친다"에 저마다 한 줄 이상
   - 확인: `mktemp -d` 시험 레포에서 본문의 명령을 적힌 차례대로 두 갈래로 돌린다.
     - `cleanup/x`가 로컬에 있을 때: `cleanup/x`에서 갈라진 `tasks/y`를 합친다. 기대: `cleanup/x`가 `tasks/y`의 끝 커밋을 품고(`git merge-base --is-ancestor tasks/y cleanup/x`가 0), 기본 브랜치의 해시가 그대로다.
     - `cleanup/x`를 지운 레포에서: 본문의 있는지 보는 명령(`git rev-parse --verify --quiet refs/heads/cleanup/x`)이 아무것도 내지 않는다. 기대: 그 갈래가 합치기 명령에 닿지 않는다.
   - 돌리지 않음: run은 에이전트를 띄우고 묻는 스킬이고 PR은 GitHub이 있어야 해 헤드리스로 끝까지 돌리지 않는다
6. 맥락 문서가 바뀐 동작과 맞다.
   - PRD 핵심 기능 9: cleanup 브랜치와 고른 발견이 없을 때의 PR
   - PRD 핵심 기능 8: 보낼 곳으로 합침
   - ARCHITECTURE: plan 문단과 run 문단, 데이터 흐름의 계획·tasks 끝·정리 점검, 디렉터리 구조의 cleanup 줄, 테스트 목록 줄
   - 확인: `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 9, ARCHITECTURE의 plan 문단과 데이터 흐름의 정리 점검에 저마다 한 줄 이상
   - 확인: `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 8, ARCHITECTURE의 run 문단과 데이터 흐름의 tasks 끝에 저마다 한 줄 이상

## 결정
- cleanup은 어느 브랜치에서 부르든 그 HEAD에서 `cleanup/<보고서 이름>`을 묻지 않고 만들어, 거기에 보고서와 미룸을 커밋한다. 다른 브랜치에서 부르면 그 브랜치의 커밋이 cleanup 브랜치에서 기본 브랜치로 가는 PR에 함께 실린다. 이유: 작업의 종류를 불문하고 main에서 작업이 이루어지는 경우를 방지해야 하고, 작업 중인 브랜치에서 바로 점검하고 싶을 때가 있다.
- plan은 `cleanup/…`에서 묻지 않고 그 HEAD에서 `tasks/<이름>`을 만들고 tasks 머리에 `**보낼 곳**:` 줄을 적는다. run은 끝에서 tasks를 그 브랜치에 로컬로 합친 뒤, 그 브랜치로 기본 브랜치에 가는 PR 하나(GitHub이 아니면 합침 하나)를 묻는다. 거기까지가 cleanup 작업의 완료다. 이유: "cleanup/...에서 다시 tasks/...으로 브랜치를 따서 작업을 진행하고 여기서의 작업은 당연히 cleanup으로 푸시 여기까지를 cleanup 작업의 완료로 보고 최종 PR여부나 머지 여부를 결정". PR과 CI 평가는 기본 브랜치로 가는 하나뿐이다.
- 고른 발견이 없으면 cleanup이 그 자리에서 cleanup 브랜치를 푸시해 기본 브랜치로 가는 PR을 열지 묻는다(GitHub 원격이 없으면 기본 브랜치에 합칠지). 이유: run의 끝과 같은 모양으로 cleanup 작업이 끝난다.
- 보낼 곳 브랜치가 로컬에 없으면 run은 합치지도 PR을 열지도 않고 알린 뒤 보고로 끝난다. 이유: 사람이 브랜치를 되살리거나 정한 뒤 다시 부르면 비운 뒤 재개로 같은 자리부터 잇는다.
- #80의 고침은 이슈 본문의 해결책대로 plan의 조건 규칙과 6번 점검, retro 4번을 넓힌다. 이유: 이슈 #80의 해결책 (추천안으로 정함)
- 스킬 본문(`plugins/plate/skills/`)을 고치는 tasks라 run을 시작하기 전에 plan 모드를 끄고 bypassPermissions로 바꾸거나 묻는 모드로 둔다. phase의 수행과 확인은 run이 넘긴 판의 본문을 따르고, 고친 본문의 동작은 본문의 명령을 시험 저장소에서 돌려 본다. 이유: AGENTS.md의 작업 규칙과 `docs/TOOLS.md`의 "플러그인 폴더의 편집과 권한 모드", "세션 도중의 스킬 본문 고침" (추천안으로 정함)

## task 목록
- `001-repeat-checks`: plan과 retro가 되풀이되는 이름과 여러 입력의 경우를 확인하고 회고한다(#80).
- `002-cleanup-branch`: cleanup, plan, run이 cleanup 브랜치에서 일하고 끝에서 그 브랜치로 기본 브랜치에 들어가며, 맥락 문서가 맞는다.
- `003-fixes`: tasks 끝에서 고치기로 한 것이 고쳐진다
