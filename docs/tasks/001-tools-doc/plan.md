# TOOLS.md를 도구 사실만 남기고 그에 기댄 규칙을 지운다

## 목표
`docs/TOOLS.md`가 계속 쓰이는 도구 사실만 담은 15KB 이하의 문서가 되고, run·eval·plan과 맥락 문서에서 TOOLS.md에 사용량 까닭과 시험 실행 기록을 적게 하는 규칙이 사라진다. 정리 점검의 성능-1·성능-2(TOOLS.md를 줄여 갈음)와 유지보수성-10(run `RUNLOG.md` 절의 TOOLS.md 커밋 단언)이 이로써 고쳐진다.

## 범위 밖
- plan과 run이 맥락 문서를 모두 읽는 규칙을 바꾸는 것
- run 본문에서 TOOLS.md에 걸리지 않는 규칙을 고치는 것(002-run-rules가 한다)
- plan 본문에서 시험 실행 기록 규칙 말고 다른 것을 고치는 것(003-plan-rules가 한다)
- eval 본문에서 규칙 준수 표의 두 행 말고 다른 것을 고치는 것

## 완료 조건
1. run 본문에 `docs/TOOLS.md`가 없고, 사용량이 돌아오지 않은 까닭은 `RUNLOG.md` 절에서 10번의 보고에만 적게 한다. eval 규칙 준수 표의 `NNN-slug: RUNLOG`와 `<tasks 이름>: RUNLOG` 행의 파일 칸은 `` `RUNLOG.md` ``뿐이다. (성능-1, 성능-2, 유지보수성-10)
   - 확인: `git grep -n 'TOOLS.md' -- plugins/`가 아무것도 내지 않는다
   - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝나고, 그 가운데 run `RUNLOG.md` 절에 TOOLS.md가 없고 까닭을 보고에 적는 글이 있는지 보는 테스트와 eval 표 두 행의 파일 칸이 `` `RUNLOG.md` ``인지 보는 테스트가 있다
   - 돌리지 않음: run은 에이전트를 띄우고 사용자에게 묻는 스킬이라 RUNLOG 커밋의 흐름을 임시 폴더에서 돌릴 수 없다. eval은 끝난 tasks의 기록 전체가 있어야 돌고, 바뀐 것은 표 두 칸의 글이다
2. `docs/TOOLS.md`가 15KB 이하이고, 다른 문서가 가리키는 네 절(`플러그인 폴더의 편집과 권한 모드`, `세션 도중의 스킬 본문 고침`, `ruleset과 CODEOWNERS로 워크플로 PR의 자동 머지를 막는지 본 것`, `도구를 넓힐 때 할 것`)과 ruleset을 거는 `gh api` 명령과 JSON이 남아 있고, 시험 실행 기록이 없다.
   - 확인: `wc -c < docs/TOOLS.md`가 15360 이하다
   - 확인: 네 절 이름마다 `grep -c '<절 이름>' docs/TOOLS.md`가 1 이상이다
   - 확인: `grep -c 'rulesets --input -' docs/TOOLS.md`가 1 이상이고 `grep -c '"enforcement"' docs/TOOLS.md`가 1 이상이다
   - 확인: `grep -cE '/var/folders/|tmp\.[A-Za-z0-9]{6,}|장면 [A-Z]' docs/TOOLS.md`가 0이다
3. plan의 적는 규칙에, 돌려 본 확인의 결과(차림, 출력, 본문 해시)는 그 phase의 기록에만 남기고 맥락 문서에 옮겨 적는 TODO를 두지 않으며, 맥락 문서에는 다음 계획이 알아야 할 도구 동작만 한 줄로 더한다는 규칙이 있다. `docs/ARCHITECTURE.md`의 TOOLS.md 규칙 줄도 같은 뜻이다.
   - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝나고, 그 가운데 plan `적는 규칙`에 이 규칙의 글이 있는지 보는 테스트가 있다
   - 확인: `docs/ARCHITECTURE.md`의 `## 패턴과 규칙`에서 `docs/TOOLS.md`를 말하는 줄을 읽어, "도구마다 다른 동작과 확인을 멈춘 지점을 적는다"와 "시험 실행 기록은 적지 않는다"가 둘 다 있다
   - 돌리지 않음: plan은 사용자에게 묻고 승인받아야 계획을 쓰는 스킬이라, 이 규칙대로 TODO를 쓰는지 임시 폴더에서 돌릴 수 없다
4. 맥락 문서(`docs/PRD.md`, `docs/ARCHITECTURE.md`)와 `README.md`에 run이 사용량 까닭을 TOOLS.md에 적거나 커밋한다는 줄이 없고, `docs/ARCHITECTURE.md`의 테스트 설명 줄이 바뀐 테스트와 맞는다.
   - 확인: `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md`가 아무것도 내지 않는다
   - 확인: `docs/ARCHITECTURE.md`의 `## 디렉터리 구조`에서 `test_skill_rules.py` 줄을 읽어, "`docs/TOOLS.md` 커밋 규칙이 `RUNLOG.md` 절 한 곳에 있음"이 없고 1·3의 새 테스트가 다루는 규칙이 적혀 있다

## 결정
- TOOLS.md에서 지우는 절에 다음 계획이 알아야 할 도구 동작(막히는 명령의 꼴, 권한, 사용량이 돌아오는지 같은 것)이 있으면, 버전과 함께 한 줄로 남기는 절에 옮긴다. 임시 경로, 본문 해시, 커밋 id, 장면의 차림과 기대는 옮기지 않는다. 이유: 요청의 결정 (1)과 (4)
- 시험 실행 기록 규칙은 TOOLS.md라는 이름 없이 "맥락 문서"로 적는다. 이유: plan은 다른 프로젝트에서도 도는 본문이고 TOOLS.md는 이 저장소에만 있다(ADR-004의 동작으로 쓰기)
