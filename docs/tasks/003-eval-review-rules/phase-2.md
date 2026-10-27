# Phase 2: 장면 H와 I를 돌린다

**목표**: eval(#36)과 review(#43)를 지난 tasks 기록으로 돌려 `docs/TOOLS.md`에 남긴다.

**테스트 먼저**: 아니오 — 스킬을 돌려 보고 `.md`에 적는다

**읽을 것**
- `plugins/plate/skills/eval/SKILL.md`의 "2. 실패를 모아 MAST 유형으로 나눈다" (phase 1이 고친 동작)
- `plugins/plate/skills/review/SKILL.md`의 "5. 등급을 매긴다"와 "결과물인 마크다운만 바뀐 경우의 테스트 적절성" 표 (#43을 볼 동작)
- `gh issue view 43 --repo werwer748/harness-plate` (원인과 해결책)
- `git show e3836b2:docs/tasks/eval.md` (장면 H와 견줄 실패 목록. "유형 없음" 13개)
- `git show aa0882b:docs/tasks/review.md` (장면 I와 견줄 평가 절. 테스트 적절성 D)
- `docs/TOOLS.md`의 "Claude Code" 절 (헤드리스 명령의 꼴, 허용 목록, 장면 절의 꼴)

**TODO**
- [x] 장면 H: 복제본의 브랜치를 `e3836b2`에 두고 `docs/tasks/eval.md`를 지운 커밋을 더하고, 기본 브랜치를 그 tasks가 갈라진 곳에 두고 eval을 부른다. 새 `eval.md`의 실패 목록에 그 task의 회고가 "문제"로 판정하지 않은 `남은 것:` 줄과 명령 절의 메모 줄이 없고, "유형 없음" 실패가 13개보다 적은지 본다 (임시 폴더)
- [x] 장면 I: 새 복제본의 브랜치를 `6292d12`에 두고 기본 브랜치를 `32e2fbb`에 두고 review를 부른다. 새 `review.md`의 테스트 적절성이 "결과물인 마크다운만 바뀐 경우의 테스트 적절성" 표로 매겨지고 근거가 완료 조건의 확인 줄과 `돌리지 않음` 줄이며, 실행 코드의 테스트가 없다는 까닭으로 D 이하를 매기지 않았는지 본다 (임시 폴더)
- [x] 장면 H가 기대와 다르면 `plugins/plate/skills/eval/SKILL.md`를 고치고 장면 H를 새 복제본에서 다시 돈다. 장면 I가 기대와 다르면 `plugins/plate/skills/review/SKILL.md`의 "5. 등급을 매긴다"를 고치고 장면 I를 새 복제본에서 다시 돈다 (`plugins/plate/skills/eval/SKILL.md`, `plugins/plate/skills/review/SKILL.md`)
- [x] `docs/TOOLS.md`의 "Claude Code" 절 끝에 eval·review 장면 H·I 절이 더해진다. task 머리의 결정에 적힌 필드를 장면마다 적고, 장면 I가 기대대로였으면 #43이 issue-sweep의 review 고침으로 이미 고쳐졌다고 적는다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건 1~3의 확인을 모두 돌린다. 완료 조건 3의 장면 H·I는 그 조건에 적힌 기대로 본다
- review 본문을 고쳤으면 그 동작과 맥락 문서가 맞는다.
  - 확인: review를 고쳤으면 `docs/ARCHITECTURE.md`의 "데이터 흐름"의 tasks 끝 갈래와 `README.md`의 `review` 행을 읽어 고친 등급 규칙과 어긋나는 줄이 없다. 고치지 않았으면 `git diff --stat {이 phase가 시작한 커밋} -- plugins/plate/skills/review/SKILL.md`가 아무것도 내지 않는다

## 한 일
- 장면 H: 임시 복제본 `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.ZrtRAkxcY3/repo`의 `tasks/issue-sweep`을 `e3836b2`에 두고 `eval.md`를 지운 `5065c9a`를 더하고 `main`을 `32e2fbb`에 두고 `claude -p "/plate:eval"`을 돌렸다. 새 `eval.md`(`4d2de49`)의 실패 15개에 `남은 것:` 줄과 명령 절의 메모 줄이 없고 "유형 없음"이 2개다(`e3836b2`는 13개). 기대와 같다 (임시 폴더)
- 장면 I: 임시 복제본 `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.cLI3gHHZIY/repo`의 `tasks/cleanup`을 `6292d12`에 두고 `main`을 `32e2fbb`에 두고 `claude -p "/plate:review"`를 돌렸다. 새 `review.md`(`e23398a`)의 테스트 적절성이 "결과물인 마크다운만 바뀐 경우" 표로 C이고, 근거는 완료 조건의 확인과 확인·`돌리지 않음` 줄이 없는 동작이며, 실행 코드의 테스트를 까닭으로 들지 않았다. 기대와 같다 (임시 폴더)
- 장면이 기대와 다르면 본문을 고치고 다시 돈다: 두 장면 모두 기대와 같아 eval과 review 본문을 고치지 않았다 (`plugins/plate/skills/eval/SKILL.md`, `plugins/plate/skills/review/SKILL.md` 그대로)
- `docs/TOOLS.md`의 "Claude Code" 절 끝(장면 G 절 뒤, "## Codex" 앞)에 "고친 eval과 review를 장면 H·I로 돌려 본 것" 절을 더했다. 장면마다 Claude Code 버전, 복제본의 브랜치와 `main`의 커밋, 돌린 시각, 세션 id, 기대한 결과, 본 결과, 걸린 시간, 막힌 명령, 임시 폴더의 기록 경로(지워질 수 있다고 밝힘)를 적고, #43이 issue-sweep의 review 고침(`4900cd3`, `d9a1097`)으로 이미 고쳐졌다고 적었다 (`docs/TOOLS.md`)

## 확인 결과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/eval/SKILL.md`의 2번을 읽음 → `남은 것:` 줄은 회고가 "문제"로 판정한 것만 실패로 센다(잡힌 곳은 그 자리)는 글과 명령 절의 사실이나 판단만 적은 메모 줄은 실패가 아니라는 글이 저마다 있다. `python3 -m unittest discover -s tests` → 마지막 줄 `OK`, `claude plugin validate .` → `✔ Validation passed`. 통과
  - 완료 조건 2: `docs/PRD.md` 핵심 기능 8, `docs/ARCHITECTURE.md` 데이터 흐름의 tasks 끝 갈래(70~74행), `README.md`의 `eval` 행, eval description을 읽음 → 모두 실패를 MAST로 나눠 센다는 수준이고 실패로 세는 줄과 어긋나는 글이 없다. 통과
  - 완료 조건 3: `docs/TOOLS.md`의 새 절을 읽음 → 장면 H·I마다 버전 2.1.311, 시각, 세션 id(`8ff2f574-…`, `85a27c0a-…`), 기대한 결과와 본 결과가 있고 본 결과가 기대와 같다. `git log -1 --format=%cI -- plugins/plate/skills/eval/SKILL.md plugins/plate/skills/review/SKILL.md` → `2026-10-27T21:34:17+09:00`, 장면 시작 21:35:55·21:35:58이 더 늦다. 통과
- review 본문을 고쳤으면 그 동작과 맥락 문서가 맞는다.
  - 고치지 않았다. `git diff --stat 040fc91 -- plugins/plate/skills/review/SKILL.md` → 출력 없음. 통과

## 계획과 달라진 점
- 결정의 허용 목록은 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"의 13이지만, 두 스킬이 갈라진 곳과 기본 브랜치를 보는 `"Bash(git merge-base:*)" "Bash(git symbolic-ref:*)"`를 더했고, 장면 I에는 review가 돌리는 명령 절의 `"Bash(claude plugin validate:*)"`도 더했다. 장면 A~D의 run처럼 스킬이 부르는 명령에 맞춘 것이다. `docs/TOOLS.md`의 장면 절에 적었다
- 장면 H의 `main`은 "그 tasks가 갈라진 곳"으로 issue-sweep의 계획 커밋 `a3c1158`의 부모인 `32e2fbb`에 두었다

## 남은 것
- 장면 I의 review는 메인에서 3개 명령(`command -v …`, `cut`과 `grep`을 이은 것, `grep -o -E` 단독)이 허용 목록에 없어 막혔다. 다른 꼴로 다시 돌려 결과에는 걸리지 않았지만, 허용 목록에 `grep`·`cut`이 없다
- 장면은 각 한 번만 돌렸다. 한 번의 실행이라 되풀이해도 같은 결과일지는 보지 않았다

## 하네스에서 걸린 것
- 계획의 결정이 허용 목록을 13으로 정했지만 eval과 review는 `git merge-base`, `git symbolic-ref`로 갈라진 곳을 보므로 그 목록으로는 막힐 수 있다. "스킬을 헤드리스로 돌려 볼 때의 허용 목록"이 스킬마다 부르는 명령을 다 담지 않는다
