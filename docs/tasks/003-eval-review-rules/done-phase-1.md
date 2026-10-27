# Phase 1: eval 본문과 문서를 고친다

**목표**: eval 본문에 #36의 해결이 들어가고 맥락 문서와 README가 맞춰진다.

**테스트 먼저**: 아니오 — `.md`(스킬 본문과 문서)만 고친다

**읽을 것**
- `plugins/plate/skills/eval/SKILL.md` (고칠 본문)
- `plugins/plate/skills/check/SKILL.md`의 "5." 절 (check가 `남은 것:` 줄을 옮기는 꼴)
- `gh issue view 36 --repo werwer748/harness-plate` (원인과 해결책)
- `git show e3836b2:docs/tasks/eval.md` (이슈가 나온 eval 절과 실패 목록)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `README.md` (맥락 문서와 README)

**TODO**
- [x] eval의 "2. 실패를 모아 MAST 유형으로 나눈다"에서 표 아래의 "실패가 아닌 줄" 목록에, `남은 것:`으로 시작하는 줄은 그 task의 회고 절에서 "문제"로 판정된 것만 실패로 센다(잡힌 곳은 그 자리)는 글과, 명령 절의 사실이나 판단을 적은 메모 줄은 실패가 아니라는 글이 더해진다 (#36) (`plugins/plate/skills/eval/SKILL.md`)
- [x] eval 본문 앞머리의 description, `docs/PRD.md`의 핵심 기능 8, `docs/ARCHITECTURE.md`의 "데이터 흐름"의 tasks 끝 갈래, `README.md`의 `eval` 행 가운데 실패로 세는 줄과 어긋나는 줄이 그 동작을 담게 바뀐다 (`plugins/plate/skills/eval/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: eval 본문의 "2. 실패를 모아 MAST 유형으로 나눈다"를 읽어 `남은 것:` 줄의 글과 메모 줄의 글이 저마다 있다. 하나라도 없으면 실패
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
- 완료 조건 2가 참이다.
  - 확인: `docs/PRD.md`의 핵심 기능 8, `docs/ARCHITECTURE.md`의 "데이터 흐름"의 tasks 끝 갈래, `README.md`의 `eval` 행, eval 본문 앞머리의 description을 저마다 읽어 실패로 세는 줄과 어긋나는 줄이 없다

## 한 일
- eval의 "2. 실패를 모아 MAST 유형으로 나눈다"의 "실패가 아닌 줄" 목록에 두 줄을 더했다: 확인 절의 "하네스에서 걸린 것"에서 `남은 것:`으로 시작하는 줄은 그 task의 회고 절 "남은 것"에서 "문제"로 판정된 것만 실패로 세고(잡힌 곳은 그 자리), "문제 아님"이거나 회고가 모으지 않은 줄(계획이 `돌리지 않음`으로 정한 위험도 회고가 "문제"로 판정하지 않았으면)은 실패가 아니다. 명령 절의 사실이나 확인한 쪽의 판단만 적은 메모 줄은 실패가 아니다 (#36) (`plugins/plate/skills/eval/SKILL.md`)
- description, PRD 핵심 기능 8, ARCHITECTURE "데이터 흐름"의 tasks 끝 갈래, README `eval` 행을 읽었다. 넷 모두 어느 줄을 실패로 세는지 적지 않아(`grep -n 'MAST\|실패로 세\|남은 것:'`이 PRD·ARCHITECTURE·ADR·README에서 아무것도 찾지 않음) 1의 동작과 어긋나는 줄이 없어 고치지 않았다 (`plugins/plate/skills/eval/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)

## 확인 결과
- 완료 조건 1이 참이다.
  - `grep -n '남은 것:\|메모 줄' plugins/plate/skills/eval/SKILL.md` → 77행(`남은 것:` 줄은 회고 절에서 "문제"로 판정된 것만 실패로 센다, 잡힌 곳은 그 자리), 78행(메모 줄은 실패가 아니다). 둘 다 "2." 절 안에 있다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 129 tests`, 마지막 줄 `OK`. `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
- 완료 조건 2가 참이다.
  - eval description, `docs/PRD.md` 핵심 기능 8, `docs/ARCHITECTURE.md` "데이터 흐름"의 tasks 끝 갈래, `README.md` `eval` 행을 읽음 → 실패로 세는 줄을 다루는 글이 없어 어긋나는 줄이 없다. 통과

## 계획과 달라진 점
없음

## 남은 것
- 바뀐 eval 2번을 실제로 돌려 보지 않았다. 장면 H로 phase 2가 돌린다

## 하네스에서 걸린 것
없음

## 확인 1

**통과 조건**
- 완료 조건 1이 참이다.
  - eval 본문의 "2. 실패를 모아 MAST 유형으로 나눈다"를 읽음 → "실패가 아닌 줄" 목록에 `남은 것:`으로 시작하는 줄은 그 task의 회고 절 "남은 것"에서 "문제"로 판정된 것만 실패로 세고 잡힌 곳은 그 자리라는 글과, 명령 절의 사실이나 확인한 쪽의 판단만 적은 메모 줄은 실패가 아니라는 글이 저마다 있다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 129 tests`, 마지막 줄 `OK`. `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
- 완료 조건 2가 참이다.
  - `docs/PRD.md` 핵심 기능 8, `docs/ARCHITECTURE.md` "데이터 흐름"의 tasks 끝 갈래, `README.md` `eval` 행, eval 본문 앞머리의 description을 읽음 → 넷 모두 어느 줄을 실패로 세는지 적지 않아("실패를 MAST 유형으로 나눠 세고", "하네스를 여섯 기준으로 A~E로" 수준) 바뀐 2번과 어긋나는 줄이 없다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 129 tests`, `OK`. 통과

**남은 것**
- 바뀐 eval 2번을 실제로 돌려 보지 않았다. 장면 H로 phase 2가 돌린다 → 이 phase의 통과 조건은 본문의 글이 있는지와 문서가 어긋나지 않는지만 보고 eval을 돌린 동작은 보지 않는다(그 동작은 phase 2의 장면 H가 본다). 걸리지 않음. 하네스에서 걸린 것

**실패**
없음

**하네스에서 걸린 것**
- 남은 것: 바뀐 eval 2번을 실제로 돌려 보지 않았다. 장면 H로 phase 2가 돌린다

**판정**: 통과
