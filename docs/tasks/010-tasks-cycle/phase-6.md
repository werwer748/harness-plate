# Phase 6: eval을 만든다

**목표**: eval 스킬이 tasks 끝에 하네스를 여섯 기준 A~E로 평가해 `docs/tasks/eval.md`에 적는다.

**테스트 먼저**: 아니오 — `.md`만 만든다.

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md` (`FRICTION.md`의 줄과 `retro.md`의 꼴)
- `plugins/plate/skills/check/SKILL.md` (확인 절의 꼴)
- `plugins/plate/skills/phase/SKILL.md` (기록 다섯 절)
- `plugins/plate/skills/review/SKILL.md` (phase 5의 리포트. 같은 꼴로 맞춘다)
- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents (결과 성공. 효율은 턴, 도구 호출, 토큰, 시간. 차원마다 루브릭과 따로 둔 판정, "Unknown" 허용)
- https://arxiv.org/abs/2406.12045 (일관성: τ-bench의 pass^k. 한 번의 실행에서는 첫 시도 통과율로 대신한다)
- https://developers.openai.com/api/docs/guides/evaluation-best-practices (규칙 준수)
- https://www.anthropic.com/research/measuring-agent-autonomy (사람 개입률)
- https://arxiv.org/html/2503.13657v3 (실패 양상: MAST의 14개 유형)
- https://platform.claude.com/docs/en/test-and-evaluate/develop-tests (점수 전에 근거를 먼저 적게 한다)
- https://arxiv.org/abs/2310.08491 (점수마다 기준 설명과 기준 답안을 준다)

**TODO**
- [x] eval 스킬이 생긴다: `docs/tasks/`의 `FRICTION.md`, `RUNLOG.md`, `review.md`와 task마다의 `done-phase-N.md`, `retro.md`, tasks의 커밋을 읽는다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] 여섯 기준(결과 성공, 일관성, 효율, 규칙 준수, 사람 개입률, 실패 양상)마다 A~E의 등급 설명을 두고, 숫자로 잴 수 있는 기준(일관성의 첫 시도 통과율, 효율의 토큰·도구 호출·시간, 사람 개입률)은 계산과 등급 구간을 적는다. 근거를 먼저 적고 등급을 매기며, 정할 수 없으면 "판단 못함"이다
- [x] 실패 양상은 MAST 유형으로 나눠 센다
- [x] 스킬로 만들 후보 절이 있다(FRICTION의 후보와 되풀이된 일에서)
- [x] 하네스 고칠 거리 목록이 항목마다 plate 자체의 것인지 그 프로젝트만의 것인지 가르고, plate 자체의 것에는 이슈로 올릴 제목과 본문을 함께 적는다
- [x] `docs/tasks/eval.md`에 적고 그 파일만 tasks 이름으로 시작하는 메시지로 커밋한다. 고치지 않고 묻지 않으며, 기준 등급, 고칠 거리 수, 기록 위치를 정해 둔 줄로 돌려준다

**통과 조건**
- eval 본문이 TODO대로다
  - 확인: `plugins/plate/skills/eval/SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- 완료 조건 1이 참이다
  - 확인: 완료 조건 1의 확인을 돌린다
- 완료 조건 2 가운데 eval 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/eval/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다

## 한 일
- eval 스킬이 생긴다: `plugins/plate/skills/eval/SKILL.md`를 새로 만들었다. 1번(읽는다)이 `FRICTION.md`, `RUNLOG.md`, `review.md`, task마다의 `done-phase-N.md`와 `retro.md`, tasks의 커밋(계획의 커밋 `plan: <tasks 이름>`부터 HEAD까지)을 읽고, 프로젝트의 지침 파일, tasks 머리, task 머리, 앞의 `eval.md`도 읽는다 (`plugins/plate/skills/eval/SKILL.md`)
- 여섯 기준의 A~E 등급 설명과 숫자 기준의 계산·구간: 3번에 기준마다 근거를 모으는 법을, 그 끝의 등급표에 여섯 기준의 A~E 칸을 두었다. 일관성은 첫 시도 통과율(첫 확인 절·첫 회고 절이 통과인 단위 ÷ 단위), 효율은 되풀이 몫(되풀이 줄의 토큰·도구 호출·시간 ÷ 전체, 셋 가운데 가장 높은 비율), 사람 개입률은 멈춤 줄 ÷ 에이전트 줄로 계산과 구간을 적었다. 절대 규칙 3과 3번 머리말이 근거를 먼저 적게 하고, 칸에 들지 못하면 "판단 못함"이다 (`plugins/plate/skills/eval/SKILL.md`)
- 실패 양상은 MAST 유형으로 나눠 센다: 2번이 모으는 곳과 잡힌 곳(그 자리, phase의 확인, task의 회고, tasks 끝)의 표, MAST 3범주 14유형의 뜻과 plate에서의 예의 표를 두고, 실패마다 유형 하나를 붙인다. 양식의 "유형마다"와 "잡힌 곳마다"에서 센다 (`plugins/plate/skills/eval/SKILL.md`)
- 스킬로 만들 후보 절: 4번이 `FRICTION.md`의 스킬 후보 줄과 둘 이상의 task에서 되풀이된 손일을 모으고, 양식에 "스킬로 만들 후보" 절을 두었다 (`plugins/plate/skills/eval/SKILL.md`)
- 하네스 고칠 거리 목록: 5번과 양식의 "하네스 고칠 거리"가 항목마다 갈래(plate 자체, 이 프로젝트만)를 가르고, plate 자체의 것에는 이슈 제목과 본문(일어난 것, 원인, 해결책, 근거)을, 이 프로젝트만의 것에는 고칠 곳과 해결책을 적게 했다 (`plugins/plate/skills/eval/SKILL.md`)
- `docs/tasks/eval.md`에 적고 커밋, 정해 둔 줄로 돌려준다: 6번이 `eval.md` 끝에 `## eval N` 절을 더하고, 7번이 그 파일만 `<tasks 이름>: 하네스 eval`로 커밋하고, 8번이 등급 여섯, 고칠 거리 수, 기록 위치의 세 줄을 돌려준다. 절대 규칙 1과 4가 고치지 않고 묻지 않게 한다 (`plugins/plate/skills/eval/SKILL.md`)

## 확인 결과
- eval 본문이 TODO대로다
  - `plugins/plate/skills/eval/SKILL.md`를 읽음 → TODO 1은 1번(57~62줄), TODO 2는 3번과 등급표(97~157줄), TODO 3은 2번의 두 표와 양식의 "실패 양상", TODO 4는 4번과 양식의 "스킬로 만들 후보", TODO 5는 5번과 양식의 "하네스 고칠 거리", TODO 6은 6~8번과 절대 규칙 1·4에 있다. 통과
- 완료 조건 1이 참이다
  - `ls plugins/plate/skills` → `check`, `context`, `eval`, `phase`, `plan`, `retro`, `review`, `run`, `setup` 아홉만 나온다. 통과
- 완료 조건 2 가운데 eval 본문의 몫이 참이다
  - `grep -n "작업" plugins/plate/skills/eval/SKILL.md` → 0줄(exit 1). 통과

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
- 읽을 것의 https://arxiv.org/abs/2406.12045 는 초록 쪽이라 pass^k의 정의가 없어 HTML판(https://arxiv.org/html/2406.12045)을 따로 읽었다. Prometheus(https://arxiv.org/abs/2310.08491)의 초록도 점수마다의 설명이 있는지는 말하지 않아, review와 같은 꼴(칸마다 설명)로 맞추고 MAST 유형마다 plate의 예를 두었다.
- eval은 `RUNLOG.md`의 줄 꼴과 run이 정해 둔 물음의 자리를 읽어야 하는데 run 본문은 아직 옛 판(phase 7 이후에 바뀜)이라, tasks 머리의 결정에 적힌 내용(에이전트 줄의 다섯 값, 물은 줄의 두 값, 실행 방식·회고 뒤·고칠지·합칠지)으로만 적었다. run을 고칠 때 줄 꼴과 물음의 자리가 이 본문과 맞는지 봐야 한다.
- 규칙 준수의 커밋 표는 phase, check, retro, review, plan 본문의 커밋 규칙을 옮겨 적은 것이라, 그 스킬들의 커밋 메시지나 넣는 파일이 바뀌면 이 표도 함께 고쳐야 한다. run의 커밋(`NNN-slug: phase N 통과`)은 넣는 파일이 아직 정해지지 않아 표에 넣지 않았다.
