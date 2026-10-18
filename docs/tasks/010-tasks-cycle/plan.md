# tasks > task > phase 구조와 자동 사이클, tasks 끝 평가

## 요청
일단 사용자가 작읍을 요청해 예를 들면 프로젝트의 세팅 그럼 세팅에서 끝. 거기서 무언가 더하진 않지 그냥 하네스를 설치만 하는거야 그 레포에 그 후에 이제 프로젝트 기본을 세팅하자 라고 하면 스펙을 선택하고 기본적인 구현형태에 대해 대화를 하겠지 계획이 세워지면 프로젝트 기본 세팅에 관한 계획을 세분화해서 tasks에 각 단계들을 만드는거야 001-react-setting / 002-tanstack-query-setting 이런식으로 그리고 그 안에서 각 task별 세부 phase를 세우는거야 지금 이게 용어가 혼동되어있으니까 tasks > task > phase로 확실히 정리를 하고 이제 task안에서 나뉜 phase들을 처리하는데 한 task를 처리할때마다 tasks 폴더에 REPAIRE 혹은 더 좋은이름이 있다면 그걸로해서 작업에 문제가 있었거나 멈췄거나 주기적으로 반복되서 스킬화하면 좋을꺼같은 제안 같은걸 기록해놔 그리고 작업 그러니까 tasks내의 모든 task를 처리하면 이번 작업에서 작성된 모든 테스트와 코드를 검증해보고 평가해 이 때 평가 기준을 만들어서 점수화해서 보여주면 좋겠어(이부분은 업계에서 많이 사용하는 체계를 적용하고싶어) 그리고 하네스에대한 eval도 수행하면 좋겠어 REPAIR에 기록도 포함해서 이 때의 평가 기준역시 업계에서 많이 쓰는 기준 6가지 정도로 판단해서 리포트를 작성해주고 고칠지 묻고 고치겠다고 하면 하네스도 한 tasks가 마무리 될때마다 평가되고 수정되는 거지 그리고 tasks 시작때 만약 여기까지 자동으로 진행할지 묻고 진행한다고하면 이과정역시 자동화로 쭈욱 tasks생성 작업마다 tasks/REPAIR(이름바꿔도됨)을 쌓고 코드평가하고 하네스평가하고 수정까지 전부 일괄로 진행 물론 tdd가드도 같이 돌겠지 그후에 마찬가지로 푸시될때 코드 평가 체계도 있어야 겠지 이건 우리가 후에 작업하기로 해놨다면 이참에 이작업에 포함해서 진행하면좋겠어 좋아 둘로 나눠서 010부터 계획하자

## 목표
plate가 요청 하나를 tasks로 계획해 task와 phase로 나누고, 실행 방식 둘(task 하나씩, tasks 일괄)로 돌리며, tasks가 끝나면 코드 평가와 하네스 eval을 보고하고 고칠지 묻는다. setup은 설치만 하고, 스킬·훅·맥락 문서의 낱말은 tasks > task > phase로 맞춘다.

## 범위 밖
- PR과 CI(로컬 리뷰 뒤 PR 열기, CI 에이전트의 자동 머지·머지 요청·닫기, 기본 브랜치 푸시를 막는 pre-push 훅). 011에서 한다.
- 하네스 자체의 업데이트 방식(이슈 → 자기 적용 → PR, 결정적 CI, 버전·릴리스).
- context 스킬과 setup의 문서 양식(PRD, ARCHITECTURE, ADR, DESIGN) 고치기.
- 옛 구조의 `docs/tasks/NNN-slug/` 폴더를 새 구조로 옮기는 것. 이 레포의 `docs/tasks/007`~`010`은 010을 합친 뒤 지운다.
- 009 검증 1에서 미룬 문제(run이 LESSONS로 옮겼는지 보는 기준). run에서 LESSONS가 빠져 그 갈래가 없어진다.
- 9단계 정리·리팩터링 스킬.
- Codex에서 확인하는 것(ADR-018).

## 완료 조건
1. 스킬은 아홉(setup, context, plan, run, phase, check, retro, review, eval)이고 verify는 없다.
   - 확인: `ls plugins/plate/skills` → `check`, `context`, `eval`, `phase`, `plan`, `retro`, `review`, `run`, `setup` 아홉만 나온다
2. 스킬, 훅, README, 맥락 문서, 이 레포의 `AGENTS.md`가 tasks, task, phase를 결정의 뜻대로 쓴다.
   - 확인: `grep -n "작업" plugins/plate/skills/*/SKILL.md plugins/plate/hooks/edit_guard.py README.md docs/PRD.md docs/ARCHITECTURE.md AGENTS.md`의 줄을 모두 읽어 tasks, task, phase 가운데 하나를 가리키는 "작업"이 없다
   - 확인: 낱말 절이 있는 스킬마다 그 절을 읽어 tasks, task, phase의 정의가 결정의 정의와 어긋나지 않는다
3. setup은 설치만 하고 끝 물음 없이 끝나며, 넣는 문서 지도의 `docs/tasks/` 행과 규칙 구간이 새 구조와 새 스킬을 말한다.
   - 확인: `grep -n "plate:context\|이어서 채울지\|verify" plugins/plate/skills/setup/SKILL.md` → 0줄
   - 확인: 장면 setup·plan에서 setup을 부른 기록(`~/plate-rail-test/logs/`)의 마지막 답에 채울지 묻는 글이 없고, 그 시험 폴더 `AGENTS.md`의 두 구간이 setup 본문의 글과 같다(UI가 아닌 프로젝트라 `docs/DESIGN.md` 행만 빠진다)
   - 확인: 완료 조건 13의 확인에 이 기록이 든다
4. plan은 tasks 머리를 먼저, 그다음 task마다 머리와 phase를 승인받아 모두 받은 뒤 한꺼번에 쓰고 한 커밋으로 넣는다. tasks가 진행 중이면 지금 tasks에 더할지 묻는다. ARCHITECTURE에 명령 절이 없으면 첫 task의 첫 phase TODO에 그 절을 쓰는 일을 넣는다.
   - 확인: 장면 setup·plan의 plan 기록을 읽어 승인 물음이 tasks 머리에 한 번, task마다 한 번 있고, 마지막 승인 전 턴마다 남긴 `git status --short`와 `ls docs/tasks`에 새 파일이 없다
   - 확인: 그 시험 폴더의 `git log -1 --stat`이 `docs/tasks/plan.md`(완료 조건 절이 비지 않았다)와 task 폴더마다의 `plan.md`, `phase-N.md`를 한 커밋에 담는다
   - 확인: 그 시험 폴더의 `docs/ARCHITECTURE.md`에 명령 절이 없고, 첫 task의 `phase-1.md` TODO에 명령 절을 쓰는 항목이 있다
   - 확인: 같은 장면에서 tasks가 진행 중일 때 새 요청으로 plan을 부른 기록의 답이 지금 tasks에 더할지 묻는다
   - 확인: 완료 조건 13의 확인에 이 기록들이 든다
5. run은 시작할 때 실행 방식을 묻고, `tasks/<이름>` 브랜치에서 phase마다 수행과 check를 새 에이전트에게 맡기고, 통과한 phase를 `done-phase-N.md`로 바꾸고, task의 phase가 모두 통과하면 task 회고를 맡긴다. task 하나씩이면 회고 뒤에 묻는다. `RUNLOG.md`에는 에이전트마다, 물은 자리마다 한 줄이 쌓이고 `FRICTION.md`에는 회고가 적은 줄이 있다.
   - 확인: 장면 run task 하나씩의 시험 폴더에서 `git branch --show-current` → `tasks/`로 시작하고, `git log --oneline`에 첫 task의 phase마다 `NNN-slug: phase N`, `NNN-slug: phase N 확인`, `NNN-slug: phase N 통과` 커밋과 그 뒤의 `NNN-slug: 회고` 커밋이 이 순서로 있다
   - 확인: 그 폴더의 첫 task 폴더에 `phase-N.md`가 없고 `done-phase-N.md`와 `retro.md`가 있다
   - 확인: 기록의 답에서 실행 방식을 묻는 글과 회고 뒤의 물음을 찾는다
   - 확인: `docs/tasks/RUNLOG.md`의 에이전트 줄 수가 기록에서 띄운 에이전트 수와 같고 줄마다 토큰, 도구 호출, 시간이 있으며, 물은 줄 수가 기록의 물음 수와 같다. `docs/tasks/FRICTION.md`에 첫 task 이름이 붙은 줄이 있다
   - 확인: 완료 조건 13의 확인에 이 기록이 든다
6. tasks 일괄은 묻지 않고 모든 task를 처리하고, 회고에서 나온 문제는 고칠 phase를 더해 고친다. 모든 task가 끝나면 review와 eval을 맡겨 전체 보고를 하고 고칠지 한 번에 묻는다. 고치면 고침 task를 더해 같은 레일로 돌리고, 미룬 소스 문제를 `docs/BACKLOG.md`에 적고, `docs/tasks/`를 비운 뒤 합칠지 묻는다.
   - 확인: 장면 run 일괄 끝까지의 기록에서 사용자에게 물은 자리가 실행 방식, 고칠지, 합칠지 셋뿐이다
   - 확인: 그 시험 폴더의 `git log --oneline`에 회고 문제로 더한 phase의 커밋, review와 eval의 커밋, 고침 task의 커밋, 비운 커밋이 이 순서로 있다
   - 확인: 비운 커밋의 부모에서 `docs/tasks/review.md`에 다섯 범주의 A~E, Sonar way 통과 여부, 판단 항목마다 파일:줄 근거가 있고, `docs/tasks/eval.md`에 여섯 기준의 A~E와 스킬로 만들 후보 절이 있다
   - 확인: `docs/BACKLOG.md`에 미룬 소스 문제가 그 tasks 이름과 함께 있고 `AGENTS.md`의 문서 지도에 그 행이 있다. `ls -A docs/tasks` → `.gitkeep`만 나온다
   - 확인: 완료 조건 13의 확인에 이 기록이 든다
7. plate 자체의 고칠 거리는 묻고 GitHub 이슈로 올리며, 같은 이슈가 있으면 "다시 나옴" 댓글을 단다. 시험에서 올린 이슈는 확인한 뒤 지운다.
   - 확인: 장면 run 일괄 끝까지의 기록에서 이슈를 올린 명령과 결과(이슈 번호)를, 같은 문제로 끝을 다시 돌린 기록에서 그 번호에 "다시 나옴" 댓글을 단 명령과 결과를 읽는다
   - 확인: 그 이슈 번호마다 `gh issue view <번호> --repo werwer748/harness-plate` → 찾을 수 없다는 오류
   - 확인: 완료 조건 13의 확인에 두 기록이 든다
8. 일괄 방식에서도 같은 phase의 check가 세 번 실패하면 멈추고, 정해 둔 선택지 대신 원인과 해결책을 보이고 논의한다.
   - 확인: 장면 check 세 번 실패의 시험 폴더에서 그 `phase-N.md`의 확인 절이 셋이고 셋 모두 판정이 실패이며, 그 뒤의 수행 커밋이 없다
   - 확인: 기록의 마지막 답이 원인과 해결책을 보이고 고를 선택지 목록을 내지 않는다
   - 확인: 완료 조건 13의 확인에 이 기록이 든다
9. 훅이 새 구조에서 돈다: `phase-N.md`가 있는 task가 없으면 코드 편집을 막고, `done-phase-N.md`만 있는 task는 끝난 task이고, 막는 글이 새 낱말을 쓰며, `task/NNN-slug` 브랜치와 `.worktrees/` 규칙이 없다.
   - 확인: `python3 -m unittest discover -s tests` → 마지막 줄 `OK`
   - 확인: `grep -n 'task/\|\.worktrees' plugins/plate/hooks/edit_guard.py` → 0줄
   - 확인: `grep -c 'done-phase' tests/test_edit_guard.py` → 1 이상
10. 맥락 문서, README, 이 레포의 `AGENTS.md`가 새 흐름을 말한다.
    - 확인: `grep -n "verify\|LESSONS\|worktree" docs/PRD.md docs/ARCHITECTURE.md README.md AGENTS.md` → 0줄
    - 확인: `diff <(sed -n '/<!-- plate:rules:start -->/,/<!-- plate:rules:end -->/p' AGENTS.md) <(sed -n '/<!-- plate:rules:start -->/,/<!-- plate:rules:end -->/p' plugins/plate/skills/setup/SKILL.md)` → 출력 없음
    - 확인: `grep -hF '| `docs/tasks/' AGENTS.md plugins/plate/skills/setup/SKILL.md | sort -u | wc -l` → `1`
    - 확인: `docs/ARCHITECTURE.md`에 명령 절이 하나 있고, 테스트는 `python3 -m unittest discover -s tests`, 빌드와 린트는 "없음"이다
    - 확인: `docs/PRD.md`의 핵심 기능 5, 7, 8과 `docs/ARCHITECTURE.md`의 디렉터리 구조, 패턴과 규칙, 데이터 흐름을 읽어 아홉 스킬과 새 흐름을 말한다
11. `docs/ADR.md`에 GitHub 이슈를 하네스 고칠 거리를 모으는 외부 서비스로 쓴다는 항목이 있다.
    - 확인: `grep -n "^### ADR-020" docs/ADR.md` → 1줄이고, 그 항목을 읽어 GitHub 이슈의 결정, 이유, 트레이드오프가 있다
12. 두 매니페스트의 버전이 0.10.0이고 설명이 아홉 스킬을 말한다.
    - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `  "version": "0.10.0",`
    - 확인: 두 매니페스트의 `description`을 읽어 아홉 스킬이 있고 verify가 없다
13. 시험 장면 넷의 기록은 바뀐 본문으로 만든 것이다.
    - 확인: `N=$(ls -t plugins/plate/skills/*/SKILL.md plugins/plate/hooks/*.py plugins/plate/hooks/*.json | head -1); find ~/plate-rail-test/logs -name '*.jsonl' -newer "$N"` → 네 장면(setup·plan, run task 하나씩, run 일괄 끝까지와 그 다시 돌림, check 세 번 실패)의 기록이 모두 나온다
14. `docs/TOOLS.md`에 이 단계의 판정에서 확인한 사실이 있다.
    - 확인: `docs/TOOLS.md`의 Claude Code 절을 읽어, 이 단계의 판정 묶음에 에이전트 결과로 돌아오는 사용량, `gh`로 이슈 올리기·댓글·지우기, 시험 폴더와 기록 위치, 실행 시간이 날짜·버전과 함께 있다
15. 프로젝트 전체 테스트가 모두 통과한다.
    - 확인: `python3 -m unittest discover -s tests` → 마지막 줄 `OK`

## 결정
- 낱말은 tasks > task > phase다. tasks는 요청 하나를 계획한 묶음이고 `docs/tasks/`에 하나만 있다. task는 tasks 안의 `NNN-slug/` 폴더 하나, phase는 task 안의 `phase-N.md` 하나다. 이유: 지금 본문의 "작업"이 task를 뜻하는지 tasks를 뜻하는지 헷갈린다.
- `docs/tasks/`에는 진행 중인 tasks 하나만 두고, tasks가 끝나면 비운다. 기록은 git 이력에 남는다. 이유: 말하지 않음.
- 기록 파일: tasks에는 `plan.md`(tasks 머리), `FRICTION.md`, `RUNLOG.md`, `review.md`, `eval.md`, task 폴더가 있고, task 폴더에는 `plan.md`(task 머리), `phase-N.md`, `done-phase-N.md`, `retro.md`가 있다. 이유: `FRICTION.md`는 사용자가 고른 이름이고, 나머지는 지금 쓰는 이름의 꼴(`plan.md`, `phase-N.md`, `verify.md`)을 따른다 (추천안으로 정함).
- tasks 머리는 제목, 브랜치에 쓸 영어 소문자 이름, 여섯 절(요청, 목표, 범위 밖, 완료 조건, 결정, task 목록)이고 완료 조건은 비울 수 없다. task 머리는 제목과 네 절(목표, 범위 밖, 완료 조건, 결정)이다. 이유: 완료 조건은 사용자가 필수로 덧붙였고, task마다 머리를 두면 phase 에이전트가 task 머리와 자기 phase 파일만 읽어 컨텍스트가 작게 유지된다.
- plan은 처음에 모든 task의 머리와 phase까지 쓴다. 승인은 tasks 머리를 먼저, 그다음 task마다 받고, 모두 받은 뒤 한꺼번에 쓰고 한 커밋으로 넣는다. 이유: 일괄 실행이 끝까지 멈추지 않고 돌 수 있고, 초안을 task 단위로 읽어 읽기 쉽다.
- tasks가 진행 중일 때 새 요청이 오면 plan이 지금 tasks에 task로 더할지 묻는다. 이유: 말하지 않음.
- 브랜치는 tasks마다 하나(`tasks/<이름>`)이고 worktree는 쓰지 않는다. 이유: 말하지 않음.
- 스킬은 일마다 하나다: setup(설치), context(맥락 채우기), plan(계획), run(조율), phase(phase 수행), check(phase 확인), retro(task 회고. 지금의 retro와 verify를 합친다), review(tasks 끝 코드 평가), eval(tasks 끝 하네스 eval). verify는 없앤다. 이유: 말하지 않음.
- 수행, 확인, 회고, 코드 평가, 하네스 eval은 매번 다른 새 에이전트가 하고, 평가한 쪽은 고치지 않는다. 이유: 말하지 않음.
- 검증 구간(check, retro, review)은 모두 빌드·린트·테스트를 돌린다. 명령은 `docs/ARCHITECTURE.md`의 명령 절 한곳에 두고, 없는 명령은 실패가 아니라 "없음"이다. 이유: 말하지 않음.
- 명령 절이 없거나 비었으면 plan이 빌드 매니페스트와 코드에서 찾고 못 찾으면 묻고, 첫 task의 첫 phase TODO에 그 절을 쓰는 일을 넣는다. 이유: 이미 셋업된 프로젝트에도 통하고 setup과 context를 고치지 않는다.
- 실행 방식은 둘이고 run이 시작할 때 묻는다. task 하나씩은 task 회고 때 묻는다. tasks 일괄은 회고에서 나온 문제를 고칠 phase를 더해 묻지 않고 고치고, 끝에서 고칠지를 한 번에 묻는다. 이유: 요청 — "tasks 시작때 만약 여기까지 자동으로 진행할지 묻고 진행한다고하면 이과정역시 자동화로 쭈욱".
- 어느 방식이든 막힘, 훅의 세 번째 막음, 계획이 틀림, 같은 phase의 check나 같은 task의 회고가 세 번 실패하면(처음과 고친 뒤 두 번) 그 자리에서 멈추고, 정해 둔 선택지 대신 원인과 해결책을 보이고 논의한다. 이유: 말하지 않음.
- 통과한 phase는 `done-phase-N.md`로 이름을 바꿔 tasks 끝까지 남긴다. 이유: 훅과 run의 "남은 phase" 판정(`phase-N.md` 꼴)이 그대로 통하고, 회고와 eval이 git 이력을 뒤지지 않고 파일을 바로 읽는다.
- `FRICTION.md`에는 retro가 task마다 tasks 끝에 볼 것(문제, 멈춤, 스킬로 만들 후보)을 task 이름과 함께 한 줄씩 적는다. 이유: 요청 — "한 task를 처리할때마다 … 작업에 문제가 있었거나 멈췄거나 주기적으로 반복되서 스킬화하면 좋을꺼같은 제안 같은걸 기록해놔".
- `RUNLOG.md`에는 run이 띄운 에이전트마다 한 줄(역할, task와 phase, 토큰, 도구 호출, 시간)과 사용자에게 물은 자리마다 한 줄(물은 것, 답)을 적고, eval이 효율과 사람 개입률을 여기서 센다. 이유: FRICTION은 사람이 읽는 "볼 것"이라 숫자 줄을 섞지 않는다.
- tasks 끝의 순서는 review와 eval → 전체 보고 → 고칠지 묻는다이다. 소스를 고치면 같은 tasks에 고침 task를 더해 같은 레일로 돌리고, 고친 뒤에는 빌드·린트·테스트와 tasks 머리의 완료 조건만 다시 본다. 이유: 말하지 않음.
- 비운 뒤 기본 브랜치로 합칠지 묻는다. 이유: 검증하지 않은 일이 기본 브랜치에 들어가지 않게 하는 지금 규칙을 011 전까지 잇는다 (추천안으로 정함).
- 코드 평가: tasks에서 바뀐 코드만 본다. 범주 다섯(신뢰성, 보안, 유지보수성, 테스트 적절성, 기능 적합성)을 A~E로 매기고 총점은 없다. 잴 수 있는 것은 도구로 재고, 판단 항목은 Google 리뷰 지침과 등급표, 근거(파일:줄)로 매긴다. 통과선은 Sonar way이고 "측정 못함"과 "판단 못함"을 허용한다. 이유: 요청 — "평가 기준을 만들어서 점수화해서 보여주면 좋겠어(이부분은 업계에서 많이 사용하는 체계를 적용하고싶어)".
- 하네스 eval: 6기준(결과 성공, 일관성, 효율, 규칙 준수, 사람 개입률, 실패 양상(MAST))을 A~E로 매기고, 스킬로 만들 후보를 리포트의 한 절로 둔다. `docs/tasks/`를 비우기 전에 한다. 이유: 요청 — "하네스에대한 eval도 수행하면 좋겠어 REPAIR에 기록도 포함해서 이 때의 평가 기준역시 업계에서 많이 쓰는 기준 6가지 정도로".
- 하네스 고칠 거리: plate 자체의 것은 묻고 `werwer748/harness-plate`에 GitHub 이슈로 올리며, 같은 이슈가 있으면 "다시 나옴" 댓글을 단다. 고침은 harness-plate에서 한다. 그 프로젝트만의 것은 묻고 그 프로젝트에서 고친다. 이유: 대상 레포에서 plate를 고치면 그 프로젝트에서만 다르게 돈다.
- 미룬 소스 문제는 `docs/BACKLOG.md`에 둔다. 프로젝트 소스 문제만 두고, 항목마다 나온 tasks를 적고, 다시 나오면 고치자고 제안하고, 세 번의 tasks 동안 다시 나오지 않으면 지운다. 이유: 말하지 않음.
- setup은 설치만 하고 끝 물음 없이 끝난다. context는 그대로 둔다. 이유: 요청 — "프로젝트의 세팅 그럼 세팅에서 끝. 거기서 무언가 더하진 않지 그냥 하네스를 설치만 하는거야".
- 요청이 맥락 문서와 어긋나는 곳(PRD 핵심 기능 5·7·8, ARCHITECTURE의 run 브랜치 규칙과 데이터 흐름, 이 레포 `AGENTS.md`의 규칙 구간)은 문서를 바꾸기로 하고 진행한다. 이유: 말하지 않음.
- 010은 저장소 밖에 둔 0.9.1 복사본을 `--plugin-dir`로 연 세션에서 실행한다. 이유: 010 내내 레일과 훅이 옛 판 그대로이고, 바뀌는 `plugins/plate/`는 그 세션에서 그냥 파일이 된다.
- phase 11에 run "멈춘다"의 해결책 하나 규칙, eval 규칙 준수 등급표의 읽기 범위 칸, 네 장면 다시 돌리기를 더한다. 이유: phase 11의 시험에서 완료 조건 8(멈춘 답이 다른 안을 늘어놓음)과 6(규칙 준수가 판단 못함)이 실패했고, 본문을 고치면 완료 조건 13이 바뀐 본문의 기록을 요구한다.
