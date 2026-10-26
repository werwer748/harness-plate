# Phase 2: 고칠 phase의 파일 목록과 통과 조건

**목표**: run의 8번이 쓰는 고칠 phase에서 파일 목록이 TODO와 맞고, 통과 조건이 앞선 회고들의 재현과 같은 뿌리의 꼴까지 본다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md`의 8번과 고칠 phase 양식, "고침 task를 더한다"의 "테스트 먼저와 읽을 것은 8번의 고칠 phase와 같은 규칙" 줄
- `git show c2a983c^:docs/tasks/003-push-guard/done-phase-6.md`, `git show c2a983c^:docs/tasks/003-push-guard/done-phase-7.md` (TODO가 "훅을 고치지 않고"라면서 파일 목록에 훅을 둔 장면)
- `git show c2a983c^:docs/tasks/003-push-guard/retro.md` (회고 1~6이 되풀이해 새 꼴을 찾은 장면)
- `docs/ARCHITECTURE.md`의 데이터 흐름 (고칠 phase 줄)

**TODO**
- [x] 8번이 TODO의 파일 경로를 회고의 문제 글에서 옮길 때 그 TODO가 고치는 파일만 적고, 쓰기 전에 TODO 글(예: "고치지 않는다")과 파일 목록을 대어 본다고 적는다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 8번과 고칠 phase 양식의 통과 조건에 앞선 회고 절들(회고 1~K)이 적은 재현을 모두 다시 돌리는 조건이 생긴다. 회고 K의 것만이 아니다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 테스트 먼저가 "예"인 고칠 phase는 고친 코드에서 같은 뿌리의 꼴(같은 함수의 다른 입력, 앞서 막던 꼴)을 찾아 테스트로 남기는 TODO를 갖는다. 8번 본문과 양식에 적힌다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `docs/ARCHITECTURE.md`에서 고칠 phase를 적은 줄이 바뀐 규칙과 어긋나면 맞춘다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 2가 참이다.
  - 확인: 8번 본문과 고칠 phase 양식을 읽어 셋(파일 목록과 TODO 글 대어 보기, 회고 1~K의 재현 다시 돌리기, 같은 뿌리의 꼴 테스트)이 하나씩 있다
- 완료 조건 3이 참이다.
  - 확인: `grep -n '고칠 phase\|PR의 본문\|이슈' docs/ARCHITECTURE.md`가 낸 줄을 하나씩 읽어 바뀐 run과 어긋나는 줄이 없다
- phase 1이 이룬 완료 조건 1이 그대로 참이다.
  - 확인: 완료 조건 1의 확인을 다시 돌린다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`

## 한 일
- 8번이 TODO의 파일 경로를 회고의 문제 글에서 옮길 때 그 TODO가 고치는 파일만 적고, 쓰기 전에 TODO 글과 파일 목록을 대어 본다고 적는다: 8번의 TODO 줄을 "문제의 글과 그 TODO가 고치는 파일의 경로를 옮긴다"로 고치고, 근거로만 든 파일은 읽을 것에만 두며, 쓰기 전에 TODO마다 글과 파일 목록을 대어 보고 글이 "고치지 않는다"고 한 파일은 뺀다고 더했다. 양식의 TODO 줄도 `({그 TODO가 고치는 파일의 경로})`로 고쳤다 (`plugins/plate/skills/run/SKILL.md`)
- 8번과 고칠 phase 양식의 통과 조건에 회고 1~K의 재현을 모두 다시 돌리는 조건이 생긴다: 8번에 "앞선 회고 절들(회고 1~K)의 문제에 적힌 재현을 모두 다시 돌려 고친 대로인지 보는 조건도 둔다. 회고 K의 것만이 아니다"를 더하고, 양식의 통과 조건에 "K가 2 이상일 때만: 앞선 회고 1~{K-1}의 문제가 고친 대로 그대로다" / "확인: 회고 1~{K-1}의 문제마다 적힌 재현을 모두 다시 돌린다"를 더했다(회고 K는 바로 위 조건이 본다). 양식의 읽을 것도 `## 회고 1`부터 `## 회고 {K}`까지의 절로 넓혔다 (`plugins/plate/skills/run/SKILL.md`)
- 테스트 먼저가 "예"인 고칠 phase는 같은 뿌리의 꼴을 테스트로 남기는 TODO를 갖는다: 8번의 테스트 먼저 규칙 바로 뒤에 "테스트 먼저가 \"예\"이면 TODO 끝에 항목 하나를 더 둔다: 고친 코드에서 같은 뿌리의 꼴(같은 함수의 다른 입력, 앞서 막던 꼴)을 찾아 테스트로 남긴다"를 더하고, 양식의 TODO에 같은 항목(테스트 먼저가 "예"일 때만)을 더했다 (`plugins/plate/skills/run/SKILL.md`)
- `docs/ARCHITECTURE.md`에서 고칠 phase를 적은 줄이 바뀐 규칙과 어긋나면 맞춘다: 63줄("회고의 문제는 고칠 phase를 더해 고친다…")은 고칠 phase의 내용을 적지 않아 바뀐 규칙과 어긋나지 않는다. 고치지 않았다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 완료 조건 2가 참이다.
  - `plugins/plate/skills/run/SKILL.md`의 8번(158~174줄)과 양식(178~201줄)을 읽음 → 파일 목록과 TODO 글 대어 보기(164줄, 양식 TODO 줄), 회고 1~K의 재현 다시 돌리기(170줄, 양식 통과 조건의 "회고 1~{K-1}" 조건), 같은 뿌리의 꼴 테스트(166줄, 양식 TODO의 둘째 항목)가 하나씩 있다. 통과
- 완료 조건 3이 참이다.
  - `grep -n '고칠 phase\|PR의 본문\|이슈' docs/ARCHITECTURE.md` → 50, 63, 67줄. 50줄은 PR 본문의 내용(요청, 목표, 전체 보고)과 PR 댓글을 적고 넘기는 방법을 적지 않아 `--body-file`과 어긋나지 않는다. 63줄은 고칠 phase를 더해 고친다는 것만, 67줄은 이슈로 올린다는 것만 적어 어긋나지 않는다. 통과
- phase 1이 이룬 완료 조건 1이 그대로 참이다.
  - `grep -n -- '--body ' plugins/plate/skills/run/SKILL.md` → 출력 없음. `grep -c -- '--body-file' …` → `6`. 314, 315, 431, 432줄을 읽음 → 이슈 댓글, 이슈 만들기, PR 열기, PR 댓글 넷 다 `--body-file`. `grep -n '"\$(' …` → 출력 없음. 통과
- 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 16.370s` / `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 없음
