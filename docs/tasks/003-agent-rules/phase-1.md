# Phase 1: 다섯 스킬의 본문과 테스트와 문서와 버전을 고친다

**목표**: retro, eval, phase, check, review 본문의 #49, #50, #51이 고쳐지고, 그 규칙 글의 테스트가 더해지고, 맥락 문서와 README가 맞춰지고, 버전이 0.18.0이 된다.

**테스트 먼저**: 아니오 — 고치는 것은 스킬 본문(`.md`)과 매니페스트의 버전 줄이고, 더하는 테스트는 그 글이 있는지를 볼 뿐 코드의 동작을 바꾸지 않는다

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md`의 "5. tasks 끝에 볼 것을 모은다"와 "9. 세 줄을 돌려준다", `plugins/plate/skills/eval/SKILL.md`의 낱말 "정해 둔 물음", "2. 실패를 모아 MAST 유형으로 나눈다"(#49가 맞출 `남은 것:` 규칙), "3. 기준마다 근거를 적고 등급을 매긴다"의 규칙 준수 표, "8. 세 줄을 돌려준다", `plugins/plate/skills/phase/SKILL.md`의 "6. 다섯 줄을 돌려준다", `plugins/plate/skills/check/SKILL.md`의 "8. 세 줄을 돌려준다", `plugins/plate/skills/review/SKILL.md`의 끝 보고 절("`문제`는 소스 문제의 수다"로 시작하는 문단이 있는 절) (고칠 자리)
- `plugins/plate/skills/run/SKILL.md`의 맡기는 글 다섯 코드 블록(001이 마지막 줄로 `부른 쪽: plate:run`을 더했다), 낱말 "작업 트리의 스킬 줄"(그 한 줄의 글), "`RUNLOG.md`" 절(물은 자리 목록과 `RUNLOG` 커밋 자리)
- `gh issue view 49`, `gh issue view 50`, `gh issue view 51` (#49는 이슈의 해결책 대신 task 머리 완료 조건 1의 글대로 고친다)
- `tests/test_skill_rules.py` (001의 run 테스트와 002의 plan 테스트가 든 꼴), `tests/test_manifests.py` (두 버전 줄이 같은지)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (버전 줄)
- `docs/PRD.md`의 5와 7, `docs/ARCHITECTURE.md`의 "패턴과 규칙"(001이 표지 줄을 더한 맡기는 글 문단과 run 문단), 데이터 흐름의 회고 줄, 디렉터리 구조의 `test_skill_rules.py` 줄(001과 002가 더한 규칙이 든다), `README.md`의 스킬 표

**TODO**
- [ ] retro 5번의 "문제" 갈래에, 확인 절 "하네스에서 걸린 것"의 `남은 것:`으로 시작하는 줄은 이번 회고 절 "남은 것"에서 "문제"로 판정한 것만 모으고 "문제 아님"인 줄은 모으지 않는다는 글이 더해진다. "멈춤" 갈래의 정해 둔 자리 목록에 `권한`이 더해진다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] eval 3번의 규칙 준수 표에 `NNN-slug: RUNLOG`와 `<tasks 이름>: RUNLOG` 행(만든 스킬 run, 넣어도 되는 파일 `RUNLOG.md`와 사용량 까닭을 적은 `docs/TOOLS.md`)이 더해지고, 낱말 "정해 둔 물음"의 목록에 `권한`이 더해진다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] phase 6번, check 8번, retro 9번, review 끝 보고 절, eval 8번의 "사용자가 직접 불렀으면" 갈래가, 맡은 글에 `부른 쪽: plate:run` 줄도 작업 트리의 스킬 줄도 없을 때로 바뀐다. 다섯 본문의 글이 같은 기준을 말한다 (`plugins/plate/skills/phase/SKILL.md`, `plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/review/SKILL.md`, `plugins/plate/skills/eval/SKILL.md`)
- [ ] 위 셋의 규칙 글이 제 절에 있는지 보는 테스트가 더해진다. #51은 다섯 스킬마다 그 절에 `부른 쪽: plate:run`과 작업 트리의 스킬 줄의 기준이 있는지 본다. 모듈 docstring의 이슈 목록에 #49, #50, 다섯 스킬의 #51이 더해진다 (`tests/test_skill_rules.py`)
- [ ] 두 매니페스트의 버전이 0.17.0에서 0.18.0으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [ ] `docs/ARCHITECTURE.md` "패턴과 규칙"의 맡기는 글 문단에 다섯 스킬이 표지 줄이나 작업 트리의 스킬 줄로 run이 띄운 것을 가른다는 글이 더해지고, 디렉터리 구조의 `test_skill_rules.py` 줄에 retro #49, eval #50, 다섯 스킬 #51 규칙이 더해진다(001, 002가 더한 규칙은 그대로 남는다). `docs/PRD.md`의 5와 7, 데이터 흐름의 회고 줄, `README.md`의 `run`, `phase`, `check`, `retro`, `review`, `eval` 행은 #49·#51과 어긋나는 곳만 고친다 (`docs/ARCHITECTURE.md`, `docs/PRD.md`, `README.md`)

**통과 조건**
- 완료 조건 1이 참이다
  - 확인: retro 5번에 #49의 글과 "멈춤" 목록의 `권한`이, eval 3번 표에 두 `RUNLOG` 행이, eval 낱말 "정해 둔 물음"에 `권한`이 task 머리 완료 조건 1의 글대로 있다. 하나라도 없으면 실패
- 완료 조건 2가 참이다
  - 확인: phase 6번, check 8번, retro 9번, review 끝 보고 절, eval 8번을 저마다 읽어, 직접 부른 꼴의 보고가 맡은 글에 `부른 쪽: plate:run` 줄도 작업 트리의 스킬 줄도 없을 때만이다. 하나라도 없으면 실패
- 완료 조건 3이 참이다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: `mktemp -d`에 `git archive HEAD`를 풀어 retro 5번의 #49 해결 글을 지우고 돌리면 실패한다. 다시 풀어 review 끝 보고 절에서 `부른 쪽: plate:run`을 지우고 돌리면 실패한다
- 완료 조건 5가 참이다
  - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.18.0`
  - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
  - 확인: task 머리 완료 조건 5의 문서들을 문서마다 따로 읽어 그 견줄 것을 저마다 담는다. 하나라도 어긋나면 실패
