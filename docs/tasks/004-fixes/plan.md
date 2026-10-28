# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리고 plate 저장소에서 고친다

## 완료 조건
1. run 3번 "상태를 읽는 법"의 `awk`·`grep` 명령과 "글을 넘기는 법"의 작은따옴표 넘기기를 단위 테스트가 조각 글로만 단언하고 돌리지 않는다. 시험 파일(코드 블록 속 판정 줄, TODO 속 `## 확인 1`)에 본문의 `awk`를 돌리는 테스트와, 가짜 `gh`에 따옴표·백틱·`$(…)`가 든 제목을 넘기는 테스트로 남긴다 (`tests/test_skill_rules.py:310-322`, `tests/test_skill_rules.py:189-208`)
   - 확인: 새 두 테스트가 run 본문에서 명령을 뽑아 임시 폴더에서 돌리고, `python3 -m unittest discover -s tests`가 `OK`로 끝난다. 본문의 `awk` 패턴이나 `'\''` 치환 글을 바꾼 사본에서 그 테스트가 실패한다
2. 한글이 든 파일을 `python3 -` heredoc으로 고치면 `SyntaxError: Non-UTF-8 code`로 깨질 수 있다는 도구 동작을 확인한 버전과 함께 한 줄로 남긴다 (`docs/TOOLS.md`의 `## Claude Code` 첫 목록)
   - 확인: `grep -c 'Non-UTF-8' docs/TOOLS.md`가 1이고 `wc -c < docs/TOOLS.md`가 15360 이하다
3. tasks 완료 조건 1, 2, 3, 4이 참이다.
   - tasks 완료 조건 1: 단위 테스트가 모두 통과한다.
     - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝난다
   - tasks 완료 조건 2: `docs/TOOLS.md`가 15KB 이하이고, 다른 문서가 가리키는 네 절(`플러그인 폴더의 편집과 권한 모드`, `세션 도중의 스킬 본문 고침`, `ruleset과 CODEOWNERS로 워크플로 PR의 자동 머지를 막는지 본 것`, `도구를 넓힐 때 할 것`)이 남아 있고, 시험 실행 기록이 없다.
     - 확인: `wc -c < docs/TOOLS.md`가 15360 이하다
     - 확인: 네 절 이름마다 `grep -c '<절 이름>' docs/TOOLS.md`가 1 이상이다
     - 확인: `grep -cE '/var/folders/|tmp\.[A-Za-z0-9]{6,}|장면 [A-Z]' docs/TOOLS.md`가 0이다
   - tasks 완료 조건 3: plate 스킬 본문 어디에도 `docs/TOOLS.md`를 쓰거나 커밋하라는 규칙이 없고, 맥락 문서와 README에도 그 규칙을 말하는 줄이 없다.
     - 확인: `git grep -n 'TOOLS.md' -- plugins/`가 아무것도 내지 않는다
     - 확인: `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md`가 아무것도 내지 않는다
   - tasks 완료 조건 4: 보고서에서 `처리: plan으로 넘김`인 발견 29건이 저마다 한 task 머리의 완료 조건에 들고, 그 task의 회고가 통과한다.
     - 확인: `grep -c '처리: plan으로 넘김' docs/cleanup/2026-10-28.md`가 29이고, 세 task 머리의 완료 조건에 적힌 발견 번호를 모으면 그 29건과 같다
     - 확인: 세 task의 `retro.md` 마지막 회고 절의 판정이 저마다 "통과"다

## 결정
- 없음
