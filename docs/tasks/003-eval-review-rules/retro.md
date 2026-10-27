# 회고

## 회고 1

**확인**
- 완료 조건 1: `plugins/plate/skills/eval/SKILL.md`의 "2. 실패를 모아 MAST 유형으로 나눈다"에 #36의 해결이 적혀 있다
  - eval 본문 55~85행을 읽음 → "실패가 아닌 줄" 목록 77행에 `남은 것:`으로 시작하는 줄은 그 task의 회고 절 "남은 것"에서 "문제"로 판정된 것만 실패로 세고 잡힌 곳은 그 자리라는 글, 78행에 명령 절의 사실이나 확인한 쪽의 판단만 적은 메모 줄은 실패가 아니라는 글이 저마다 있다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 129 tests in 16.191s`, 마지막 줄 `OK`. `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
- 완료 조건 2: 맥락 문서와 README가 1의 동작과 맞는다
  - `docs/PRD.md` 핵심 기능 8(18행), `docs/ARCHITECTURE.md` "데이터 흐름"의 tasks 끝 갈래(70행), `README.md`의 `eval` 행(15행), eval 본문 앞머리의 description을 읽음 → 모두 하네스를 여섯 기준으로 A~E로 매기고 실패를 MAST 유형으로 나눠 센다는 수준이고 어느 줄을 실패로 세는지 적지 않아 어긋나는 줄이 없다. 통과
- 완료 조건 3: 두 동작을 지난 tasks 기록으로 돌린 결과가 `docs/TOOLS.md`에 있고 저마다 기대대로다
  - `docs/TOOLS.md` "Claude Code" 절 끝(장면 G 뒤, "## Codex" 앞)의 "고친 eval과 review를 장면 H·I로 돌려 본 것" 절을 읽음 → 장면 H·I마다 Claude Code 2.1.311, 돌린 시각(21:35:55, 21:35:58), 세션 id(`8ff2f574-…`, `85a27c0a-…`), 기대한 결과, 본 결과, 걸린 시간, 막힌 명령, 임시 폴더 기록 경로(지워질 수 있다고 밝힘)가 있고 본 결과가 기대와 같다고 적혀 있다. 통과
  - 장면 H: 임시 복제본 `tmp.ZrtRAkxcY3/repo`의 `4d2de49:docs/tasks/eval.md`를 직접 읽음 → 유형마다 줄이 "유형 없음 2개"(11행, 19행)이고, `남은 것:` 문자열은 고칠 거리의 이슈 본문(110행)과 메모(121행)에만 있어 실패 목록에 `남은 것:` 줄과 명령 절의 메모 줄이 없다. 2 < 13. 통과
  - 장면 I: 임시 복제본 `tmp.cLI3gHHZIY/repo`의 `e23398a:docs/tasks/review.md`를 직접 읽음 → 테스트 적절성의 첫 근거가 "결과물인 마크다운만 바뀐 경우" 표로 매긴다는 것이고, 나머지 근거가 완료 조건의 확인과 확인·`돌리지 않음` 줄이 없는 동작이며, 등급 C로 실행 코드의 테스트를 까닭으로 들지 않았다. 통과
  - `git log -1 --format=%cI -- plugins/plate/skills/eval/SKILL.md plugins/plate/skills/review/SKILL.md` → `2026-10-27T21:34:17+09:00`. 절의 돌린 시각 21:35:55·21:35:58이 더 늦다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 129 tests in 16.191s`, `OK`. 통과

**남은 것**
- phase 1: 바뀐 eval 2번을 실제로 돌려 보지 않았다. 장면 H로 phase 2가 돌린다 → 문제 아님 (phase 2의 장면 H가 바뀐 eval을 돌렸고, 복제본의 `4d2de49` `eval.md`로 기대대로임을 직접 봤다)
- phase 2: 장면 I의 review가 메인에서 `command -v …`, `cut`과 `grep`을 이은 것, `grep -o -E` 단독 3개가 허용 목록에 없어 막혔다 → 문제 아님 (다른 꼴로 다시 돌려 장면 I의 결과가 기대대로이고, 막힘은 헤드리스 허용 목록의 문제라 task의 목표·결정·맥락 문서와 어긋나지 않는다)
- phase 2: 장면 H·I를 각 한 번만 돌려 되풀이해도 같은 결과일지 보지 않았다 → 문제 아님 (완료 조건 3과 결정이 되풀이를 요구하지 않는다)

**문제**
없음

**판정**: 통과
