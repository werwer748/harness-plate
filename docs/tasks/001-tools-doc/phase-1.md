# Phase 1: run·eval의 TOOLS.md 규칙과 그 테스트를 지운다

**목표**: run과 eval 본문에서 TOOLS.md에 사용량 까닭을 적고 커밋하는 규칙이 사라지고, 테스트와 맥락 문서가 그에 맞는다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트, 맥락 문서만 바꾼다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (절대 규칙 5, 6번·7번·8번·10번·"멈춘다"·"코드 평가를 맡긴다"·"하네스 eval을 맡긴다"·"비운다"의 괄호 글 `(사용량 까닭을 적은 \`docs/TOOLS.md\`는 "\`RUNLOG.md\`" 절을 따른다)`, 10번 첫 문단, `RUNLOG.md` 절의 첫 문단과 에이전트 줄 규칙)
- `plugins/plate/skills/eval/SKILL.md` (`## 3. 기준마다 근거를 적고 등급을 매긴다`의 규칙 준수 표에서 `NNN-slug: RUNLOG`와 `<tasks 이름>: RUNLOG` 행)
- `tests/test_skill_rules.py` (`RunRulesTest.test_tools_md_commit_rule_in_one_place`, `test_50_runlog_commits_in_rule_table`)
- `docs/PRD.md` (핵심 기능 7)
- `docs/ARCHITECTURE.md` (`## 디렉터리 구조`의 `test_skill_rules.py` 줄, `## 패턴과 규칙`의 run RUNLOG 줄, `## 데이터 흐름`의 실행 단계)
- `docs/cleanup/2026-10-28.md` (유지보수성-10)
- `README.md` (스킬 표의 `run` 행)

**TODO**
- [x] run 본문에서 `docs/TOOLS.md`를 말하는 글이 모두 지워진다. 절대 규칙 5의 직접 고치는 파일 목록에서 TOOLS.md가 빠지고, 일곱 절의 괄호 글이 빠지고, 10번 첫 문단(TOOLS.md를 보고 전에 커밋하는 문단)이 지워지고, `RUNLOG.md` 절의 TOOLS.md를 함께 넣는다는 문장들과 그 단언이 지워지고, 에이전트 줄 규칙은 돌아오지 않은 까닭을 10번의 보고에만 적는다로 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] eval 규칙 준수 표의 두 `RUNLOG` 행의 파일 칸이 `` `RUNLOG.md` ``로 바뀐다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] `test_tools_md_commit_rule_in_one_place`가 run 본문 어디에도 `docs/TOOLS.md`가 없고 `RUNLOG.md` 절에 까닭을 10번의 보고에 적는 글이 있는지 보는 테스트로 바뀌고, `test_50_runlog_commits_in_rule_table`이 두 행의 파일 칸을 `` `RUNLOG.md` ``로 본다 (`tests/test_skill_rules.py`)
- [x] PRD 핵심 기능 7의 "(사용량이 돌아오지 않은 까닭을 `docs/TOOLS.md`에 적었으면 그것도)"가 빠진다 (`docs/PRD.md`)
- [x] ARCHITECTURE의 run RUNLOG 줄, 데이터 흐름의 실행 단계, `test_skill_rules.py` 줄에서 TOOLS.md 커밋을 말하는 글이 빠지고, 테스트 설명이 바뀐 테스트와 맞는다 (`docs/ARCHITECTURE.md`)
- [x] README 스킬 표 `run` 행의 "(사용량이 돌아오지 않은 까닭을 적은 `docs/TOOLS.md`도 함께)"가 빠진다 (`README.md`)

**통과 조건**
- run과 eval 본문에 `docs/TOOLS.md`가 없다. (완료 조건 1)
  - 확인: `git grep -n 'TOOLS.md' -- plugins/plate/skills/run plugins/plate/skills/eval`이 아무것도 내지 않는다
- run `RUNLOG.md` 절이 사용량이 돌아오지 않은 까닭을 10번의 보고에 적게 한다.
  - 확인: run `RUNLOG.md` 절을 읽어 그 글이 있고, 10번의 보고 목록에 "사용량이 돌아오지 않은 에이전트가 있으면 그 까닭(알면)" 줄이 그대로 있다
- 테스트가 통과하고 바뀐 두 테스트가 새 규칙을 본다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝난다
  - 확인: `tests/test_skill_rules.py`에서 두 테스트를 읽어, 하나는 run 본문 전체에 `docs/TOOLS.md`가 없음을 단언하고 다른 하나는 두 행을 `` | `RUNLOG.md` | ``로 끝나는 꼴로 단언한다
- 맥락 문서에 run이 사용량 까닭을 TOOLS.md에 적는다는 줄이 없다. (완료 조건 4)
  - 확인: `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md`가 아무것도 내지 않는다

## 한 일
- run 본문에서 `docs/TOOLS.md`를 말하는 글이 모두 지워진다: 절대 규칙 5의 파일 목록에서 TOOLS.md를 빼고, 6번·7번·8번·멈춘다·코드 평가를 맡긴다·하네스 eval을 맡긴다·비운다의 괄호 글 일곱 개를 빼고, 10번 첫 문단을 지우고, `RUNLOG.md` 절 첫 문단의 TOOLS.md를 함께 넣는다는 세 문장을 지우고, 에이전트 줄 규칙을 "알면 10번의 보고에만 적는다."로 바꿨다 (`plugins/plate/skills/run/SKILL.md`)
- eval 규칙 준수 표의 두 `RUNLOG` 행의 파일 칸이 `` `RUNLOG.md` ``로 바뀐다: 두 행 모두 `| run | \`RUNLOG.md\` |`로 바꿨다 (`plugins/plate/skills/eval/SKILL.md`)
- 두 테스트를 새 규칙에 맞췄다: `test_tools_md_commit_rule_in_one_place`는 run 본문 전체에 `docs/TOOLS.md`가 없음, `RUNLOG.md` 절에 "…을 알면 10번의 보고에만 적는다", 10번에 "사용량이 돌아오지 않은 에이전트가 있으면 그 까닭(알면)"을 단언하고, `test_50_runlog_commits_in_rule_table`은 두 행을 `| {메시지} | run | \`RUNLOG.md\` |`로 단언한다 (`tests/test_skill_rules.py`)
- PRD 핵심 기능 7의 괄호 글을 뺐다 (`docs/PRD.md`)
- ARCHITECTURE: `## 패턴과 규칙`의 run RUNLOG 줄에서 TOOLS.md 커밋 문장을 "사용량이 돌아오지 않은 까닭은 보고에만 적는다."로 바꾸고, `## 데이터 흐름`의 괄호 글을 빼고, `test_skill_rules.py` 줄의 설명을 "run 본문에 맥락 문서 커밋 규칙이 없고 사용량 까닭을 10번의 보고에만 적음", "eval 규칙 준수 표의 `RUNLOG` 커밋 두 행의 파일 칸이 `RUNLOG.md`뿐임"으로 바꿨다 (`docs/ARCHITECTURE.md`)
- README 스킬 표 `run` 행의 괄호 글을 뺐다 (`README.md`)

## 확인 결과
- run과 eval 본문에 `docs/TOOLS.md`가 없다.
  - `git grep -n 'TOOLS.md' -- plugins/plate/skills/run plugins/plate/skills/eval` → 출력 없음(종료 코드 1). 통과
- run `RUNLOG.md` 절이 사용량이 돌아오지 않은 까닭을 10번의 보고에 적게 한다.
  - run `RUNLOG.md` 절 518줄에 "돌아오지 않은 까닭(도구가 사용량을 돌려주지 않는다 같은 것)을 알면 10번의 보고에만 적는다."가 있고, 10번 247줄에 "사용량이 돌아오지 않은 에이전트가 있으면 그 까닭(알면)"이 그대로 있다. 통과
- 테스트가 통과하고 바뀐 두 테스트가 새 규칙을 본다.
  - `python3 -m unittest discover -s tests` → `Ran 164 tests in 17.520s` / `OK`. 통과
  - `tests/test_skill_rules.py`를 읽음 → `test_tools_md_commit_rule_in_one_place`가 `self.assertNotIn("docs/TOOLS.md", self.text)`로 run 본문 전체를 보고, `test_50_runlog_commits_in_rule_table`이 `"| %s | run | \`RUNLOG.md\` |" % message`로 단언한다. 통과
- 맥락 문서에 run이 사용량 까닭을 TOOLS.md에 적는다는 줄이 없다.
  - `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md` → 출력 없음(종료 코드 1). 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 테스트 이름 `test_tools_md_commit_rule_in_one_place`는 TODO가 이름을 바꾸라고 하지 않아 그대로 두었다. 이제 "한 곳에 있음"이 아니라 "없음"을 보므로 이름과 내용이 어긋난다.

## 하네스에서 걸린 것
- `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄에 처음 "run 본문에 `docs/TOOLS.md`가 없고 사용량 까닭을…"이라고 적었더니 통과 조건의 grep(`사용량.*TOOLS\.md|TOOLS\.md.*사용량`)이 그 설명 줄에 걸렸다. 설명을 "맥락 문서 커밋 규칙이 없고"로 바꿔 피했다. 통과 조건의 grep이 규칙의 부재를 설명하는 줄까지 잡는다.

## 확인 1

**통과 조건**
- run과 eval 본문에 `docs/TOOLS.md`가 없다. (완료 조건 1)
  - `git grep -n 'TOOLS.md' -- plugins/plate/skills/run plugins/plate/skills/eval` → 출력 없음(종료 코드 1). 통과
- run `RUNLOG.md` 절이 사용량이 돌아오지 않은 까닭을 10번의 보고에 적게 한다.
  - `plugins/plate/skills/run/SKILL.md`의 `## \`RUNLOG.md\`` 절(505줄~) 518줄 → "돌아오지 않은 까닭(도구가 사용량을 돌려주지 않는다 같은 것)을 알면 10번의 보고에만 적는다."가 있다. `## 10. 보고한다`(238줄~) 247줄 → "사용량이 돌아오지 않은 에이전트가 있으면 그 까닭(알면)"이 그대로 있다. 통과
- 테스트가 통과하고 바뀐 두 테스트가 새 규칙을 본다.
  - `python3 -m unittest discover -s tests` → `Ran 164 tests in 17.348s` / `OK`. 통과
  - `tests/test_skill_rules.py` 174줄 `test_tools_md_commit_rule_in_one_place` → `self.assertNotIn("docs/TOOLS.md", self.text)`로 run 본문 전체를 단언한다. 318줄 `test_50_runlog_commits_in_rule_table` → `"| %s | run | \`RUNLOG.md\` |" % message`로 두 행을 단언한다(eval 본문 136·140줄이 이 꼴이다). 통과
- 맥락 문서에 run이 사용량 까닭을 TOOLS.md에 적는다는 줄이 없다. (완료 조건 4)
  - `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md` → 출력 없음(종료 코드 1). 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 164 tests` / `OK`. 통과

**남은 것**
- 없음

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
