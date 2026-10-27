# FRICTION

- `001-cleanup-skill` 문제: phase 1 수행에서 `plugins/plate/skills/cleanup/SKILL.md`를 만드는 파일 쓰기 호출이 auto mode 분류기의 판정 없음으로 두 번 막혀 수행을 다시 맡겼다. 수행 기록은 plan 모드가 켜진 채라 쓰기가 판정되지 않은 것으로 봤다(`done-phase-1.md`의 "하네스에서 걸린 것"). 이 저장소에서 스킬 본문을 쓰는 tasks는 run 전에 권한 모드를 정해 두라는 `docs/TOOLS.md`의 줄이 있었는데도 걸렸다
- `001-cleanup-skill` 멈춤: phase 1의 첫 수행이 파일 쓰기 권한에 막혀, 권한을 허용한 뒤 phase 1을 다시 맡길지 사용자에게 물었다(`RUNLOG.md`의 멈춤 줄. 답: 허용하고 다시 맡김)
- `001-cleanup-skill` 문제: task 머리 결정의 "확인용 실행"이 장면 2를 먼저 잇는 까닭을 "plan은 승인 전에 아무것도 쓰지 않으므로 폴더가 바뀌지 않는다"로 적었으나, phase 1이 쓴 스킬 7번은 plan을 부르기 전에 미룸 커밋을 넣어 HEAD가 옮겨졌다. phase 2가 장면 1 전에 복제본을 `git reset --hard fd899a0`으로 되돌려야 했다(`done-phase-2.md`의 "계획과 달라진 점"). 계획이 정한 확인 차례가 뒤 phase가 정할 스킬 절차에 기대었다
- `001-cleanup-skill` 문제: task 머리 결정의 허용 목록(`git add/commit/log/diff/show/status`, `gh issue list`, `python3`)에 스킬이 쓰는 `git ls-files`와 `git rev-parse`, `git -C … show` 꼴, 파이프·`;`를 이은 Bash가 맞지 않아 첫 턴의 메인과 서브에이전트 명령 20여 개가 막혔고, 일부 2라운드 에이전트는 git 이력의 지난 tasks 기록을 다시 읽지 못하고 작업 트리로만 판정했다(`docs/TOOLS.md`의 cleanup 절 "막힌 명령"). 계획이 확인용 허용 목록을 스킬 본문의 명령에 대어 보지 않았다
- `001-cleanup-skill` 문제: phase 스킬(`plate:phase`)의 1번은 task 머리와 그 phase의 파일만 읽는다고 하는데, phase 2 수행이 시작할 때 `done-phase-1.md`를 읽었다(`done-phase-2.md`의 "하네스에서 걸린 것"). 바꾼 것은 없었다
