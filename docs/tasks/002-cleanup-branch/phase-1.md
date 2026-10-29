# Phase 1: cleanup이 cleanup 브랜치에서 커밋하고 끝을 묻는다

**목표**: cleanup이 `cleanup/<보고서 이름>`을 만들어 거기서만 커밋하고, 고른 발견이 없으면 PR이나 합침을 묻는다. 그 동작이 PRD와 ARCHITECTURE와 테스트에 맞는다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트, 맥락 문서만 고친다

**읽을 것**
- `plugins/plate/skills/cleanup/SKILL.md`의 절대 규칙, "1. 범위를 정한다"(보고서 경로의 번호 붙이기), "5. 보고서를 쓰고 커밋한다", "6. tasks로 만들지 묻는다", "7. 고른 것을 plan에 넘기고 고르지 않은 것을 미룬다", "8. 보고한다"
- `plugins/plate/skills/run/SKILL.md`의 낱말 "글을 넘기는 법", "GitHub 원격", "plate 워크플로", "기본 브랜치"와 "PR을 연다", "합친다" (같은 뜻으로 맞출 글)
- `tests/test_cleanup_skill.py`의 `AbsoluteRulesTest`, `CommitAndAskTest`
- `docs/PRD.md`의 핵심 기능 9
- `docs/ARCHITECTURE.md`의 디렉터리 구조의 `cleanup/SKILL.md` 줄, 데이터 흐름의 "정리 점검"
- `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`

**TODO**
- [ ] cleanup의 절대 규칙 2·3·4가 바뀐다.
  - 2: 커밋은 `cleanup/<보고서 이름>`에만 넣는다.
  - 3: 푸시는 고른 발견이 없을 때 승인받아 그 브랜치를 origin에 올릴 때만 하고, 그 브랜치를 만들고 바꾸는 것만 한다.
  - 4: 묻는 자리는 6번과 그 PR·합침 물음이다.
  (`plugins/plate/skills/cleanup/SKILL.md`)
- [ ] 보고서를 쓰기 전에 브랜치를 맞추는 일이 더해진다. git 레포이면 지금 브랜치의 HEAD에서 `cleanup/<보고서 이름>`을 묻지 않고 `git switch -c`로 만든다. 같은 이름의 로컬 브랜치가 있으면 보고서 번호처럼 없는 번호를 붙인다. 만들지 못하면 쓰지 않고 실패한 명령과 오류를 보고하고 끝난다. 명령 치환 없이 한 명령씩 부른다 (`plugins/plate/skills/cleanup/SKILL.md`)
- [ ] 고른 발견이 없을 때(6번에서 하나도 고르지 않았거나 남은 발견이 없을 때) PR이나 합침을 묻는 자리가 더해진다.
  - origin이 GitHub이면: 그 브랜치를 푸시해 기본 브랜치로 가는 PR(제목은 보고서의 제목, 본문은 보고서 파일)을 열지 묻는다.
  - 그 밖이면: 기본 브랜치에 합칠지 묻는다. squash하지 않고, 충돌하면 되돌린다.
  - 제목은 작은따옴표로, 본문은 `--body-file`로 넘기는 법과 GitHub 원격·기본 브랜치의 뜻은 run의 낱말과 같게 cleanup의 낱말에 둔다.
  - 8번 보고에 브랜치, PR 주소나 합친 곳, 하지 않았으면 그 까닭이 더해진다.
  (`plugins/plate/skills/cleanup/SKILL.md`)
- [ ] 바뀐 글을 지키는 시험이 된다. `AbsoluteRulesTest.test_core_rules_present`의 규칙 3 단언이 새 글을 지키고, 브랜치 만들기(같은 이름이면 번호), 고른 발견이 없을 때의 PR·합침 물음을 보는 시험이 더해진다 (`tests/test_cleanup_skill.py`)
- [ ] 맥락 문서가 맞는다. PRD 핵심 기능 9, ARCHITECTURE 디렉터리 구조의 cleanup 줄, 데이터 흐름의 "정리 점검"이 cleanup 브랜치와 고른 발견이 없을 때의 PR·합침을 적는다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`)

**통과 조건**
- task 머리의 완료 조건 1이 참이다.
  - 확인: `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 절대 규칙, 보고서를 쓰고 커밋하는 절, 고른 발견이 없을 때의 절에 저마다 한 줄 이상
  - 확인: `grep -n -e '브랜치를 만들거나 바꾸지 않는다' -e '^3\. \*\*푸시하지 않는다' plugins/plate/skills/cleanup/SKILL.md` → 절대 규칙 절에서는 아무것도 나오지 않음. 1·2라운드에 맡기는 글의 줄만 나와도 된다
  - 확인: `mktemp -d` 시험 레포(기본 브랜치 `main`, 커밋 하나)에서 본문의 브랜치 명령을 적힌 차례대로 세 갈래로 돌린다. `main`에서 돌리면 새 `cleanup/…`가 `main`의 HEAD에서 생기고 `git rev-parse main`이 전과 같다. `tasks/x`(커밋 하나 더)에서 돌리면 새 `cleanup/…`가 `tasks/x`의 HEAD에서 생기고 `main`이 전과 같다. 같은 이름의 `cleanup/…`가 이미 있으면 번호를 붙인 새 이름의 브랜치가 생기고 옛 브랜치의 해시는 그대로다
- task 머리의 완료 조건 4 가운데 cleanup 쪽이 참이다.
  - 확인: `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 9, ARCHITECTURE 디렉터리 구조의 cleanup 줄, 데이터 흐름의 "정리 점검"에 저마다 한 줄 이상
- 테스트가 통과한다.
  - 확인: `python3 -m unittest tests.test_cleanup_skill -v` → `OK`, 새 시험 이름이 나온다
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
