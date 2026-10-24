# Phase 1: tasks 끝의 PR

**목표**: run이 tasks 끝에 PR을 열지 묻고, 승인하면 tasks 브랜치를 푸시해 PR을 연다.

**테스트 먼저**: 아니오 — 스킬 본문과 문서(`.md`)만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (절대 규칙, 낱말의 기본 브랜치, tasks 끝, 비운다, 합친다, 10번 보고, `RUNLOG.md`)
- `plugins/plate/skills/eval/SKILL.md` (정해 둔 물음)
- `plugins/plate/skills/setup/SKILL.md`의 양식 절 (`002-ci-workflow`가 만든 plate 워크플로의 파일 이름)
- `docs/TOOLS.md`의 "tasks 실행의 판정에서 본 것" (`gh`로 이슈를 올린 꼴, 본문을 heredoc으로 넘기는 꼴)
- `docs/ARCHITECTURE.md` (패턴과 규칙의 run 규칙, 데이터 흐름), `docs/PRD.md` (핵심 기능 8)

**TODO**
- [x] tasks 끝의 "비운다" 뒤에 PR 절이 생긴다. origin이 GitHub이면 푸시할 브랜치와 PR 제목·본문을 보여 주고 PR을 열지 묻는다. 승인하면 `tasks/<이름>`을 origin에 푸시하고 기본 브랜치로 가는 PR을 연다. 본문에는 tasks 머리의 요청과 목표, tasks 끝의 전체 보고가 들고, 둘은 비우기 전에 읽어 둔다. plate의 CI 워크플로가 없으면 `review.md`의 마지막 평가 절을 PR 댓글로 단다. 거절하면 브랜치를 그대로 둔다 (`plugins/plate/skills/run/SKILL.md`)
- [x] origin이 GitHub이 아니거나 없으면 지금의 "합친다"로 간다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 절대 규칙 5가 tasks 브랜치를 PR로 열 때의 푸시를 허락하고, 10번 보고에 PR 주소와 댓글 주소(열지 않았으면 그 까닭)가 들며, 설명(description)이 PR을 적는다 (`plugins/plate/skills/run/SKILL.md`)
- [x] eval의 "정해 둔 물음"에 PR을 열지가 든다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] ARCHITECTURE의 run 규칙과 데이터 흐름, PRD의 핵심 기능 8이 PR로 가는 tasks 끝을 적는다 (`docs/ARCHITECTURE.md`, `docs/PRD.md`)

**통과 조건**
- 완료 조건 1, 2, 3이 참이다.
  - 확인: 완료 조건 1, 2, 3의 확인을 모두 돌린다

## 한 일
- tasks 끝의 "비운다" 뒤에 PR 절이 생긴다: "비운다"의 첫 글에 origin이 GitHub 원격이면 "PR을 연다"에 쓸 것(tasks 머리의 제목, 요청, 목표, `review.md`의 마지막 평가 절, `eval.md`의 마지막 eval 절, 고침 task 머리의 완료 조건)을 지우기 전에 읽어 둔다를 더했다. 새 절 "PR을 연다"는 푸시할 브랜치, PR이 가는 곳, 제목(tasks 머리의 제목), 본문을 보여 주고 PR을 열지 묻고(plate 워크플로가 없으면 댓글을 단다는 것도 적는다), 승인하면 `git push origin tasks/<이름>`, `gh pr create --base {기본 브랜치} --head tasks/<이름>`(본문은 heredoc), plate 워크플로가 없으면 `gh pr comment`로 `review.md`의 마지막 평가 절을 단다. 거절하면 푸시하지 않고 합치지 않고 브랜치를 그대로 둔다. 푸시나 `gh`가 실패하면 다시 시도하지 않고 명령과 오류를 보고에 적는다. PR 본문의 꼴(요청, 목표, 코드 평가의 등급과 Sonar way 게이트, 하네스 eval의 등급, 고친 것, 올린 이슈)을 두었고, 올린 이슈의 주소를 모르면 plate 저장소의 열린 이슈에서 이 tasks 이름이 있는 것을 찾는다. 낱말에 "GitHub 원격"(`git remote get-url origin`의 URL이 `github.com`)과 "plate 워크플로"(`plate@harness-plate`가 적힌 `.github/workflows/` 아래 파일, setup의 `plate-review.yml`)를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- origin이 GitHub이 아니거나 없으면 지금의 "합친다"로 간다: "비운다"의 끝을 origin이 GitHub 원격이면 "PR을 연다", 그 밖(origin이 없거나 GitHub의 것이 아니다, git 레포가 아니다)이면 "합친다"로 가게 바꾸고, "합친다"의 첫 줄을 "'비운다'에서 origin이 GitHub 원격이 아닐 때 온다"로 바꿨다. "합친다"의 단계는 그대로다 (`plugins/plate/skills/run/SKILL.md`)
- 절대 규칙 5, 10번 보고, 설명: 절대 규칙 5의 "푸시하지 않는다"를 "푸시는 'PR을 연다'에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 한다"로, "GitHub 이슈와 댓글"을 "GitHub 이슈, PR, 댓글"로 바꿨다. 10번에 "PR을 열지 물었으면 연 PR의 주소와 단 댓글의 주소. 열지 않았으면 그 까닭(거절, 실패한 명령과 오류), 댓글을 달지 않았으면 그 까닭(plate 워크플로가 있다, 실패한 명령과 오류)" 줄을 합칠지 줄 앞에 더했다. 설명의 끝을 "origin이 GitHub이면 tasks 브랜치를 푸시해 기본 브랜치로 가는 PR을 열지(plate의 CI 워크플로가 없으면 코드 평가를 PR 댓글로 단다), 아니면 기본 브랜치로 합칠지 묻는다"로 바꿨다. `RUNLOG.md` 절의 비운 뒤에 적지 않는 물음에 "PR을 열지"를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- eval의 "정해 둔 물음"에 PR을 열지가 든다: "tasks 끝의 고칠지와 합칠지다"를 "tasks 끝의 고칠지, PR을 열지, 합칠지다"로 바꿨다 (`plugins/plate/skills/eval/SKILL.md`)
- ARCHITECTURE의 run 규칙과 데이터 흐름, PRD의 핵심 기능 8: run 규칙을 비운 뒤 origin이 GitHub이면 PR을 열지, 아니면 합칠지 묻는 것으로 바꾸고 PR 본문, plate 워크플로가 없을 때의 댓글, run이 머지하거나 닫지 않는다는 것, 푸시는 이 PR을 열 때만 한다는 것과 이유를 적었다. 데이터 흐름의 tasks 끝 마지막 줄을 비운다, PR을 열지, 합칠지의 세 줄로 나눴다. PRD 8의 "로컬 리뷰 뒤 PR을 열고 CI 에이전트가 판정하는 일은 011에서 만든다"를 PR로 가는 tasks 끝(PR 본문, CI의 판정, 워크플로가 없을 때의 댓글, GitHub이 아닐 때의 합침)과 "PR과 CI는 011에서 만든다"로 바꿨다 (`docs/ARCHITECTURE.md`, `docs/PRD.md`)

## 확인 결과
- 완료 조건 1: `plugins/plate/skills/run/SKILL.md`의 tasks 끝, "합친다", 새 PR 절에 조건 1의 것이 있다
  - `plugins/plate/skills/run/SKILL.md`의 `### 비운다`부터 `## RUNLOG.md` 앞까지를 awk로 잘라 grep → "비운다"의 읽어 둘 것(제목, 요청, 목표, review.md와 eval.md의 마지막 절, 고침 task의 완료 조건), 끝의 갈림("PR을 연다" / 그 밖이면 "합친다"), `## PR을 연다`의 1번(보여 주고 묻는다, 거절하면 "푸시하지 않고 합치지도 않고 브랜치를 그대로 둔 채 10번으로 간다"), 2번 `git push origin tasks/<이름>`, 3번 `gh pr create --base {기본 브랜치} --head tasks/<이름>`, 4번 plate 워크플로가 없으면 `gh pr comment`로 `review.md`의 마지막 평가 절, PR 본문의 꼴(`## 요청`, `## 목표`, `## 코드 평가`와 Sonar way 게이트, `## 하네스 eval`, `## 고친 것`, `## 올린 이슈`), `## 합친다`의 "'비운다'에서 origin이 GitHub 원격이 아닐 때 온다"가 나왔다. 통과
- 완료 조건 2: 절대 규칙 5, 10번, `RUNLOG.md` 절, eval의 "정해 둔 물음"이 PR 열기와 맞는다
  - `grep -n "^5\. "` → "푸시는 \"PR을 연다\"에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 한다.", "GitHub 이슈, PR, 댓글은 승인받은 것만 올린다." / 10번 절 grep → "PR을 열지 물었으면 연 PR의 주소와 단 댓글의 주소. 열지 않았으면 그 까닭(거절, 실패한 명령과 오류)…" / `grep -n "비운 뒤에 물은 것"` → 485행 "(PR을 열지, 합칠지, 그 자리의 커밋하지 않은 변경)은 적지 않는다" / 설명 3행 → "origin이 GitHub이면 tasks 브랜치를 푸시해 기본 브랜치로 가는 PR을 열지(…), 아니면 기본 브랜치로 합칠지 묻는다" / `plugins/plate/skills/eval/SKILL.md` 40행 → "tasks 끝의 고칠지, PR을 열지, 합칠지다". 통과
- 완료 조건 3: `docs/ARCHITECTURE.md`의 run 규칙과 데이터 흐름, `docs/PRD.md`의 핵심 기능 8에 "GitHub 원격이 있어도 기본 브랜치로 합칠지 묻는다"는 뜻의 옛 글이 없다
  - `grep -n "합칠지\|PR" docs/ARCHITECTURE.md docs/PRD.md` → ARCHITECTURE 49행은 "`origin`이 GitHub이면 … PR을 열지 묻고, `origin`이 없거나 GitHub의 것이 아니면 기본 브랜치로 합칠지 묻는다", 68~69행은 "origin이 GitHub이면 … PR을 열지 묻는다" / "origin이 없거나 GitHub의 것이 아니면 기본 브랜치로 합칠지 묻는다", PRD 18행은 "origin이 GitHub이면 run이 tasks 브랜치를 푸시해 … PR을 열지 묻고 … origin이 GitHub이 아니거나 없으면 기본 브랜치로 합칠지 묻는다"다. 조건 없이 합칠지 묻는 글은 없다. 통과
- (명령 절의 테스트) `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.375s` / `OK`

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
- TODO가 `docs/ARCHITECTURE.md`에서 run 규칙과 데이터 흐름만 가리켜, 같은 문서 패턴과 규칙의 푸시 훅 문단에 있는 "에이전트의 푸시를 막는 기본은 스킬마다의 '푸시하지 않는다' 규칙이고"는 고치지 않았다. run의 절대 규칙 5는 이제 PR을 열 때 `tasks/<이름>`의 푸시를 허락한다.
