# plan과 phase의 이슈 셋을 고치고 장면으로 돌려 본다

## 목표
plan의 #37, #41과 phase의 #42가 고쳐지고, 맥락 문서와 README가 고친 동작에 맞춰지며, 고친 동작을 임시 복제본의 세 장면으로 돌린 결과가 `docs/TOOLS.md`에 남는다.

## 범위 밖
- run이 앞 phase의 "계획과 달라진 점"을 다음 phase 에이전트에게 넘기는 것
- run, check, retro, review, eval, cleanup의 본문
- 버전을 올리는 것과 테스트를 더하는 것. `004-tests-version`이 한다

## 완료 조건
1. 두 본문에 세 이슈의 해결이 적혀 있다: #37(`plugins/plate/skills/plan/SKILL.md`. 완료 조건의 글이 갈래(만들거나 바꾼다, 있거나 없다)를 가지면 갈래마다 돌리는 확인을 두고, 맥락 문서나 README의 요약 줄을 보는 확인에는 견줄 갈래를 적고, git 원격이 있는 장면은 푸시 없이 채운다(원격의 내용이 필요하면 `git clone --bare`로 만든 저장소, URL만 보면 `git remote add`로 URL만 둔다). 6번의 점검에도 같은 줄), #41(plan 본문. 뒤 phase의 실행 조건(허용 목록, 차례)이 앞 phase의 산출물에 기대면 그 phase의 TODO 첫 항목에 "앞 phase의 산출물에 대어 조건을 맞춘다"를 두거나 결정에 "앞 phase의 결과로 정한다"고 적는다. 6번의 점검에도 같은 줄), #42(`plugins/plate/skills/phase/SKILL.md`. 앞 phase의 결과가 필요하면 계획의 읽을 것에 적힌 산출물 파일만 읽고, 그 밖의 앞 phase 기록이 필요하면 읽지 않고 "하네스에서 걸린 것"에 적는다)
   - 확인: plan 본문의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건", "TODO" 절, phase 본문의 "1. 읽는다" 절을 읽어 세 해결이 저마다 적혀 있다. 하나라도 없으면 실패
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
2. 맥락 문서와 README가 1의 동작과 맞는다.
   - 확인: `docs/PRD.md`의 핵심 기능 3·4, `docs/ARCHITECTURE.md`의 "데이터 흐름"의 계획과 실행 갈래, `README.md`의 `plan`·`phase` 행, 두 본문 앞머리의 description을 저마다 읽어, 갈래마다의 확인, 앞 phase 산출물에 기대는 조건, phase가 앞 phase 기록을 읽지 않는 것과 어긋나는 줄이 없다. 하나라도 있으면 실패
3. 고친 동작을 세 장면으로 돌린 결과가 `docs/TOOLS.md`에 있고, 저마다 기대대로다.
   - 확인: `docs/TOOLS.md`의 "Claude Code" 절에 더해진 plan·phase 장면 절(phase 2의 것, phase 3의 것)을 읽어, 장면 E~G마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있고 본 결과가 기대와 같다. 하나라도 없거나 다르면 실패
     - 장면 E(#37): 복제본에서 "setup이 `.github/CODEOWNERS`가 없으면 만들고, 있으면 줄을 더하게 바꾼다"를 plan에 넘겨 모든 물음에 추천안으로 답하면, 보여 준 tasks 머리나 task 초안의 완료 조건이 없을 때와 있을 때의 두 갈래마다 돌리는 확인을 두고, git 원격이 있는 장면을 푸시 없이 채우는 법(`git clone --bare`나 URL만 둔 `git remote add`)을 적는다
     - 장면 F(#41): 복제본에서 "새 스킬 하나를 더하고, 임시 복제본에서 그 스킬을 헤드리스로 돌려 본다"를 plan에 넘겨 모든 물음에 추천안으로 답하면, 스킬을 돌려 보는 phase의 초안이 TODO 첫 항목이나 결정에 앞 phase의 산출물에 대어 조건을 맞춘다고 적는다
     - 장면 G(#42): 복제본에 `done-phase-1.md`(기록 절과 판정 통과인 확인 절이 있다)와, 읽을 것에 phase 1의 산출물 파일이 적힌 `phase-2.md`가 있는 작은 task를 차려 phase 스킬로 phase 2를 수행하면, 그 세션 기록(`~/.claude/projects/` 아래의 그 세션 id의 `.jsonl`)에 `done-phase-1.md`를 읽은 도구 호출이 없고, phase 2의 TODO가 끝나 커밋된다
   - 확인: 그 절들의 돌린 시각이 모두 `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md plugins/plate/skills/phase/SKILL.md`보다 늦다

## 결정
- 장면은 `mktemp -d`에 이 저장소의 main을 복제한 곳에서 작업 트리의 `plugins/plate`를 `--plugin-dir`로 실어 헤드리스(`claude -p`, 물음에는 `--resume <세션 id>`로 답한다)로 돌린다. 장면의 작은 task는 그 복제본에 장면마다 새로 차리고, git 원격이 필요하면 `git clone --bare`로 채워 푸시하지 않는다. 허용 목록은 `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"을 쓴다. 이유: tasks 머리의 결정
- 장면 절은 장면마다 Claude Code 버전, 복제본의 main 커밋, 돌린 시각, 세션 id, 넘긴 요청이나 차린 task의 꼴, 기대한 결과, 본 결과, 걸린 시간, 막힌 명령을 적고, 임시 폴더의 기록 경로도 적되 지워질 수 있다고 밝힌다. 이유: tasks 완료 조건 2의 확인이 이 필드를 본다
- plan 장면(E, F)은 보는 글이 든 초안이 나올 때까지 앞 초안은 승인하고, 마지막 초안은 승인하지 않는다. 이유: 보는 것은 초안의 글이고, 승인하면 복제본에 계획을 쓰고 실행으로 이어 갈지 묻는 데까지 간다 (추천안으로 정함)
- #37의 해결을 `git clone --bare` 하나로 좁히면 URL만 보는 장면(setup의 GitHub 원격)에서 맞는 차림을 막아, 푸시 없이 채우는 두 법으로 넓혔다 (002 phase 2의 멈춤에서 승인)
