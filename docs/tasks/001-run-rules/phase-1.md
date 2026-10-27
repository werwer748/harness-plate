# Phase 1: run 본문과 문서를 고친다

**목표**: run 본문에 다섯 이슈의 해결이 들어가고 맥락 문서와 README가 맞춰진다.

**테스트 먼저**: 아니오 — `.md`(스킬 본문과 문서)만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (고칠 본문)
- `gh issue view 34 --repo werwer748/harness-plate`, 35, 38, 40, 44 (이슈마다의 원인과 해결책)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `README.md` (맥락 문서와 README)

**TODO**
- [ ] "1. 시작 조건을 본다"에 첫 에이전트를 띄우기 전의 권한 확인이 더해진다: plan 모드가 켜져 있거나 쓰기가 막힐 권한 모드면 알리고 바꿀지 묻고 멈추며, 확인할 수 없는 도구면 그렇다고 적고 잇는다. "`RUNLOG.md`" 절의 물은 자리 목록과 task에 걸리지 않는 물음 목록에 `권한`이 더해진다 (#40) (`plugins/plate/skills/run/SKILL.md`)
- [ ] "7. task 회고를 맡긴다", "코드 평가를 맡긴다", "하네스 eval을 맡긴다"에서 돌아와 더한 `RUNLOG.md` 줄을 그 자리에서 그 파일만 넣는 커밋(회고 뒤 `NNN-slug: RUNLOG`, 평가 뒤 `<tasks 이름>: RUNLOG`)으로 넣는다는 글이 더해지고, "`RUNLOG.md`" 절의 커밋 자리 글이 이 자리를 담게 바뀐다 (#44) (`plugins/plate/skills/run/SKILL.md`)
- [ ] "`RUNLOG.md`" 절의 사용량 줄이 돌아오지 않은 값은 단위 없이 `모름`(`시간 모름`)으로 적고, 돌아오지 않은 까닭을 알면 `docs/TOOLS.md`에 적는다로 바뀐다 (#35) (`plugins/plate/skills/run/SKILL.md`)
- [ ] "8. 고칠 phase를 더한다"의 앞에 회고의 문제를 고치려면 계획 파일의 목표나 완료 조건을 바꾸거나 좁혀야 하면 고칠 phase를 더하지 않고 어느 실행 방식이든 "멈춘다"로 간다는 글이 더해지고, "멈춘다"의 자리 목록에 그 자리가 더해지며, 그때 물은 것은 `멈춤`이라고 "`RUNLOG.md`" 절과 맞는다 (#34, #38) (`plugins/plate/skills/run/SKILL.md`)
- [ ] "8. 고칠 phase를 더한다"의 TODO 규칙에 고칠 동작을 적은 맥락 문서와 README의 줄도 TODO에 넣는다는 글과, 계획 커밋(`plan: NNN-slug 수정`)으로 이미 고친 문제는 TODO에 넣지 않고 통과 조건에 "계획 커밋 `{해시}`로 고쳤다"와 그 확인을 따로 적는다는 글이 더해지고, 고칠 phase의 양식 블록이 그 통과 조건 자리를 담게 바뀐다 (#38) (`plugins/plate/skills/run/SKILL.md`)
- [ ] run 본문 앞머리의 description, `docs/PRD.md`의 핵심 기능 7, `docs/ARCHITECTURE.md`의 "패턴과 규칙"의 run 문단과 "데이터 흐름"의 실행 갈래와 그 아래 멈추는 자리 문단, `README.md`의 `run` 행이 시작할 때의 권한 물음, `RUNLOG.md`의 커밋 자리, 회고가 계획을 바꾸게 할 때 멈추는 것을 담게 바뀐다 (`plugins/plate/skills/run/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)

**통과 조건**
- 완료 조건 1의 본문이 적혀 있다.
  - 확인: run 본문의 "1. 시작 조건을 본다", "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "멈춘다", "코드 평가를 맡긴다", "하네스 eval을 맡긴다", "`RUNLOG.md`" 절을 읽어 다섯 해결이 저마다 적혀 있다. 하나라도 없으면 실패
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
- 완료 조건 2가 참이다.
  - 확인: `docs/PRD.md`의 핵심 기능 7, `docs/ARCHITECTURE.md`의 "패턴과 규칙"의 run 문단과 "데이터 흐름"의 실행 갈래와 그 아래 멈추는 자리 문단, `README.md`의 `run` 행, run 본문 앞머리의 description을 저마다 읽어 세 동작과 어긋나는 줄이 없다
