# Phase 2: 규칙 준수 표에 run의 두 꼴을 더한다

**목표**: eval 3번의 규칙 준수 표가 run이 만드는 두 커밋 꼴을 보고, ARCHITECTURE가 바뀐 eval과 맞는다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/eval/SKILL.md`의 낱말 "더한 phase"와 3번의 규칙 준수
- `plugins/plate/skills/run/SKILL.md`에서 `plan: NNN-slug 수정`과 `NNN-slug: phase N 통과`로 커밋하는 곳 모두(넣는 파일을 대어 보려고)
- `git show c2a983c^:docs/tasks/FRICTION.md` (42줄)
- `docs/ARCHITECTURE.md`

**TODO**
- [x] 3번 표에 두 행을 더한다. `plan: NNN-slug 수정`(만든 스킬 run, 넣어도 되는 파일: 더한 `phase-M.md`, 고친 계획 파일, `RUNLOG.md`)과 `NNN-slug: phase N 통과`(만든 스킬 run, 넣어도 되는 파일: 그 `phase-N.md`를 `done-phase-N.md`로 바꾼 이름 바꾸기와 `RUNLOG.md`). 넣어도 되는 파일은 run 본문에서 그 메시지로 커밋하는 곳마다 대어 보고 적는다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] 낱말 "더한 phase"가 바뀐 표와 어긋나지 않게 맞춘다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] `docs/ARCHITECTURE.md`에서 eval을 적은 줄이 바뀐 eval과 어긋나면 맞춘다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1의 둘째, 셋째 확인이 참이다.
  - 확인: 3번 표를 읽어 두 행과 넣어도 되는 파일이 완료 조건 1에 적힌 대로 있다
  - 확인: `grep -n 'plan: NNN-slug 수정' plugins/plate/skills/eval/SKILL.md`가 낱말의 줄과 표의 줄을 둘 다 낸다
- 완료 조건 2가 참이다.
  - 확인: `grep -n 'plan: NNN-slug 수정\|phase N 통과' plugins/plate/skills/run/SKILL.md`가 낸 줄마다 넣는 파일이 eval 표의 같은 행에 모두 든다
- 완료 조건 3이 참이다.
  - 확인: `grep -n 'eval\|규칙 준수\|실패 양상' docs/ARCHITECTURE.md`가 낸 줄을 하나씩 읽어 어긋나는 줄이 없다
- phase 1이 이룬 완료 조건 1의 첫째 확인이 그대로 참이다.
  - 확인: phase 1의 통과 조건 확인을 다시 돌린다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`

## 한 일
- 3번 표에 두 행을 더한다: `NNN-slug: phase N 통과`(run, 그 `phase-N.md`를 `done-phase-N.md`로 바꾼 이름 바꾸기와 `RUNLOG.md`)와 `plan: NNN-slug 수정`(run, 더한 `phase-M.md`, 고친 계획 파일(tasks 머리, task 머리, `phase-N.md`의 계획 다섯 항목), `RUNLOG.md`)을 `NNN-slug: phase N 확인` 행 아래에 더했다. run 본문에서 그 메시지로 커밋하는 곳(6번 2단계, 회고 뒤 phase를 더하는 곳, "멈춘다" 4번)을 대어 보고 적었다 (`plugins/plate/skills/eval/SKILL.md`)
- 낱말 "더한 phase"가 바뀐 표와 어긋나지 않게 맞춘다: "`plan:`으로 시작하는 메시지로 커밋하므로"를 "멈춘 뒤 계획을 고칠 때와 같은 메시지(`plan: NNN-slug 수정`)로 커밋하므로"로 바꾸고, 그 커밋의 넣어도 되는 파일은 3번 표에 있다는 문장을 더했다 (`plugins/plate/skills/eval/SKILL.md`)
- `docs/ARCHITECTURE.md`에서 eval을 적은 줄이 바뀐 eval과 어긋나면 맞춘다: grep이 낸 26, 31, 48, 49, 50, 65줄을 읽었다. 실패 모으기나 규칙 준수 표의 내용을 적은 줄이 없어 고치지 않았다 (`docs/ARCHITECTURE.md` 바꾸지 않음)

## 확인 결과
- 3번 표를 읽어 두 행과 넣어도 되는 파일이 완료 조건 1에 적힌 대로 있다
  - `sed -n '125,137p' plugins/plate/skills/eval/SKILL.md` → 132줄 `NNN-slug: phase N 통과` | run | 이름 바꾸기와 `RUNLOG.md`, 133줄 `plan: NNN-slug 수정` | run | 더한 `phase-M.md`, 고친 계획 파일(tasks 머리, task 머리, `phase-N.md`의 계획 다섯 항목), `RUNLOG.md`. 통과
- `grep -n 'plan: NNN-slug 수정' plugins/plate/skills/eval/SKILL.md`가 낱말의 줄과 표의 줄을 둘 다 낸다
  - → 36줄(낱말 "더한 phase")과 133줄(표). 통과
- `grep -n 'plan: NNN-slug 수정\|phase N 통과' plugins/plate/skills/run/SKILL.md`가 낸 줄마다 넣는 파일이 eval 표의 같은 행에 모두 든다
  - → 140줄 "이 변경(이름 바꾸기)과 `RUNLOG.md`" ⊂ `phase N 통과` 행. 177줄 "`phase-M.md`와 `RUNLOG.md`" ⊂ `plan: NNN-slug 수정` 행. 245줄 "고친 계획 파일과 `RUNLOG.md`"(run 31줄의 계획 파일: tasks 머리, task 머리, `phase-N.md`의 계획 다섯 항목) ⊂ `plan: NNN-slug 수정` 행. 통과
- `grep -n 'eval\|규칙 준수\|실패 양상' docs/ARCHITECTURE.md`가 낸 줄을 하나씩 읽어 어긋나는 줄이 없다
  - → 26, 31, 48, 49, 50, 65줄. 어느 줄도 eval의 실패 모으기, 규칙 준수 표를 적지 않아 어긋남 없음. 통과
- phase 1의 통과 조건 확인을 다시 돌린다(완료 조건 1의 첫째 확인)
  - `sed -n '64,80p' plugins/plate/skills/eval/SKILL.md` → 74줄 tasks 끝 행이 "그 절의 "하네스에서 걸린 것" 가운데 하네스의 규칙이나 계획에서 걸린 줄"만 들고, 77줄에 "측정 못함의 까닭(측정 도구가 없다, 환경이 막는다)만 적은 줄은 실패가 아니다"가 있다. 통과
- `python3 -m unittest discover -s tests`가 `OK`
  - → `Ran 99 tests in 16.196s` / `OK`. 통과

## 계획과 달라진 점
- 완료 조건 1과 TODO는 `plan: NNN-slug 수정`의 고친 계획 파일을 "(tasks 머리, task 머리)"로 적었으나, 표에는 `phase-N.md`의 계획 다섯 항목도 넣었다. run의 "계획 파일" 낱말(31줄)이 이를 들고 "멈춘다" 4번(245줄)이 그것을 커밋하므로, 빼면 완료 조건 2(run과 어긋나지 않음)가 거짓이 된다.

## 남은 것
- 없음

## 하네스에서 걸린 것
- 계획의 읽을 것인 `git show c2a983c^:docs/tasks/FRICTION.md`(42줄)는 이 phase의 TODO에 쓸 사실(`NNN-slug: phase N 통과` 꼴이 표에 없다는 고칠 거리)을 확인하는 데만 썼다. 완료 조건 1의 "고친 계획 파일(tasks 머리, task 머리)"가 run의 계획 파일 낱말보다 좁아 위의 달라진 점이 생겼다.

## 확인 1

**통과 조건**
- 완료 조건 1의 둘째, 셋째 확인이 참이다.
  - `sed -n '120,140p' plugins/plate/skills/eval/SKILL.md` → 132줄 `NNN-slug: phase N 통과` | run | 그 `phase-N.md`를 `done-phase-N.md`로 바꾼 이름 바꾸기와 `RUNLOG.md`, 133줄 `plan: NNN-slug 수정` | run | 더한 `phase-M.md`, 고친 계획 파일(tasks 머리, task 머리, `phase-N.md`의 계획 다섯 항목), `RUNLOG.md`. 완료 조건 1이 적은 파일이 모두 들고, 더 든 `phase-N.md`의 계획 다섯 항목은 run의 "계획 파일" 낱말(run 31줄)과 같다. 통과
  - `grep -n 'plan: NNN-slug 수정' plugins/plate/skills/eval/SKILL.md` → 36줄(낱말 "더한 phase")과 133줄(3번 표). 통과
- 완료 조건 2가 참이다.
  - `grep -n 'plan: NNN-slug 수정\|phase N 통과' plugins/plate/skills/run/SKILL.md` → 140줄 "이 변경(이름 바꾸기)과 `RUNLOG.md`" ⊂ eval 132줄 행. 177줄 "`phase-M.md`와 `RUNLOG.md`" ⊂ eval 133줄 행. 245줄 "고친 계획 파일과 `RUNLOG.md`"(run 31줄: tasks 머리, task 머리, `phase-N.md`의 계획 다섯 항목) ⊂ eval 133줄 행. 통과
- 완료 조건 3이 참이다.
  - `grep -n 'eval\|규칙 준수\|실패 양상' docs/ARCHITECTURE.md` → 26, 31, 48, 49, 50, 65줄. 모두 eval의 위치, 부르는 때, 절대 규칙, 푸시 규칙, tasks 끝 흐름만 적고 실패 모으기나 규칙 준수 표를 적지 않아 어긋나는 줄이 없다. 통과
- phase 1이 이룬 완료 조건 1의 첫째 확인이 그대로 참이다.
  - `sed -n '64,80p' plugins/plate/skills/eval/SKILL.md` → 74줄 tasks 끝 행이 "그 절의 "하네스에서 걸린 것" 가운데 하네스의 규칙이나 계획에서 걸린 줄"만 들고, 77줄 표 아래 목록에 "측정 못함의 까닭(측정 도구가 없다, 환경이 막는다)만 적은 줄은 실패가 아니다"가 있다. 통과
- 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.969s` / `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests` / `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
