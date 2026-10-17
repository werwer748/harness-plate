# Phase 5: 맥락 문서와 버전

**목표**: `docs/TOOLS.md`와 `docs/ADR.md`가 바뀐 훅과 6단계를 반영하고, 두 매니페스트의 버전이 0.9.1이다.

**테스트 먼저**: 아니오 — 문서와 매니페스트의 버전만 고친다

**읽을 것**
- `docs/TOOLS.md` (머리글, "지금 상태" 표, Claude Code 절의 훅 묶음)
- `docs/ADR.md` (ADR-018의 이유, ADR-019의 트레이드오프)
- `plugins/plate/hooks/hooks.json` (phase 1이 바꾼 명령)
- `plugins/plate/skills/context/SKILL.md`의 답을 적는 규칙 (문장 중간에 있는 칸)
- code.claude.com/docs/en/hooks (종료 코드: 2만 막고 다른 0이 아닌 코드는 막지 않는다. 명령은 macOS와 Linux에서 `sh -c`, Windows에서 Git Bash나 PowerShell로 돈다)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`
- `git show ec2f192:docs/LESSONS.md`의 하네스의 문제점 절에서 (008-tdd, phase 4)의 첫째 줄, (008-tdd, phase 5)의 셋째 줄과, 프로젝트에서 배운 것 절의 (004-context-rules, 검증 1) 둘째 줄 (고칠 문제의 원문)

**TODO**
- [x] TOOLS.md의 머리글과 "지금 상태" 표의 Claude Code 행이 6단계(TDD와 엣지케이스)까지 적는다 (`docs/TOOLS.md`)
- [x] TOOLS.md의 훅 묶음에 종료 코드와 명령 실행의 사실이 출처 문서와 확인한 날짜와 함께 있다: 2만 막고 1이나 127 같은 다른 0이 아닌 코드는 막지 않는다, `python3`는 스크립트 파일을 열지 못하면 2로 끝난다, 명령은 macOS와 Linux에서 `sh -c`로 돌고, Windows에서는 Git Bash, Git Bash가 없으면 PowerShell로 돈다 (`docs/TOOLS.md`)
- [x] ADR-019의 트레이드오프가 `python3`가 없거나 스크립트 파일이 없을 때 훅이 돌지 않고 규칙 구간만 남는다고 적는다 (`docs/ADR.md`)
- [x] ADR-018의 이유 끝 "멈춘 이유는 없음"이 "멈춘 이유는 없다."다 (`docs/ADR.md`)
- [x] 두 매니페스트의 버전이 0.9.1이다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)

**통과 조건**
- 완료 조건 8이 참이다.
  - 확인: 완료 조건 8의 확인을 모두 돌린다
- 완료 조건 14가 참이다.
  - 확인: 완료 조건 14의 확인을 돌린다

## 한 일
- TOOLS.md의 머리글과 "지금 상태" 표의 Claude Code 행이 6단계(TDD와 엣지케이스)까지 적는다: 머리글 문단에 "6단계에서 확인한 것은 마지막 phase에서 판정을 돌리면서 적었다"를 잇고(008-tdd의 마지막 phase 5가 판정을 돌리고 같은 커밋 `6fe5830`에서 훅 묶음을 적었다), 표의 Claude Code 행에 "6단계(TDD와 엣지케이스)"를 더했다 (`docs/TOOLS.md`)
- TOOLS.md의 훅 묶음에 종료 코드와 명령 실행의 사실이 출처 문서와 확인한 날짜와 함께 있다: 훅 묶음의 기록 줄 뒤, 실행 시간 줄 앞에 세 줄을 더했다. 종료 코드(2만 막고 1이나 127은 막지 않는 오류, `onFailure: block`의 예외)는 code.claude.com/docs/en/hooks의 "Exit code output", "Other exit codes"를, 명령 실행(macOS·Linux는 `sh -c`, Windows는 Git Bash, 없으면 PowerShell)은 같은 문서의 "Exec form and shell form"을 2026-10-17에 WebFetch로 읽어 적었다. `python3`가 스크립트 파일을 열지 못하면 2로 끝나는 것은 `python3 /nonexistent_script.py; echo "exit=$?"` → `can't open file '/nonexistent_script.py': [Errno 2] No such file or directory`, `exit=2`(Python 3.13.2)로 확인해 적었다 (`docs/TOOLS.md`)
- ADR-019의 트레이드오프가 `python3`가 없거나 스크립트 파일이 없을 때 훅이 돌지 않고 규칙 구간만 남는다고 적는다: 트레이드오프 줄을 그 글로 바꿨다. 근거로 `hooks.json`의 명령 글을 `/bin/sh -c`로 돌려 스크립트 파일이 없으면 `0`, `PATH=/nonexistent`이면 `exec: python3: not found`와 `127`, 스크립트가 2로 끝나면 `2`를 봤고, 문서상 0과 127은 막지 않는다 (`docs/ADR.md`)
- ADR-018의 이유 끝 "멈춘 이유는 없음"이 "멈춘 이유는 없다."다: 그 글자만 바꿨다(context 본문 답을 적는 규칙의 문장 중간 칸 예와 같은 꼴) (`docs/ADR.md`)
- 두 매니페스트의 버전이 0.9.1이다: `"version": "0.9.0",`을 `"version": "0.9.1",`로 바꿨고 `python3 -m json.tool`로 두 파일이 JSON으로 읽히는 것을 봤다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)

## 확인 결과
- 완료 조건 8이 참이다.
  - `grep -n '멈춘 이유는 없음' docs/ADR.md` → 출력 없음(종료 코드 1). 통과
  - `docs/TOOLS.md` 3행(머리글)과 9행(지금 상태 표)을 읽었다 → 머리글에 6단계를 어떻게 적었는지가, 표의 Claude Code 행에 "6단계(TDD와 엣지케이스)"가 있다. 72~74행(훅 묶음)을 읽었다 → 2만 막고 1이나 127 같은 다른 0이 아닌 코드는 막지 않는다, `python3`는 스크립트 파일을 열지 못하면 2로 끝난다, macOS와 Linux는 `sh -c`, Windows는 Git Bash, 없으면 PowerShell이 출처 문서(code.claude.com/docs/en/hooks)와 날짜(2026-10-17)와 함께 있다. `docs/ADR.md` 26행(ADR-019 트레이드오프) → "`python3`가 없거나 스크립트 파일이 없을 때 훅이 돌지 않고 규칙 구간만 남는다.", 20행(ADR-018 이유) → 끝이 "멈춘 이유는 없다.". 통과
- 완료 조건 14가 참이다.
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `  "version": "0.9.1",`. 통과

## 계획과 달라진 점
- TODO 2는 훅 묶음에 세 사실을 적으라고 했는데, 둘째 줄(`python3`)에 `hooks.json`의 명령을 `sh -c`로 돌린 결과(스크립트 파일이 없으면 0, `python3`가 없으면 127, 있으면 스크립트의 종료 코드)도 더했다. 까닭: TODO 3의 ADR-019 트레이드오프가 기대는 사실이고, 옛 LESSONS (008-tdd, phase 4) 첫째 줄이 그 트레이드오프가 확인되지 않았다고 적었다.

## 남은 것
없음

## 하네스에서 걸린 것
없음

## 회고 1: 확인만

**확인**
- 완료 조건 8이 참이다.
  - `grep -n '멈춘 이유는 없음' docs/ADR.md` → 출력 없음(종료 코드 1). 통과
  - `docs/TOOLS.md` 3행(머리글), 9행("지금 상태" 표), 66~75행(훅 묶음)과 `docs/ADR.md` 20행(ADR-018 이유), 26행(ADR-019 트레이드오프)을 읽었다 → 머리글이 "6단계에서 확인한 것은 마지막 phase에서 판정을 돌리면서 적었다"까지 적고, 표의 Claude Code 행에 "6단계(TDD와 엣지케이스)"가 있다. 훅 묶음 72행에 2만 막고 1이나 127 같은 다른 0이 아닌 코드는 막지 않는다는 것이 출처(code.claude.com/docs/en/hooks의 "Exit code output", "Other exit codes", 2026-10-17)와 함께, 73행에 `python3`는 스크립트 파일을 열지 못하면 2로 끝난다는 것이, 74행에 macOS와 Linux는 `sh -c`, Windows는 Git Bash, 없으면 PowerShell이라는 것이 출처("Exec form and shell form", 2026-10-17)와 함께 있다. ADR-019 트레이드오프가 "`python3`가 없거나 스크립트 파일이 없을 때 훅이 돌지 않고 규칙 구간만 남는다."이고, ADR-018 이유 끝이 "멈춘 이유는 없다."다. 통과
- 완료 조건 14가 참이다.
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `  "version": "0.9.1",`. 통과

**문제**
- 없음

**판정**: 통과
