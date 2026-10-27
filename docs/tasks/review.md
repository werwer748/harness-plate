# 코드 평가

## 평가 1

**대상**
- 범위: `509b234`(main에서 갈라진 곳)부터 `bb41212`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 8개, 새 줄 214줄, 잴 새 줄 168줄
  - `plugins/plate/.claude-plugin/plugin.json` +1
  - `plugins/plate/.codex-plugin/plugin.json` +1
  - `tests/test_manifests.py` +30
  - `tests/test_skill_rules.py` +136
  - `plugins/plate/skills/eval/SKILL.md` +2 (결과물인 마크다운)
  - `plugins/plate/skills/phase/SKILL.md` +2 (결과물인 마크다운)
  - `plugins/plate/skills/plan/SKILL.md` +6 (결과물인 마크다운)
  - `plugins/plate/skills/run/SKILL.md` +36 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 143 tests in 16.255s`, `OK`. 통과
- 커버리지: 측정 못함 — 명령 절과 ADR-024가 커버리지 도구를 두지 않는다고 정했고, 그대로 찾지 않았다
- 중복: 측정 못함 — 명령 절과 ADR-024가 중복 검사 도구를 두지 않는다고 정했다
- 정적 분석: `python3 -m py_compile tests/test_manifests.py tests/test_skill_rules.py` → 오류 없음(ADR-024가 정한 범위까지만 돌렸다)
- 보안 검사: 측정 못함 — 명령 절과 ADR-024가 보안 검사 도구를 두지 않는다고 정했다(의존성 목록도 없다)

**완료 조건**
- 1. run의 이슈 다섯(#34, #35, #38, #40, #44)이 고쳐졌다
  - `plugins/plate/skills/run/SKILL.md`의 "1. 시작 조건을 본다"(권한 물음, #40), "7. task 회고를 맡긴다"(회고 뒤 `RUNLOG.md` 커밋, #44), "8. 고칠 phase를 더한다"(목표·완료 조건을 바꾸면 "멈춘다", TODO에 맥락 문서·README 줄, 계획 커밋으로 고친 문제는 통과 조건에, #34·#38), "tasks 끝"(코드 평가·eval 뒤 `RUNLOG.md` 커밋, #44), "`RUNLOG.md`"(단위 없는 `모름`, #35. 멈춘 자리의 물음은 `멈춤`, #34)를 읽었다 → 다섯 해결이 모두 적혀 있다. 통과
  - `docs/TOOLS.md`의 "고친 run을 장면 A·B로 돌려 본 것", "고친 run을 장면 C·D로 돌려 본 것"을 읽었다 → 장면 A(세션 `75d5f20c-…`), B(마지막 다시 돌림 세션 `8d673fe3-…`), C(`515d9b64-…`), D(`6b7d5d04-…`) 모두 Claude Code 2.1.311, 돌린 시각, 세션 id, 기대한 결과, 본 결과가 있고 본 결과가 "기대와 같다". 통과
  - `git rev-parse HEAD:plugins/plate/skills/run/SKILL.md` → `6fb11a43b9f522cbaf0686c4ccbe098bd43036e0`, 장면 B 마지막 절의 해시와 같다. 장면 A 18:40:01, C 19:30:40, D 19:32:30이 `dfb0852`(18:38:03)보다 늦다. `git diff dfb0852 HEAD -- plugins/plate/skills/run/SKILL.md`의 바뀐 줄은 모두 `docs/TOOLS.md`를 커밋 자리(6번, 7번, 8번, 10번 앞, "멈춘다", tasks 끝, 비운다, `RUNLOG.md` 절)에 넣는 글이다. 통과
- 2. plan과 phase의 이슈 셋(#37, #41, #42)이 고쳐졌다
  - `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"(갈래 확인과 푸시 없는 원격, 앞 phase 산출물), 적는 규칙의 "조건"(갈래마다 확인, 요약 줄의 갈래, `git clone --bare`/`git remote add`), "TODO"(앞 phase의 산출물에 대어 맞춘다), `plugins/plate/skills/phase/SKILL.md`의 "1. 읽는다"(산출물 파일만 읽고 기록은 읽지 않는다)를 읽었다 → 셋 모두 적혀 있다. 통과
  - `docs/TOOLS.md`의 장면 E(세션 `62e87d97-…`), F(`0dc6d879-…`), G(`937e2145-…`)를 읽었다 → 버전, 시각, 세션 id, 기대, 본 결과가 있고 기대와 같다. 통과
  - `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md plugins/plate/skills/phase/SKILL.md` → `2026-10-27T21:16:02+09:00`. 장면 E·F 21:16:18, G 21:28:06이 더 늦다. 통과
- 3. eval과 review의 이슈 둘(#36, #43)이 고쳐졌다
  - `plugins/plate/skills/eval/SKILL.md`의 "2. 실패를 모아 MAST 유형으로 나눈다"를 읽었다 → `남은 것:` 줄은 회고가 "문제"로 판정한 것만, 메모 줄은 실패가 아니다가 적혀 있다. 통과
  - `docs/TOOLS.md`의 장면 H(세션 `8ff2f574-…`), I(`85a27c0a-…`)를 읽었다 → 버전, 시각, 세션 id, 기대, 본 결과가 있고 기대와 같다. 통과
  - `git log -1 --format=%cI -- plugins/plate/skills/eval/SKILL.md plugins/plate/skills/review/SKILL.md` → `2026-10-27T21:34:17+09:00`. 장면 H 21:35:55, I 21:35:58이 더 늦다. 통과
- 4. BACKLOG의 항목이 고쳐졌다
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
  - `mktemp -d`에 `git archive HEAD`를 풀고 `.codex-plugin/plugin.json`의 버전만 `0.17.1`로 바꿔 돌림 → `FAILED (failures=1)`. 다시 풀어 run 본문의 #44 해결 글(`그 자리에서 \`RUNLOG.md\`만 한/넣는 커밋으로 넣는다`)을 지우고 돌림 → `test_44_runlog_commit_after_retro`, `test_44_runlog_commit_after_review_and_eval` 실패, `FAILED (failures=2)`. 통과
  - `cat docs/BACKLOG.md` → `# BACKLOG` 한 줄뿐. 통과
- 5. 버전 0.17.0, 마켓플레이스 유효, 맥락 문서·README가 바뀐 동작과 맞다
  - `grep -h '"version"' …/.claude-plugin/plugin.json …/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.17.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 따로 읽었다(run의 시작 물음, RUNLOG 커밋, 고칠 phase, 멈춤, 새 테스트 파일은 PRD 7, ARCHITECTURE의 디렉터리 구조·run 문단·데이터 흐름, README의 `run` 행에 반영됐고, plan·phase·eval의 바뀐 규칙과 어긋나는 줄은 찾지 못했다) → 어긋나는 줄 없음. 통과

**범주**
- 신뢰성
  - 근거: `plugins/plate/skills/run/SKILL.md:3` run의 description이 946자에서 1142자로 늘어 Agent Skills 규격의 1024자 한도를 넘었다. 임시 폴더의 `.agents/skills/longrun/SKILL.md`에 같은 description을 두고 `codex debug prompt-input "hi"`(codex-cli 0.163.0)로 보니 Codex는 스킬을 싣되 description을 1024자로 자르고 `...`를 붙여, 끝의 "아니면 기본 브랜치로 합칠지 묻는다. 계획을 쓴 뒤에, 또는 "실행해줘", "phase 진행하자", "이어서 하자", "끝까지 돌려줘"라고 할 때 쓴다. 계획이 없는 요청에는 쓰지 않는다."가 모델에게 가지 않는다. Codex에서 그 말로 run을 고르는 길과 쓰지 않을 때를 가르는 글이 빠진다. Claude Code에서는 장면 B가 같은 본문(해시 `6fb11a43…`)으로 `/plate:run`을 돌렸다 (기능, 중간)
  - 그 밖에 run의 1번·7번·8번·10번·"멈춘다"·tasks 끝·`RUNLOG.md` 절, plan 6번과 적는 규칙, phase 1번, eval 2번의 새 줄을 앞뒤 절과 대어 읽었고 서로 어긋나는 흐름을 찾지 못했다. 테스트 두 파일은 143개 테스트가 모두 통과했다
  - 등급: C — 가장 무거운 문제가 중간
- 보안
  - 핫스팟: `plugins/plate/skills/run/SKILL.md:182` 고칠 phase 앞에 셸 명령 치환 `git log … $(git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md)..HEAD -- docs/tasks/`를 돌리게 한다 → 안전(경로는 계획의 task 폴더 이름이고 밖의 입력이 들지 않는다)
  - 근거: `tests/test_manifests.py`, `tests/test_skill_rules.py`는 저장소 안의 고정 경로만 읽고 셸을 부르지 않는다. 매니페스트는 버전 줄만 바뀌었다. 스킬 본문의 새 줄에 비밀, 권한 건너뛰기, 밖의 입력을 쓰는 명령이 없다. 문제 없음
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: `plugins/plate/skills/run/SKILL.md:154`(6번), `:167`(7번), `:195`(8번), `:269`("멈춘다" 4), `:294`(코드 평가 뒤), `:304`(eval 뒤), `:443`(비운다 1) 일곱 자리에 같은 괄호 글 "(사용량이 돌아오지 않은 까닭을 적고 아직 커밋하지 않은 `docs/TOOLS.md`가 있으면 그것도 넣는다. "`RUNLOG.md`" 절)"이 되풀이되고, 같은 규칙이 `:503`의 `RUNLOG.md` 절에 커밋 자리 목록으로 또 적혀 있다. 커밋 자리가 늘거나 규칙이 바뀌면 여덟 곳을 함께 고쳐야 하고, description이 1024자를 넘은 것도 이 글이 커진 탓이다 (설계·복잡도, 15분)
  - 테스트 두 파일은 표준 라이브러리만 쓰고 기존 `tests/`의 꼴(`unittest`, `ROOT` 경로)과 같다. 이름과 모듈 docstring이 무엇을 시험하는지 적는다
  - 부채 비율: 15분 ÷ (214줄 × 30분) = 0.2%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: 커버리지는 측정 못함이라 판단만으로 매긴다
  - 근거: `tests/test_manifests.py:25` 두 매니페스트의 버전이 다르면 실패한다(완료 조건 4의 확인에서 버전 하나만 바꿔 실패를 봤다)
  - 근거: `tests/test_skill_rules.py:55`~`:132` run(#34, #35, #38, #40, #44), plan(#37, #41), phase(#42), eval(#36)의 규칙 글이 제 절에 없으면 실패한다(#44 글을 지워 두 테스트가 실패하는 것을 봤다). 동작은 `docs/TOOLS.md`의 장면 A~I가 실제로 돌려 봤다
  - 근거: 테스트도 장면도 없는 동작은 엣지케이스뿐이다. run 10번 앞의 `docs/TOOLS.md` 커밋(사용량이 돌아오지 않는 경우, tasks 머리의 `돌리지 않음` 줄), plan 6번의 요약 줄·원격 차림 점검 글(`tests/test_skill_rules.py:108`은 갈래 글만 본다), phase description의 바뀐 괄호 글
  - 등급: B — 커버리지 측정 못함이라 판단으로, 테스트가 빠진 동작이 엣지케이스뿐이다
- 기능 적합성
  - 근거: 완료 조건 1 통과: 다섯 이슈의 해결 글, 장면 A~D, 해시와 시각
  - 근거: 완료 조건 2 통과: 세 이슈의 해결 글, 장면 E~G, 시각
  - 근거: 완료 조건 3 통과: #36 해결 글, 장면 H·I, 시각
  - 근거: 완료 조건 4 통과: 테스트 `OK`, 버전과 #44 글을 깨면 실패, BACKLOG 비움
  - 근거: 완료 조건 5 통과: 두 버전 0.17.0, validate 통과, 다섯 문서에 어긋나는 줄 없음
  - 등급: A — 완료 조건의 확인이 모두 통과한다

**Sonar way 게이트**
- 새 문제 0개: 2개(신뢰성 1, 유지보수성 1). 실패
- 새 보안 핫스팟 모두 검토: 1/1. 통과
- 새 줄 커버리지 80% 이상: 측정 못함(잴 새 줄 168줄). 측정 못함
- 새 줄 중복 3% 이하: 측정 못함(잴 새 줄 168줄). 측정 못함
- 게이트: 실패

**소스 문제**
1. run의 description이 1142자로 1024자 한도를 넘어, Codex(0.163.0)가 1024자로 잘라 끝의 부르는 말("실행해줘" 등)과 "계획이 없는 요청에는 쓰지 않는다"를 모델에게 싣지 않는다 (`plugins/plate/skills/run/SKILL.md:3`). 범주: 신뢰성
2. `docs/TOOLS.md`를 `RUNLOG.md`와 함께 커밋한다는 같은 괄호 글이 run 본문 일곱 커밋 자리에 되풀이되고 `RUNLOG.md` 절에도 목록으로 있어, 규칙이 바뀌면 여덟 곳을 함께 고쳐야 한다 (`plugins/plate/skills/run/SKILL.md:154`). 범주: 유지보수성

**하네스에서 걸린 것**
- 프로젝트의 규칙을 따름: ADR-024와 명령 절이 커버리지·중복·보안 검사 도구를 찾지 않고 측정 못함으로 적고 정적 분석은 `py_compile`까지만 돌리라고 해서, 2번의 도구를 찾지 않았다. 그래서 게이트의 커버리지와 중복은 늘 측정 못함이다
- tasks 머리의 완료 조건과 plan의 초안 점검에 스킬 description 길이(1024자 한도)를 보는 확인이 없어, run description이 한도를 넘은 것이 phase 확인과 task 회고를 지나왔다. 지난 tasks(issue-sweep의 003-base-branch)에서 960자로 "여유가 적다"는 메모가 이미 나왔었다
