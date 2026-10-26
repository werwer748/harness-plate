# 0.13.0으로 올리고 문서를 맞춘다

## 목표
두 매니페스트의 버전이 0.13.0이 되고, 마켓플레이스가 유효하며, 맥락 문서와 README가 이 tasks가 바꾼 동작(plan의 초안 전 점검, run이 넘기는 작업 트리 경로, review의 결과물인 마크다운)과 맞는다.

## 범위 밖
- 스킬 본문을 더 고치는 것. 어긋남을 찾으면 문서 쪽을 고친다
- CHANGELOG를 만드는 것. 이 저장소에는 없다

## 완료 조건
1. 두 매니페스트의 버전이 0.13.0이다.
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `"version": "0.13.0",`
2. 마켓플레이스가 유효하다.
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
3. 테스트가 모두 통과한다.
   - 확인: `python3 -m unittest discover -s tests`가 `OK`
4. 맥락 문서와 README가 바뀐 동작과 맞는다. (tasks 완료 조건 1~7이 바꾼 스킬과 문서를 이 task가 고칠 수 있다)
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어, 이 tasks가 바꾼 동작(plan의 초안 전 점검, run이 넘기는 작업 트리 경로, review의 결과물인 마크다운과 그 줄을 커버리지·중복에서 빼는 것)과 어긋나는 줄이 없다. 한 문서라도 어긋나는 줄이 있으면 실패
5. 앞 task가 이룬 tasks 완료 조건 7이 그대로 참이다. 이 task가 `docs/ARCHITECTURE.md`를 고칠 수 있다.
   - 확인: `grep -n -A3 '^## 결과물인 마크다운' docs/ARCHITECTURE.md`가 그 절과 `plugins/plate/skills/*/SKILL.md` 경로를 낸다

## 결정
- 버전은 0.13.0이다. 이유: 요청
- 확인은 문서를 읽어 한다. 이유: 바뀌는 것이 스킬 본문의 규칙 글과 문서다 (추천안으로 정함)
