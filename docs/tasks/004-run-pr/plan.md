# tasks 끝의 PR

## 목표
GitHub 원격이 있는 프로젝트에서 run이 tasks 끝에 `docs/tasks/`를 비운 뒤 PR을 열지 묻는다. 승인하면 tasks 브랜치를 origin에 푸시하고 기본 브랜치로 가는 PR을 연다. plate의 CI 워크플로가 없으면 로컬 평가서를 PR 댓글로 단다. GitHub 원격이 없으면 지금처럼 합칠지 묻는다.

## 범위 밖
- PR을 머지하거나 닫는 것. CI의 판정 스크립트나 사용자가 한다
- PR을 연 뒤 CI의 판정을 기다리거나 받아 보는 것
- tasks 끝의 코드 평가, 하네스 eval, 고칠 안의 물음을 바꾸는 것

## 완료 조건
1. run의 tasks 끝에서 "비운다" 뒤가 이렇게 된다. origin이 GitHub이면 푸시할 브랜치와 PR 제목·본문을 보여 주고 PR을 열지 묻는다. 승인하면 `tasks/<이름>`을 origin에 푸시하고 기본 브랜치로 가는 PR을 연다. PR 본문에는 tasks 머리의 요청과 목표, tasks 끝의 전체 보고(코드 평가와 하네스 eval의 등급, 게이트, 고친 것, 올린 이슈)가 든다. plate의 CI 워크플로가 없으면 `review.md`의 마지막 평가 절을 PR 댓글로 단다. 거절하면 브랜치를 그대로 둔다. origin이 GitHub이 아니거나 없으면 지금의 "합친다"를 따른다.
   - 확인: `plugins/plate/skills/run/SKILL.md`의 tasks 끝, "합친다", 새 PR 절을 읽어 위의 것이 있다
2. run의 절대 규칙, 10번 보고, `RUNLOG.md` 규칙이 PR 열기와 맞는다. 푸시는 tasks 브랜치를 PR로 열 때만 하고, 보고에 PR 주소와 댓글 주소(열지 않았으면 그 까닭)가 든다. eval의 "정해 둔 물음"에 PR을 열지가 든다.
   - 확인: `plugins/plate/skills/run/SKILL.md`의 절대 규칙 5, 10번, `RUNLOG.md` 절과 `plugins/plate/skills/eval/SKILL.md`의 "정해 둔 물음"을 읽는다
3. `docs/ARCHITECTURE.md`의 run 규칙과 데이터 흐름, `docs/PRD.md`의 핵심 기능 8이 PR로 가는 tasks 끝을 적는다.
   - 확인: 두 문서의 그 곳을 읽어 "GitHub 원격이 있어도 기본 브랜치로 합칠지 묻는다"는 뜻의 옛 글이 남지 않았다

## 결정
없음
