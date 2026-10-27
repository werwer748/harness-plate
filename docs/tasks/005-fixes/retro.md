# 회고

## 회고 1

**확인**
- 1. run의 description이 1024자 이하이고 부르는 말과 "계획이 없는 요청에는 쓰지 않는다"가 남아 있다
  - `python3`으로 `plugins/plate/skills/run/SKILL.md` 앞머리의 description 글자 수 → `988`. `"실행해줘"`, `"phase 진행하자"`, `"이어서 하자"`, `"끝까지 돌려줘"`, `계획이 없는 요청에는 쓰지 않는다`가 모두 있다. 통과
- 2. `docs/TOOLS.md` 커밋 규칙이 "`RUNLOG.md`" 절 한 곳에 있다
  - `grep -n '아직 커밋하지 않은 \`docs/TOOLS.md\`' plugins/plate/skills/run/SKILL.md` → 1줄(503행, "`RUNLOG.md`" 절, "이 스킬이 `RUNLOG.md`를 넣는 커밋마다 함께 넣는다"). `"\`RUNLOG.md\`" 절을 따른다`는 7곳(6번, 7번, 8번, "멈춘다" 4, 코드 평가 뒤, 하네스 eval 뒤, "비운다" 1)이고 10번은 그 절을 가리킨다. 커밋 자리의 글이 그 절을 따른다고 읽힌다. 통과
- 3. 헤드리스 장면의 차림 사실
  - `docs/TOOLS.md` "스킬을 헤드리스로 돌려 볼 때의 허용 목록" 절을 읽음 → `git remote`, `git rm`, `git merge-base`, `git symbolic-ref`, `git switch`, `git branch`, `claude plugin validate`, `grep`, `cut` 아홉 항목과 "차림에서 지킬 것"의 세 사실(프롬프트는 `-p` 바로 뒤, 복제한 뒤 `git remote set-head origin main`, 세션 기록은 `${CLAUDE_CONFIG_DIR:-~/.claude}/projects/` 아래)이 저마다 있다. 통과
- 4. description 길이 테스트
  - `python3 -m unittest discover -s tests` → `Ran 149 tests`, 마지막 줄 `OK`. 통과
  - `mktemp -d`에 저장소를 `rsync`로 복사해 `context`의 description 앞에 글자를 채워 정확히 1025자로 늘리고 돌림 → `FAIL: test_description_at_most_1024_chars (test_skill_rules.DescriptionTest) (skill='context')`, `FAILED (failures=1)`. 통과
- 5. 장면 A~D를 다시 돌린 결과
  - `docs/TOOLS.md`의 "description을 줄이고 `docs/TOOLS.md` 커밋 규칙을 한 곳에 모은 run을 장면 A~D로 다시 돌려 본 것" 절을 읽음 → 장면 A~D마다 2.1.311, 돌린 시각(23:00:10~23:06:20), 세션 id(`1abe1354-…`, `448bb591-…`, `6e0f7103-…`, `ce45e487-…`), run 본문 해시 `ece6d9e47aad79886e5ffa5b968ed93a8a098dbd`, 기대한 결과, 본 결과가 있고 넷 모두 "기대와 같다". 통과
- 6. tasks 완료 조건 1~5가 참이다
  - run의 "1. 시작 조건을 본다", "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "tasks 끝", "`RUNLOG.md`" 절 → 다섯 이슈의 해결이 저마다 있다(`RunRulesTest`가 이 글들을 본다, 통과). 통과
  - `docs/TOOLS.md` run 장면 절(위 5의 절) → 장면 A(plan 모드, Agent 0, 묻고 멈춤), B(회고·코드 평가·eval 뒤 `RUNLOG` 커밋, "고칠지"에서 `git status --short` 빔), C(완료 조건을 좁히는 회고 문제에 멈추고 답한 뒤 `멈춤` 줄), D(TODO에 `README.md`, 통과 조건에 `2813e4a`)가 기대와 같다. 통과
  - `git hash-object plugins/plate/skills/run/SKILL.md` → `ece6d9e47aad79886e5ffa5b968ed93a8a098dbd`, `git rev-parse HEAD:plugins/plate/skills/run/SKILL.md` → `ece6d9e47aad79886e5ffa5b968ed93a8a098dbd`. 장면 A~D의 해시와 같다. 통과
  - plan의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙 "조건"·"TODO", phase의 "1. 읽는다" → #37, #41, #42의 해결이 있다(`PlanRulesTest`, `PhaseRulesTest` 통과). 통과
  - `docs/TOOLS.md` 장면 E·F·G 절 → 버전, 시각, 세션 id, 기대, 본 결과가 있고 기대와 같다. 통과
  - `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md plugins/plate/skills/phase/SKILL.md` → `2026-10-27T21:16:02+09:00`. 장면 E·F 21:16:18, G 21:28:06이 더 늦다. 통과
  - eval의 "2. 실패를 모아 MAST 유형으로 나눈다" → #36의 해결이 있다(`EvalRulesTest` 통과). 통과
  - `docs/TOOLS.md` 장면 H·I 절 → 버전, 시각, 세션 id, 기대, 본 결과가 있고 기대와 같다. 통과
  - `git log -1 --format=%cI -- plugins/plate/skills/eval/SKILL.md plugins/plate/skills/review/SKILL.md` → `2026-10-27T21:34:17+09:00`. 장면 H 21:35:55, I 21:35:58이 더 늦다. 통과
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
  - 복사본에서 `.codex-plugin/plugin.json`의 버전만 `0.17.1`로 → `FAIL: test_versions_match`, `FAILED (failures=1)`. 새 복사본에서 run의 #44 글(`그 자리에서 \`RUNLOG.md\`만 한 커밋으로 넣는다` 3곳과 `RUNLOG.md` 절의 같은 글)을 지움 → `test_44_runlog_commit_after_retro`, `test_44_runlog_commit_after_review_and_eval` 실패, `FAILED (failures=2)`. 통과
  - `cat docs/BACKLOG.md` → `# BACKLOG` 한 줄. 통과
  - `grep -h '"version"' …` → 두 줄 모두 `"version": "0.17.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `docs/PRD.md`(7항), `docs/ARCHITECTURE.md`(39행, 명령 절), `docs/ADR.md`(걸리는 줄 없음), `docs/TOOLS.md`, `README.md`(`run` 행)를 따로 읽음 → 시작 물음, RUNLOG 커밋, 고칠 phase, 새 테스트 설명이 바뀐 동작과 맞는다. run의 description에서 줄인 글("확인할 수 없으면 그렇다고 적고 잇는다", "tasks 브랜치에 없는 커밋이 있으면 묻지 않고 그대로 둔다")은 run 본문과 README·PRD에 그대로 있어 어긋나지 않는다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 149 tests`, `OK`. 통과
- 테스트 먼저 기록: phase 1
  - `done-phase-1.md` "한 일"의 "테스트 먼저" → 실패 출력(`AssertionError: 1142 not less than or equal to 1024`, `FAILED (failures=1)`) 다음에 통과 출력(`Ran 17 tests`, `OK`)이 이 순서로 있다. 통과

**남은 것**
- phase 1: 장면 A~D의 해시가 `git rev-parse HEAD:…`와 같다는 것은 커밋 뒤에야 볼 수 있다 → 문제 아님 (이 회고에서 HEAD의 값 `ece6d9e…`이 장면의 해시와 같음을 직접 봤다)
- phase 1: 장면 D는 프로세스를 끝내 결과 줄(`duration_ms`)이 없다 → 문제 아님 (완료 조건 5가 보는 버전, 시각, 세션 id, 해시, 기대, 본 결과는 모두 있다)
- phase 1: description 길이를 `len()`(글자 수)으로 세고, Codex가 자르는 단위가 글자인지 바이트인지는 다시 보지 않았다 → 문제 아님 (완료 조건 1은 `python3`의 글자 수를 기준으로 정했고 그 안에서 988자다. 바이트 단위일 가능성은 경계 밖으로 FRICTION에 적는다)
- phase 1: `test_tools_md_commit_rule_in_one_place`는 run 본문을 고친 뒤에 썼다 → 문제 아님 (phase의 테스트 먼저는 description 길이 테스트로 정했고 그 순서는 지켰다. 이 테스트는 `.md` 글을 보는 테스트로 지금 통과한다)

**문제**
- 없음

**판정**: 통과
