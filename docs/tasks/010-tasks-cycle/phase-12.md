# Phase 12: 맥락 문서, README, AGENTS.md, ADR, 매니페스트를 새 흐름에 맞춘다

**목표**: 맥락 문서, README, 이 레포의 `AGENTS.md`, 두 매니페스트가 새 흐름과 0.10.0을 말한다.

**테스트 먼저**: 아니오 — `.md`와 매니페스트의 버전·설명만 고친다.

**읽을 것**
- `docs/PRD.md` (목표 문단의 규칙 구간 설명, 핵심 기능 5, 7, 8)
- `docs/ARCHITECTURE.md` (디렉터리 구조, 패턴과 규칙의 run 브랜치 규칙과 막는 장치, 데이터 흐름)
- `docs/ADR.md` (항목의 꼴. 마지막은 ADR-019)
- `README.md` (스킬 표와 두 도구에서 부르는 이름)
- `AGENTS.md` (이 레포의 문서 지도와 규칙 구간)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (버전 0.9.1과 설명)
- `plugins/plate/skills/setup/SKILL.md` (phase 2가 바꾼 두 구간의 글)
- `plugins/plate/skills/run/SKILL.md` (새 흐름 전체)

**TODO**
- [x] `docs/PRD.md`의 목표 문단과 핵심 기능 5, 7, 8이 새 흐름을 말한다: 5는 task 회고, 7은 두 실행 방식(이 단계에서 만들었다), 8은 tasks 끝의 코드 평가와 하네스 eval(이 단계에서 만들었다)과 011의 PR·CI
- [x] `docs/ARCHITECTURE.md`의 디렉터리 구조가 아홉 스킬을, 패턴과 규칙이 `tasks/<이름>` 브랜치와 새 규칙 구간을, 데이터 흐름이 새 흐름을 말하고, 명령 절이 생긴다(테스트 `python3 -m unittest discover -s tests`, 빌드와 린트는 "없음"). "verify", "LESSONS", "worktree"가 남지 않는다
- [x] `README.md`의 스킬 표와 두 도구에서 부르는 이름이 아홉 스킬이다
- [x] 이 레포 `AGENTS.md`의 `docs/tasks/` 행과 규칙 구간이 setup 본문의 글과 같아진다
- [x] `docs/ADR.md`에 ADR-020이 더해진다: GitHub 이슈(`werwer748/harness-plate`, `gh`)를 plate 자체의 고칠 거리를 모으는 외부 서비스로 쓴다. 결정, 이유, 트레이드오프를 적고 계획이나 task 폴더는 적지 않는다
- [x] 두 매니페스트의 버전이 0.10.0이 되고 설명이 아홉 스킬을 말한다

**통과 조건**
- 완료 조건 2, 10, 11, 12가 참이다
  - 확인: 네 완료 조건의 확인을 모두 돌린다
- 완료 조건 15가 참이다
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄 `OK`

## 한 일
- `docs/PRD.md`의 목표 문단과 핵심 기능 5, 7, 8이 새 흐름을 말한다: 목표 문단의 규칙 구간 설명을 새 규칙(task는 회고가 통과해야, tasks는 끝의 코드 평가와 하네스 eval을 담은 보고가 나와야 끝난다)으로 바꿨다. 5를 "task 회고"(retro.md와 FRICTION.md, 5단계의 검증을 합침)로, 7을 두 실행 방식과 멈추는 자리로, 8을 "평가"(코드 다섯 범주와 하네스 여섯 기준의 A~E, Sonar way, 고칠지 묻기, 고침 task, ADR-020의 이슈, BACKLOG)와 011의 PR·CI로 고쳤다. 7과 8의 "이 단계"는 `010-tasks-cycle`로 적었다. 같은 문서의 3, 4도 고쳤다(계획과 달라진 점) (`docs/PRD.md`)
- `docs/ARCHITECTURE.md`의 디렉터리 구조, 패턴과 규칙, 데이터 흐름, 명령 절: 스킬 트리에서 verify를 빼고 check, review, eval을 더해 아홉으로, run과 retro의 주석을 새 일로 바꿨다. 패턴과 규칙에서 프로젝트 규칙 우선이 든 스킬을 일곱(plan, run, phase, check, retro, review, eval)으로, 규칙 구간 설명을 새 규칙으로, 훅 설명을 "`phase-N.md`가 있는 task가 없을 때"로, run 브랜치 규칙을 `tasks/<이름>`과 비운 뒤 합칠지 묻기로 바꾸고 worktree 문장을 지웠다. 데이터 흐름을 셋업 → 맥락 → 계획 → 실행(실행 방식, 수행, 확인, `done-phase-N.md`, 회고와 FRICTION, 고칠 phase, RUNLOG) → tasks 끝(review, eval, 보고와 물음, 이슈, BACKLOG, 고침 task, 비우기, 합칠지)으로 다시 쓰고 LESSONS와 verify를 지웠다. 끝에 `## 명령` 절(빌드 없음, 린트 없음, 테스트 `python3 -m unittest discover -s tests`)을 더했다 (`docs/ARCHITECTURE.md`)
- `README.md`의 스킬 표와 두 도구에서 부르는 이름이 아홉 스킬이다: "일곱"을 "아홉"으로, 표에서 verify를 빼고 check, review, eval을 더하고 plan, run, retro의 글을 새 흐름으로 바꿨다. `/plate:…`와 `$plate:…` 목록을 아홉으로, Codex 확인 문단의 새로 더한 스킬 목록에서 verify를 빼고 check, review, eval을 넣었다 (`README.md`)
- 이 레포 `AGENTS.md`의 `docs/tasks/` 행과 규칙 구간이 setup 본문의 글과 같아진다: 두 곳을 setup 본문의 글로 바꿨다. 표 위의 "작업 기록"도 setup 본문대로 "tasks 기록"으로 바꿨다. `docs/TOOLS.md` 행은 그대로 뒀다 (`AGENTS.md`)
- `docs/ADR.md`에 ADR-020이 더해진다: "plate 자체의 고칠 거리는 GitHub 이슈로 모은다"를 결정(묻고 `gh`로 `werwer748/harness-plate`에 올림, 같은 이슈엔 "다시 나옴" 댓글, 고침은 harness-plate, 이 프로젝트만의 것은 그 프로젝트에서, `gh` 실패 때 보고하고 잇기), 이유, 트레이드오프(GitHub과 `gh` 인증에 기댐, 권한 있는 계정, 같은 이슈 판단의 오류)로 적었다. 계획과 task 폴더는 적지 않았다 (`docs/ADR.md`)
- 두 매니페스트의 버전이 0.10.0이 되고 설명이 아홉 스킬을 말한다: `"version"`을 0.9.1에서 0.10.0으로, 설명의 스킬 목록을 아홉(setup, context, plan, run, phase, check, retro, review, eval)으로 바꾸고 verify를 뺐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)

## 확인 결과
- 완료 조건 2가 참이다
  - `grep -n "작업" plugins/plate/skills/*/SKILL.md plugins/plate/hooks/edit_guard.py README.md docs/PRD.md docs/ARCHITECTURE.md AGENTS.md` → 10줄. 모두 읽었다: context:8 "다음 작업의 근거"(일반의 일), edit_guard.py:23 "작업 트리"(git의 working tree), AGENTS.md:16과 setup:132 "## 작업 규칙", setup:3과 setup:10 "작업 규칙"(규칙 구간의 이름), PRD:4 "작업하게 하는"(동사)과 "작업 규칙", PRD:7 "그 프로젝트의 모든 작업"과 PRD:24 "모든 작업이 파이프라인을 거친다"(단위가 아닌 일반의 일), ARCHITECTURE:36 "작업 디렉터리"(working directory). tasks, task, phase를 가리키는 "작업"은 없다. 통과
  - 낱말 절이 있는 스킬(check, eval, phase, plan, retro, review, run. context에는 tasks, task, phase의 정의가 없다)의 tasks, task(task 폴더), task 머리, tasks 머리, phase(`phase-N.md`, `done-phase-N.md`) 정의를 `awk`로 뽑아 읽었다 → 모두 tasks는 요청 하나를 계획한 묶음으로 `docs/tasks/`에 하나, task는 `NNN-slug/` 폴더 하나, phase는 `phase-N.md` 하나, tasks 머리는 제목·이름·여섯 절, task 머리는 제목·네 절로 결정과 같다. 통과
- 완료 조건 10이 참이다
  - `grep -n "verify\|LESSONS\|worktree" docs/PRD.md docs/ARCHITECTURE.md README.md AGENTS.md` → 0줄(종료 코드 1). 통과
  - `diff <(sed -n '/<!-- plate:rules:start -->/,/<!-- plate:rules:end -->/p' AGENTS.md) <(sed -n '/<!-- plate:rules:start -->/,/<!-- plate:rules:end -->/p' plugins/plate/skills/setup/SKILL.md)` → 출력 없음(종료 코드 0). 통과
  - `grep -hF '| `docs/tasks/' AGENTS.md plugins/plate/skills/setup/SKILL.md | sort -u | wc -l` → `1`. 통과
  - `grep -c "^## 명령" docs/ARCHITECTURE.md` → `1`, `grep -n -A4 "^## 명령" docs/ARCHITECTURE.md` → `- 빌드: 없음`, `- 린트: 없음`, ``- 테스트: `python3 -m unittest discover -s tests` ``. 통과
  - `docs/PRD.md`의 핵심 기능 5(task 회고), 7(두 실행 방식과 멈추는 자리), 8(review의 다섯 범주, eval의 여섯 기준, 고칠지 묻기, 고침 task, 이슈, BACKLOG, 011의 PR·CI)과 `docs/ARCHITECTURE.md`의 디렉터리 구조(아홉 스킬), 패턴과 규칙(새 규칙 구간, `tasks/<이름>` 브랜치), 데이터 흐름(계획 → 실행 → tasks 끝)을 `sed -n`으로 읽었다 → 아홉 스킬과 새 흐름을 말한다. 통과
- 완료 조건 11이 참이다
  - `grep -n "^### ADR-020" docs/ADR.md` → `28:### ADR-020: plate 자체의 고칠 거리는 GitHub 이슈로 모은다` 1줄. 항목을 읽어 결정, 이유, 트레이드오프가 있고 GitHub 이슈(`werwer748/harness-plate`, `gh`)를 말한다. 통과
- 완료 조건 12가 참이다
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json | grep -cx '  "version": "0.10.0",'` → `2`(두 줄 모두 `  "version": "0.10.0",`). 통과
  - 두 매니페스트의 `description`을 `python3 -c "import json…"`로 읽었다 → setup, context, plan, run, phase, check, retro, review, eval 아홉 스킬이 있고, `grep -o verify` → 0. 통과
- 완료 조건 15가 참이다
  - `python3 -m unittest discover -s tests` → `Ran 39 tests in 13.139s`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- TODO는 `docs/PRD.md`의 목표 문단과 핵심 기능 5, 7, 8만 적었지만 3과 4도 고쳤다. 3에 tasks를 가리키는 "요청 하나를 작업으로 계획해"가 있어 이 phase의 통과 조건인 완료 조건 2를 어겼고, 4는 "회고에서 통과한 phase의 파일은 지운다"로 이 phase의 목표(새 흐름을 말한다)와 어긋났다.
- TODO는 `AGENTS.md`의 `docs/tasks/` 행과 규칙 구간만 적었지만 표 위의 "작업 기록"도 setup 본문의 글("tasks 기록")로 바꿨다. tasks의 기록을 가리키는 "작업"이라 완료 조건 2를 어겼고, setup의 3번이 맞추는 "표 위의 글"과도 다르다.
- TODO의 "(이 단계에서 만들었다)"는 PRD에 단계 번호 대신 `010-tasks-cycle`로 적었다. 010은 7단계와 8단계의 앞부분을 함께 담아 단계 번호 하나로 적을 수 없다.

## 남은 것
- 없음

## 하네스에서 걸린 것
- 이 phase가 이 레포 `AGENTS.md`의 규칙 구간을 새 글(retro, review, eval)로 바꿔, 아직 0.9.1 레일(verify)로 도는 010의 남은 단계(이 phase의 회고와 작업 검증)를 맡은 에이전트에게 새 규칙이 실린다. 010의 검증 에이전트가 `verify.md` 대신 retro·review·eval을 찾을 수 있다.

## 회고 1: 확인만

**확인**
- 완료 조건 2, 10, 11, 12가 참이다
  - 완료 조건 2: `grep -n "작업" plugins/plate/skills/*/SKILL.md plugins/plate/hooks/edit_guard.py README.md docs/PRD.md docs/ARCHITECTURE.md AGENTS.md` → 10줄. 모두 읽었다: context:8 "다음 작업의 근거"(일반의 일), edit_guard.py:23 "작업 트리"(git의 working tree), AGENTS.md:16과 setup:132 "## 작업 규칙", setup:3과 setup:10 "작업 규칙"(규칙 구간의 이름), PRD:4 "작업하게 하는"(동사)과 "작업 규칙", PRD:7 "그 프로젝트의 모든 작업"과 PRD:24 "모든 작업이 파이프라인을 거친다"(일반의 일), ARCHITECTURE:36 "작업 디렉터리"(working directory). tasks, task, phase를 가리키는 "작업"은 없다. 통과
  - 완료 조건 2: 낱말 절이 있는 스킬 여덟(check, context, eval, phase, plan, retro, review, run. setup에는 낱말 절이 없고, context의 낱말 절에는 tasks, task, phase의 정의가 없다)의 절을 `awk`로 뽑아 읽었다 → tasks는 요청 하나를 계획한 묶음으로 `docs/tasks/`에 하나, task(task 폴더)는 `NNN-slug/` 폴더 하나, phase는 `phase-N.md` 하나(통과하면 `done-phase-N.md`), tasks 머리는 제목·이름·여섯 절, task 머리는 제목·네 절로 결정의 정의와 어긋나지 않는다. 통과
  - 완료 조건 10: `grep -n "verify\|LESSONS\|worktree" docs/PRD.md docs/ARCHITECTURE.md README.md AGENTS.md` → 0줄(종료 코드 1). 통과
  - 완료 조건 10: `diff <(sed -n '/<!-- plate:rules:start -->/,/<!-- plate:rules:end -->/p' AGENTS.md) <(sed -n '/<!-- plate:rules:start -->/,/<!-- plate:rules:end -->/p' plugins/plate/skills/setup/SKILL.md)` → 출력 없음(종료 코드 0). 통과
  - 완료 조건 10: `grep -hF '| `docs/tasks/' AGENTS.md plugins/plate/skills/setup/SKILL.md | sort -u | wc -l` → `1`. 통과
  - 완료 조건 10: `grep -c "^## 명령" docs/ARCHITECTURE.md` → `1`, `grep -n -A5 "^## 명령" docs/ARCHITECTURE.md` → `- 빌드: 없음`, `- 린트: 없음`, ``- 테스트: `python3 -m unittest discover -s tests` ``. 통과
  - 완료 조건 10: `docs/PRD.md` 전체와 `docs/ARCHITECTURE.md` 전체를 `cat`으로 읽었다 → PRD 핵심 기능 5(task 회고, `retro.md`, `FRICTION.md`), 7(두 실행 방식, 멈추는 자리), 8(다섯 범주와 여섯 기준의 A~E, Sonar way, 고칠지 묻기, 고침 task, ADR-020의 이슈, `docs/BACKLOG.md`, 011의 PR·CI)과 ARCHITECTURE의 디렉터리 구조(아홉 스킬), 패턴과 규칙(새 규칙 구간, `tasks/<이름>` 브랜치, 비운 뒤 합칠지 묻기), 데이터 흐름(셋업 → 맥락 → 계획 → 실행 → tasks 끝)이 아홉 스킬과 새 흐름을 말한다. 통과
  - 완료 조건 11: `grep -n "^### ADR-020" docs/ADR.md` → `28:### ADR-020: plate 자체의 고칠 거리는 GitHub 이슈로 모은다` 1줄. 항목을 읽어 결정(`gh`로 `werwer748/harness-plate`에 이슈, "다시 나옴" 댓글), 이유, 트레이드오프가 있다. 통과
  - 완료 조건 12: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `  "version": "0.10.0",`. 통과
  - 완료 조건 12: 두 매니페스트의 `description`을 `python3`의 `json`으로 읽었다 → setup, context, plan, run, phase, check, retro, review, eval 아홉 스킬이 있고, `grep -n verify` 두 매니페스트 → 0줄(종료 코드 1). 통과
- 완료 조건 15가 참이다
  - `python3 -m unittest discover -s tests` → `Ran 39 tests in 13.789s`, 마지막 줄 `OK`. 통과

**문제**
- 없음

**판정**: 통과
