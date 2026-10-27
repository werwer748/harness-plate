# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리고 plate 저장소에서 고친다

## 완료 조건
1. run의 description이 1142자로 1024자 한도를 넘어, Codex(0.163.0)가 1024자로 잘라 끝의 부르는 말("실행해줘" 등)과 "계획이 없는 요청에는 쓰지 않는다"를 모델에게 싣지 않는다 (`plugins/plate/skills/run/SKILL.md:3`)
   - 확인: run 본문 앞머리의 description 글자 수를 `python3`으로 세어 1024 이하이고, 부르는 말과 "계획이 없는 요청에는 쓰지 않는다"가 남아 있다
2. `docs/TOOLS.md`를 `RUNLOG.md`와 함께 커밋한다는 같은 괄호 글이 run 본문 일곱 커밋 자리에 되풀이되고 `RUNLOG.md` 절에도 목록으로 있어, 규칙이 바뀌면 여덟 곳을 함께 고쳐야 한다 (`plugins/plate/skills/run/SKILL.md:154`)
   - 확인: run 본문에서 `아직 커밋하지 않은 \`docs/TOOLS.md\``를 grep한 줄 수가 1 이하이고, 그 규칙이 "`RUNLOG.md`" 절 한 곳에 있으며 커밋 자리의 글이 그 절을 따른다고 읽힌다
3. 헤드리스 장면의 차림 사실이 모자라다: "스킬을 헤드리스로 돌려 볼 때의 허용 목록"에 `git remote`, `git rm`, `git merge-base`, `git symbolic-ref`, `git switch`, `git branch`, `claude plugin validate`, `grep`, `cut`을 더하고, 프롬프트는 `-p` 바로 뒤에 둔다(`--allowedTools`가 뒤의 값을 삼킨다), 복제한 뒤 `git remote set-head origin main`을 한다, 세션 기록은 `${CLAUDE_CONFIG_DIR:-~/.claude}/projects/` 아래에 있다를 적는다 (`docs/TOOLS.md`)
   - 확인: `docs/TOOLS.md`의 그 절을 읽어 아홉 명령과 세 사실이 저마다 있다
4. 스킬 description 길이를 보는 테스트가 없다. 모든 `plugins/plate/skills/*/SKILL.md`의 description이 1024자 이하인지 보는 테스트를 더한다 (`tests/test_skill_rules.py`)
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `mktemp -d`에 저장소를 복사해 아무 스킬의 description을 1025자로 늘리고 테스트를 돌리면 실패한다
5. 1·2가 바꾼 run 본문으로 장면 A~D를 다시 돌린 결과가 `docs/TOOLS.md`에 있다 (`docs/TOOLS.md`)
   - 확인: run 장면 절에서 다시 돌린 장면 A~D마다 Claude Code 버전, 돌린 시각, 세션 id, 돌릴 때의 run 본문 해시(`git hash-object plugins/plate/skills/run/SKILL.md`), 기대한 결과, 본 결과가 있고 본 결과가 기대와 같다
6. tasks 완료 조건 1, 2, 3, 4, 5가 참이다.
   - 확인: `plugins/plate/skills/run/SKILL.md`의 "1. 시작 조건을 본다", "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "tasks 끝", "`RUNLOG.md`" 절을 읽어 다섯 이슈의 해결이 저마다 적혀 있다. 하나라도 없으면 실패
   - 확인: `docs/TOOLS.md`의 run 장면 절을 읽어 장면마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있고, 본 결과가 기대와 같다. 장면은 넷이다: plan 모드에서 run을 부르면 첫 에이전트를 띄우기 전에 묻고 멈춘다(#40), 회고 뒤와 하네스 eval 뒤의 `RUNLOG.md` 줄이 커밋되어 "고칠지"를 묻는 자리에서 `git status --short`가 비었다(#44), 회고의 문제가 task 머리의 완료 조건을 좁혀야 하면 tasks 일괄에서도 "멈춘다"로 가고 답한 뒤 `RUNLOG.md`의 물은 자리가 `멈춤`이다(#34, #38), 고칠 phase의 TODO에 맥락 문서·README의 줄이 들고 계획 커밋으로 고친 문제는 통과 조건에 커밋 해시와 함께 따로 적힌다(#38)
   - 확인: 장면 A~D 절마다 적힌, 장면을 돌릴 때의 run 본문 해시(`git hash-object plugins/plate/skills/run/SKILL.md`)가 `git rev-parse HEAD:plugins/plate/skills/run/SKILL.md`와 같다
   - 확인: `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건", "TODO" 절, `plugins/plate/skills/phase/SKILL.md`의 "1. 읽는다" 절을 읽어 세 이슈의 해결이 저마다 적혀 있다. 하나라도 없으면 실패
   - 확인: `docs/TOOLS.md`의 plan·phase 장면 절을 읽어 장면마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있고, 본 결과가 기대와 같다. 장면은 셋이다: "만들거나 바꾼다" 갈래가 있는 요청의 tasks 머리 초안이 두 갈래마다 확인을 두고 git 장면을 푸시 없이 채우는 법(`git clone --bare`나 URL만 둔 `git remote add`)을 적는다(#37), 뒤 phase가 앞 phase의 산출물을 돌리는 요청의 초안이 그 phase의 TODO 첫 항목이나 결정에 앞 phase의 산출물에 대어 맞춘다고 적는다(#41), 앞 phase의 산출물이 읽을 것에 든 phase를 수행한 세션의 기록에 `done-phase-1.md`를 읽은 도구 호출이 없다(#42)
   - 확인: 그 절의 돌린 시각이 `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md plugins/plate/skills/phase/SKILL.md`보다 늦다
   - 확인: `plugins/plate/skills/eval/SKILL.md`의 "2. 실패를 모아 MAST 유형으로 나눈다" 절을 읽어 #36의 해결이 적혀 있다
   - 확인: `docs/TOOLS.md`의 eval·review 장면 절을 읽어 장면마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있고, 본 결과가 기대와 같다. 장면은 둘이다: issue-sweep의 기록(`e3836b2`의 `docs/tasks/`에서 `eval.md`를 뺀 것)으로 돌린 eval의 실패 목록에, 그 task의 회고가 "문제"로 판정하지 않은 `남은 것:` 줄과 메모 줄이 하나도 없다(#36), cleanup의 기록(`6292d12`)으로 돌린 review의 테스트 적절성이 "결과물인 마크다운만 바뀐 경우"의 표로 매겨지고 근거가 완료 조건의 확인 줄이다(#43)
   - 확인: 그 절의 돌린 시각이 `git log -1 --format=%cI -- plugins/plate/skills/eval/SKILL.md plugins/plate/skills/review/SKILL.md`보다 늦다
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `mktemp -d`에 저장소를 복사해 `plugins/plate/.codex-plugin/plugin.json`의 버전만 바꾸고 테스트를 돌리면 실패한다. 다시 복사해 run 본문의 #44 해결 글을 지우고 돌리면 실패한다
   - 확인: `docs/BACKLOG.md`에 `# BACKLOG` 줄만 남고 그 항목이 없다
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.17.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어, 1~4가 바꾼 동작(run의 시작 물음, RUNLOG 커밋, 고칠 phase, plan의 갈래 확인과 앞 phase 산출물, phase의 읽기, eval의 남은 것 줄, 새 테스트 파일)과 어긋나는 줄이 없다. 하나라도 있으면 실패

## 결정
- 장면 A~D는 tasks 머리의 결정대로 `mktemp -d`의 복제본에서 작업 트리의 `plugins/plate`를 `--plugin-dir`로 실어 헤드리스로 다시 돌리고, 장면마다 돌릴 때의 run 본문 해시를 적는다. 이유: 1·2가 run 본문을 바꿔 tasks 완료 조건 1의 해시 확인이 이것을 본다
