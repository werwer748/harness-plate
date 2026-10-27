# FRICTION

- `001-plan-rules` 문제: `docs/tasks/RUNLOG.md`의 이 task phase 1 확인 에이전트 줄이 `토큰 모름 | 도구 호출 모름 | 시간 모름초`로 적혀, 값을 모를 때 단위 "초"가 "모름" 뒤에 그대로 붙었다. 실행 스킬(`plate:run`)의 `RUNLOG.md` 에이전트 줄 양식에서 모르는 값의 꼴을 정해 둘지 볼 거리다
- `002-check-retro` 문제: phase 1 확인 1의 "하네스에서 걸린 것"에, 불러 온 `plate:check` 스킬(설치된 판)에는 "남은 것"을 보는 단계가 없어 부른 쪽의 지시대로 작업 트리의 `plugins/plate/skills/check/SKILL.md`를 따랐다고 적혔다. plate 자체를 고치는 tasks에서는 설치된 스킬과 작업 트리의 스킬이 어긋나, 실행 스킬(`plate:run`)이 에이전트에게 작업 트리의 본문을 따르라고 따로 일러야 한다
- `002-check-retro` 문제: phase 1 확인 1의 "하네스에서 걸린 것"에 옮겨진 "남은 것: check의 절 번호가 6~8번으로 밀렸다". 절을 더하면 다른 스킬이 번호로 가리키는 곳이 깨질 수 있어, 지금은 run 스킬의 "`plate:check`의 1번"뿐이라 어긋나지 않는다
- `002-check-retro` 문제: phase 1 확인 1의 "하네스에서 걸린 것"에 옮겨진 "남은 것: 바뀐 check와 retro를 헤드리스로 돌려 보지 않았다". tasks 머리의 결정대로 에이전트가 도는 동작은 본문을 읽어서만 확인했다
