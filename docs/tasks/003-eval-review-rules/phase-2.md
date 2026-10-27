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
- [ ] 장면 H: 복제본의 브랜치를 `e3836b2`에 두고 `docs/tasks/eval.md`를 지운 커밋을 더하고, 기본 브랜치를 그 tasks가 갈라진 곳에 두고 eval을 부른다. 새 `eval.md`의 실패 목록에 그 task의 회고가 "문제"로 판정하지 않은 `남은 것:` 줄과 명령 절의 메모 줄이 없고, "유형 없음" 실패가 13개보다 적은지 본다 (임시 폴더)
- [ ] 장면 I: 새 복제본의 브랜치를 `6292d12`에 두고 기본 브랜치를 `32e2fbb`에 두고 review를 부른다. 새 `review.md`의 테스트 적절성이 "결과물인 마크다운만 바뀐 경우의 테스트 적절성" 표로 매겨지고 근거가 완료 조건의 확인 줄과 `돌리지 않음` 줄이며, 실행 코드의 테스트가 없다는 까닭으로 D 이하를 매기지 않았는지 본다 (임시 폴더)
- [ ] 장면 H가 기대와 다르면 `plugins/plate/skills/eval/SKILL.md`를 고치고 장면 H를 새 복제본에서 다시 돈다. 장면 I가 기대와 다르면 `plugins/plate/skills/review/SKILL.md`의 "5. 등급을 매긴다"를 고치고 장면 I를 새 복제본에서 다시 돈다 (`plugins/plate/skills/eval/SKILL.md`, `plugins/plate/skills/review/SKILL.md`)
- [ ] `docs/TOOLS.md`의 "Claude Code" 절 끝에 eval·review 장면 H·I 절이 더해진다. task 머리의 결정에 적힌 필드를 장면마다 적고, 장면 I가 기대대로였으면 #43이 issue-sweep의 review 고침으로 이미 고쳐졌다고 적는다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건 1~3의 확인을 모두 돌린다. 완료 조건 3의 장면 H·I는 그 조건에 적힌 기대로 본다
- review 본문을 고쳤으면 그 동작과 맥락 문서가 맞는다.
  - 확인: review를 고쳤으면 `docs/ARCHITECTURE.md`의 "데이터 흐름"의 tasks 끝 갈래와 `README.md`의 `review` 행을 읽어 고친 등급 규칙과 어긋나는 줄이 없다. 고치지 않았으면 `git diff --stat {이 phase가 시작한 커밋} -- plugins/plate/skills/review/SKILL.md`가 아무것도 내지 않는다
