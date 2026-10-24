# 회고

## 회고 1

**확인**
- run의 tasks 끝에서 "비운다" 뒤가 이렇게 된다. origin이 GitHub이면 푸시할 브랜치와 PR 제목·본문을 보여 주고 PR을 열지 묻는다. 승인하면 `tasks/<이름>`을 origin에 푸시하고 기본 브랜치로 가는 PR을 연다. PR 본문에는 tasks 머리의 요청과 목표, tasks 끝의 전체 보고(코드 평가와 하네스 eval의 등급, 게이트, 고친 것, 올린 이슈)가 든다. plate의 CI 워크플로가 없으면 `review.md`의 마지막 평가 절을 PR 댓글로 단다. 거절하면 브랜치를 그대로 둔다. origin이 GitHub이 아니거나 없으면 지금의 "합친다"를 따른다.
  - `plugins/plate/skills/run/SKILL.md`의 tasks 끝(244~), "비운다"(408~416), "PR을 연다"(418~455), "합친다"(457~466)를 읽었다 → "비운다"가 origin이 GitHub 원격이면 지우기 전에 tasks 머리의 제목·요청·목표, `review.md`의 마지막 평가 절, `eval.md`의 마지막 eval 절, 고침 task 머리의 완료 조건을 읽어 두고, 끝에서 GitHub 원격이면 "PR을 연다", 그 밖(origin 없음, GitHub 아님, git 레포 아님)이면 "합친다"로 간다. "PR을 연다" 1번이 푸시할 브랜치, 가는 곳(기본 브랜치), 제목과 본문을 보여 주고 묻고(plate 워크플로가 없으면 댓글을 단다는 것도 적는다), 거절하면 "푸시하지 않고 합치지도 않고 브랜치를 그대로 둔 채" 10번으로 간다. 2번 `git push origin tasks/<이름>`, 3번 `gh pr create --base {기본 브랜치} --head tasks/<이름>`, 4번 plate 워크플로가 없으면 `gh pr comment`로 `review.md`의 마지막 평가 절. "PR 본문의 꼴"에 요청, 목표, 코드 평가의 다섯 등급과 Sonar way 게이트, 하네스 eval의 여섯 등급, 고친 것, 올린 이슈가 있다. "합친다"의 첫 글은 "'비운다'에서 origin이 GitHub 원격이 아닐 때 온다"이고 1~6번은 그대로다. 통과
  - 스크래치 레포(문서 지도 구간, origin `https://github.com/werwer748/plate-ci-test.git`, `origin/HEAD` → `main`, 지금 브랜치 `tasks/pr-ci`)에서 PreToolUse JSON을 `plugins/plate/hooks/push_guard.py`에 넣었다 → `git push origin tasks/pr-ci`, heredoc 본문에 `git push origin main`과 작은따옴표가 든 `gh pr create … --body "$(cat <<'EOF' … EOF)"`와 `gh pr comment …` 모두 종료 코드 0, 대조로 넣은 `git push origin main`은 2. "PR을 연다"의 명령을 푸시 훅이 막지 않는다. 통과
- run의 절대 규칙, 10번 보고, `RUNLOG.md` 규칙이 PR 열기와 맞는다. 푸시는 tasks 브랜치를 PR로 열 때만 하고, 보고에 PR 주소와 댓글 주소(열지 않았으면 그 까닭)가 든다. eval의 "정해 둔 물음"에 PR을 열지가 든다.
  - `plugins/plate/skills/run/SKILL.md`의 절대 규칙 5(20줄), 10번(209~223), `RUNLOG.md` 절(468~486)과 `plugins/plate/skills/eval/SKILL.md`의 "정해 둔 물음"(40줄)을 읽었다 → 절대 규칙 5는 "푸시는 'PR을 연다'에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 한다. GitHub 이슈, PR, 댓글은 승인받은 것만 올린다." 10번 218줄은 "PR을 열지 물었으면 연 PR의 주소와 단 댓글의 주소. 열지 않았으면 그 까닭(거절, 실패한 명령과 오류), 댓글을 달지 않았으면 그 까닭(plate 워크플로가 있다, 실패한 명령과 오류)". `RUNLOG.md` 절 485줄은 비운 뒤에 물은 것(PR을 열지, 합칠지, 커밋하지 않은 변경)을 적지 않는다고 해 PR 물음이 비운 뒤에 오는 것과 맞는다. eval 40줄은 "tasks 끝의 고칠지, PR을 열지, 합칠지다". 통과
- `docs/ARCHITECTURE.md`의 run 규칙과 데이터 흐름, `docs/PRD.md`의 핵심 기능 8이 PR로 가는 tasks 끝을 적는다.
  - `grep -n "합칠\|합친\|PR을 열" docs/ARCHITECTURE.md docs/PRD.md`와 ARCHITECTURE 데이터 흐름(52~78줄)을 읽었다 → ARCHITECTURE 49줄은 "`origin`이 GitHub이면 … PR을 열지 묻고, `origin`이 없거나 GitHub의 것이 아니면 기본 브랜치로 합칠지 묻는다", 데이터 흐름 67~69줄은 "docs/tasks/를 비운다" → "origin이 GitHub이면 … PR을 열지 묻는다" → "origin이 없거나 GitHub의 것이 아니면 기본 브랜치로 합칠지 묻는다", PRD 18줄은 "origin이 GitHub이면 run이 tasks 브랜치를 푸시해 기본 브랜치로 가는 PR을 열지 묻고 … origin이 GitHub이 아니거나 없으면 기본 브랜치로 합칠지 묻는다"다. 조건 없이 합칠지 묻는 옛 글은 없다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.397s` / `OK`. 통과

**문제**
- `docs/ARCHITECTURE.md` 48줄(패턴과 규칙의 막는 장치 문단)은 "에이전트의 푸시를 막는 기본은 스킬마다의 '푸시하지 않는다' 규칙이고, 푸시 훅은 흔한 꼴을 한 번 더 막는다"고 적는데, 이 task가 run의 절대 규칙 5(`plugins/plate/skills/run/SKILL.md` 20줄)의 "푸시하지 않는다"를 "푸시는 'PR을 연다'에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 한다"로 바꿔 run에는 그 규칙이 없다. 49줄의 run 규칙은 이 푸시를 적지만 48줄은 고치지 않아 같은 문서의 두 줄이 어긋난다. phase 1의 TODO와 완료 조건 3이 ARCHITECTURE에서 run 규칙과 데이터 흐름만 가리켰다(`done-phase-1.md`의 하네스에서 걸린 것) (`docs/ARCHITECTURE.md`). 기준: 맥락 문서

**판정**: 문제 있음

## 회고 2

**확인**
- run의 tasks 끝에서 "비운다" 뒤가 이렇게 된다. origin이 GitHub이면 푸시할 브랜치와 PR 제목·본문을 보여 주고 PR을 열지 묻는다. 승인하면 `tasks/<이름>`을 origin에 푸시하고 기본 브랜치로 가는 PR을 연다. PR 본문에는 tasks 머리의 요청과 목표, tasks 끝의 전체 보고(코드 평가와 하네스 eval의 등급, 게이트, 고친 것, 올린 이슈)가 든다. plate의 CI 워크플로가 없으면 `review.md`의 마지막 평가 절을 PR 댓글로 단다. 거절하면 브랜치를 그대로 둔다. origin이 GitHub이 아니거나 없으면 지금의 "합친다"를 따른다.
  - `plugins/plate/skills/run/SKILL.md`의 tasks 끝(244~301), "고침 task를 더한다"(343~351), "비운다"(408~416), "PR을 연다"(418~455), "합친다"(457~466)를 읽었다 → 410줄이 origin이 GitHub 원격이면 지우기 전에 tasks 머리의 제목·요청·목표, `review.md`의 마지막 평가 절, `eval.md`의 마지막 eval 절, 고침 task 머리의 완료 조건을 읽어 두게 하고, 416줄이 GitHub 원격이면 "PR을 연다", 그 밖(origin 없음, GitHub 아님, git 레포 아님)이면 "합친다"로 보낸다. 422줄이 푸시할 브랜치, 가는 곳, 제목과 본문을 보여 주고 묻고(plate 워크플로가 없으면 댓글을 단다는 것도 적는다) 거절하면 "푸시하지 않고 합치지도 않고 브랜치를 그대로 둔 채" 10번으로 간다. 423줄 `git push origin tasks/<이름>`, 424줄 `gh pr create --base {기본 브랜치} --head tasks/<이름>`, 425줄 plate 워크플로가 없으면 `gh pr comment`로 `review.md`의 마지막 평가 절. 436~455줄 본문의 꼴에 요청, 목표, 코드 평가의 다섯 등급과 Sonar way 게이트, 하네스 eval의 여섯 등급, 고친 것, 올린 이슈가 있다. 459줄 "합친다"는 "'비운다'에서 origin이 GitHub 원격이 아닐 때 온다"이고 1~6번은 앞의 것 그대로다. 고침 task가 없을 때(345줄)도 "비운다"로 와서 PR로 간다. 통과
  - 이 레포(셋업됨, origin `github.com`, `origin/HEAD` → `main`, 지금 브랜치 `tasks/pr-ci`)를 cwd로 PreToolUse JSON을 `plugins/plate/hooks/push_guard.py`에 넣었다 → `git push origin tasks/pr-ci`, 본문이 `docs/tasks/004-run-pr/retro.md`, `docs/tasks/FRICTION.md`, `docs/tasks/003-push-guard/retro.md`, tasks 머리의 요청·목표인 423~425줄 꼴의 `gh pr create`와 `gh pr comment` 모두 종료 코드 0, 대조로 넣은 `git push origin main`은 2. "PR을 연다"의 명령을 푸시 훅이 막지 않는다. 통과
- run의 절대 규칙, 10번 보고, `RUNLOG.md` 규칙이 PR 열기와 맞는다. 푸시는 tasks 브랜치를 PR로 열 때만 하고, 보고에 PR 주소와 댓글 주소(열지 않았으면 그 까닭)가 든다. eval의 "정해 둔 물음"에 PR을 열지가 든다.
  - `plugins/plate/skills/run/SKILL.md`의 절대 규칙 5(20줄), 10번(209~223), `RUNLOG.md` 절(468~486)과 `grep -n "정해 둔 물음" plugins/plate/skills/eval/SKILL.md` → 20줄 "푸시는 "PR을 연다"에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 한다. GitHub 이슈, PR, 댓글은 승인받은 것만 올린다." 218줄 "PR을 열지 물었으면 연 PR의 주소와 단 댓글의 주소. 열지 않았으면 그 까닭(거절, 실패한 명령과 오류), 댓글을 달지 않았으면 그 까닭(plate 워크플로가 있다, 실패한 명령과 오류)". 485줄 비운 뒤에 물은 것(PR을 열지, 합칠지, 그 자리의 커밋하지 않은 변경)은 적지 않는다. eval 40줄 "tasks 끝의 고칠지, PR을 열지, 합칠지다". run 본문에서 푸시를 적은 곳은 3, 20, 420~427줄뿐이다. 통과
- `docs/ARCHITECTURE.md`의 run 규칙과 데이터 흐름, `docs/PRD.md`의 핵심 기능 8이 PR로 가는 tasks 끝을 적는다.
  - `grep -n "합칠\|합친\|PR을 열\|푸시하지 않는다" docs/ARCHITECTURE.md docs/PRD.md`와 ARCHITECTURE 52~78줄(데이터 흐름)을 읽었다 → ARCHITECTURE 49줄 "`origin`이 GitHub이면 `tasks/<이름>`을 origin에 푸시해 기본 브랜치로 가는 PR을 열지 묻고, `origin`이 없거나 GitHub의 것이 아니면 기본 브랜치로 합칠지 묻는다", 67~69줄 비운다 → GitHub이면 PR을 열지 → 없거나 GitHub의 것이 아니면 합칠지, PRD 18줄 "origin이 GitHub이면 run이 tasks 브랜치를 푸시해 기본 브랜치로 가는 PR을 열지 묻고 … origin이 GitHub이 아니거나 없으면 기본 브랜치로 합칠지 묻는다". 조건 없이 합칠지 묻는 옛 글은 없다. 48줄의 막는 장치 문단은 run을 ""PR을 연다"에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 푸시한다"로 적어 run 20줄, ARCHITECTURE 49줄과 맞고, 괄호 안의 다섯 스킬은 `grep -ln '푸시하지 않는다' plugins/plate/skills/*/SKILL.md`가 낸 check, eval, phase, retro, review와 같다(회고 1의 문제). 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.216s` / `OK`. 통과

**문제**
- 없음

**판정**: 통과
