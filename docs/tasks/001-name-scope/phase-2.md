# Phase 2: retro가 이번 task의 커밋만 보고 결정의 빈틈을 문제로 판정한다

**목표**: retro의 "task의 커밋"이 task 머리를 마지막으로 더한 커밋 뒤의 것만 센다. 결정이 정한 동작이 세 경우에서 목표를 해치면 retro가 문제(기준: 계획, 고칠 쪽: 계획)로 판정한다. 두 동작을 헤드리스 시험으로 본다.

**테스트 먼저**: 아니오 — `.md`인 스킬 본문만 고치고, 테스트는 그 글을 지키는 시험이라 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md` (낱말의 **task의 커밋**, "1. 읽는다", "4. task의 변경을 점검한다"의 `지난 tasks의 같은 이름` 줄과 경계 밖 문단, "5. tasks 끝에 볼 것을 모은다"의 **경계 밖**, 기록의 양식의 "고칠 쪽" 칸, 적는 규칙의 "고칠 쪽"과 경계 밖 줄)
- `docs/ARCHITECTURE.md` (패턴과 규칙의 훅 문단: 편집 훅이 task 머리 `plan.md`를 마지막으로 더하거나 지운 커밋 뒤에서 phase 커밋을 찾는 글. 디렉터리 구조의 `test_skill_rules.py` 줄)
- `docs/TOOLS.md` ("세션 도중의 스킬 본문 고침", "스킬을 헤드리스로 돌려 볼 때의 허용 목록", 한글 heredoc 줄)
- `tests/test_skill_rules.py` (`RetroRulesTest`)
- `docs/PRD.md`, `docs/ADR.md`, `docs/BACKLOG.md`

**TODO**
- [ ] 낱말의 **task의 커밋**이 그 task 머리 `plan.md`를 마지막으로 더한 커밋 뒤의 커밋으로 좁혀진다. 그 커밋이 없으면 지금 꼴로 본다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] 4번의 `지난 tasks의 같은 이름` 줄이 바뀐다. 결정이나 완료 조건이 정한 동작이 세 경우에서 목표를 해치면 "문제"에 기준 "계획", 고칠 쪽 "계획"으로 적는다. 기록의 "남은 것"에 그 꼴이 적힌 줄도 같다. 양식과 적는 규칙의 "고칠 쪽"에 "계획"이 더해진다. 경계 밖 문단과 5번의 **경계 밖**, 적는 규칙의 경계 밖 줄은 이 꼴을 빼게 맞춘다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] 바뀐 두 글을 지키는 시험이 생긴다: `RetroRulesTest.test_80_task_commits_after_task_head`, `RetroRulesTest.test_80_decided_gap_is_plan_problem`. 옛 시험 `test_80_decided_behavior_with_repeated_names_goes_out_of_bounds`는 새 글을 지키게 바뀌거나 이 시험으로 갈음된다 (`tests/test_skill_rules.py`)
- [ ] 완료 조건 2의 시험 레포 A와 완료 조건 3의 시험 레포 B를 scratchpad의 `mktemp -d`에 차린다. 두 레포에서 `claude -p "/plate:retro docs/tasks/001-x" --plugin-dir {이 저장소}/plugins/plate --permission-mode bypassPermissions --output-format json`을 돌리고, 결과와 그때의 `git hash-object plugins/plate/skills/retro/SKILL.md`를 기록에 남긴다(이 저장소의 파일은 바꾸지 않는다)
- [ ] 디렉터리 구조의 `test_skill_rules.py` 줄에 두 규칙(`task 머리를 마지막으로 더한 커밋`, `고칠 쪽이 계획`)이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 2가 참이다.
  - 확인: `grep -n -F '**task의 커밋**' plugins/plate/skills/retro/SKILL.md` → 그 줄에 `마지막으로 더한 커밋`이 있다
  - 확인: 시험 레포 A의 `docs/tasks/001-x/retro.md`에서 `grep -c 'old.txt'` → `0`, `grep -c 'new.txt'` → 1 이상
- 완료 조건 3이 참이다.
  - 확인: 시험 레포 B의 retro 결과의 첫 줄이 `판정: 문제 있음`이고, 그 `retro.md`의 "문제"에 `기준: 계획`과 `고칠 쪽: 계획`이 든 줄이 있다
  - 확인: 두 헤드리스 시험 전후로 이 저장소의 `git status --porcelain`이 `docs/tasks/RUNLOG.md`와 이 phase가 고친 파일을 빼면 같고, `git rev-parse HEAD`가 같다
  - 확인: 기록에 적은 retro 본문 해시가 작업 트리의 `git hash-object plugins/plate/skills/retro/SKILL.md`와 같다
- 두 시험이 글을 지킨다.
  - 확인: `cp -R` 사본에서 **task의 커밋** 줄의 `마지막으로 더한 커밋`을 지우면 `RetroRulesTest.test_80_task_commits_after_task_head`가 `FAILED`이고, `고칠 쪽: 계획`이 든 4번의 줄을 지우면 `RetroRulesTest.test_80_decided_gap_is_plan_problem`이 `FAILED`다
- 완료 조건 1이 그대로다(앞 phase가 이룬 조건의 파일을 고친다).
  - 확인: `grep -n '합쳐지지 않은 다른 브랜치' plugins/plate/skills/retro/SKILL.md` → 4번에 한 줄 이상이고, 그 줄에 `지난 tasks의 같은 이름`과 `이름마다`가 함께 있다
- 테스트 묶음이 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
