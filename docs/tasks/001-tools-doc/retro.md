# 회고

## 회고 1

**확인**
- run 본문에 `docs/TOOLS.md`가 없고, 사용량이 돌아오지 않은 까닭은 `RUNLOG.md` 절에서 10번의 보고에만 적게 한다. eval 규칙 준수 표의 `NNN-slug: RUNLOG`와 `<tasks 이름>: RUNLOG` 행의 파일 칸은 `` `RUNLOG.md` ``뿐이다. (성능-1, 성능-2, 유지보수성-10)
  - `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 코드 1). 통과
  - `python3 -m unittest discover -s tests` → `Ran 165 tests`, `OK`. `tests/test_skill_rules.py`의 `test_tools_md_commit_rule_in_one_place`가 run 본문 전체에 `docs/TOOLS.md`가 없음과 `RUNLOG.md` 절의 "…을 알면 10번의 보고에만 적는다"를 단언하고, `test_50_runlog_commits_in_rule_table`이 두 행을 `| {메시지} | run | \`RUNLOG.md\` |`로 단언한다. eval 본문 두 행도 이 꼴이다. 통과
- `docs/TOOLS.md`가 15KB 이하이고, 네 절과 ruleset의 `gh api` 명령과 JSON이 남아 있고, 시험 실행 기록이 없다.
  - `wc -c < docs/TOOLS.md` → `14287`. 통과
  - 네 절 이름마다 `grep -c` → `1`, `1`, `1`, `1`. 통과
  - `grep -c 'rulesets --input -'` → `1`, `grep -c '"enforcement"'` → `1`. 통과
  - `grep -cE '/var/folders/|tmp\.[A-Za-z0-9]{6,}|장면 [A-Z]' docs/TOOLS.md` → `0`. 통과
- plan의 적는 규칙에 돌려 본 확인의 결과는 phase 기록에만 두고 맥락 문서에는 도구 동작만 한 줄로 더한다는 규칙이 있고, ARCHITECTURE의 TOOLS.md 줄도 같은 뜻이다.
  - `python3 -m unittest discover -s tests` → `OK`. `PlanRulesTest.test_run_results_stay_in_phase_record`가 `part(section(..., "적는 규칙"), "조건")`에서 규칙의 글을 단언하고, plan 본문 `적는 규칙`의 **조건**에 그 줄이 있다. 통과
  - `docs/ARCHITECTURE.md` 50줄을 읽음 → "도구마다 다른 동작과 확인을 멈춘 지점은 `docs/TOOLS.md`에 적는다(ADR-018). 시험 실행 기록은 적지 않는다." 둘 다 있다. 통과
- 맥락 문서와 README에 run이 사용량 까닭을 TOOLS.md에 적거나 커밋한다는 줄이 없고, ARCHITECTURE의 테스트 설명 줄이 바뀐 테스트와 맞는다.
  - `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md` → 출력 없음(종료 코드 1). 통과
  - `docs/ARCHITECTURE.md` 39줄 `test_skill_rules.py` 줄을 읽음 → "`docs/TOOLS.md` 커밋 규칙이 `RUNLOG.md` 절 한 곳에 있음"이 없고, "돌려 본 확인의 결과는 phase 기록에만 두고 맥락 문서에는 도구 동작만 한 줄로 더함", "run 본문에 맥락 문서 커밋 규칙이 없고 사용량 까닭을 10번의 보고에만 적음", "eval 규칙 준수 표의 `RUNLOG` 커밋 두 행의 파일 칸이 `RUNLOG.md`뿐임"이 있다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 165 tests in 17.688s`, `OK`. 통과

**남은 것**
- phase 1: 테스트 이름 `test_tools_md_commit_rule_in_one_place`가 이제 "없음"을 보므로 이름과 내용이 어긋난다 → 문제 아님 (테스트의 단언은 완료 조건 1대로 돌고, 이름은 취향에 드는 것이라 넷 가운데 어느 기준에도 걸리지 않는다)
- phase 2: 지운 절의 실행 시간, 판정마다의 관찰, 시험 폴더와 스크립트 경로는 git 기록에만 남는다 → 문제 아님 (task 머리 결정이 임시 경로, 장면의 차림과 기대는 옮기지 않는다고 정했고, 다음 계획이 알아야 할 도구 동작은 `## Claude Code` 첫 목록과 소절들로 옮겨진 것을 읽어 봤다)
- phase 2: "도구를 넓힐 때 할 것"에서 시험 폴더 `~/plate-rail-test`의 위치를 뺐다 → 문제 아님 (시험 차림의 경로라 task 머리 결정이 옮기지 않기로 한 것에 들고, 그 절의 할 일 다섯 줄은 남아 있다)

**문제**
- 없음

**판정**: 통과
