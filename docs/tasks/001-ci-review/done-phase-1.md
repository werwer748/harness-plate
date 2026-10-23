# Phase 1: 명령 절의 설치 줄

**목표**: 명령 절이 설치, 빌드, 린트, 테스트 네 줄로 정의되고, plan이 설치 명령도 챙기며, 이 저장소의 명령 절에 설치 줄이 생긴다.

**테스트 먼저**: 아니오 — 스킬 본문과 문서(`.md`)만 고친다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (낱말의 명령 절, 3번의 명령 찾기, 5번의 물음, 적는 규칙의 명령 절 고침)
- `plugins/plate/skills/check/SKILL.md` (낱말의 명령 절, 3번)
- `plugins/plate/skills/retro/SKILL.md` (낱말의 명령 절, 3번)
- `plugins/plate/skills/review/SKILL.md` (낱말의 명령 절, 2번)
- `docs/ARCHITECTURE.md` (`## 명령` 절)

**TODO**
- [x] 명령 절의 정의가 설치, 빌드, 린트, 테스트 네 줄이 되고, 없는 명령은 "없음"이다 (`plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/review/SKILL.md`의 낱말)
- [x] plan이 명령 절을 볼 때 설치 명령도 빌드 매니페스트와 코드에서 찾고, 찾지 못하면 묻는다 (`plugins/plate/skills/plan/SKILL.md`의 3번, 5번)
- [x] check, retro, tasks 끝의 review는 설치 명령을 돌리지 않는다고 적힌다 (`plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/review/SKILL.md`)
- [x] 이 저장소의 명령 절에 `- 설치: 없음` 줄이 생긴다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: 완료 조건 1의 확인을 모두 돌린다

## 한 일
- 명령 절의 정의가 설치, 빌드, 린트, 테스트 네 줄이 되고, 없는 명령은 "없음"이다: 네 스킬의 낱말에서 명령 절 정의가 드는 줄 목록 맨 앞에 `- 설치: {명령}`을 더하고 "세 줄"을 "네 줄"로 바꿨다. plan의 정의에는 "설치는 의존성을 설치하는 명령이다"를 더했다 (`plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/review/SKILL.md`)
- plan이 명령 절을 볼 때 설치 명령도 빌드 매니페스트와 코드에서 찾고, 찾지 못하면 묻는다: 3번의 "빌드, 린트, 테스트 가운데 적히지 않은 것"을 "설치, 빌드, 린트, 테스트 가운데"로, 5번의 "3번에서 찾지 못한 명령도"를 "3번에서 찾지 못한 명령(설치, 빌드, 린트, 테스트)도"로 바꿨다. 읽을 것에 적힌 적는 규칙의 명령 절 고침 줄도 "설치, 빌드, 린트, 테스트의 명령이 생기거나 바뀐다"로 바꿨다 (`plugins/plate/skills/plan/SKILL.md`)
- check, retro, tasks 끝의 review는 설치 명령을 돌리지 않는다고 적힌다: check와 retro는 3번 첫 문장 뒤에 "설치는 돌리지 않는다."를 더했다. review는 낱말의 명령 절 정의 끝에 "tasks 끝의 코드 평가는 설치를 돌리지 않는다."를 더했고, 2번의 1(명령 절)은 그대로 빌드, 린트, 테스트만 돌린다 (`plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/review/SKILL.md`)
- 이 저장소의 명령 절에 `- 설치: 없음` 줄이 생긴다: `## 명령` 절의 첫 줄로 `- 설치: 없음`을 더했다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 완료 조건 1이 참이다.
  - `grep -n "설치" plugins/plate/skills/plan/SKILL.md plugins/plate/skills/check/SKILL.md plugins/plate/skills/retro/SKILL.md plugins/plate/skills/review/SKILL.md` → plan:29, check:29, retro:29, review:32에 명령 절 정의의 `` `- 설치: {명령}` `` 줄이 나온다(그 밖에 plan:62, 76, 260, check:48, retro:60, review:60). 통과
  - `grep -c "^- 설치: 없음$" docs/ARCHITECTURE.md` → `1`. 통과
  - `plugins/plate/skills/plan/SKILL.md`의 3번과 5번을 읽음 → 3번(62줄)이 "설치, 빌드, 린트, 테스트 가운데 적히지 않은 것"을 빌드 매니페스트와 코드에서 찾고 찾지 못한 명령은 5번에서 묻는다, 5번(76줄)이 "3번에서 찾지 못한 명령(설치, 빌드, 린트, 테스트)도 여기서 묻는다". check 3번(48줄)과 retro 3번(60줄)은 "설치는 돌리지 않는다", review는 2번의 1이 빌드, 린트, 테스트만 돌리고 명령 절 정의(32줄)에 "tasks 끝의 코드 평가는 설치를 돌리지 않는다"가 있다. 통과

## 계획과 달라진 점
- TODO 3은 review에서 적을 곳을 정하지 않았다. check와 retro는 명령을 돌리는 3번에 적었지만, review는 2번이 아니라 낱말의 명령 절 정의에 적었다. 까닭: task 머리의 완료 조건 2가 phase 1 커밋의 부모부터의 diff로 "tasks 끝 코드 평가의 절차(0~9번)가 명령 절 정의 말고는 바뀌지 않았다"를 보므로, 2번을 고치면 그 확인에 걸린다
- 읽을 것에만 적힌 plan의 적는 규칙(명령 절 고침 줄)에도 설치를 더했다. 까닭: 설치 명령이 생기거나 바뀔 때도 명령 절을 고치는 TODO가 들어가야 완료 조건 1의 "plan이 명령 절을 챙길 때 설치 명령도"와 맞는다

## 남은 것
없음

## 하네스에서 걸린 것
- task 머리의 완료 조건 1의 확인은 "review의 명령을 돌리는 절을 읽어" 설치를 돌리지 않는지 보고, 완료 조건 2의 확인은 review의 0~9번이 "명령 절 정의 말고는" 바뀌지 않았는지 본다. 둘을 함께 맞추려면 review의 설치 문장을 2번이 아닌 정의에 둘 수밖에 없어, review만 check, retro와 적은 자리가 다르다

## 확인 1

**통과 조건**
- 완료 조건 1이 참이다.
  - `grep -n "설치" plugins/plate/skills/plan/SKILL.md plugins/plate/skills/check/SKILL.md plugins/plate/skills/retro/SKILL.md plugins/plate/skills/review/SKILL.md` → 네 파일 모두 명령 절 정의에 `` `- 설치: {명령}` ``으로 시작하는 네 줄 정의가 나온다(plan:29, check:29, retro:29, review:32). 그 밖에 plan:62, 76, 260, check:48, retro:60, review:60이 나온다. 통과
  - `grep -c "^- 설치: 없음$" docs/ARCHITECTURE.md` → `1`. 통과
  - `plugins/plate/skills/plan/SKILL.md`의 3번과 5번, check 3번, retro 3번, review 낱말과 2번을 읽음 → plan 3번(62줄)은 "설치, 빌드, 린트, 테스트 가운데 적히지 않은 것"을 빌드 매니페스트와 코드에서 찾고 찾지 못한 명령은 5번에서 묻는다. plan 5번(76줄)은 "3번에서 찾지 못한 명령(설치, 빌드, 린트, 테스트)도 여기서 묻는다". check 3번(48줄)과 retro 3번(60줄)에 "설치는 돌리지 않는다"가 있다. review 2번의 1은 빌드, 린트, 테스트만 돌리고, 명령 절 정의(32줄)에 "tasks 끝의 코드 평가는 설치를 돌리지 않는다"가 있다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 39 tests in 15.006s`, `OK`(exit 0). 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
