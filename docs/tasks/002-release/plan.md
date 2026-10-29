# plate를 1.0.0으로 낸다

## 목표
두 매니페스트의 버전이 1.0.0이 되고, PRD의 1.0.0 줄이 9단계까지 만들어 1.0.0을 냈다고 적는다.

## 범위 밖
- git 태그와 GitHub 릴리스
- 1.0.0 뒤에 하기로 한 일(다른 도구로 넓히기, 검증 없는 종료를 막는 훅)
- 마켓플레이스 목록의 고침(버전 칸이 없다)

## 완료 조건
1. 두 매니페스트의 버전이 1.0.0이다(tasks 완료 조건 6).
   - 확인: `grep -n '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "1.0.0"`
   - 확인: `claude plugin validate plugins/plate` → `Validation passed`
2. PRD의 핵심 기능 아래 줄이 1.0.0을 냈다고 적는다(tasks 완료 조건 6).
   - 확인: `grep -n '1.0.0' docs/PRD.md` → 핵심 기능 아래의 줄이 `9단계까지 만들어 1.0.0을 냈다`를 적고, `낸다`로 끝나는 옛 줄은 없다
3. 테스트 묶음이 모두 통과한다(tasks 완료 조건 1).
   - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 결정
- 없음
