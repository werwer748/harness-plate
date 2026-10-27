# 코드 평가

## 평가 1

**대상**
- 범위: `bf8ee2c`(main에서 갈라진 곳)부터 `74aea89`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 10개, 새 줄 118줄, 잴 새 줄 93줄
  - `plugins/plate/.claude-plugin/plugin.json` +1
  - `plugins/plate/.codex-plugin/plugin.json` +1
  - `tests/test_skill_rules.py` +91
  - `plugins/plate/skills/check/SKILL.md` +1 (결과물인 마크다운)
  - `plugins/plate/skills/eval/SKILL.md` +4 (결과물인 마크다운)
  - `plugins/plate/skills/phase/SKILL.md` +1 (결과물인 마크다운)
  - `plugins/plate/skills/plan/SKILL.md` +3 (결과물인 마크다운)
  - `plugins/plate/skills/retro/SKILL.md` +3 (결과물인 마크다운)
  - `plugins/plate/skills/review/SKILL.md` +1 (결과물인 마크다운)
  - `plugins/plate/skills/run/SKILL.md` +12 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 161 tests in 16.100s`, `OK`. 통과
- 커버리지: 측정 못함 — 명령 절과 ADR-024가 커버리지 도구를 두지 않는다고 정했고, 이 환경에도 `coverage` 모듈이 없다
- 중복: 측정 못함 — 명령 절과 ADR-024가 중복 검사 도구를 두지 않는다고 정했다
- 정적 분석: `python3 -m py_compile tests/test_skill_rules.py` → 오류 없음(`pyflakes`, `pycodestyle`, `flake8`, `mypy`, `pylint`는 이 환경에 없다)
- 보안 검사: 측정 못함 — 명령 절과 ADR-024가 보안 검사 도구를 두지 않는다고 정했다(의존성 목록도 없다)

**완료 조건**
- 1. run의 이슈 넷(#46, #47, #48, #51)이 고쳐졌다
  - `plugins/plate/skills/run/SKILL.md`의 "8. 고칠 phase를 더한다"(고칠 파일이 시각·본문 해시로 보는 파일인데 다시 참으로 둘 길이 없으면 "멈춘다", #46. 계획 커밋 찾기를 두 단계로, #47), "멈춘다"(#46의 계획이 틀림 갈래, 4의 "계획 수정마다 결정 줄 하나다"와 커밋 전 결정 줄 보기, #48), 낱말의 "작업 트리의 스킬 줄"(merge-base 해시를 먼저 얻고 `git diff --name-only {해시} HEAD`를 따로 부른다, #47)과 "표지 줄", 맡기는 글 다섯(4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다")을 읽었다 → 다섯 코드 블록 모두 `부른 쪽: plate:run`으로 끝나고 네 이슈의 해결이 저마다 적혀 있다. 통과
  - `grep -n 'git[^`]*\$(' plugins/plate/skills/run/SKILL.md` → 출력 없음(종료 코드 1). 통과
- 2. plan의 이슈 셋(#46, #52, #53)이 고쳐졌다
  - `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"(돌려 보는 확인마다 차림·관찰할 기대·결정과 TODO의 멈출 자리를 본다, #53), 적는 규칙 "조건"(본문 해시 `git hash-object`와 `git rev-parse HEAD:<경로>`로 견준다, #46), "phase의 파일"의 읽을 것(이슈 번호만이 아니라 경로·절 이름·바뀐 글, #52)을 읽었다 → 셋 모두 적혀 있다. 통과
- 3. retro, eval과 다섯 스킬의 이슈 셋(#49, #50, #51)이 고쳐졌다
  - `plugins/plate/skills/retro/SKILL.md` 5번 "문제"(`남은 것:` 줄은 회고가 "문제"로 판정한 것만, #49)와 "멈춤"(`권한`, #50), `plugins/plate/skills/eval/SKILL.md` 낱말 "정해 둔 물음"(`권한`)과 3번 규칙 준수 표(`NNN-slug: RUNLOG`, `<tasks 이름>: RUNLOG` 행, run, `RUNLOG.md`와 사용량 까닭을 적은 `docs/TOOLS.md`, #50), phase 6번·check 8번·retro 9번·review 9번·eval 8번의 끝 보고(표지 줄도 작업 트리의 스킬 줄도 없을 때만 직접 부른 꼴, #51)를 읽었다 → 모두 적혀 있다. 통과
  - `docs/TOOLS.md`의 "고친 retro·eval·phase를 장면 R·E·P1·P2로 돌려 본 것"을 읽었다 → 네 장면 모두 Claude Code 2.1.311, 돌린 시각, 세션 id(R `30311367-…`, E `7962db1f-…`, P1 `e9132b71-…`, P2 `a2104649-…`), 대상 본문 해시, 기대한 결과, 본 결과가 있고 본 결과가 "기대와 같다". 통과
  - `git rev-parse HEAD:plugins/plate/skills/{retro,eval,phase}/SKILL.md` → retro `f1d13ac4…`, eval `9414c9dc…`, phase `69385efa…`. 장면 절의 해시와 모두 같다. 통과
- 4. 고친 규칙마다 글이 빠지면 실패하는 테스트가 있고 모든 테스트가 통과한다
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
  - `mktemp -d`에 `git archive HEAD`를 풀고 run 본문의 첫 `부른 쪽: plate:run` 줄(4번의 맡기는 글)을 지우고 돌림 → `FAILED (failures=1)`. 다시 풀어 retro 5번의 #49 해결 글("다만 확인 절 … 갈린다.")을 지우고 돌림 → `FAILED (failures=1)`. 통과
- 5. 버전 0.18.0, 마켓플레이스 유효, 맥락 문서·README가 바뀐 동작과 어긋나지 않는다
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.18.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `docs/PRD.md`의 7(해시로 보는 파일을 고칠 때의 멈춤, 계획 수정의 결정 줄), `docs/ARCHITECTURE.md`의 "패턴과 규칙" 맡기는 글 문단(표지 줄, 다섯 스킬의 가름, 두 단계 git)과 run 문단(#46, #47, #48), 디렉터리 구조의 `test_skill_rules.py` 줄(시험하는 규칙 목록이 이번 테스트와 맞다), `README.md`의 `run` 행(해시로 보는 파일의 멈춤)을 따로 읽었다 → 어긋나는 줄 없음. 통과

**범주**
- 신뢰성
  - 근거: run의 8번·"멈춘다"·낱말 두 줄·맡기는 글 다섯, plan 6번과 적는 규칙 두 줄, retro 5번·9번, eval 낱말·3번 표·8번, phase 6번, check 8번, review 9번의 새 줄을 앞뒤 절과 대어 읽었다. 표지 줄이 코드 블록의 마지막 줄이고 작업 트리의 스킬 줄은 그 뒤에 붙는다는 run 낱말(`plugins/plate/skills/run/SKILL.md:48`)과 다섯 스킬의 가름 글이 맞물리고, 4번의 `고칠 문제:` 줄을 빼도 표지 줄은 남는다. retro #49 글은 eval 2번의 `남은 것:` 셈과 같다. 어긋나는 흐름을 찾지 못했다
  - 근거: 스킬 description은 모두 1024자 안이다(가장 긴 run이 988자, 지난 평가의 1142자에서 줄었다). 161개 테스트가 모두 통과했다
  - 등급: A — 문제 0개
- 보안
  - 핫스팟: `plugins/plate/skills/run/SKILL.md:47` `git merge-base {기본 브랜치} HEAD`로 얻은 해시를 `git diff --name-only {해시} HEAD`에 넣게 한다 → 안전(해시와 기본 브랜치 이름은 git이 낸 값이고 밖의 입력이 들지 않는다)
  - 핫스팟: `plugins/plate/skills/run/SKILL.md:186` `git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md`로 얻은 해시를 `git log --format='%h %s' {해시}..HEAD -- docs/tasks/`에 넣게 한다 → 안전(경로는 계획의 task 폴더 이름, 해시는 git이 낸 값)
  - 근거: `tests/test_skill_rules.py`의 새 줄은 저장소 안의 고정 경로만 읽고 셸을 부르지 않는다. 매니페스트는 버전 줄만 바뀌었다. 스킬 본문의 새 줄에 비밀, 권한 건너뛰기, 밖의 입력을 쓰는 명령이 없고, 명령 치환을 없앤 것은 오히려 셸 해석 면을 줄였다. 문제 없음
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: `tests/test_skill_rules.py:296` `RetroRulesTest.test_49_stop_list_includes_permission`은 retro 5번 "멈춤"의 `권한`을 보는데, tasks 머리 완료 조건 3은 이 규칙을 #50의 해결로 적었다. 파일이 이슈 번호로 테스트를 묶는 꼴(모듈 docstring `:3`~`:5`)인데 이 테스트는 #49로 이름 붙고, docstring의 retro 목록도 `#49·#51`이라 #50이 빠진다. #50의 시험을 이슈 번호로 찾으면 이 테스트가 보이지 않는다 (이름, 2분)
  - 근거: 테스트의 새 줄은 기존 꼴(`section`, `part`, `subsection` 도우미, `subTest`, `unittest`)을 그대로 쓴다. 다섯 스킬의 끝 보고에 같은 가름 글이 되풀이되는 것은 tasks 머리의 결정(#51은 다섯 스킬을 모두 고친다)이 정한 것이라 문제로 적지 않는다
  - 부채 비율: 2분 ÷ (118줄 × 30분) = 0.06%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: 커버리지는 측정 못함이라 판단만으로 매긴다
  - 근거: `tests/test_skill_rules.py:192`~`:222` run #46·#47·#48·#51(맡기는 글 다섯의 마지막 줄, `고칠 문제:` 줄 글, 낱말 "표지 줄"), `:247`~`:260` plan #46·#52·#53, `:269`~`:287` 다섯 스킬의 끝 보고 #51, `:290`~`:299` retro #49·`권한`, `:302`~`:311` eval #50의 규칙 글이 제 절에 없으면 실패한다. 완료 조건 4에서 표지 줄 하나와 retro #49 글을 지워 저마다 실패하는 것을 봤다. 매니페스트 버전은 기존 `tests/test_manifests.py`가 두 버전의 일치를 본다
  - 근거: retro·eval·phase의 고친 동작은 `docs/TOOLS.md`의 장면 R·E·P1·P2가 지금 본문과 같은 해시로 실제로 돌려 봤다. plan과 run은 tasks 머리에 `돌리지 않음`으로 두었다
  - 근거: 글 테스트가 빠진 것은 곁가지뿐이다. plan 6번 #53의 고치는 길("아니면 차림에 앞 단계를 더하고, 기대를 관찰할 결과로 고치고, 결정과 TODO를 한 멈출 자리로 맞춘다", `plugins/plate/skills/plan/SKILL.md:101`), run "멈춘다" 4의 "같은 멈춤 안에서 계획을 두 번 고치면 결정 줄도 두 번 더한다"는 시험하지 않는다
  - 등급: B — 커버리지 측정 못함이라 판단으로, 테스트가 빠진 동작이 엣지케이스뿐이다
- 기능 적합성
  - 근거: 완료 조건 1 통과: 네 이슈의 해결 글, 명령 치환 grep 출력 없음
  - 근거: 완료 조건 2 통과: 세 이슈의 해결 글
  - 근거: 완료 조건 3 통과: 세 이슈의 해결 글, 장면 R·E·P1·P2, 본문 해시 일치
  - 근거: 완료 조건 4 통과: 테스트 `OK`, 표지 줄과 #49 글을 지우면 실패
  - 근거: 완료 조건 5 통과: 두 버전 0.18.0, validate 통과, PRD·ARCHITECTURE·README에 어긋나는 줄 없음
  - 등급: A — 완료 조건의 확인이 모두 통과한다

**Sonar way 게이트**
- 새 문제 0개: 1개(유지보수성 1). 실패
- 새 보안 핫스팟 모두 검토: 2/2. 통과
- 새 줄 커버리지 80% 이상: 측정 못함(잴 새 줄 93줄). 측정 못함
- 새 줄 중복 3% 이하: 측정 못함(잴 새 줄 93줄). 측정 못함
- 게이트: 실패

**소스 문제**
1. retro 5번 "멈춤"의 `권한`을 보는 테스트가 `test_49_stop_list_includes_permission`으로 이름 붙고 모듈 docstring의 retro 목록에도 #50이 없어, tasks 머리가 #50의 해결로 적은 규칙의 시험을 이슈 번호로 찾을 수 없다 (`tests/test_skill_rules.py:296`). 범주: 유지보수성

**하네스에서 걸린 것**
- 프로젝트의 규칙을 따름: ADR-024와 명령 절이 커버리지·중복·보안 검사 도구를 찾지 않고 측정 못함으로 적으라고 해서, 2번의 도구를 찾지 않았다. 그래서 게이트의 커버리지와 중복은 늘 측정 못함이다
- 완료 조건 4의 둘째 확인은 "retro 5번의 #49 해결 글을 지운다"만 적고 지울 글의 경계를 적지 않았다. 해결 글이 줄 끝에 있어 앞 공백까지 지워야 해서, 처음 고른 글(뒤 공백 포함)이 맞지 않아 한 번 다시 골랐다
