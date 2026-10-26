# eval의 실패 모으기와 규칙 준수 표를 고친다

## 목표
eval 2번이 코드 평가의 "하네스에서 걸린 것" 가운데 측정 못함의 까닭(도구가 없다, 환경이 막는다)을 실패로 세지 않고, tasks 끝의 실패를 완료 조건 확인의 실패, 신뢰성 문제, 하네스의 규칙이나 계획에서 걸린 것으로 둔다(#15). eval 3번의 규칙 준수 표에 run이 만드는 `plan: NNN-slug 수정`과 `NNN-slug: phase N 통과`를 넣어도 되는 파일과 함께 더한다(#16).

## 범위 밖
- 등급표의 칸과 기준
- review가 "하네스에서 걸린 것"에 적는 규칙
- tasks가 끝난 뒤의 run 커밋(`<tasks 이름>: BACKLOG`, `<tasks 이름>: RUNLOG`, `<tasks 이름>: 비움`). eval이 돈 뒤에 생겨 eval이 보는 커밋에 들지 않는다
- `FRICTION.md`의 `경계 밖` 갈래. `004-retro-phase`에서 한다

## 완료 조건
1. tasks 완료 조건 10이 참이다.
   - 확인: `plugins/plate/skills/eval/SKILL.md`의 2번을 읽어 둘을 찾는다. 첫째, 모으는 곳 표의 tasks 끝 행이 코드 평가의 "하네스에서 걸린 것" 가운데 하네스의 규칙이나 계획에서 걸린 줄만 든다. 둘째, 측정 못함의 까닭(도구가 없다, 환경이 막는다)을 적은 줄은 실패가 아니라는 규칙이 표 아래 목록에 있다
   - 확인: 3번의 규칙 준수 표를 읽어 두 행이 있다. `plan: NNN-slug 수정`은 만든 스킬이 run이고 넣어도 되는 파일이 더한 `phase-M.md`, 고친 계획 파일(tasks 머리, task 머리), `RUNLOG.md`다. `NNN-slug: phase N 통과`는 만든 스킬이 run이고 넣어도 되는 파일이 그 phase의 이름 바꾸기와 `RUNLOG.md`다
   - 확인: `grep -n 'plan: NNN-slug 수정' plugins/plate/skills/eval/SKILL.md`가 낱말 "더한 phase"의 줄과 3번 표의 줄을 둘 다 낸다
2. 바뀐 eval이 run과 어긋나지 않는다.
   - 확인: `grep -n 'plan: NNN-slug 수정\|phase N 통과' plugins/plate/skills/run/SKILL.md`가 낸 줄마다, 그 줄이 넣는다고 한 파일이 eval 표의 같은 메시지 행의 넣어도 되는 파일에 모두 든다
3. `docs/ARCHITECTURE.md`에서 eval을 적은 줄이 바뀐 eval과 어긋나지 않는다.
   - 확인: `grep -n 'eval\|규칙 준수\|실패 양상' docs/ARCHITECTURE.md`가 낸 줄을 하나씩 읽어 어긋나는 줄이 없다

## 결정
- 없음
