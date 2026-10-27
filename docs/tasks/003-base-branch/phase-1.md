# Phase 1: run과 review에 로컬 기본 브랜치를 다루는 글을 넣는다

**목표**: run 1번이 앞선 커밋을 알리고 되돌릴지 묻고, 두 스킬의 낱말과 맥락 문서, README가 그와 맞는다.

**테스트 먼저**: 아니오 — `.md`(스킬 본문과 문서)만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (고칠 스킬. frontmatter의 description, 낱말 "기본 브랜치"와 "작업 트리의 스킬 줄", 1번의 "tasks 브랜치", `RUNLOG.md` 절)
- `plugins/plate/skills/review/SKILL.md` (낱말 "기본 브랜치"와 "갈라진 곳")
- `docs/ARCHITECTURE.md` ("패턴과 규칙"에서 "run은 기본 브랜치"로 시작하는 항목, "데이터 흐름"의 실행 줄)
- `README.md` (표의 `run` 행)
- `docs/TOOLS.md`의 "Claude Code" 절에서 run의 시험 폴더가 셋업 커밋과 계획 커밋을 로컬 `main`에 둔 채 tasks 브랜치를 가른 일을 적은 줄 (이 문제가 처음 드러난 곳)
- `gh issue view 29` (#29의 본문)

**TODO**
- [ ] run 1번의 "tasks 브랜치" 항목에, 브랜치를 만들거나 바꾼 뒤 origin과 `origin/<기본 브랜치>`가 있고 로컬 기본 브랜치에 거기 없는 커밋이 있으면 그 커밋을 보여 주고 로컬 기본 브랜치를 `origin/<기본 브랜치>`로 되돌릴지 묻는 글이 더해진다. 알아보는 명령, 되돌리는 명령, 승인과 거절 뒤의 길, 커밋이 tasks 브랜치에 남는다는 것, `git fetch`를 하지 않는다는 것이 함께 적힌다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] run의 `RUNLOG.md` 절의 물은 자리 목록과 task에 걸리지 않는 물음의 목록에 `기본 브랜치`가 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] run의 낱말 "작업 트리의 스킬 줄"과 review의 낱말 "갈라진 곳"이 로컬 기본 브랜치(원격 추적 ref가 아님)의 `git merge-base <기본 브랜치> HEAD`라고 밝히도록 바뀐다 (`plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/review/SKILL.md`)
- [ ] run의 frontmatter의 description이 새 물음과 어긋나면 맞게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `docs/ARCHITECTURE.md`의 "패턴과 규칙"에서 "run은 기본 브랜치"로 시작하는 항목과 "데이터 흐름"의 실행 줄에 새 물음이 더해지고, `README.md`의 표의 `run` 행이 새 물음과 어긋나면 맞게 바뀐다 (`docs/ARCHITECTURE.md`, `README.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `mktemp -d` 안에 bare 원격과 그 복제본을 만들고, 복제본의 기본 브랜치에 원격에 없는 커밋 하나를 더한 뒤 run 1번에 적힌 브랜치 만들기, 알아보기, 되돌리기 명령을 적힌 그대로 돌린다. 되돌리기 전에는 알아보기가 커밋 1개를, 되돌린 뒤에는 0개를 내고, 되돌린 뒤 `git merge-base <기본 브랜치> tasks/<이름>`이 원격 기본 브랜치의 끝이고, `git log tasks/<이름>`에 그 커밋이 있다. 하나라도 다르면 실패. 임시 디렉터리는 지운다
- 완료 조건 2가 참이다.
  - 확인: `plugins/plate/skills/run/SKILL.md`의 `RUNLOG.md` 절을 읽어 물은 자리 목록과 task에 걸리지 않는 물음의 목록에 저마다 `기본 브랜치`가 있다
- 완료 조건 3이 참이다.
  - 확인: run의 낱말 "작업 트리의 스킬 줄"과 review의 낱말 "갈라진 곳"을 읽어 둘 다 로컬 기본 브랜치의 merge-base라고 적는다. 하나라도 없으면 실패
- 완료 조건 4가 참이다.
  - 확인: `docs/ARCHITECTURE.md`의 "패턴과 규칙"에서 "run은 기본 브랜치"로 시작하는 항목과 "데이터 흐름"의 실행 줄, `README.md`의 표의 `run` 행을 하나씩 읽어 새 물음과 어긋나지 않는다
