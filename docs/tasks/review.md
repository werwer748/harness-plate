# 코드 평가

## 평가 1

**대상**
- 범위: `c71d3ac`(main에서 갈라진 곳)부터 `0bcf7b1`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 5개, 새 줄 39줄, 잴 새 줄 2줄
  - `plugins/plate/.claude-plugin/plugin.json` +1
  - `plugins/plate/.codex-plugin/plugin.json` +1
  - `plugins/plate/skills/plan/SKILL.md` +13 (결과물인 마크다운)
  - `plugins/plate/skills/review/SKILL.md` +18 (결과물인 마크다운)
  - `plugins/plate/skills/run/SKILL.md` +6 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests in 17.164s`, `OK`. 통과
- 커버리지: 측정 못함 — 명령 절이 커버리지 도구를 두지 않는다고 적고 찾지 말라고 한다. 잴 새 줄 2줄은 매니페스트의 버전 값(JSON)이라 실행되는 줄도 아니다
- 중복: 측정 못함 — 명령 절이 중복 검사 도구를 두지 않는다고 적는다
- 정적 분석: `python3 -m json.tool plugins/plate/.claude-plugin/plugin.json`, `python3 -m json.tool plugins/plate/.codex-plugin/plugin.json` → 두 파일 모두 유효한 JSON. `claude plugin validate .` → `✔ Validation passed`. 바뀐 코드 파일에 걸린 결과 없음
- 보안 검사: 측정 못함 — 명령 절이 보안 검사 도구와 의존성 목록을 두지 않는다고 적는다

**완료 조건**
- 1. (#19) plan 6번의 초안 전 점검 넷과, 절대 규칙 3과의 맞춤
  - `plugins/plate/skills/plan/SKILL.md:98`(저장소 밖 경로), `:99`(읽을 것의 명령을 돌려 기대한 것이 나오는지), `:100`(가져올 값이 가리킨 기록에 있는지), `:101`(푸시·권한·인증이 훅이나 권한 범위에 막히면 사용자의 단계로 결정에 적는다)를 읽음 → 넷이 따로 있다. 통과
  - `:18`(절대 규칙 3)과 `:99`를 함께 읽음 → 3이 "완료 조건과 통과 조건에 적는 확인 명령은 미리 돌려 보지 않고", "읽을 것에 적는 명령은 6번의 점검에서 돌려 보되 읽기만 하는 명령만"으로 둘을 갈라 어긋나지 않는다. 통과
- 2. (#20) 다른 phase의 확인을 옮겨 적는 줄
  - "조건" 절 `plan/SKILL.md:235`, 6번 `:102`를 읽음 → 두 줄이 저마다 있다. 통과
- 3. (#23) "조건"의 세 줄
  - `plan/SKILL.md:236`(도구가 실제로 내는 필드나 줄), `:237`(금지를 보는 `grep`은 대상 줄로 좁힌다), `:238`(견줄 커밋이나 시점)을 읽음 → 셋이 하나씩 있다. 통과
- 4. (#24) TODO의 자리와 바뀜의 종류, 다른 스킬의 낱말
  - "TODO" 절 `plan/SKILL.md:268`, 양식의 TODO 줄 `:194`, 6번 `:103`을 읽음 → 268과 194가 "어느 자리에 어떻게(더해진다, 바뀐다, 지워진다)"를 적고 268의 예(`cli.py`의 명령 목록에 … 더해진다)가 그와 맞으며, 103이 다른 스킬의 낱말 절과 대어 보라고 적는다. 통과
- 5. (#21) run의 다섯 곳에 작업 트리의 스킬 줄
  - `plugins/plate/skills/run/SKILL.md:109`(4번), `:125`(5번), `:147`(7번), `:265`(코드 평가를 맡긴다), `:275`(하네스 eval을 맡긴다)를 읽음 → 다섯 곳 모두 "tasks 커밋이 그 스킬의 `SKILL.md`를 바꿨으면 글의 끝에 작업 트리의 스킬 줄을 붙인다"와 "다른 글을 더하지 않는다는 규칙의 예외"가 있고, 낱말 `:47`이 조건(`git merge-base`부터의 diff)과 줄의 꼴을 정한다. 통과
- 6. (#22) review의 결과물인 마크다운
  - `plugins/plate/skills/review/SKILL.md:32-36`(낱말), `:52`(git 레포가 아닐 때), `:173`(PR 모드가 절을 기준 브랜치에서 읽는다), `:215`, `:218`, `:270`(평가 절의 대상)을 읽음 → 네 곳이 결과물인 마크다운을 넣고 절이 없으면 `.md`를 뺀다는 것과 맞는다. 통과
  - `grep -rn '바뀐 코드 파일' plugins/plate docs README.md` → review 밖의 줄은 `docs/ARCHITECTURE.md:82`와 `docs/tasks/` 아래의 계획·기록 줄뿐이고, 읽어 보니 모두 바뀐 낱말과 맞는다. 통과
- 7. 이 저장소의 결과물인 마크다운 절
  - `grep -n -A3 '^## 결과물인 마크다운' docs/ARCHITECTURE.md` → `81:## 결과물인 마크다운`, `83:- \`plugins/plate/skills/*/SKILL.md\``. 통과
- 8. 버전, 마켓플레이스, 테스트, 맥락 문서
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.13.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `python3 -m unittest discover -s tests` → `OK`. 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 읽고 `새 세션`, `reload-plugins`, `.md` 제외, `확인 명령`으로 grep → `ARCHITECTURE.md`의 스킬 호출 예외와 결과물인 마크다운 절, `TOOLS.md:84`의 0.13.0 줄, `README.md:25`의 결과물인 마크다운 줄이 바뀐 동작과 맞고, PRD와 ADR에는 어긋나는 줄이 없다. 통과

**범주**
- 신뢰성
  - 근거: `plugins/plate/skills/run/SKILL.md:47`, `:109`, `:265` 작업 트리의 스킬 줄은 맡기는 글에 "plate의 {스킬}을 불러 그 절차를 따른다"와 "작업 트리의 {경로}를 읽어 그 절차를 따른다"를 함께 둔다. 이 줄이 붙는 때는 바로 세션에 실린 본문과 작업 트리의 본문이 다를 수 있는 때인데, 둘이 다르면 어느 쪽을 따르는지가 띄운 에이전트가 받는 글에 없다. 작업 트리 쪽이 이긴다는 이유는 run의 낱말 `:47`에만 있어 띄운 에이전트는 보지 못한다. 지금은 에이전트가 뒤의 줄을 따르면 맞게 돌지만, 세션의 본문을 따르면 고치기 전의 절차로 돈다 (기능, 낮음)
  - 등급: B — 가장 무거운 문제가 낮음
- 보안
  - 핫스팟: `plugins/plate/skills/run/SKILL.md:47` 셸 명령 치환 `git diff --name-only $(git merge-base {기본 브랜치} HEAD) HEAD`. 값은 `origin/HEAD`에서 얻은 브랜치 이름이고 run은 사용자의 로컬 tasks에서만 돈다 → 안전
  - 핫스팟: `plugins/plate/skills/run/SKILL.md:47` 띄운 에이전트가 저장소 안의 `SKILL.md`를 읽어 따르게 한다. tasks 모드는 사용자가 계획하고 승인한 커밋의 본문만 읽고, 밖에서 들어온 글을 지시로 따르는 CI(PR 모드)는 run을 거치지 않는다 → 안전
  - 핫스팟: `plugins/plate/skills/review/SKILL.md:173` PR 모드가 결과물인 마크다운 절을 PR의 작업 트리가 아니라 기준 브랜치에서 읽는다. PR이 절을 바꿔 평가 대상을 빼는 길을 막는 방어다 → 안전
  - 근거: 바뀐 코드 파일 5개의 새 줄 39줄을 모두 읽음. 매니페스트 두 줄은 버전 값뿐이고 비밀, 토큰, 권한을 다루는 줄이 없다. 취약점 없음
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: 새 줄 39줄을 맥락 문서(`docs/ARCHITECTURE.md`의 "스킬이 다른 스킬의 절차를 써야 하면 이름으로 부른다"와 그 예외, `## 결과물인 마크다운` 절)와 주변 본문에 대어 읽음. 새 낱말(결과물인 마크다운 절, 결과물인 마크다운, 잴 새 줄, 작업 트리의 스킬 줄)은 낱말 절에 정의되고 쓰는 곳(`review/SKILL.md:52`, `:70`, `:129`, `:201`, `:215-218`, `:270`, `run/SKILL.md:109`, `:125`, `:147`, `:265`, `:275`)이 정의와 같은 말을 쓴다. plan의 새 점검(`plan/SKILL.md:98-103`)은 기존 점검 줄과 같은 꼴("초안을 보여 주기 전에 …")이고, 조건의 새 줄(`:235-238`)은 그 절의 다른 줄처럼 규칙 뒤에 이유를 단다. 문제 없음
  - 부채 비율: 0분 ÷ (39줄 × 30분) = 0%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: 커버리지는 측정 못함이라 판단만으로 매긴다. `tests/`의 세 파일(`test_edit_guard.py`, `test_push_guard.py`, `test_verdict.py`)은 매니페스트도 스킬 본문도 읽지 않는다(`grep -ln 'version\|plugin.json\|SKILL.md' tests/*.py` → 없음). 바뀐 동작(plan의 초안 전 점검·조건·TODO 규칙, run의 작업 트리의 스킬 줄, review의 결과물인 마크다운, 버전 0.13.0)마다 깨지면 실패할 테스트가 없다. tasks 머리의 결정("확인은 스킬 본문을 읽어 한다")과 범위 밖("시험 저장소나 헤드리스 실행으로 바뀐 동작을 시험하는 것")이 정한 것이라 소스 문제로는 적지 않는다
  - 등급: E — 바뀐 동작에 테스트가 하나도 없다
- 기능 적합성
  - 근거: 완료 조건 1~8의 확인 13개를 모두 돌렸고 모두 통과
  - 등급: A — 완료 조건의 확인이 모두 통과한다

**Sonar way 게이트**
- 새 문제 0개: 1개. 실패
- 새 보안 핫스팟 모두 검토: 3/3. 통과
- 새 줄 커버리지 80% 이상: 잴 새 줄 2줄로 20줄 미만. 보지 않음
- 새 줄 중복 3% 이하: 잴 새 줄 2줄로 20줄 미만. 보지 않음
- 게이트: 실패

**소스 문제**
1. 작업 트리의 스킬 줄을 붙인 맡기는 글이 세션의 스킬과 작업 트리의 `SKILL.md`를 둘 다 "그 절차를 따른다"로 가리키고, 둘이 다를 때 작업 트리 쪽을 따르라는 말이 띄운 에이전트가 받는 글에 없다 (`plugins/plate/skills/run/SKILL.md:47`). 범주: 신뢰성

**하네스에서 걸린 것**
- 프로젝트의 규칙을 따름: `docs/ARCHITECTURE.md`의 명령 절이 "코드 평가는 이 도구들을 찾지 않고 측정 못함으로 적는다"고 적어, 2번의 커버리지·중복·보안 검사를 환경에서 찾지 않고 측정 못함으로 적었다.
- #22로 스킬 본문이 바뀐 코드 파일에 들면서, 스킬 본문만 고치는 tasks는 테스트 적절성이 늘 E가 된다. 스킬 본문을 시험할 길이 없고 tasks 결정이 본문을 읽는 확인을 정해도 등급표에는 그것을 댈 칸이 없다(review 5번의 테스트 적절성 칸).
- 이 평가는 run이 붙인 작업 트리의 스킬 줄(`작업 트리의 plugins/plate/skills/review/SKILL.md를 읽어 그 절차를 따른다.`)을 받아 작업 트리의 본문을 따랐다. 소스 문제 1의 모호함을 이 자리에서 겪었다.
- 로컬 `main`이 `origin/main`(`6cf56cb`)보다 plan 커밋 `c71d3ac` 하나 앞서 있다. plan이 기본 브랜치에서 커밋하고 tasks 브랜치가 그 위에서 갈라져, 갈라진 곳은 로컬 `main`의 `c71d3ac`로 잡았다. 그 커밋은 `docs/tasks/`만 바꿔 바뀐 코드 파일은 어느 쪽으로 잡아도 같다.
