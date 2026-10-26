# 0.12.0을 내고 문서를 맞춘다

## 목표
두 매니페스트의 버전을 0.12.0으로 올리고, 매니페스트의 설명, README, 맥락 문서 넷(PRD 밖의 ARCHITECTURE, ADR, TOOLS와 README)이 001~005가 바꾼 동작과 맞는다. 플러그인 검증과 테스트가 통과한다.

## 범위 밖
- 스킬과 워크플로 템플릿의 동작을 바꾸는 것. 001~005에서 했다
- GitHub 이슈를 닫는 것과 PR, 태그, 릴리스를 만드는 것
- 1.0.0을 내는 것. 9단계 뒤에 한다

## 완료 조건
1. tasks 완료 조건 11이 참이다.
   - 확인: `grep -n '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`이 두 줄 모두 `"0.12.0"`을 낸다
   - 확인: `claude plugin validate .`가 오류 없이 끝난다
   - 확인: `python3 -m unittest discover -s tests`가 `OK`
   - 확인: `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 하나씩 따로 읽어, 문서마다 001~005가 바꾼 동작(아래 2번의 일곱)과 어긋나는 줄이 없다. 네 문서 모두 어긋남이 없어야 통과다
2. 두 매니페스트의 설명이 바뀐 동작과 어긋나지 않는다.
   - 확인: 두 `plugin.json`의 `description`을 읽어 일곱 가운데 설명이 다루는 것과 어긋나는 글이 없다. 일곱: PR 모드 review가 지침을 기준 브랜치에서 읽음(#11), 워크플로가 지침 파일을 기준 브랜치로 되돌리고 실패 때 오류 줄을 남김(#11, #13), 새 줄 20줄 미만의 커버리지(#12), 고칠 phase와 이슈·PR의 본문 넘기기(#4, #8, #10), plan의 TODO·조건·경계 규칙(#5, #6, #7), retro의 고칠 쪽·경계 밖·남은 것과 phase의 남은 것(#4, #5, #9), eval의 실패 모으기와 규칙 준수 표(#15, #16)
3. TOOLS.md의 판정 버전 줄에 이 tasks가 든다.
   - 확인: `grep -n 'issue-fixes(0.12.0)' docs/TOOLS.md`가 17줄 근처의 판정 버전 문단에서 한 줄을 낸다

## 결정
- 없음
