# Phase 1: review의 테스트 적절성과 eval의 정해 둔 물음을 고친다

**목표**: review가 결과물인 마크다운만 바꾼 tasks의 테스트 적절성을 완료 조건으로 매기고, eval과 retro가 run의 물은 자리로 정해 둔 물음과 멈춤을 가른다.

**테스트 먼저**: 아니오 — `.md`(스킬 본문과 문서)만 고친다

**읽을 것**
- `plugins/plate/skills/review/SKILL.md` (고칠 스킬. 낱말 "결과물인 마크다운"과 "바뀐 코드 파일", 1번, 4번의 표, 5번의 등급표와 그 아래 줄, PR 모드 절, 기록의 양식의 테스트 적절성)
- `plugins/plate/skills/eval/SKILL.md` (고칠 스킬. 낱말 "정해 둔 물음"과 "멈춤", 3번의 사람 개입률)
- `plugins/plate/skills/retro/SKILL.md` (5번의 "멈춤")
- `plugins/plate/skills/run/SKILL.md` (`RUNLOG.md` 절의 물은 자리 목록. 읽기만 한다)
- `plugins/plate/skills/plan/SKILL.md` (적는 규칙 "조건"의 돌려 보는 확인과 `돌리지 않음` 줄. 읽기만 한다)
- `docs/ADR.md` (ADR-024의 트레이드오프)
- `gh issue view 27`과 `gh issue view 28` (두 이슈의 본문)

**TODO**
- [ ] review 4번의 표에서 테스트 적절성이 보는 것에, 바뀐 코드 파일이 결과물인 마크다운뿐이면 tasks 머리와 task 머리의 완료 조건이 바뀐 동작마다 돌려 보는 확인을 두었는지를 본다는 것이 더해진다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] review 5번에 결과물인 마크다운만 바뀐 경우의 테스트 적절성 칸(A~E)이 더해진다. 읽기만 하는 확인과 `- 돌리지 않음: {까닭}` 줄은 돌려 보는 확인보다 낮은 칸에 들고, 등급표 아래 줄이 이 경우에는 커버리지 대신 이 칸으로 매긴다고 적는다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] review의 PR 모드 절에 바뀐 코드 파일이 결과물인 마크다운뿐이면 테스트 적절성이 판단 못함(완료 조건이 없다)이라는 줄이 더해진다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] eval의 낱말 "정해 둔 물음"이 run의 `RUNLOG.md` 절의 물은 자리 가운데 `멈춤` 말고 모두로, "멈춤"이 물은 자리가 `멈춤`인 줄로 바뀌고, 3번의 사람 개입률이 그와 맞게 바뀐다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] retro 5번의 "멈춤" 줄이 eval의 낱말과 맞게 바뀐다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] ADR-024의 트레이드오프에서 테스트 적절성을 말하는 문장이 결과물인 마크다운만 바뀐 경우와 어긋나면 맞게 바뀐다 (`docs/ADR.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `plugins/plate/skills/review/SKILL.md`의 4번의 표, 5번의 등급표와 그 아래 줄, PR 모드 절을 하나씩 읽어 위의 것이 적혀 있다. 그 경우의 칸이 A~E로 나뉘어 있지 않거나 `돌리지 않음` 줄이 돌려 보는 확인과 같은 칸에 들면 실패
- 완료 조건 2가 참이다.
  - 확인: `plugins/plate/skills/run/SKILL.md`의 `RUNLOG.md` 절의 물은 자리 목록과 `plugins/plate/skills/eval/SKILL.md`의 낱말 "정해 둔 물음"을 견줘, `멈춤`을 뺀 목록이 같다. 다르면 실패
  - 확인: eval 3번의 사람 개입률과 retro 5번의 "멈춤" 줄을 읽어 eval의 낱말과 어긋나지 않는다
- 완료 조건 3이 참이다.
  - 확인: ADR-024의 트레이드오프에서 테스트 적절성을 말하는 문장을 읽어 결과물인 마크다운만 바뀐 경우와 어긋나지 않는다
- 완료 조건 4가 참이다.
  - 확인: `plugins/plate/skills/retro/SKILL.md`의 4번과 회고 절의 양식을 읽어, `done-phase-N.md`마다 "남은 것"의 줄(부작용과 한계, 동작의 결함, 돌려 보지 않은 위험)을 모아 줄마다 문제인지 판정해 회고 절에 적는다는 것이 있다
  - 확인: eval의 낱말 `done-phase-N.md`와 `retro.md`를 읽어 check의 확인 절과 retro의 회고 절의 항목과 어긋나지 않는다
  - 확인: review의 낱말 "갈라진 곳"을 읽어 로컬 기본 브랜치의 `git merge-base <기본 브랜치> HEAD`라고 적는다
