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
- [ ] eval 스킬이 생긴다: `docs/tasks/`의 `FRICTION.md`, `RUNLOG.md`, `review.md`와 task마다의 `done-phase-N.md`, `retro.md`, tasks의 커밋을 읽는다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] 여섯 기준(결과 성공, 일관성, 효율, 규칙 준수, 사람 개입률, 실패 양상)마다 A~E의 등급 설명을 두고, 숫자로 잴 수 있는 기준(일관성의 첫 시도 통과율, 효율의 토큰·도구 호출·시간, 사람 개입률)은 계산과 등급 구간을 적는다. 근거를 먼저 적고 등급을 매기며, 정할 수 없으면 "판단 못함"이다
- [ ] 실패 양상은 MAST 유형으로 나눠 센다
- [ ] 스킬로 만들 후보 절이 있다(FRICTION의 후보와 되풀이된 일에서)
- [ ] 하네스 고칠 거리 목록이 항목마다 plate 자체의 것인지 그 프로젝트만의 것인지 가르고, plate 자체의 것에는 이슈로 올릴 제목과 본문을 함께 적는다
- [ ] `docs/tasks/eval.md`에 적고 그 파일만 tasks 이름으로 시작하는 메시지로 커밋한다. 고치지 않고 묻지 않으며, 기준 등급, 고칠 거리 수, 기록 위치를 정해 둔 줄로 돌려준다

**통과 조건**
- eval 본문이 TODO대로다
  - 확인: `plugins/plate/skills/eval/SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- 완료 조건 1이 참이다
  - 확인: 완료 조건 1의 확인을 돌린다
- 완료 조건 2 가운데 eval 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/eval/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다
