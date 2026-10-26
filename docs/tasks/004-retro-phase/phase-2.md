# Phase 2: phase가 부작용과 한계를 남은 것에 적는다

**목표**: phase의 기록 규칙이 수행이 아는 부작용과 한계를 "남은 것"에 적게 하고, ARCHITECTURE가 바뀐 두 스킬과 맞는다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/phase/SKILL.md`의 4번, 기록의 양식, 적는 규칙
- `git show c2a983c^:docs/tasks/003-push-guard/done-phase-2.md` (부작용을 "한 일"에만 적고 "남은 것"을 "없음"으로 둔 곳)
- `docs/ARCHITECTURE.md`

**TODO**
- [x] 기록 양식의 "남은 것"을 `{끝내지 못한 TODO나 막힌 곳, 수행이 아는 부작용과 한계, 그 까닭}`으로 고친다 (`plugins/plate/skills/phase/SKILL.md`)
- [x] 적는 규칙에 생긴다. 고친 것이 다른 꼴이나 다른 곳을 잘못 다룬다는 것처럼 수행이 아는 부작용과 한계는 "한 일"에 적었어도 "남은 것"에 적는다. 상태가 "끝남"이어도 그렇다 (`plugins/plate/skills/phase/SKILL.md`)
- [x] `docs/ARCHITECTURE.md`에서 회고, phase 기록, `FRICTION.md`를 적은 줄이 바뀐 두 스킬과 어긋나면 맞춘다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1의 둘째 확인이 참이다.
  - 확인: phase의 적는 규칙과 기록 양식의 "남은 것"을 읽어, 부작용과 한계를 "남은 것"에 적는 규칙이 둘 다에 있다
- 완료 조건 3이 참이다.
  - 확인: `grep -n '회고\|남은 것\|FRICTION' docs/ARCHITECTURE.md`가 낸 줄을 하나씩 읽어 어긋나는 줄이 없다
- phase 1이 이룬 완료 조건 1의 첫째 확인과 완료 조건 2가 그대로 참이다.
  - 확인: phase 1의 통과 조건 확인을 다시 돌린다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`

## 한 일
- 기록 양식의 "남은 것"을 `{끝내지 못한 TODO나 막힌 곳, 수행이 아는 부작용과 한계, 그 까닭}`으로 고친다: 기록 양식의 "남은 것" 줄을 그 글로 바꿨다 (`plugins/plate/skills/phase/SKILL.md`)
- 적는 규칙에 부작용과 한계를 "남은 것"에 적는 규칙을 더한다: 적는 규칙의 "막힘" 줄 앞에 "고친 것이 다른 꼴이나 다른 곳을 잘못 다룬다는 것처럼 수행이 아는 부작용과 한계는 "한 일"에 적었어도 "남은 것"에 적는다. 상태가 "끝남"이어도 그렇다." 줄을 더했다 (`plugins/plate/skills/phase/SKILL.md`)
- `docs/ARCHITECTURE.md`에서 회고, phase 기록, `FRICTION.md`를 적은 줄이 바뀐 두 스킬과 어긋나면 맞춘다: grep이 낸 26, 29, 49, 62, 63, 79줄을 읽었다. 회고와 `FRICTION.md`를 "tasks 끝에 볼 것"처럼 갈래를 늘어놓지 않고 적어 바뀐 두 스킬과 어긋나지 않아 고치지 않았다 (`docs/ARCHITECTURE.md` 바꾸지 않음)

## 확인 결과
- 완료 조건 1의 둘째 확인이 참이다.
  - `plugins/plate/skills/phase/SKILL.md`의 기록 양식 "남은 것"(`{끝내지 못한 TODO나 막힌 곳, 수행이 아는 부작용과 한계, 그 까닭}`)과 적는 규칙의 새 줄("수행이 아는 부작용과 한계는 "한 일"에 적었어도 "남은 것"에 적는다. 상태가 "끝남"이어도 그렇다")을 읽음 → 둘 다에 있다. 통과
- 완료 조건 3이 참이다.
  - `grep -n '회고\|남은 것\|FRICTION' docs/ARCHITECTURE.md` → 26, 29, 49, 62, 63, 79줄. 하나씩 읽음 → 회고를 맡기는 곳, retro.md와 FRICTION.md에 적는 곳, 회고의 문제를 고칠 phase로 고치는 곳, 회고의 세 번 실패에서 멈추는 곳이고 갈래나 "남은 것"의 내용을 적지 않아 어긋나는 줄이 없다. 통과
- phase 1이 이룬 완료 조건 1의 첫째 확인과 완료 조건 2가 그대로 참이다.
  - `grep -n '고칠 쪽\|경계 밖\|남은 것' plugins/plate/skills/retro/SKILL.md` → 고칠 쪽: 4번(73줄)과 회고 절 양식의 "문제" 줄(145줄). 경계 밖: 4번(75줄), 5번(88줄), `FRICTION.md` 줄 양식(153줄), 적는 규칙(167줄). "남은 것"을 4번 점검에 대어 봄: 77줄. 통과
  - `grep -rn '스킬 후보' plugins/plate/skills docs/ARCHITECTURE.md` → retro 153줄과 eval 31줄은 `경계 밖`을 함께 늘어놓고, eval 161줄은 스킬 후보 갈래 하나만 가리킨다. 통과
- 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 16.343s` / `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- TODO 2의 글이 "적는 규칙에 생긴다."로 시작해 동사가 어색하다. "적는 규칙에 더한다"로 읽고 그 뒤의 글을 규칙으로 더했다.
- 통과 조건 셋째가 "phase 1의 통과 조건 확인을 다시 돌린다"인데 이 스킬은 다른 phase의 파일을 읽지 않으므로, task 머리의 완료 조건 1 첫째 확인과 완료 조건 2의 확인을 돌렸다.

## 확인 1

**통과 조건**
- 완료 조건 1의 둘째 확인이 참이다.
  - `plugins/plate/skills/phase/SKILL.md`를 읽음 → 기록 양식의 "남은 것"(120줄)이 `{끝내지 못한 TODO나 막힌 곳, 수행이 아는 부작용과 한계, 그 까닭}`이고, 적는 규칙(132줄)에 "수행이 아는 부작용과 한계는 "한 일"에 적었어도 "남은 것"에 적는다. 상태가 "끝남"이어도 그렇다"가 있음. 둘 다에 있다. 통과
- 완료 조건 3이 참이다.
  - `grep -n '회고\|남은 것\|FRICTION' docs/ARCHITECTURE.md` → 26, 29, 49, 62, 63, 79줄. 하나씩 읽음 → 회고를 맡기는 곳, retro 스킬을 부르는 곳, 작업 규칙, 회고를 retro.md에 tasks 끝에 볼 것을 FRICTION.md에 적는 곳, 회고의 문제를 고칠 phase로 고치는 곳, 세 번 실패에서 멈추는 곳이고 갈래나 "남은 것"의 내용을 적지 않아 바뀐 두 스킬과 어긋나는 줄이 없다. 통과
- phase 1이 이룬 완료 조건 1의 첫째 확인과 완료 조건 2가 그대로 참이다.
  - `plugins/plate/skills/retro/SKILL.md`를 읽음 → 고칠 쪽: 4번(72줄)과 회고 절 양식 "문제" 줄(145줄). 경계 밖: 4번(74줄), 5번(88줄), `FRICTION.md` 줄 양식(153줄). "남은 것"을 4번 점검에 대어 봄: 76줄. 셋 모두 있음. 통과
  - `grep -rn '스킬 후보' plugins/plate/skills docs/ARCHITECTURE.md` → 세 줄. retro 153줄과 eval 31줄은 넷을 늘어놓고 `경계 밖`이 있음. eval 161줄은 스킬 후보 갈래 하나만 가리킴. 통과
- 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 16.228s`, `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests`, `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 통과 조건 셋째가 "phase 1의 통과 조건 확인을 다시 돌린다"라 다른 phase의 파일(`done-phase-1.md`)을 읽어야 돌릴 수 있었다. check의 1번 읽을 것에는 들지 않아 그 통과 조건만 읽고 돌렸다.

**판정**: 통과
