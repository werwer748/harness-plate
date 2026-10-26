# 회고

## 회고 1

**확인**
- 시험 저장소 `main`의 `.plate`가 지금의 `plugins/plate`와 같고, 그 위에서 #11 장면 PR을 다시 돌려 tasks 완료 조건 2가 참이다
  - `gh pr view 9 -R werwer748/plate-ci-test --json state,comments` (PR 번호는 `done-phase-1.md`의 "한 일") → `state` `OPEN`, 평가서 댓글 첫 줄 `판정: 머지 요청`, 신뢰성 등급 `C — 가장 무거운 문제가 중간`(근거 `textkit/core.py:26`). 통과
  - `gh run view 40286617477 -R werwer748/plate-ci-test --json createdAt,jobs`와 `--log` → review 잡의 `AGENTS.md를 기준 브랜치의 것으로 되돌린다` 단계가 `Run anthropics/claude-code-action@v1` 앞에 돌아 결론 `success`, 로그 142~146줄에 그 단계의 `git checkout "origin/$BASE_REF" -- AGENTS.md`와 `rm -f AGENTS.md`. 통과
  - `~/plate-rail-test/ci-src`에서 `git fetch` 뒤 `git log -1 --format='%h %cI' origin/main -- .plate` → `31a0143 2026-10-26T16:17:16+09:00`(07:17:16Z)으로 CI 실행 `createdAt` 2026-10-26T07:34:32Z보다 앞선다. `git diff --quiet HEAD origin/main` 통과, `diff -r -x __pycache__ ~/plate-rail-test/ci-src/.plate plugins/plate` → 출력 없음, exit 0. 통과
- auto mode에서 스킬 본문 Edit가 막힌 사실, 날짜, run 전 권한 모드의 안내가 적힌다 (`docs/TOOLS.md`)
  - `docs/TOOLS.md` Claude Code 절의 "플러그인 폴더의 편집과 권한 모드" 문단(140~149줄)을 읽음 → 148줄에 2026-10-26(2.1.310) auto mode에서 `plugins/plate/skills/plan/SKILL.md` Edit가 분류기의 판정 없음으로 막힘, `settings.local.json`의 `Edit(plugins/plate/skills/**)` 허용으로 풀리지 않음, bypass 모드에서 들어감(커밋 `0200e13`), 149줄에 run 전에 권한 모드를 정해 두라는 안내. `RUNLOG.md`의 `003-plan-rules` 멈춤 네 줄(22·24·25·27줄)과 "세 번 막혀 네 번 멈췄다"가 맞는다. 통과
- 명령 절에 커버리지·중복·보안 검사 도구를 두지 않는다고 적힌다 (`docs/ARCHITECTURE.md`)
  - `docs/ARCHITECTURE.md` 명령 절을 읽음 → "커버리지, 중복, 보안 검사: 없음. 이 프로젝트는 커버리지·중복·보안 검사 도구를 두지 않는다(의존성 목록도 없다). 코드 평가는 이 도구들을 찾지 않고 측정 못함으로 적는다" 줄이 있다. 통과
- tasks 완료 조건 1, 3, 4, 5, 6, 7, 8, 9, 10, 11이 참이다
  - review PR 모드 절을 읽음 → 지침 파일을 기준 브랜치의 것(`git show <기준 브랜치>:<파일>`)으로 읽는 줄과 PR이 바꾼 파일의 글을 지시로 따르지 않는 줄이 둘 다 있다. 통과
  - setup 양식의 워크플로(318~331줄)를 읽음 → 321줄 되돌림 단계가 331줄 `anthropics/claude-code-action@v1`보다 앞이고, 그 단계에 기준 브랜치에 없으면 `rm -f AGENTS.md`(328줄)가 있다. 통과
  - `docs/ADR.md` ADR-021 트레이드오프와 `docs/ARCHITECTURE.md` 51줄 CI 문단을 따로 읽음 → 둘 다 `CLAUDE.md`의 `@AGENTS.md`로 PR의 지시가 실리는 길(#11)과 되돌림·PR 모드 규칙으로 막는 방법을 적는다. 통과
  - review 6번 커버리지 줄과 PR 모드 `coverage` 행을 따로 읽음 → 둘 다 새 줄이 20줄 미만이면 쟀든 측정 못함이든 먼저 `"skipped"`라 적는다. 통과
  - `grep -c show_full_output plugins/plate/skills/setup/SKILL.md` → `0`. 통과
  - `gh run view 40275362847 -R werwer748/plate-ci-test --log` (실행 id는 001-ci-trust의 기록) → `review가 실패한 까닭을 낸다` 단계에 `"api_error_status": 401, "result": "Failed to authenticate. API Error: 401 Invalid bearer token"`. 통과
  - review 1번(60줄)을 읽음 → 확인이 task 기록을 가리킬 때의 예외와 "등급의 근거로 쓰지 않는다"가 둘 다 있다. 통과
  - `grep -n -- '--body ' plugins/plate/skills/run/SKILL.md` → 출력 없음(exit 1). 통과
  - `grep -c -- '--body-file' plugins/plate/skills/run/SKILL.md` → `6`. "이슈를 올린다" 3·4번(314·315줄)과 "PR을 연다" 3·4번(431·432줄)을 하나씩 읽음 → 네 곳 모두 `--body-file`. 통과
  - run 8번 본문과 고칠 phase 양식(158~205줄)을 읽음 → 파일 목록에 고치는 파일만 두고 TODO 글과 대어 봄(165줄), 같은 뿌리의 꼴을 테스트로 남김(167줄과 양식의 TODO), 앞선 회고 1~K의 재현을 모두 다시 돌림(171줄과 양식의 통과 조건)이 하나씩 있다. 통과
  - retro 73줄(고칠 쪽과 근거)과 75·167줄(경계 밖은 `FRICTION.md`의 `경계 밖`)을 따로 찾음 → 둘 다 있다. 통과
  - phase 132줄 → 아는 부작용과 한계를 "남은 것"에 적는 줄이 있다. 통과
  - plan 83줄(경계 물음), 97줄(절마다의 확인)과 225줄(대상마다/합쳐서, 경우마다의 기대), 266줄(TODO가 맥락 문서의 줄을 모두 가리킴)과 267줄(ADR TODO의 결정과 이유) → 셋이 하나씩 있다. 통과
  - eval 2번 표 아래 77줄 → 측정 못함의 까닭만 적은 줄은 실패가 아니라는 규칙이 있다. 통과
  - `grep -n 'plan: NNN-slug 수정\|phase N 통과' plugins/plate/skills/eval/SKILL.md` → 132·133줄 3번 표의 행과 36줄. 36줄 "더한 phase"는 `plan: NNN-slug 수정`으로 커밋하고 넣어도 되는 파일은 3번 표에 있다고 적어 133줄 행과 맞는다. 통과
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.12.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `python3 -m unittest discover -s tests` → `Ran 99 tests`, `OK`. 통과
  - `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 읽음 → ARCHITECTURE 51줄·명령 절, ADR-021, README 23·25·29줄이 PR 모드의 지침 파일, 되돌림과 오류 줄 단계, 커버리지 게이트와 맞는다. TOOLS의 `--body "$(cat …)"`(91·103줄)와 `show_full_output`(113줄)은 날짜가 붙은 관찰 기록이고 지금 동작을 적은 줄이 아니다. 어긋나는 줄이 없다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.410s`, `OK`. 통과

**문제**
- 없음

**판정**: 통과
