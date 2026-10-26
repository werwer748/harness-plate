# Phase 1: 환경의 한계를 실패로 세지 않는다

**목표**: eval 2번이 코드 평가의 측정 못함 까닭을 실패로 세지 않는다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/eval/SKILL.md`의 낱말("측정 못함", "잡힌 곳", "실패")과 2번
- `plugins/plate/skills/review/SKILL.md`에서 "하네스에서 걸린 것"과 "측정 못함"을 적는 곳
- `git show c2a983c^:docs/tasks/review.md` (평가 1의 "하네스에서 걸린 것")
- `git show c2a983c^:docs/tasks/FRICTION.md` (41줄)

**TODO**
- [x] 2번 모으는 곳 표의 tasks 끝 행을 고친다. 마지막 평가 절에서 실패한 완료 조건의 확인, 신뢰성의 문제, "하네스에서 걸린 것" 가운데 하네스의 규칙이나 계획에서 걸린 줄을 모은다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] 2번 표 아래 목록에 생긴다. 코드 평가의 "하네스에서 걸린 것" 가운데 측정 못함의 까닭(측정 도구가 없다, 환경이 막는다)만 적은 줄은 실패가 아니다. 그런 줄은 5번의 이 프로젝트만의 고칠 거리를 정할 때만 본다 (`plugins/plate/skills/eval/SKILL.md`)

**통과 조건**
- 완료 조건 1의 첫째 확인이 참이다.
  - 확인: 2번을 읽어 tasks 끝 행의 범위와 측정 못함 까닭을 빼는 규칙이 둘 다 있다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`

## 한 일
- 2번 모으는 곳 표의 tasks 끝 행을 고친다: 행을 "`review.md`의 마지막 평가 절에서 실패한 완료 조건의 확인, 신뢰성의 문제, 그 절의 "하네스에서 걸린 것" 가운데 하네스의 규칙이나 계획에서 걸린 줄"로 바꿨다 (`plugins/plate/skills/eval/SKILL.md`)
- 2번 표 아래 목록에 생긴다: "프로젝트의 규칙을 따름" 줄 바로 아래에 "코드 평가의 "하네스에서 걸린 것" 가운데 측정 못함의 까닭(측정 도구가 없다, 환경이 막는다)만 적은 줄은 실패가 아니다. 그런 줄은 5번에서 이 프로젝트만의 고칠 거리를 정할 때만 본다."를 더했다 (`plugins/plate/skills/eval/SKILL.md`)

## 확인 결과
- 완료 조건 1의 첫째 확인이 참이다.
  - `plugins/plate/skills/eval/SKILL.md` 68~78줄을 읽음 → 74줄 tasks 끝 행이 하네스의 규칙이나 계획에서 걸린 줄만 들고, 77줄에 측정 못함 까닭을 적은 줄은 실패가 아니라는 규칙이 있다. 통과
- 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.826s` / `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 없음
