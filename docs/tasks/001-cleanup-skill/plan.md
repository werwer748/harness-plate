# cleanup 스킬 본문을 쓰고 두 장면으로 돌려 확인한다

## 목표
`plugins/plate/skills/cleanup/SKILL.md`가 생겨, 부르면 여섯 기준의 에이전트가 2라운드로 저장소를 살펴 `docs/cleanup/YYYY-MM-DD.md`에 보고서를 쓰고 tasks로 만들지 묻는다. 임시 복제본에서 두 장면(만들지 않음, 만든다)으로 돌린 결과가 `docs/TOOLS.md`에 남는다.

## 범위 밖
- 매니페스트, README, PRD, ARCHITECTURE를 고치는 것(`002-docs-release`가 한다)
- 다른 스킬(plan, run, review, eval, check, retro, setup, context, phase)의 본문
- 정기 실행의 계기, `docs/BACKLOG.md`
- 이 레포 자체에 cleanup을 돌려 보고서를 커밋하는 것

## 완료 조건
1. cleanup 스킬 본문이 tasks 결정대로 절차를 적는다(tasks 완료 조건 1).
   - 확인: `test -f plugins/plate/skills/cleanup/SKILL.md`가 0으로 끝나고, `head -3 plugins/plate/skills/cleanup/SKILL.md`에 `name: cleanup`이 있다
   - 확인: `grep -c -E '보안|성능|신뢰성|유지보수성|기능 적합성|기존 작업 정합성' plugins/plate/skills/cleanup/SKILL.md`가 6 이상이고, `grep -E 'docs/cleanup/|plate:plan' plugins/plate/skills/cleanup/SKILL.md`가 두 낱말을 모두 낸다
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
2. 두 장면의 결과가 `docs/TOOLS.md`에 있고 SKILL.md의 마지막 커밋 뒤에 돌린 것이다(tasks 완료 조건 2).
   - 확인: `docs/TOOLS.md`의 새 절을 읽어 두 장면이 저마다 Claude Code 버전, 돌린 시각, 세션 id, 결과를 적었다. 장면 1은 커밋된 파일 목록(보고서와 `AGENTS.md`뿐)과 보고서의 여섯 기준 절, 장면 2는 `plate:plan` 호출 줄이다. 하나라도 없으면 실패
   - 확인: 그 절의 첫 턴 시각이 `git log -1 --format=%cI -- plugins/plate/skills/cleanup/SKILL.md`보다 늦다
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`

## 결정
- 스킬은 아래 차례로 돈다. 셋업 확인 → 범위 정하기(인자의 경로, 없으면 저장소 전체) → 지난 `docs/cleanup/` 보고서 읽기 → 1라운드 → 2라운드 → 보고서 쓰고 커밋 → tasks로 만들지 묻기 → 동의하면 고른 발견을 `plate:plan`에 넘기고, 고르지 않은 발견은 보고서에 "미룸"으로 표시해 커밋. 이유: tasks 결정
- 여섯 기준: 보안, 성능, 신뢰성(오류 처리, 테스트 공백), 유지보수성(중복, 복잡도, 죽은 코드, 구조), 기능 적합성(PRD와 코드), 기존 작업 정합성(ADR, `docs/BACKLOG.md`, 열린 GitHub 이슈, 지난 tasks 기록). 이유: tasks 결정
- 1라운드는 기준마다 새 에이전트 하나가 따로 찾아 발견마다 근거(파일:줄)를 적는다. 2라운드는 기준마다 다시 새 에이전트 하나를 띄워, 자기 기준으로 다른 다섯의 발견에 동의, 반박, 중복, 충돌을 달고 근거를 직접 다시 본다. 메인은 반박이 이긴 발견을 "버림"으로 까닭과 함께 보고서에 남긴다. 이유: tasks 결정. 2라운드를 새 에이전트로 띄우는 것은 이어 말하기 기능이 도구마다 달라서다 (추천안으로 정함)
- 살피는 범위의 "코드 파일"과 "결과물인 마크다운"은 review와 같은 뜻으로 적는다(`.md`가 아니거나 `docs/ARCHITECTURE.md`의 `## 결과물인 마크다운` 절에 든 것, `docs/tasks/`와 도구가 만든 파일은 뺀다). 이유: tasks 결정
- 스킬이 쓰는 파일은 그 날의 보고서와 `AGENTS.md` 문서 지도의 행뿐이고, 커밋에도 그것만 넣는다. 코드를 고치지 않고 푸시하지 않고 브랜치를 만들거나 바꾸지 않는다. 같은 날 다시 부르면 `YYYY-MM-DD-2.md`처럼 뒤에 번호를 붙인다. 이유: tasks 결정의 "코드는 직접 고치지 않는다"와 plan의 커밋 규칙과 맞춘다 (번호 붙이기는 추천안으로 정함)
- 보고서는 묻기 전에 먼저 커밋한다. 이유: 묻는 자리에서 세션이 끊겨도 보고서가 남는다 (추천안으로 정함)
- `gh`가 없거나 인증이 안 됐으면 기존 작업 정합성의 이슈 확인은 "측정 못함"으로 적고 잇는다. 이유: ADR-020의 `gh` 실패 처리와 맞춘다 (추천안으로 정함)
- 문서 지도에 더할 행은 `| \`docs/cleanup/\` | 정리 점검 보고서(날짜마다 하나), 기준별 발견과 미룬 것 | 정리 tasks를 계획하거나 지난 점검과 견줄 때 |`이고, `docs/tasks/` 행 앞에 넣는다. 이유: run이 BACKLOG 행을 더하는 방식과 같다 (추천안으로 정함)
- 확인용 실행은 이렇게 한다. `mktemp -d` 아래에 `git clone --branch main /Users/hugo/Desktop/harness-plate`로 복제하고, 그 폴더에서 `claude -p`에 `--plugin-dir /Users/hugo/Desktop/harness-plate-cleanup/plugins/plate --permission-mode acceptEdits --output-format stream-json --verbose`와, git add·commit·log·diff·show·status와 `gh issue list`·`python3`를 `--allowedTools`로 주어 돌린다. 첫 턴이 묻는 자리에서 멈추면 장면 2를 `--resume <id> --fork-session`으로 먼저 잇고(plan은 승인 전에 아무것도 쓰지 않으므로 폴더가 바뀌지 않는다), 그다음 장면 1을 원래 세션 id로 잇는다. 오래 걸리므로 백그라운드로 돌린다. 이유: 세션은 폴더에 묶여(`docs/TOOLS.md`) 두 장면이 한 폴더를 써야 한다 (차례는 추천안으로 정함)
