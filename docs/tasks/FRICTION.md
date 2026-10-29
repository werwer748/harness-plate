# FRICTION

- `001-repeat-checks` 없음
- `002-cleanup-branch` 문제: tasks 머리 완료 조건 6과 task 머리 완료 조건 4가 고칠 ARCHITECTURE 자리를 디렉터리 구조, plan·run 문단, 데이터 흐름으로만 들어, 패턴과 규칙의 훅 문단(54행)이 적는 스킬마다의 푸시 규칙(cleanup "푸시하지 않는다", run "`tasks/<이름>`만 푸시")이 계획에서 빠졌다. phase 1 기록과 확인 절이 이를 "남은 것"으로 적었으나 뒤 phase의 TODO에 들지 않아 task 끝까지 남았다(plan의 6번 초안 점검이 바뀐 규칙을 적은 맥락 문서의 다른 줄을 grep으로 찾지 않았다)
- `002-cleanup-branch` 문제: phase 3 수행에서 셸 heredoc으로 넘긴 파이썬 스크립트가 `SyntaxError: Non-UTF-8 code`로 돌지 않아 스크래치 파일로 써서 돌렸다(`done-phase-3.md`의 "하네스에서 걸린 것"). 한글이 든 스크립트를 heredoc으로 넘기는 손일이 깨지는 곳이다
- `002-cleanup-branch` 스킬 후보: phase 1·2·3의 수행과 확인이 저마다 스킬 본문의 브랜치 명령(`git rev-parse --verify --quiet refs/heads/…`, `git switch -c`, `git merge --no-ff`, `git show HEAD^…`)을 손으로 셸에 옮겨 `mktemp -d` 시험 레포를 차리고 갈래마다 해시를 견주었다. 시험 레포를 차리고 갈래별 기대(조상 관계, 기본 브랜치 해시 불변)를 보는 도우미가 있으면 phase마다의 옮겨 적기와 그 옮김의 어긋남이 줄어든다
- `002-cleanup-branch` 경계 밖: cleanup이 고른 발견을 plan에 넘겼을 때 plan이 진행 중인 tasks에 더하기로 하면(plan 7번 "더하는 경우는 tasks 머리의 보낼 곳을 고치지 않는다") 그 tasks의 `tasks/<이름>`으로 바뀌고, `cleanup/<보고서 이름>`의 보고서·미룸 커밋은 그 tasks에도 들지 않고 cleanup도 "고른 발견이 있으면" PR·합침을 묻지 않아 어느 PR·합침에도 실리지 않는다. 결정은 cleanup 브랜치에서 갈라진 새 tasks만 다뤄, 더하는 경우에 보낼 곳을 더하거나 cleanup이 PR·합침을 묻게 할지를 약속에 넣을지 볼 거리다
