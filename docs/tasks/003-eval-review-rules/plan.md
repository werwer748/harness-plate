# eval의 #36을 고치고, eval과 review를 지난 기록으로 돌려 본다

## 목표
eval의 #36이 고쳐지고, review의 #43이 고쳐졌는지(이미 고쳐졌으면 그대로인지) 확인되며, 두 동작을 지난 tasks 기록으로 돌린 결과가 `docs/TOOLS.md`에 남는다.

## 범위 밖
- 장면에서 #43이 기대대로면 review 본문을 고치는 것
- run, plan, phase, check, retro, cleanup의 본문
- 버전을 올리는 것과 테스트를 더하는 것. `004-tests-version`이 한다

## 완료 조건
1. `plugins/plate/skills/eval/SKILL.md`의 "2. 실패를 모아 MAST 유형으로 나눈다"에 #36의 해결이 적혀 있다: `남은 것:`으로 시작하는 줄은 그 task의 회고 절에서 "문제"로 판정된 것만 실패로 세고(잡힌 곳은 그 자리), 명령 절의 사실이나 판단을 적은 메모 줄은 실패가 아니다
   - 확인: eval 본문의 그 절을 읽어 두 글이 저마다 있다. 하나라도 없으면 실패
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
2. 맥락 문서와 README가 1의 동작과 맞는다.
   - 확인: `docs/PRD.md`의 핵심 기능 8, `docs/ARCHITECTURE.md`의 "데이터 흐름"의 tasks 끝 갈래, `README.md`의 `eval` 행, eval 본문 앞머리의 description을 저마다 읽어, 실패로 세는 줄과 어긋나는 줄이 없다. 하나라도 있으면 실패
3. 두 동작을 지난 tasks 기록으로 돌린 결과가 `docs/TOOLS.md`에 있고, 저마다 기대대로다.
   - 확인: `docs/TOOLS.md`의 "Claude Code" 절에 더해진 eval·review 장면 절을 읽어, 장면 H·I마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있고 본 결과가 기대와 같다. 하나라도 없거나 다르면 실패
     - 장면 H(#36): 복제본의 브랜치를 issue-sweep의 기록(`e3836b2`)에 두고 `docs/tasks/eval.md`를 지운 커밋을 더하고, 기본 브랜치를 그 tasks가 갈라진 곳에 두고 eval을 부르면, 새 `eval.md`의 실패 목록에 그 task의 회고가 "문제"로 판정하지 않은 `남은 것:` 줄과 명령 절의 메모 줄이 하나도 없고, "유형 없음" 실패가 `e3836b2`의 `eval.md`의 13개보다 적다
     - 장면 I(#43): 복제본의 브랜치를 cleanup의 기록(`6292d12`, 코드 평가 앞)에 두고 기본 브랜치를 `32e2fbb`에 두고 review를 부르면, 새 `review.md`의 테스트 적절성이 "결과물인 마크다운만 바뀐 경우의 테스트 적절성" 표로 매겨지고 근거가 완료 조건의 확인 줄과 `돌리지 않음` 줄이며, "실행 코드의 테스트가 없다"를 까닭으로 D 이하를 매기지 않는다
   - 확인: 그 절의 돌린 시각이 `git log -1 --format=%cI -- plugins/plate/skills/eval/SKILL.md plugins/plate/skills/review/SKILL.md`보다 늦다

## 결정
- 장면은 `mktemp -d`에 이 저장소를 복제한 곳에서 작업 트리의 `plugins/plate`를 `--plugin-dir`로 실어 헤드리스(`claude -p`)로 돌린다. 장면의 tasks 기록은 이력의 지난 tasks 기록(`e3836b2`, `6292d12`)을 그대로 쓰고, 복제본의 브랜치와 기본 브랜치만 장면에 맞춰 둔다. 허용 목록은 `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"을 쓴다. 이유: tasks 머리의 결정
- 장면 절은 장면마다 Claude Code 버전, 복제본의 브랜치와 기본 브랜치의 커밋, 돌린 시각, 세션 id, 기대한 결과, 본 결과, 걸린 시간, 막힌 명령을 적고, 임시 폴더의 기록 경로도 적되 지워질 수 있다고 밝힌다. 이유: tasks 완료 조건 3의 확인이 이 필드를 본다
- #43은 장면 I를 먼저 돌려 기대대로면 review 본문을 고치지 않는다. 기대와 다르면 review의 "5. 등급을 매긴다"를 고치고 장면 I를 다시 돈다. 이유: tasks 머리의 결정
