# FRICTION

- `001-plan-rules` 문제: `docs/tasks/RUNLOG.md`의 이 task phase 1 확인 에이전트 줄이 `토큰 모름 | 도구 호출 모름 | 시간 모름초`로 적혀, 값을 모를 때 단위 "초"가 "모름" 뒤에 그대로 붙었다. 실행 스킬(`plate:run`)의 `RUNLOG.md` 에이전트 줄 양식에서 모르는 값의 꼴을 정해 둘지 볼 거리다
- `002-check-retro` 문제: phase 1 확인 1의 "하네스에서 걸린 것"에, 불러 온 `plate:check` 스킬(설치된 판)에는 "남은 것"을 보는 단계가 없어 부른 쪽의 지시대로 작업 트리의 `plugins/plate/skills/check/SKILL.md`를 따랐다고 적혔다. plate 자체를 고치는 tasks에서는 설치된 스킬과 작업 트리의 스킬이 어긋나, 실행 스킬(`plate:run`)이 에이전트에게 작업 트리의 본문을 따르라고 따로 일러야 한다
- `002-check-retro` 문제: phase 1 확인 1의 "하네스에서 걸린 것"에 옮겨진 "남은 것: check의 절 번호가 6~8번으로 밀렸다". 절을 더하면 다른 스킬이 번호로 가리키는 곳이 깨질 수 있어, 지금은 run 스킬의 "`plate:check`의 1번"뿐이라 어긋나지 않는다
- `002-check-retro` 문제: phase 1 확인 1의 "하네스에서 걸린 것"에 옮겨진 "남은 것: 바뀐 check와 retro를 헤드리스로 돌려 보지 않았다". tasks 머리의 결정대로 에이전트가 도는 동작은 본문을 읽어서만 확인했다
- `003-base-branch` 문제: phase 1의 기록과 확인 1의 "하네스에서 걸린 것"에, 통과 조건 1의 확인 글이 bare 원격을 어떻게 채우는지 적지 않아 `git push origin main`으로 채우자 plate의 푸시 훅(`push_guard.py`)이 임시 디렉터리의 원격이어도 기본 브랜치로의 푸시라며 막았다고 적혔다. `git clone --bare`로 푸시 없이 채워 돌렸다. 계획 스킬(`plate:plan`)이 `mktemp -d`의 git 장면을 확인으로 둘 때 원격을 푸시 없이 채우라고 적게 할지 볼 거리다
- `003-base-branch` 문제: task 머리의 완료 조건 1은 "브랜치를 만들거나 바꾼 뒤"를 말하지만 그 확인은 `git switch -c`로 새로 만드는 길만 돌려, 이미 있는 tasks 브랜치로 바꾸는 길에서 앞선 커밋이 tasks 브랜치에 없는 결함(회고 1의 문제)을 수행도 확인도 잡지 못했다. 계획 스킬(`plate:plan`)의 "조건"이 완료 조건의 갈래마다 돌려 보는 확인을 두게 할지 볼 거리다
