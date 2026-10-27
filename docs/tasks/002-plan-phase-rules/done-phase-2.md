# Phase 2: plan 장면 E와 F를 돌린다

**목표**: 갈래마다의 확인(#37)과 앞 phase 산출물에 기대는 조건(#41)을 임시 복제본에서 plan으로 돌려 `docs/TOOLS.md`에 남긴다.

**테스트 먼저**: 아니오 — 스킬을 돌려 보고 `.md`에 적는다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건", "TODO" 절 (phase 1이 고친 동작)
- `docs/TOOLS.md`의 "Claude Code" 절 (헤드리스 명령의 꼴, `--resume`, "스킬을 헤드리스로 돌려 볼 때의 허용 목록", 장면 절의 꼴)

**TODO**
- [x] 장면 E: 복제본에서 plan에 "setup이 `.github/CODEOWNERS`가 없으면 만들고, 있으면 줄을 더하게 바꾼다"를 넘기고, 물음마다 `--resume`으로 추천안을 골라 초안을 보여 주고 승인을 묻는 자리까지 잇는다. 보여 준 초안의 완료 조건이 없을 때와 있을 때의 두 갈래마다 돌리는 확인을 두고, git 원격이 있는 장면을 `git clone --bare`로 채운다고 적었는지 본다 (임시 폴더)
- [x] 장면 F: 새 복제본에서 plan에 "새 스킬 하나를 더하고, 임시 복제본에서 그 스킬을 헤드리스로 돌려 본다"를 넘기고 같은 방법으로 task 초안을 보여 주는 자리까지 잇는다. 스킬을 돌려 보는 phase의 초안이 TODO 첫 항목이나 결정에 앞 phase의 산출물에 대어 조건을 맞춘다고 적었는지 본다 (임시 폴더)
- [x] plan 본문의 #37 글(적는 규칙 "조건"과 6번 점검)을 "푸시 없이 채운다. 원격의 내용이 필요하면 `git clone --bare`, URL만 보면 `git remote add`로 URL만 둔다"로 넓히고, 두 장면을 새 복제본에서 다시 돈다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] `docs/TOOLS.md`의 "Claude Code" 절 끝에 plan 장면 E·F 절이 더해진다. task 머리의 결정에 적힌 필드를 장면마다 적는다 (`docs/TOOLS.md`)

**통과 조건**
- 장면 E와 F의 결과가 남았고 기대대로다(완료 조건 3의 E, F).
  - 확인: 더해진 절을 읽어 장면 E·F마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있고 본 결과가 기대와 같다. 장면 E의 기대는 초안의 완료 조건이 두 갈래마다 돌리는 확인을 두고 git 원격 장면을 푸시 없이 채우는 법(`git clone --bare`나 URL만 둔 `git remote add`)을 적은 것, 장면 F의 기대는 스킬을 돌려 보는 phase의 초안이 TODO 첫 항목이나 결정에 앞 phase의 산출물에 대어 조건을 맞춘다고 적은 것이다
  - 확인: 그 절의 돌린 시각이 `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md`보다 늦다
- 완료 조건 1이 여전히 참이다(이 phase가 plan 본문을 고쳤을 때).
  - 확인: plan 본문의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건", "TODO" 절, phase 본문의 "1. 읽는다" 절을 읽어 세 해결이 저마다 적혀 있다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`

## 한 일
- (첫 수행) 아래 둘은 #37의 원격 차림을 `git clone --bare` 하나로 적은 plan 본문(커밋 2026-10-27T20:54:45+09:00)으로 돌린 것이다. 장면 E가 기대와 달라 "계획이 틀림"으로 멈췄고, 계획 수정(`fe2879f plan: 002-plan-phase-rules 수정`)으로 TODO 3이 더해졌다
  - 장면 E: 돌렸다. 기대의 두 쪽 가운데 갈래마다의 확인은 기대대로이고, git 원격을 `git clone --bare`로 채운다는 쪽은 기대와 다르다(그 뒤 계획 수정으로 TODO 3이 됐다). 걸린 것은 Claude Code 2.1.311, plan 본문은 phase 1이 고친 것(마지막 커밋 2026-10-27T20:54:45+09:00), 복제본 main은 `509b234 Merge pull request #45 from werwer748/tasks/cleanup`이다. 복제본은 `mktemp -d`의 `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.ixJoXa5EcF/repo`에 `git clone --branch main /Users/hugo/Desktop/harness-plate`로 만들고 `git remote set-head origin main`을 했다. 플러그인은 `--plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate`, 허용 목록은 `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"의 13개, 옵션은 `--permission-mode acceptEdits --output-format stream-json --verbose`다. 세션 id `7592bfe8-0336-40a1-95f4-c713753edf1e`, 첫 턴 2026-10-27T20:56:29+09:00에 시작해 열째 턴이 21:05:43에 끝났다. 기록은 `…/tmp.ixJoXa5EcF/turnE1.jsonl`~`turnE10.jsonl`이고 임시 폴더라 지워질 수 있다 (임시 폴더)
    - 턴: 1 `/plate:plan setup이 \`.github/CODEOWNERS\`가 없으면 만들고, 있으면 줄을 더하게 바꾼다` → 요청이 ADR-023·ARCHITECTURE와 어긋난다며 A(문서를 바꾸고 진행, 추천)/B/C를 물음. 2~7 추천안 → 훅의 덧붙임 처리(A), 더할 줄(A, 같은 패턴이 있으면 더하지 않음), 같은 패턴의 판정(A, 첫 칸 글자 비교), 버전(A, 0.17.0), 돌려 보는 법(A, 시험 저장소에서 `claude -p`로 setup), 엣지케이스(A, 논의 안 함). 8 → tasks 머리 초안. 9 "tasks 머리 초안을 승인한다" → task 001(`001-guard-append`) 초안. 10 "task 001 초안을 승인한다" → task 002(`002-setup-append`) 초안. 마지막 초안은 승인하지 않았고, 끝난 뒤 복제본의 HEAD는 `509b234` 그대로, `git status --short`는 비었다
    - 갈래마다의 확인(기대대로): tasks 머리 완료 조건 2의 확인이 "시험 저장소 넷(없음, 다른 줄만 있음, `/.github/workflows/` 줄만 있음, 두 패턴 다 있음)마다" setup을 부르고, task 002의 결정 "갈래와 기대"가 네 갈래의 끝난 내용을 저마다 적고, phase 2의 통과 조건이 네 갈래의 `cmp`를 저마다 본다. 요약 줄의 확인에 견줄 갈래도 있다(tasks 완료 조건 3 "두 갈래가 함께 있거나 '없을 때만 쓴다'는 옛 동작이 남지 않는다", task 002 완료 조건 3 "모두 두 갈래를 적고"). task 001의 완료 조건 1도 "남은 phase가 없을 때와 테스트 먼저인 phase에서" 덧붙임의 통과와 막음을 갈래마다 시험한다
    - git 원격(기대와 다름): tasks 머리 결정은 "시험 저장소의 GitHub 원격은 `git remote add`로 URL만 두고 푸시하지 않는다", task 002 결정은 "`git remote add origin https://github.com/werwer748/codeowners-probe.git`(URL만 두고 푸시하지 않는다)"다. 어디에도 `git clone --bare`가 없다. 푸시 없이 채우는 법을 적었으나 기대한 `git clone --bare`는 아니다
    - 막힌 명령: 메인에서 2개. 턴 1의 명령 치환을 이은 `grep -n '"version"' …`("A nested command … can't be checked"), 턴 10의 `grep -rn … | cut -c1-200; gh api user --jq .login`(`cut`과 `gh api`가 허용 목록에 없다). Agent 호출은 0
  - 장면 F: 돌렸다. 기대대로다. 복제본 `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.elMEM59RVT/repo`(만든 법, main, 플러그인, 허용 목록, 옵션은 장면 E와 같다). 세션 id `730a8d3e-3b75-45b3-8b90-3e26257c7897`, 첫 턴 2026-10-27T20:56:29+09:00에 시작해 열두째 턴이 21:03:35에 끝났다. 기록은 `…/tmp.elMEM59RVT/turnF1.jsonl`~`turnF12.jsonl`이고 임시 폴더라 지워질 수 있다 (임시 폴더)
    - 턴: 1 `/plate:plan 새 스킬 하나를 더하고, 임시 복제본에서 그 스킬을 헤드리스로 돌려 본다` → 더할 스킬이 무엇인지 물음. 추천 (가)는 "직접 정한 스킬을 적어 달라"여서 2에 "(가). 스킬 이름은 `hello`다. 사용자가 `/plate:hello`로 부르면 `docs/HELLO.md`에 오늘 날짜와 인사 한 줄을 더하고 그 파일만 커밋한다. 묻는 자리는 없다."로 답했다. 3~10 추천안 → 줄의 꼴, 없을 때, 문서 지도, 셋업, git 아님, 커밋 메시지, 버전과 문서, 테스트, 헤드리스 장면 셋. 11 → tasks 머리 초안(이름 `hello-skill`). 12 "tasks 머리 초안을 승인한다" → task 001(`001-hello-skill`) 초안. 마지막 초안은 승인하지 않았고, 복제본의 HEAD는 `509b234` 그대로, `git status --short`는 비었다
    - 본 결과: 스킬을 돌려 보는 `phase-2.md` 초안의 TODO 첫 항목이 "앞 phase의 산출물에 대어 조건을 맞춘다. `plugins/plate/skills/hello/SKILL.md`가 부르게 하는 명령(날짜 얻기, `git` 명령)을 보고, task 머리 결정의 허용 목록에 빠진 항목(예: `"Bash(date:*)"`)을 더해 이 phase에서 쓸 `--allowedTools`를 정한다"이고, task 머리 결정의 확인용 실행이 "`--allowedTools`는 … 목록에서 시작해 phase 1이 쓴 본문의 명령에 맞춘다(phase 1의 결과로 정한다)"다. 질문 10의 답글에도 "그 phase의 첫 TODO에서 다시 맞추도록 적겠습니다"가 있었다. TODO 첫 항목과 결정 둘 다에 있다
    - 막힌 명령: 메인에서 2개. 턴 1의 `for f in …; do cat "$f"; done`(변수), 턴 10의 `git show … | head -12; git show … | sed -n …`(`sed`). Agent 호출은 0
- plan 본문의 #37 글(적는 규칙 "조건"과 6번 점검)을 "푸시 없이 채운다. 원격의 내용이 필요하면 `git clone --bare`, URL만 보면 `git remote add`로 URL만 둔다"로 넓히고, 두 장면을 새 복제본에서 다시 돈다: 6번의 점검 줄을 "git 원격이 있어야 하는 장면에 푸시 없이 채우는 법(원격의 내용이 필요하면 `git clone --bare`로 만든 저장소, URL만 보면 `git remote add`로 URL만 둔다)이 적혀 있는지도 본다"로, 적는 규칙 "조건"의 줄을 "그 원격을 푸시 없이 채우는 법을 확인이나 결정에 적는다. 원격의 내용(브랜치, 커밋)이 필요하면 `git clone --bare`로 만든 저장소로 채우고, 원격의 URL만 보면(GitHub 원격인지 보는 장면처럼) `git remote add`로 URL만 둔다. 푸시로 채우지 않는다"로 바꿨다. 커밋 `584ae16`(2026-10-27T21:16:02+09:00, 본문 해시 `19eee06edc1daf93b472921518396a614d9b9fd2`) 뒤 새 복제본 둘(`/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.XesauNiY37/repo`, `…/tmp.ICuIxE73mN/repo`, main `509b234`, 복제한 뒤 `git remote set-head origin main`)에서 Claude Code 2.1.311로 다시 돌렸다 (`plugins/plate/skills/plan/SKILL.md`, 임시 폴더)
  - 장면 E: 세션 `62e87d97-c7c3-4d0b-8e98-9740e7636234`, 21:16:18~21:20:10, 턴 일곱(요청, 추천안 여섯). 일곱째 턴의 tasks 머리 초안에 보는 글이 모두 있어 승인하지 않았다. 완료 조건 2의 확인이 네 갈래(없음, 다른 줄만, 한 줄만·줄바꿈 없음, 두 줄 다)마다 setup을 돌려 바이트로 견주고, 완료 조건 4의 요약 줄 확인이 "만드는 갈래와 더하는 갈래를 둘 다 적었는지" 견주고, origin은 "`git remote add origin https://github.com/werwer748/codeowners-probe.git`로 URL만 둔다. 푸시하지 않는다"다. 기대대로. 막힌 명령 0, Agent 0
  - 장면 F: 세션 `0dc6d879-5d3f-48a0-845d-dd5b696d5822`, 21:16:18~21:24:17, 턴 열둘(첫 물음에는 지난 수행과 같은 `hello` 스킬로 답했다). tasks 머리 초안을 승인하고 받은 task `001-hello-skill` 초안의 `phase-3.md`(스킬을 돌려 보는 phase) TODO 첫 항목이 "앞 phase의 산출물에 대어 조건을 맞춘다. hello 본문이 부르는 명령을 읽고, task 머리 결정의 허용 목록에 맞지 않는 것이 있으면 그 항목을 더해 돌린다 …"다. 기대대로. 마지막 초안은 승인하지 않았다. 막힌 명령 2(턴 1의 `for` 변수, 이은 `grep -v`), Agent 0
  - 두 복제본 모두 끝난 뒤 HEAD `509b234`, `git status --short` 비었음
- `docs/TOOLS.md`의 "Claude Code" 절 끝에 plan 장면 E·F 절이 더해진다: `## Codex` 앞에 "고친 plan을 장면 E·F로 돌려 본 것" 절을 더했다. 머리에 버전, 본문 커밋과 해시, 복제본 차림, 플러그인, 허용 목록, 옵션, 명령 꼴, 기록이 지워질 수 있다는 것을 적고, 장면마다 넘긴 요청, 시각, 걸린 시간(`duration_ms` 합), 세션 id, 복제본과 기록 경로, 턴, 기대한 결과, 본 결과, 막힌 명령을 적었다. `--allowedTools` 뒤 프롬프트가 삼켜지는 것과 첫 수행의 `git clone --bare` 경위도 한 줄씩 적었다 (`docs/TOOLS.md`)

## 확인 결과
- 장면 E와 F의 결과가 남았고 기대대로다(완료 조건 3의 E, F).
  - `docs/TOOLS.md`의 "고친 plan을 장면 E·F로 돌려 본 것" 절을 읽음 → 장면 E·F마다 Claude Code 버전(2.1.311), 돌린 시각, 세션 id, 기대한 결과, 본 결과가 있고, E는 갈래마다의 확인과 URL만 둔 `git remote add`(푸시 없음), F는 `phase-3.md` 초안의 TODO 첫 항목 "앞 phase의 산출물에 대어 조건을 맞춘다"로 본 결과가 기대와 같다. 통과
  - `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md` → `2026-10-27T21:16:02+09:00`. 두 장면의 시작 21:16:18이 더 늦다. 통과
- 완료 조건 1이 여전히 참이다(이 phase가 plan 본문을 고쳤다).
  - plan 본문 6번(100·101번째 줄)과 적는 규칙 "조건"(갈래마다의 확인, 견줄 갈래, 푸시 없이 채우는 두 차림)과 "TODO"(앞 phase의 산출물에 대어 조건을 맞춘다), phase 본문 "1. 읽는다"(읽을 것의 산출물 파일만 읽고 그 밖은 "하네스에서 걸린 것"에 적는다)를 읽음 → 세 해결이 저마다 있다. 통과
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과

## 계획과 달라진 점
- 결정은 plan 장면을 보는 글이 든 초안까지 잇는다고 했고, 장면 E는 tasks 머리 초안에 보는 글이 모두 있어 거기서 멈췄다(task 초안까지 가지 않았다). 첫 수행은 task 002 초안까지 갔다
- 장면 F의 첫 물음은 추천안이 "사용자가 스킬을 정한다"여서 `hello` 스킬을 지어 답했다(첫 수행과 같다)
- 시각 확인이 plan 본문의 마지막 커밋보다 늦은 장면을 요구해, 본문 고침을 장면 전에 따로 커밋했다(`584ae16 002-plan-phase-rules: phase 2 (plan 본문 #37 넓힘)`). 기록과 `docs/TOOLS.md`는 그 뒤 `002-plan-phase-rules: phase 2` 커밋으로 넣는다. phase 커밋이 둘이다

## 남은 것
- 장면 E는 setup처럼 원격의 URL만 보는 요청이라 `git remote add` 갈래만 나왔다. 원격의 내용이 필요한 장면에서 plan이 `git clone --bare`를 고르는지는 돌려 보지 않았다
- 두 장면은 대화의 답을 추천안으로만 주었다. 다른 답에서의 초안은 보지 않았다

## 하네스에서 걸린 것
- 계획의 결정 "plan 장면(E, F)은 초안을 보여 주고 승인을 묻는 자리까지만 돌리고 승인하지 않는다"가 F의 TODO "task 초안을 보여 주는 자리까지 잇는다"와 맞지 않는다. task 초안은 tasks 머리 초안을 승인해야 나온다. "마지막 초안을 승인하지 않는다"로 읽고 앞 초안은 승인했다
- 장면 E의 기대가 #37의 해결책을 한 가지 차림(`git clone --bare`)으로 좁혀 적어, URL만 필요한 장면(setup의 GitHub 원격)에서 plan이 맞게 고른 다른 차림을 실패로 만든다. 계획할 때 장면 E의 요청이 어떤 원격을 요구하는지 보지 않았다
- 헤드리스 명령의 꼴: `--allowedTools`는 값을 여럿 받는 옵션이라 그 뒤에 둔 프롬프트를 값으로 삼켜 "Input must be provided either through stdin or as a prompt argument"로 끝났다. 프롬프트를 `-p` 바로 뒤에 두어 풀었다. `docs/TOOLS.md`의 헤드리스 명령 꼴에 적을 만하다
- 허용 목록(`docs/TOOLS.md`의 13개)으로 plan을 돌려도 메인에서 이은 Bash 4개가 막혔다(위 "한 일"의 막힌 명령). 막힌 쪽은 다른 꼴로 다시 읽어 초안에는 걸리지 않았다
- 통과 조건의 시각 확인("돌린 시각이 `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md`보다 늦다")과 phase 스킬 5번("끝남일 때만" `NNN-slug: phase N` 한 커밋)이 함께 서지 않는다. 본문을 고치는 phase가 장면을 돌리면, 끝에 한 번만 커밋할 때 본문 커밋이 장면보다 늦어진다. 본문만 먼저 커밋해 풀었다

## 확인 1

**통과 조건**
- 장면 E와 F의 결과가 남았고 기대대로다(완료 조건 3의 E, F).
  - `docs/TOOLS.md`의 "고친 plan을 장면 E·F로 돌려 본 것" 절을 읽음 → 머리에 Claude Code 2.1.311, 장면 E는 2026-10-27T21:16:18+09:00~21:20:10·세션 `62e87d97-c7c3-4d0b-8e98-9740e7636234`, 장면 F는 21:16:18~21:24:17·세션 `0dc6d879-5d3f-48a0-845d-dd5b696d5822`, 저마다 기대한 결과와 본 결과가 있다. E의 본 결과는 네 갈래마다 setup을 돌려 견주는 확인, 요약 줄 확인의 견줄 갈래(만드는 갈래와 더하는 갈래), origin을 `git remote add`로 URL만 두고 푸시하지 않음이고, F의 본 결과는 `phase-3.md` 초안 TODO 첫 항목 "앞 phase의 산출물에 대어 조건을 맞춘다"다. 둘 다 기대와 같다. 임시 폴더의 기록도 대어 봄: `tmp.XesauNiY37/turnE1.start`·`turnE7.end`가 21:16:18·21:20:10, `turnE7.jsonl`의 session_id가 `62e87d97-…`이고 `git remote add origin https://github.com/werwer748/codeowners-probe.git`가 있다. `tmp.ICuIxE73mN/turnF1.start`·`turnF12.end`가 21:16:18·21:24:17, `turnF12.jsonl`의 session_id가 `0dc6d879-…`이고 "앞 phase의 산출물에 대어 조건을 맞춘다"가 있다. 통과
  - `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md` → `2026-10-27T21:16:02+09:00`. 두 장면의 돌린 시각 21:16:18이 더 늦다. 통과
- 완료 조건 1이 여전히 참이다(이 phase가 plan 본문을 고쳤을 때).
  - plan 본문 "6. 초안을 보여 주고 승인받는다"(갈래마다의 확인·견줄 갈래·푸시 없이 채우는 두 차림의 점검 줄, 앞 phase 산출물에 기대는 조건의 점검 줄), 적는 규칙 "조건"(갈래마다 돌리는 확인, 요약 줄의 견줄 갈래, `git clone --bare`/`git remote add`로 푸시 없이 채움), "TODO"("앞 phase의 산출물에 대어 조건을 맞춘다" 또는 "앞 phase의 결과로 정한다"), phase 본문 "1. 읽는다"(읽을 것에 적힌 산출물 파일만 읽고 그 밖의 앞 phase 기록은 읽지 않고 "하네스에서 걸린 것"에 적는다)를 읽음 → #37, #41, #42의 해결이 저마다 있다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 129 tests`, 마지막 줄 `OK`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → 129개, `OK`. 통과

**남은 것**
- 장면 E는 URL만 보는 요청이라 `git remote add` 갈래만 나왔고, 원격의 내용이 필요한 장면에서 `git clone --bare`를 고르는지는 돌려 보지 않았다 → 통과 조건의 장면 E 기대는 두 차림 가운데 하나를 적는 것이라 `git clone --bare` 갈래를 따로 보지 않는다. 걸리지 않는다. 하네스에서 걸린 것
- 두 장면은 답을 추천안으로만 주었다 → 통과 조건(완료 조건 3의 E, F)이 추천안으로 답한 장면만 본다. 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 원격의 내용이 필요한 장면에서 plan이 `git clone --bare`를 고르는지는 돌려 보지 않았다
- 남은 것: 추천안이 아닌 답에서의 초안은 보지 않았다

**판정**: 통과
