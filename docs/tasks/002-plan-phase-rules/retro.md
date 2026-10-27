# 회고

## 회고 1

**확인**
- 1. 두 본문에 세 이슈(#37, #41, #42)의 해결이 적혀 있다
  - plan 본문 "6. 초안을 보여 주고 승인받는다"(갈래마다의 확인·견줄 갈래·`git clone --bare`/`git remote add`로 푸시 없이 채움 점검 줄, 앞 phase 산출물에 기대는 조건 점검 줄), 적는 규칙 "조건"(갈래마다 돌리는 확인, 요약 줄의 견줄 갈래, 원격을 푸시 없이 채우는 두 차림 세 줄), "TODO"("앞 phase의 산출물에 대어 조건을 맞춘다" 또는 "앞 phase의 결과로 정한다" 줄), phase 본문 "1. 읽는다"(읽을 것의 산출물 파일만 읽고 그 밖의 앞 phase 기록은 읽지 않고 "하네스에서 걸린 것"에 적는 줄)를 읽음 → 세 해결이 저마다 있다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 129 tests`, 마지막 줄 `OK`. `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
- 2. 맥락 문서와 README가 1의 동작과 맞는다
  - `docs/PRD.md` 핵심 기능 3·4, `docs/ARCHITECTURE.md` "데이터 흐름"의 계획·실행 갈래, `README.md`의 `plan`·`phase` 행, 두 본문의 description을 읽음 → 갈래마다의 확인, 앞 phase 산출물에 기대는 조건, phase가 앞 phase 기록을 읽지 않는 것과 어긋나는 줄이 없다(phase description은 "앞 phase의 기록은 읽지 않는다"를 적는다). 통과
- 3. 세 장면 결과가 `docs/TOOLS.md`에 있고 기대대로다
  - `docs/TOOLS.md` "Claude Code" 절의 "고친 plan을 장면 E·F로 돌려 본 것"과 "고친 phase를 장면 G로 돌려 본 것"을 읽음 → E·F·G마다 Claude Code 2.1.311, 돌린 시각(E·F 21:16:18, G 21:28:06), 세션 id, 기대한 결과, 본 결과가 있고 본 결과가 기대와 같다. E: 네 갈래마다 setup을 돌려 견주는 확인, 요약 줄 확인의 견줄 갈래, origin을 `git remote add`로 URL만 두고 푸시하지 않음. F: `phase-3.md` 초안 TODO 첫 항목 "앞 phase의 산출물에 대어 조건을 맞춘다". G: 세션 기록 `~/.claude-my/projects/…-tmp-9LxrVnuCdx-repo/937e2145-….jsonl`의 tool_use 입력을 직접 뽑아 `done-phase-1`이 든 것이 없고(Read는 `phase-2.md` 하나), 복제본 `git log`에 `e861f57 001-greet: phase 2`가 있다. 통과
  - `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md plugins/plate/skills/phase/SKILL.md` → `2026-10-27T21:16:02+09:00`. 세 장면의 시각이 모두 늦다. 두 본문의 `git hash-object`(`19eee06…`, `f1c9b08…`)가 TOOLS.md에 적힌 해시와 같다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 129 tests`, `OK`. 통과

**남은 것**
- phase 1: PRD·ARCHITECTURE·README는 어긋나는 줄이 없어 바꾸지 않았고 세 동작을 요약에 새로 적지 않았다 → 문제 아님 (완료 조건 2는 어긋나는 줄이 없는지를 보고, 직접 읽어 어긋나는 줄이 없다)
- phase 1: 고친 동작은 아직 돌려 보지 않았다 → 문제 아님 (phase 2·3이 장면 E~G로 돌렸고 위 확인에서 봤다)
- phase 2: 원격의 내용이 필요한 장면에서 plan이 `git clone --bare`를 고르는지는 돌려 보지 않았다 → 문제 아님 (완료 조건 3의 장면 E는 두 차림 가운데 하나를 기대로 정했고, 본문에는 두 갈래가 모두 적혀 있다. 갈래를 장면으로 두지 않은 것은 FRICTION에 적는다)
- phase 2: 두 장면은 답을 추천안으로만 주었다 → 문제 아님 (완료 조건 3이 추천안으로 답한 장면만 정했다)
- phase 3: 읽을 것에 산출물이 없어 앞 기록이 필요한 꼴("하네스에서 걸린 것"에 적는 갈래)은 돌려 보지 않았다 → 문제 아님 (완료 조건 3의 장면 G는 산출물이 적힌 꼴만 정했고, 그 갈래의 글은 phase 본문 "1. 읽는다"에 있다. FRICTION에 적는다)
- phase 3: 헤드리스로 부른 phase가 사용자가 직접 부른 꼴로 보고하고 run 안내를 붙였다 → 문제 아님 (run이 띄우지 않은 호출이라 phase 본문대로의 동작이고, 장면 G의 기대에 걸리지 않는다)

**문제**
- 없음

**판정**: 통과
