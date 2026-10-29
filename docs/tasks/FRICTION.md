# FRICTION

- `001-issue-criteria` 문제: plate:plan이 phase 4의 통과 조건 "시험이 이 저장소를 바꾸지 않았다"를 `git status --porcelain -- . ':!docs/tasks/001-issue-criteria/phase-4.md'`로 적어, plate:run이 수행 뒤 확인 전에 `docs/tasks/RUNLOG.md`에 줄을 더하는 것을 빼지 않았다. 그대로면 시험과 상관없이 확인이 실패할 것이라 실행 중 고칠 phase 물음으로 계획을 고쳤다(`47c67c2 plan: 001-issue-criteria 수정`, `docs/tasks/RUNLOG.md`의 물음 줄). 저장소 불변을 보는 확인을 쓸 때 실행이 그 사이에 쓰는 하네스 기록을 빼라는 것이 계획의 초안 점검에 없다
