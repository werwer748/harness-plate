# Phase 2: 고칠 phase의 파일 목록과 통과 조건

**목표**: run의 8번이 쓰는 고칠 phase에서 파일 목록이 TODO와 맞고, 통과 조건이 앞선 회고들의 재현과 같은 뿌리의 꼴까지 본다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md`의 8번과 고칠 phase 양식, "고침 task를 더한다"의 "테스트 먼저와 읽을 것은 8번의 고칠 phase와 같은 규칙" 줄
- `git show c2a983c^:docs/tasks/003-push-guard/done-phase-6.md`, `git show c2a983c^:docs/tasks/003-push-guard/done-phase-7.md` (TODO가 "훅을 고치지 않고"라면서 파일 목록에 훅을 둔 장면)
- `git show c2a983c^:docs/tasks/003-push-guard/retro.md` (회고 1~6이 되풀이해 새 꼴을 찾은 장면)
- `docs/ARCHITECTURE.md`의 데이터 흐름 (고칠 phase 줄)

**TODO**
- [ ] 8번이 TODO의 파일 경로를 회고의 문제 글에서 옮길 때 그 TODO가 고치는 파일만 적고, 쓰기 전에 TODO 글(예: "고치지 않는다")과 파일 목록을 대어 본다고 적는다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 8번과 고칠 phase 양식의 통과 조건에 앞선 회고 절들(회고 1~K)이 적은 재현을 모두 다시 돌리는 조건이 생긴다. 회고 K의 것만이 아니다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 테스트 먼저가 "예"인 고칠 phase는 고친 코드에서 같은 뿌리의 꼴(같은 함수의 다른 입력, 앞서 막던 꼴)을 찾아 테스트로 남기는 TODO를 갖는다. 8번 본문과 양식에 적힌다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `docs/ARCHITECTURE.md`에서 고칠 phase를 적은 줄이 바뀐 규칙과 어긋나면 맞춘다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 2가 참이다.
  - 확인: 8번 본문과 고칠 phase 양식을 읽어 셋(파일 목록과 TODO 글 대어 보기, 회고 1~K의 재현 다시 돌리기, 같은 뿌리의 꼴 테스트)이 하나씩 있다
- 완료 조건 3이 참이다.
  - 확인: `grep -n '고칠 phase\|PR의 본문\|이슈' docs/ARCHITECTURE.md`가 낸 줄을 하나씩 읽어 바뀐 run과 어긋나는 줄이 없다
- phase 1이 이룬 완료 조건 1이 그대로 참이다.
  - 확인: 완료 조건 1의 확인을 다시 돌린다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`
