# Phase 3: phase 장면 G를 돌린다

**목표**: phase가 앞 phase의 기록을 읽지 않는 것(#42)을 임시 복제본에서 돌려 `docs/TOOLS.md`에 남긴다.

**테스트 먼저**: 아니오 — 스킬을 돌려 보고 `.md`에 적는다

**읽을 것**
- `plugins/plate/skills/phase/SKILL.md`의 "1. 읽는다" 절 (phase 1이 고친 동작)
- `docs/TOOLS.md`의 "Claude Code" 절 (헤드리스 명령의 꼴, 허용 목록, phase 2가 더한 plan 장면 E·F 절)

**TODO**
- [x] 장면 G: 복제본에 `done-phase-1.md`(기록 절과 판정 통과인 확인 절)와, 읽을 것에 phase 1의 산출물 파일이 적힌 `phase-2.md`가 있는 작은 task를 차려 phase 스킬로 phase 2를 수행한다. 그 세션 기록(`~/.claude/projects/` 아래의 그 세션 id의 `.jsonl`)에서 `done-phase-1.md`를 읽은 도구 호출이 없는지와 phase 2의 TODO가 끝나 커밋됐는지 본다 (임시 폴더)
- [x] 결과가 phase 본문의 결함을 보이면 `plugins/plate/skills/phase/SKILL.md`를 고치고 장면 G를 새 복제본에서 다시 돈다 (`plugins/plate/skills/phase/SKILL.md`)
- [x] plan 본문을 고쳤으면 장면 E(복제본에서 plan에 "setup이 `.github/CODEOWNERS`가 없으면 만들고, 있으면 줄을 더하게 바꾼다"를 넘겨 추천안으로 답하면 초안의 완료 조건이 두 갈래마다 돌리는 확인을 두고 git 원격 장면을 푸시 없이 채우는 법(`git clone --bare`나 URL만 둔 `git remote add`)을 적는다)와 장면 F(plan에 "새 스킬 하나를 더하고, 임시 복제본에서 그 스킬을 헤드리스로 돌려 본다"를 넘기면 그 phase의 초안이 TODO 첫 항목이나 결정에 앞 phase의 산출물에 대어 조건을 맞춘다)를 새 복제본에서 다시 돌고 phase 2의 절 아래에 결과를 더한다 (`docs/TOOLS.md`)
- [x] `docs/TOOLS.md`의 plan 장면 E·F 절 뒤에 phase 장면 G 절이 더해진다. task 머리의 결정에 적힌 필드를 적는다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건 1~3의 확인을 모두 돌린다. 완료 조건 3의 장면 E~G는 그 조건에 적힌 기대로 본다

## 한 일
- 장면 G: `mktemp -d`의 복제본(`/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.9LxrVnuCdx/repo`, main `509b234`)의 `tasks/greet` 브랜치에 작은 task `001-greet`(`done-phase-1.md`에 기록 다섯 절과 판정 통과인 `## 확인 1`, 읽을 것에 phase 1의 산출물 `notes/greeting.txt`가 적힌 `phase-2.md`)를 차리고 `claude -p "/plate:phase task 폴더: docs/tasks/001-greet, phase: 2"`로 phase 2를 수행했다. 세션 `937e2145-d2d1-4ed6-879f-7ac55fbb2f08`의 기록에서 `done-phase-1.md`를 인자로 가진 도구 호출이 없고(그 이름은 첫 `ls`의 출력에만 나온다), TODO가 `- [x]`가 되고 `e861f57 001-greet: phase 2`로 커밋된 것을 봤다 (임시 폴더)
- 결과가 phase 본문의 결함을 보이면 고치고 다시 돈다: 결함이 보이지 않아 `plugins/plate/skills/phase/SKILL.md`를 고치지 않았다 (없음)
- plan 본문을 고쳤으면 장면 E·F를 다시 돈다: 이 phase에서 plan 본문을 고치지 않아 다시 돌지 않았다 (없음)
- `docs/TOOLS.md`에 phase 장면 G 절을 더한다: "고친 plan을 장면 E·F로 돌려 본 것" 절 뒤에 "고친 phase를 장면 G로 돌려 본 것" 절을 더했다. Claude Code 버전, 복제본의 main 커밋, 돌린 시각, 세션 id, 차린 task의 꼴, 기대한 결과, 본 결과, 걸린 시간, 막힌 명령, 임시 폴더의 기록 경로(지워질 수 있다고 밝힘)를 적었다 (`docs/TOOLS.md`)

## 확인 결과
- 완료 조건 1, 첫 확인
  - `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"(100행 #37, 101행 #41), 적는 규칙의 조건 줄(236~238행 #37), TODO 줄(288행 #41), `plugins/plate/skills/phase/SKILL.md`의 "1. 읽는다"(37행 #42)를 읽음 → 세 해결이 저마다 있다. 통과
- 완료 조건 1, 둘째 확인
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
- 완료 조건 2
  - `docs/PRD.md` 핵심 기능 3·4, `docs/ARCHITECTURE.md` "데이터 흐름"의 계획과 실행 갈래(60~68행), `README.md`의 `plan`·`phase` 행, 두 본문의 description을 읽음 → 갈래마다의 확인, 앞 phase 산출물에 기대는 조건, phase가 앞 phase 기록을 읽지 않는 것과 어긋나는 줄이 없다(어느 줄도 이 동작을 반대로 적지 않는다). 통과
- 완료 조건 3, 첫 확인
  - `docs/TOOLS.md`의 "고친 plan을 장면 E·F로 돌려 본 것"과 "고친 phase를 장면 G로 돌려 본 것"을 읽음 → 장면 E·F·G마다 Claude Code 버전(2.1.311), 돌린 시각, 세션 id, 기대한 결과, 본 결과가 있고 본 결과가 기대와 같다. 장면 G는 이 phase에서 돌린 결과로 직접 봤다(`done-phase-1.md`를 읽은 도구 호출 없음, TODO 끝나 커밋됨). 통과
- 완료 조건 3, 둘째 확인
  - `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md plugins/plate/skills/phase/SKILL.md` → `2026-10-27T21:16:02+09:00`. 장면 E·F 시작 21:16:18, 장면 G 시작 21:28:06으로 모두 늦다. 통과

## 계획과 달라진 점
- TODO와 완료 조건 3은 세션 기록을 `~/.claude/projects/` 아래로 적었으나, 이 기계는 `CLAUDE_CONFIG_DIR`이 `~/.claude-my`라 `~/.claude-my/projects/` 아래에서 찾았다. `docs/TOOLS.md`의 장면 G 절에 그 경로를 적었다

## 남은 것
- 장면 G는 앞 phase 기록을 읽지 않은 것을 한 번, 읽을 것에 산출물이 적힌 꼴로만 봤다. 읽을 것에 산출물이 없어 앞 기록이 필요한 꼴("하네스에서 걸린 것"에 적는 갈래)은 돌려 보지 않았다
- 장면 G의 수행은 사용자가 직접 부른 것으로 보고 다섯 줄 아래에 run 안내를 붙였다(run이 띄운 꼴과 다르다). 확인에는 걸리지 않는다

## 하네스에서 걸린 것
- 계획(task 머리 완료 조건 3, phase-3 TODO 1)이 세션 기록 위치를 `~/.claude/projects/`로 못박아 `CLAUDE_CONFIG_DIR`을 바꾼 환경과 어긋났다

## 확인 1

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1, 첫 확인: `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"(100행: 갈래마다의 확인, 요약 줄의 견줄 갈래, `git clone --bare`/`git remote add`로 푸시 없이 채움 = #37, 101행: 앞 phase 산출물에 기대는 조건 = #41), 적는 규칙의 조건 줄(236~238행 #37), TODO 줄(288행 #41), `plugins/plate/skills/phase/SKILL.md`의 "1. 읽는다"(37행: 읽을 것에 적힌 산출물 파일만 읽고 그 밖의 앞 phase 기록은 읽지 않고 "하네스에서 걸린 것"에 적음 = #42)를 읽음 → 세 해결이 저마다 있다. 통과
  - 완료 조건 1, 둘째 확인: `python3 -m unittest discover -s tests` → `Ran 129 tests`, 마지막 줄 `OK`. `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - 완료 조건 2: `docs/PRD.md` 핵심 기능 3·4, `docs/ARCHITECTURE.md` "데이터 흐름"의 계획·실행 갈래, `README.md`의 `plan`·`phase` 행, 두 본문의 description(phase의 description은 "앞 phase의 결과는 계획의 읽을 것에 적힌 산출물 파일로만 보고, 앞 phase의 기록은 읽지 않는다"를 적음)을 읽음 → 갈래마다의 확인, 앞 phase 산출물에 기대는 조건, phase가 앞 phase 기록을 읽지 않는 것과 어긋나는 줄이 없다. 통과
  - 완료 조건 3, 첫 확인: `docs/TOOLS.md` "Claude Code" 절의 "고친 plan을 장면 E·F로 돌려 본 것"(317~331행)과 "고친 phase를 장면 G로 돌려 본 것"(333~338행)을 읽음 → 장면 E·F·G마다 Claude Code 버전(2.1.311), 돌린 시각, 세션 id, 기대한 결과, 본 결과가 있고 본 결과가 기대와 같다. 세션 기록을 직접 봄: E(`62e87d97-…`)에 갈래별 기대("한 줄만 있고 줄바꿈 없이 끝남 → …")와 "`git remote add origin https://github.com/werwer748/codeowners-probe.git`로 URL만 둔다. 푸시하지 않는다"가 있음, F(`0dc6d879-…`)에 TODO 첫 항목 "앞 phase의 산출물에 대어 조건을 맞춘다. hello 본문이 부르는 명령을 읽고 …"가 있음, G(`~/.claude-my/projects/…-tmp-9LxrVnuCdx-repo/937e2145-….jsonl`)의 tool_use를 id로 모아 Bash 6, Edit 2, Write 1, Read 1이고 `done-phase-1`을 인자에 가진 호출이 없음(Read는 `phase-2.md` 하나). 복제본의 `git log`에 `e861f57 001-greet: phase 2`가 `phase-2.md`와 `notes/greeting-upper.txt`(`HELLO PLATE`) 두 파일만 넣었고 TODO가 `- [x]`. 통과
  - 완료 조건 3, 둘째 확인: `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md plugins/plate/skills/phase/SKILL.md` → `2026-10-27T21:16:02+09:00`. 장면 E·F 21:16:18, G 21:28:06으로 모두 늦다. 두 본문의 `git hash-object`도 TOOLS.md에 적힌 해시(`19eee06…`, `f1c9b08…`)와 같다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → 129개, `OK`. 통과

**남은 것**
- 장면 G는 읽을 것에 산출물이 적힌 꼴로만 봤고, 앞 기록이 필요한 꼴("하네스에서 걸린 것"에 적는 갈래)은 돌려 보지 않았다 → 돌려 보지 않은 위험. 통과 조건(완료 조건 3의 장면 G)은 읽을 것에 산출물이 적힌 꼴만 기대로 정했고, 완료 조건 1은 본문의 글만 본다. 걸리지 않는다. 하네스에서 걸린 것
- 장면 G의 수행이 사용자가 직접 부른 것으로 보고 run 안내를 붙였다 → 완료 조건 3의 장면 G 기대(기록에 `done-phase-1.md` 읽기 없음, TODO 끝나 커밋)에 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 장면 G는 읽을 것에 산출물이 없어 앞 기록이 필요한 꼴(#42의 "하네스에서 걸린 것"에 적는 갈래)을 돌려 보지 않았다. 계획의 완료 조건 3이 그 갈래를 장면으로 두지 않았다
- 남은 것: 헤드리스로 부른 phase가 run이 띄운 꼴이 아닌 사용자가 직접 부른 꼴로 보고하고 run 안내를 붙였다
- 계획(task 머리 완료 조건 3, phase-3 TODO 1)이 세션 기록 위치를 `~/.claude/projects/`로 못박았으나 이 기계는 `CLAUDE_CONFIG_DIR`이 `~/.claude-my`라 `~/.claude-my/projects/`에서 봤다
- 명령 절의 빌드·린트가 "없음"이다

**판정**: 통과
