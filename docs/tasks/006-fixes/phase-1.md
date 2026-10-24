# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/hooks/push_guard.py`
- `plugins/plate/.claude-plugin/plugin.json`
- `plugins/plate/.codex-plugin/plugin.json`
- `~/plate-rail-test/bin/run.sh`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [ ] `scan`의 인지 복잡도가 어림 67로 기준 15를 넘어, 셸 꼴 하나를 고칠 때 다른 꼴을 깨뜨리기 쉽다 (`plugins/plate/hooks/push_guard.py:62`)
- [ ] `push_args`의 인지 복잡도가 어림 24로 기준 15를 넘는다 (`plugins/plate/hooks/push_guard.py:168`)
- [ ] 푸시 훅의 옵션과 설정을 읽는 가지 일곱 곳(따옴표 밖 이스케이프, 환경 변수 앞붙임, `git -c` 같은 git 옵션, `--`, `-o`·`--repo` 같은 push 옵션, 짧은 옵션 묶음의 `-o`, 설정의 원격)에 시험이 없어 깨져도 알 수 없다 (`plugins/plate/hooks/push_guard.py:71`)
- [ ] 완료 조건 1의 셋째 확인 `diff -r <복사본> plugins/plate`가 `.gitignore`에 걸린 `__pycache__`를 다른 것으로 내어 실패한다. 추적되는 파일은 같다 (`plugins/plate/hooks/__pycache__`)
- [ ] 두 매니페스트의 `description`이 0.11.0의 푸시 훅과 CI(review의 PR 모드, 판정 스크립트)를 적지 않는다 (`plugins/plate/.claude-plugin/plugin.json:4`, `plugins/plate/.codex-plugin/plugin.json:4`)
- [ ] 띄운 에이전트에 실린 plate 스킬 본문이 tasks가 고친 저장소의 본문을 따라오지 않는다. 세션에 실린 plate 스킬 본문은 세션을 띄울 때의 것이라 같은 세션에서 띄운 에이전트에는 tasks가 고치기 전의 본문이 실린다는 사실을 적고, 스킬의 절차를 바꾸는 tasks는 그 절차에 기대는 다음 단계를 새 세션에서 이어 간다고 적는다 (`docs/TOOLS.md`)
- [ ] 복사본과 견주는 `diff -r`가 git이 무시하는 `__pycache__`를 다른 것으로 낸다. 테스트와 `--plugin-dir` 세션의 훅이 `plugins/plate/hooks/__pycache__`를 만든다는 것을 적고, `plugins/plate`를 복사본과 견주는 확인은 `diff -r -x __pycache__`로 쓴다 (`docs/ARCHITECTURE.md`)
- [ ] 시험 폴더의 run 허용 목록에 푸시가 없다. run의 허용 목록에 `Bash(git push:*)`를 넣어 장면마다 `RUN_ALLOW`로 더하지 않게 한다 (`~/plate-rail-test/bin/run.sh`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
