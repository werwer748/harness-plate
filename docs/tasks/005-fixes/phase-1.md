# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 예 — 완료 조건 4의 description 길이 테스트를 먼저 써서 run의 1142자에서 실패하는 것을 본 뒤 1을 고친다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/run/SKILL.md`
- `tests/test_skill_rules.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`
- `README.md`

**TODO**
- [x] 스킬 description 길이를 보는 테스트가 없다. 모든 `plugins/plate/skills/*/SKILL.md`의 description이 1024자 이하인지 보는 테스트를 더한다 (`tests/test_skill_rules.py`)
- [x] run의 description이 1142자로 1024자 한도를 넘어 Codex가 끝의 부르는 말과 "계획이 없는 요청에는 쓰지 않는다"를 자른다. 1024자 이하로 줄이되 그 둘은 남긴다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `docs/TOOLS.md`를 `RUNLOG.md`와 함께 커밋한다는 괄호 글이 일곱 커밋 자리에 되풀이된다. 규칙을 "`RUNLOG.md`" 절 한 곳에 두고 커밋 자리는 그 절을 따르게 한다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 헤드리스 장면의 차림 사실을 더한다: 허용 목록의 아홉 명령, 프롬프트는 `-p` 바로 뒤, 복제한 뒤 `git remote set-head origin main`, 세션 기록은 `${CLAUDE_CONFIG_DIR:-~/.claude}/projects/` 아래 (`docs/TOOLS.md`)
- [x] 고친 run 본문으로 장면 A~D를 다시 돌려, 장면마다 버전, 시각, 세션 id, 돌릴 때의 run 본문 해시, 기대, 본 결과를 run 장면 절에 더한다 (`docs/TOOLS.md`)
- [x] 고친 코드에서 같은 뿌리의 꼴(같은 함수의 다른 입력, 앞서 막던 꼴)을 찾아 테스트로 남긴다 (`tests/test_skill_rules.py`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 스킬 description 길이를 보는 테스트: `DescriptionTest`를 더해 모든 `plugins/plate/skills/*/SKILL.md`의 앞머리를 한 줄 `키: 값` 꼴로 읽고 description이 비지 않고 1024자 이하인지 본다 (`tests/test_skill_rules.py`)
- run의 description: 1142자를 988자로 줄였다. 시작 권한 물음, 기본 브랜치 되돌림 물음, 계획이 틀림, RUNLOG 커밋의 괄호 글을 줄였고 끝의 부르는 말 넷과 "계획이 없는 요청에는 쓰지 않는다."는 그대로 두었다 (`plugins/plate/skills/run/SKILL.md`)
- `docs/TOOLS.md` 커밋 규칙: 6번, 7번, 8번, "멈춘다" 4, 코드 평가 뒤, 하네스 eval 뒤, "비운다" 1의 괄호 글을 "(사용량 까닭을 적은 `docs/TOOLS.md`는 "`RUNLOG.md`" 절을 따른다)"로 바꾸고, 10번 앞 문장도 그 절을 가리키게 고쳤다. 규칙 본문은 "`RUNLOG.md`" 절에 커밋 자리 목록 없이 "이 스킬이 `RUNLOG.md`를 넣는 커밋마다 함께 넣는다"로 한 번만 둔다 (`plugins/plate/skills/run/SKILL.md`)
- 헤드리스 장면의 차림 사실: "스킬을 헤드리스로 돌려 볼 때의 허용 목록"에 아홉 명령(`git remote`, `git rm`, `git merge-base`, `git symbolic-ref`, `git switch`, `git branch`, `claude plugin validate`, `grep`, `cut`)과 쓰임, "차림에서 지킬 것"(프롬프트는 `-p` 바로 뒤, 복제한 뒤 `git remote set-head origin main`, 세션 기록은 `${CLAUDE_CONFIG_DIR:-~/.claude}/projects/` 아래)을 더했다 (`docs/TOOLS.md`)
- 장면 A~D 다시 돌림: 고친 run(해시 `ece6d9e47aad79886e5ffa5b968ed93a8a098dbd`)으로 네 장면을 돌려 새 절 "description을 줄이고 `docs/TOOLS.md` 커밋 규칙을 한 곳에 모은 run을 장면 A~D로 다시 돌려 본 것"에 버전, 시각, 세션 id(A `1abe1354-…`, B `448bb591-…`, C `6e0f7103-…`, D `ce45e487-…`), 해시, 기대, 본 결과를 적었다. 넷 모두 기대와 같다 (`docs/TOOLS.md`)
- 같은 뿌리의 꼴: name이 폴더 이름과 같고 64자 이하인지(`test_name_matches_folder_and_limit`), 줄인 description이 끝의 "쓰지 않는다." 문장을 잃지 않는지(`test_description_ends_with_when_not_to_use`), run description이 부르는 말 넷과 "계획이 없는 요청에는 쓰지 않는다"를 지니는지(`test_run_description_keeps_triggers`), 앞머리가 여러 줄 꼴로 바뀌면 실패하는지(`front_matter`), 되풀이를 없앤 `docs/TOOLS.md` 규칙이 한 곳에만 있고 일곱 커밋 자리가 그 절을 따르는지(`test_tools_md_commit_rule_in_one_place`, `###` 절을 읽는 `subsection`)를 테스트로 남겼다 (`tests/test_skill_rules.py`)
- 테스트 먼저
  - 실패: `python3 -m unittest tests.test_skill_rules` → `FAIL: test_description_at_most_1024_chars (tests.test_skill_rules.DescriptionTest) (skill='run')`, `AssertionError: 1142 not less than or equal to 1024`, `FAILED (failures=1)`
  - 통과: `python3 -m unittest tests.test_skill_rules` → `Ran 17 tests in 0.009s`, `OK`

## 확인 결과
- 완료 조건 1: run description이 1024자 이하이고 부르는 말과 "계획이 없는 요청에는 쓰지 않는다"가 남는다
  - `python3`으로 앞머리 description 글자 수 → `988`. `"실행해줘", "phase 진행하자", "이어서 하자", "끝까지 돌려줘"`와 `계획이 없는 요청에는 쓰지 않는다.`가 끝에 있다(`test_run_description_keeps_triggers` 통과). 통과
- 완료 조건 2: 괄호 글이 한 곳에
  - `grep -c` (찾는 글: 아직 커밋하지 않은 `docs/TOOLS.md`) → `1`(503행 "`RUNLOG.md`" 절). 154, 167, 195, 269, 294, 304, 443행은 "`RUNLOG.md`" 절을 따른다, 236행(10번)은 그 절의 파일을 가리킨다. 통과
- 완료 조건 3: 허용 목록 절의 아홉 명령과 세 사실
  - `docs/TOOLS.md`의 그 절을 읽었다 → 아홉 명령 저마다의 항목과 "-p 바로 뒤", "`git remote set-head origin main`", "`${CLAUDE_CONFIG_DIR:-~/.claude}/projects/`"가 있다. 통과
- 완료 조건 4: description 길이 테스트
  - `python3 -m unittest discover -s tests` → `Ran 149 tests`, 마지막 줄 `OK`. 통과
  - `mktemp -d`에 작업 트리를 `rsync`로 복사해 `context`의 description을 1025자로 늘리고 돌림 → `FAIL: test_description_at_most_1024_chars … (skill='context')`, `AssertionError: 1025 not less than or equal to 1024`, `FAILED (failures=1)`. 통과
- 완료 조건 5: 장면 A~D 다시 돌린 결과
  - `docs/TOOLS.md` 새 절을 읽었다 → 네 장면마다 Claude Code 2.1.311, 시각(23:00:10~23:06:20), 세션 id, 해시 `ece6d9e…`, 기대, 본 결과가 있고 넷 모두 "기대와 같다". 통과
- 완료 조건 6
  - run의 "1. 시작 조건을 본다"(권한 물음 #40), "7. task 회고를 맡긴다"(회고 뒤 RUNLOG 커밋 #44), "8. 고칠 phase를 더한다"(멈춤·TODO의 문서 줄·계획 커밋 문제 #34·#38), "tasks 끝"(코드 평가·eval 뒤 커밋 #44), "`RUNLOG.md`"(단위 없는 `모름` #35, `멈춤` #34)를 읽었다 → 다섯 해결이 모두 있다(`RunRulesTest` 통과). 통과
  - `docs/TOOLS.md`의 run 장면 절(새 절)을 읽었다 → 장면 A(plan 모드에서 Agent 0, 묻고 멈춤), B("고칠지"에서 `git status --short` 빔, 회고·eval 뒤 RUNLOG 커밋), C(`멈춤` 줄), D(README 경로와 `2813e4a`)가 기대와 같다. 통과
  - 장면 A~D의 해시 `ece6d9e47aad79886e5ffa5b968ed93a8a098dbd`를 커밋 뒤 `git rev-parse HEAD:plugins/plate/skills/run/SKILL.md`와 견준다 → 커밋 전 `git hash-object` → `ece6d9e47aad79886e5ffa5b968ed93a8a098dbd`(이 phase 뒤로 run 본문을 고치지 않았다. 커밋 뒤의 값은 확인 절이 본다). 통과
  - plan의 "6. 초안을 보여 주고 승인받는다", 적는 규칙 "조건"·"TODO", phase의 "1. 읽는다"를 읽었다 → #37, #41, #42의 해결이 있다(`PlanRulesTest`, `PhaseRulesTest` 통과). 통과
  - `docs/TOOLS.md`의 장면 E, F, G 절 → 버전, 시각, 세션 id, 기대, 본 결과가 있고 기대와 같다. 통과
  - `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md plugins/plate/skills/phase/SKILL.md` → `2026-10-27T21:16:02+09:00`. 장면 E·F 21:16:18, G 21:28:06이 더 늦다. 통과
  - eval의 "2. 실패를 모아 MAST 유형으로 나눈다" → #36 해결(`남은 것:` 줄은 회고가 "문제"로 판정한 것만)이 있다. 통과
  - `docs/TOOLS.md`의 장면 H, I 절 → 버전, 시각, 세션 id, 기대, 본 결과가 있고 기대와 같다. 통과
  - `git log -1 --format=%cI -- plugins/plate/skills/eval/SKILL.md plugins/plate/skills/review/SKILL.md` → `2026-10-27T21:34:17+09:00`. 장면 H 21:35:55, I 21:35:58이 더 늦다. 통과
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
  - 복사본에서 `.codex-plugin/plugin.json`의 버전만 `0.17.1`로 → `FAIL: test_versions_match`, `FAILED (failures=1)`. 다시 복사해 run의 #44 글 둘을 지움 → `test_44_runlog_commit_after_retro`, `test_44_runlog_commit_after_review_and_eval` 실패, `FAILED (failures=2)`. 통과
  - `cat docs/BACKLOG.md` → `# BACKLOG` 한 줄. 통과
  - `grep -h '"version"' …/.claude-plugin/plugin.json …/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.17.0",`. 통과
  - `claude plugin validate .` → `✔ Validation passed`. 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 따로 읽고 `grep`(`TOOLS.md`, `RUNLOG`, `test_skill_rules`, `description`)으로 걸리는 줄을 봤다 → PRD 7, ARCHITECTURE 54·71행, README `run` 행이 run의 동작과 맞고, ARCHITECTURE 39행의 `test_skill_rules.py` 설명에 description 한도와 한 곳의 커밋 규칙을 더해 새 테스트와 맞췄다. 어긋나는 줄 없음. 통과

## 계획과 달라진 점
- 계획의 TODO는 `docs/ARCHITECTURE.md`를 적지 않았지만, 완료 조건 6의 마지막 확인(맥락 문서가 새 테스트와 어긋나지 않는다)을 위해 39행의 `tests/test_skill_rules.py` 설명 한 줄에 description 한도와 `docs/TOOLS.md` 규칙 테스트를 더했다
- 장면 B는 처음에 넷을 함께 띄웠는데 장면 D를 끝내려고 보낸 `pkill`이 묶인 배경 작업 전체를 끝내 결과 줄 없이 멈췄다. 새 복제본에서 따로 다시 돌린 것을 결과로 적었고, 그 일을 장면 B 항목에 적었다

## 남은 것
- 장면 A~D의 해시가 `git rev-parse HEAD:plugins/plate/skills/run/SKILL.md`와 같다는 것은 이 phase의 커밋 뒤에야 볼 수 있다. 커밋 전 `git hash-object`로 같은 값을 봤고 이 phase 안에서 run 본문을 다시 고치지 않았다
- 장면 D는 계획 커밋을 본 뒤 프로세스를 끝내 결과 줄(`duration_ms`)이 없다. 지난 장면 D와 같은 방식이다
- description 길이는 `len()`(유니코드 글자 수)으로 센다. Codex가 자르는 단위가 글자인지 바이트인지는 이번에 다시 보지 않았다(코드 평가 1은 Codex 0.163.0이 1024자로 자른다고 적었다)
- 같은 뿌리의 꼴 테스트 가운데 `test_tools_md_commit_rule_in_one_place`는 run 본문을 고친 뒤에 썼다. `.md`의 글을 보는 테스트라 테스트 먼저의 대상(코드 파일의 동작)이 아니다

## 하네스에서 걸린 것
- 장면을 돌린 Bash 셸이 zsh라 `set -- $x`가 낱말로 나뉘지 않았고, 허용 목록의 `"Bash(gh issue list:*)"`처럼 빈칸이 든 항목을 빈칸으로 나누면 깨져 줄마다 하나로 읽게 했다. 헤드리스 장면을 차리는 스크립트가 하네스에 없어 장면마다 손으로 차린다(eval 1의 스킬로 만들 후보)
- 네 장면을 한 배경 명령으로 띄우면 하나를 끝내려는 신호가 나머지를 함께 끝낸다. 중간에 끝낼 장면은 따로 띄워야 한다
- 22개 허용 목록으로도 명령 치환(`$(git merge-base …)`)과 `;`·변수로 이은 Bash가 메인과 서브에이전트에서 막혔다(지난 장면들과 같다. 허용 목록으로는 풀리지 않는다)
