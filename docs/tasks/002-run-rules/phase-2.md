# Phase 2: 상태 판정과 멈춘 뒤의 재개를 파일로 정한다

**목표**: 3번이 상태를 줄 머리 패턴으로 읽고, 세 번 실패로 멈춘 뒤 다시 맡기기로 한 답이 `RUNLOG.md`로 이어지고, 회고의 세 번 실패는 8번으로 가고, 다시 띄운 까닭이 남고, 세 표의 행 차례를 테스트가 지킨다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트, 맥락 문서만 바꾼다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (`## 3. 갈 곳을 정한다`의 두 표, `## 멈춘다`의 4번 "다시 맡긴다", `## tasks 끝`의 표, `## `RUNLOG.md``의 꼴과 에이전트 줄 규칙과 물은 자리 목록)
- `plugins/plate/skills/check/SKILL.md` (`## 확인 절의 양식`: `## 확인 {몇 번째}` 머리와 `**판정**:` 줄)
- `plugins/plate/skills/retro/SKILL.md` (`## 기록의 양식`의 회고 절: `## 회고 {몇 번째}` 머리와 `**판정**:` 줄)
- `docs/cleanup/2026-10-28.md` (성능-3, 신뢰성-1, 신뢰성-7, 신뢰성-8, 기존 작업 정합성-4와 그 2라운드)
- `tests/test_skill_rules.py` (`RunRulesTest`, `section`·`subsection` 도우미)
- `docs/ARCHITECTURE.md` (`## 데이터 흐름` 끝 문단의 멈춤 문장)

**TODO**
- [ ] 3번에, 남은 첫 phase와 지금 task의 상태를 읽는 법이 더해진다. 줄 머리에 맞춘 패턴으로 확인 절·회고 절의 머리와 그 절의 판정 줄을 뽑고 마지막 것을 고르며, 코드 블록과 TODO 속의 같은 글자는 세지 않는다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 3번의 두 표의 "멈춘다" 행이, `RUNLOG.md`에서 그 phase(또는 task)의 마지막 `멈춤` 줄이 지금과 같은 확인 절 수(또는 회고 절 수)에서 다시 맡기기로 한 답이면 한 번 건너뛰게 바뀐다. "멈춘다" 4번 "다시 맡긴다"는 그 답을 그 자리와 함께 `멈춤` 줄에 적게 바뀌고, "회고면 7번"이 "회고면 8번"으로 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `RUNLOG.md` 절에, 확인이나 회고를 거치지 않고 같은 phase의 수행(또는 같은 역할)을 다시 띄우면 그 에이전트 줄 끝에 까닭을 덧붙인다는 규칙이 더해지고, 꼴에 그 덧붙임 자리가 보인다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `RunRulesTest`에 테스트가 더해진다. `test_state_tables_row_order`는 3번의 두 표와 tasks 끝 표에서 (상태, 갈 곳) 행을 차례대로 뽑아 이 phase가 바꾼 뒤의 기대 목록과 견준다. 나머지 셋은 "멈춘다"의 `회고면 8번` 있음과 `회고면 7번` 없음, 3번의 읽는 법과 `멈춤` 줄 행, `RUNLOG.md` 절의 다시 띄운 까닭 글을 본다 (`tests/test_skill_rules.py`)
- [ ] ARCHITECTURE `## 데이터 흐름` 끝 문단의 멈춤 문장에, 다시 맡기기로 한 답을 `RUNLOG.md`에 남겨 다시 불러도 같은 자리로 간다는 뜻이 더해진다. `## 디렉터리 구조`의 `test_skill_rules.py` 줄에 새 테스트가 다루는 규칙이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 상태 판정과 재개가 완료 조건 2대로다. (완료 조건 2)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝나고, `test_state_tables_row_order`와 TODO의 나머지 세 테스트가 그 안에 있다
  - 확인: `cp -R`로 작업 트리를 `<임시>/repo`에 베낀다(`<임시>`는 `mktemp -d`로 만든 폴더). 사본의 run 본문 3번 첫 표에서 갈 곳이 `5번`인 첫 행과 `6번`인 행의 자리를 바꾸고, 사본에서 `python3 -m unittest tests.test_skill_rules`를 돌린다. `test_state_tables_row_order`가 실패한다
  - 확인: `<임시>`에 시험 파일을 둔다.
    - (가) 기록 절이 있고, TODO 줄에 `` `## 확인 1` ``을 인용하고, 확인 절이 없는 `phase-1.md`
    - (나) `## 확인 1`의 판정이 실패, `## 확인 2`의 판정이 통과인 `phase-2.md`
    - (다) 회고 절 셋에 마지막 판정이 "문제 있음"인 `retro.md`
    - (라) 기록 절 안의 코드 블록에 `**판정**: 통과` 줄이 있고, 그 뒤 `## 확인 1`의 판정이 실패인 `phase-3.md`
    - (마) 그 phase의 다시 맡기기로 한 `멈춤` 줄과 다른 phase의 `멈춤` 줄이 있는 `RUNLOG.md`

    3번에 적은 읽는 법의 명령을 저마다 돌린다. 기대는 다음과 같다.
    - (가): 확인 절 0개
    - (나): 2개, 마지막 통과
    - (다): 3개, 마지막 "문제 있음"
    - (라): 1개, 마지막 실패
    - (마): 그 phase의 `멈춤` 줄 하나
  - 확인: ARCHITECTURE `## 데이터 흐름` 끝 문단의 멈춤 문장을 읽는다. "세 번 실패에서는 멈추고"가 그대로 있고, 다시 맡기기로 한 답을 `RUNLOG.md`에 남긴다는 뜻이 더해져 있다
- 앞 phase가 이룬 이슈·PR 규칙이 그대로다. (완료 조건 1, 5)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝난다. 완료 조건 1의 테스트가 그 안에 있다
  - 확인: `git grep -n 'TOOLS.md' -- plugins/`가 아무것도 내지 않는다
