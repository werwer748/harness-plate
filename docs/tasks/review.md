# 코드 평가

## 평가 1

**대상**
- 범위: `92f895e`(main에서 갈라진 곳)부터 `5482090`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 20개, 새 줄 661줄, 잴 새 줄 623줄
  - `plugins/plate/ci/verdict.py` +23
  - `plugins/plate/hooks/edit_guard.py` +82
  - `plugins/plate/hooks/push_guard.py` +18
  - `tests/hook_helpers.py` +74
  - `tests/test_cleanup_skill.py` +25
  - `tests/test_edit_guard.py` +139
  - `tests/test_manifests.py` +12
  - `tests/test_push_guard.py` +27
  - `tests/test_skill_rules.py` +99
  - `tests/test_verdict.py` +124
  - `plugins/plate/skills/check/SKILL.md` +1 (결과물인 마크다운)
  - `plugins/plate/skills/cleanup/SKILL.md` +4 (결과물인 마크다운)
  - `plugins/plate/skills/context/SKILL.md` +1 (결과물인 마크다운)
  - `plugins/plate/skills/eval/SKILL.md` +1 (결과물인 마크다운)
  - `plugins/plate/skills/phase/SKILL.md` +7 (결과물인 마크다운)
  - `plugins/plate/skills/plan/SKILL.md` +1 (결과물인 마크다운)
  - `plugins/plate/skills/retro/SKILL.md` +1 (결과물인 마크다운)
  - `plugins/plate/skills/review/SKILL.md` +2 (결과물인 마크다운)
  - `plugins/plate/skills/run/SKILL.md` +14 (결과물인 마크다운)
  - `plugins/plate/skills/setup/SKILL.md` +6 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 239 tests in 20.637s`, `OK`. 통과
- 커버리지: 측정 못함 — 프로젝트에 커버리지 도구가 없고(`python3 -c "import coverage"` → `ModuleNotFoundError`) ADR-024가 두지 않기로 했다
- 중복: 측정 못함 — 중복 검사 도구가 없다(ADR-024)
- 정적 분석: 측정 못함 — 타입·복잡도 검사 도구가 없다(`mypy`, `pyflakes`, `ruff`, `pylint`, `radon` 모두 없음). 참고로 `python3 -m py_compile` 바뀐 Python 파일 넷 → 오류 없음
- 보안 검사: 측정 못함 — 의존성 목록이 없고 보안 규칙 검사 도구(`bandit`, `semgrep`, `pip-audit`)가 없다(ADR-024)

**완료 조건**
- 1. 테스트 묶음이 모두 통과한다.
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
- 2. 편집 훅과 푸시 훅이 결정대로 돈다(신뢰성-1·4·5·10, 성능-5·6, 유지보수성-5).
  - `docs/tasks/001-hook-fixes/plan.md`의 완료 조건 확인을 `5482090`에서 다시 돌림(시험 레포는 `mktemp -d`로 그 꼴대로 만듦) → 1: 테스트를 바꾼 `001-a: phase 1` 커밋과 `## 확인 1` → 종료 0, `src.py`만 바꾼 커밋 → 종료 2, 확인 절 없음 → 종료 2. 2: `printf '{'` → `plate:` 줄과 `exit=2`, phase 파일에 `\xff` → `plate:` 줄(`UnicodeDecodeError`)과 종료 2, 푸시 훅 `{"git push` → `exit=2`, `{"ls` → `exit=0`. 3: 세는 파일 자리에 폴더 → `세 번째 막았다` 줄과 종료 2, `os.replace` 237행. 4: `git rm tests/test_x.py`만 → 종료 2. 5: `PATH=/nonexistent`에서 `README.md` → 종료 0, `src.py` → `FileNotFoundError: 'git'`로 종료 2, `check` 안에서 `has_uncommitted_test_change` 285행이 `has_tests` 290행보다 앞. 6: `grep -c` → `0`, 상수 확인 → `True`. 7: ARCHITECTURE 54행에 `다시 수행`·`예외`·`결과물인 마크다운`이 모두 있고, `### ADR-027` 63행 한 줄, PRD 목표(4행)와 핵심 기능 6(16행)이 "코드 파일(`.md`가 아닌 파일)"로 좁힘. 8: 1과 같음. 모두 기대대로. 통과
- 3. 판정 스크립트가 깨진 입력에서 `request`를 내고 0으로 끝나고, 액션이 SHA로 고정되고, 등급 묶음 꼴 세 곳을 테스트가 본다(신뢰성-7, 보안-4, 유지보수성-1).
  - `printf 'not json' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`. 통과
  - `grep -nE 'uses: [^ ]+@' plugins/plate/skills/setup/SKILL.md` → 352·365·399·411·415행 다섯 줄 모두 40자리 16진수와 `# v7`·`# v1`·`# v8` 주석. 덧붙여 `git ls-remote`로 본 태그(`actions/checkout` v7, `anthropics/claude-code-action` v1의 `^{}`, `actions/upload-artifact` v7, `actions/download-artifact` v8)의 해시가 줄의 SHA와 같음. 통과
- 4. run, phase, cleanup, review 본문이 발견대로 고쳐지고 PRD·ARCHITECTURE와 맞는다(신뢰성-2·3·8, 기존 작업 정합성-5·7·8, 성능-2·4).
  - `docs/tasks/003-skill-fixes/plan.md`의 완료 조건 확인을 다시 돌림 → 1: `다시 띄움: 결과 없음`이 run 293행("멈춘다")과 570행(`RUNLOG.md`)에, 두 RunRulesTest `OK`. 2: `tasks 브랜치` 89행 < `계획의 커밋` 96행. 3: `gh api user`가 376행("이슈를 올린다")과 519행("PR 본문의 꼴"), `gh api user --jq .login` → `werwer748`, `gh issue view 68 … --jq '.author.login'` → `werwer748`. 4: `test_stop_line_grep_runs_on_fake_runlog` `OK`. 5: `부모 커밋에 없` phase 59행("2. TODO를 차례로 끝낸다"), 시험 레포에서 바꾼 파일은 `git checkout <커밋>^ --`/`git checkout HEAD --`, 새 파일은 `mv`로 옮겼다 되살린 뒤 `git status --porcelain` 빈 출력. 6: review 72행 커버리지 항목에 `한 번`. 7: `맥락 문서를 모두 읽는다` 없음, `결정 절` 99행("4. 2라운드")과 190행("2라운드에 맡기는 글"). 8: `결과 없`이 PRD 17행과 ARCHITECTURE 99행, `gh api user`가 ARCHITECTURE 57행 run 문단. 9: 1과 같음. 모두 기대대로. 통과
  - 돌리지 않음 줄(run·cleanup·review를 헤드리스로 끝까지 돌리지 않는다)은 확인이 아니어서 돌리지 않음
- 5. 결과물인 마크다운을 편집 훅이 막지 않는다는 결정이 맥락 문서에 있고 PRD가 좁혀진다(기능 적합성-2).
  - `grep -n '결과물인 마크다운' docs/ADR.md docs/ARCHITECTURE.md docs/PRD.md` → ADR 63·64·66행(ADR-027), ARCHITECTURE 54행("막는 장치" 문단, "막지 않고 git을 부르기 전에 통과시키며"), PRD 4행(목표)과 16행(핵심 기능 6, "막지 않는다(ADR-027)"). 통과
- 6. 스킬 description 열 개가 400자 이하이고 테스트가 지키며, 테스트 도우미의 중복과 낡은 글이 정리된다(성능-7, 유지보수성-2·3·4·6).
  - `python3 -m unittest tests.test_skill_rules tests.test_manifests tests.test_cleanup_skill tests.test_edit_guard tests.test_push_guard` → `OK`. 통과
  - `grep -n '^def section' tests/test_cleanup_skill.py` → 아무것도 나오지 않음(종료 1). 통과
  - 덧붙여 description 길이를 직접 셈 → 184~321자, 모두 400자 이하

**범주**
- 신뢰성
  - 근거: `plugins/plate/hooks/edit_guard.py:146-150` `phase_commit_has_test_change`가 `git log` 전체 역사에서 제목이 `NNN-slug: phase N`인 커밋을 모두 본다. tasks를 비운 뒤 같은 폴더 이름(`001-setup` 같은 것)과 phase 번호를 쓰는 다음 tasks에서, 지난 tasks의 같은 제목 커밋이 테스트를 바꿨으면 이번 phase 커밋이 테스트를 바꾸지 않았어도 다시 수행의 구현 편집을 통과시킨다. 갈라진 곳 뒤의 커밋으로 좁히지 않았다 (기능, 낮음)
  - 근거: `plugins/plate/skills/phase/SKILL.md:59` 새로 만든 구현 파일이 둘 이상이면 파일마다 `tmp=$(mktemp -d)`를 다시 잡아 앞 파일의 임시 자리를 잃거나, 한 자리에 모으면 같은 이름(`pkg/a/__init__.py`, `pkg/b/__init__.py`)이 서로 덮인다. 되살리는 명령이 그 파일을 찾지 못하고, 본문은 `git status --porcelain`이 다르면 무엇을 할지(`git checkout HEAD -- <파일>`로 되살린다) 적지 않는다. 커밋돼 있어 잃지는 않는다 (기능, 낮음)
  - 근거: 그 밖의 새 줄(`verdict.py`의 `decide`, `push_guard.py`의 예외 갈래, `edit_guard.py`의 `.md` 앞 통과·삭제 항목 거름·`write_counts`·`has_check_section`, run의 결과 없는 에이전트 셈과 1번의 차례, cleanup·review의 고친 줄)을 읽고 완료 조건 2·4의 시험 레포 확인으로 돌려 틀린 동작을 찾지 못함. `decide`가 `--changed-files`를 읽지 못하면 `close`도 `request`로 내리는 것은 ARCHITECTURE 58행과 002 task 머리의 결정이 정한 것이라 문제로 적지 않음
  - 등급: B — 가장 무거운 문제가 낮음
- 보안
  - 핫스팟: `plugins/plate/hooks/edit_guard.py:52` `git`을 `subprocess.run`의 인자 목록으로 부른다(셸 없음) → 안전
  - 핫스팟: `plugins/plate/hooks/edit_guard.py:234-237` git 폴더 안에 `mkstemp`로 임시 파일을 만들고 `os.replace`로 바꿔 넣는다 → 안전(`mkstemp`가 0600으로 새로 만들고, 같은 폴더라 바꿔 넣기가 원자적이다)
  - 핫스팟: `plugins/plate/hooks/push_guard.py:364-367` 깨진 stdin에서 바이트에 `push`가 있으면 막는다 → 안전(해석하지 못한 입력을 막는 쪽으로 다룬다)
  - 핫스팟: `plugins/plate/ci/verdict.py:70,78` stdin과 `--changed-files`의 경로를 연다 → 안전(워크플로가 넘긴 경로이고, 읽지 못하면 머지 요청으로 간다)
  - 핫스팟: `plugins/plate/skills/setup/SKILL.md:352,365,399,411,415` 워크플로 액션을 커밋 SHA로 고정 → 안전(태그를 옮겨 바뀐 코드를 돌리는 길을 닫는다. `git ls-remote`로 SHA를 맞춰 봄)
  - 핫스팟: `plugins/plate/skills/run/SKILL.md:376` 이슈의 "이미 있음"을 `gh api user`의 login이 쓴 글로 좁힌다 → 안전(밖의 댓글이 올림을 막는 길을 닫는다. login을 얻지 못하면 이미 있지 않은 것으로 본다)
  - 핫스팟: `plugins/plate/skills/phase/SKILL.md:58-59` 셸로 구현 파일을 되돌리고 옮긴다 → 안전(저장소 안의 파일을 에이전트가 돌리고, 밖의 입력이 들지 않는다)
  - 근거: 취약점 없음. 보안 검사는 측정 못함
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: `plugins/plate/hooks/edit_guard.py:30,45` `STOP_COUNT = 3`을 상수로 두었지만 `STOP`의 글이 "세 번째 막았다"를 손으로 적어, 상수를 바꾸면 글이 어긋난다. 같은 phase에서 `TEST_FIRST`를 상수에서 만들도록 고친 것(유지보수성-5)과 일관되지 않다 (일관성, 5분)
  - 근거: 그 밖에 `tests/hook_helpers.py`로 모은 도우미, `test_verdict.py`의 꼴 견주기, 훅의 새 함수 이름·docstring을 ARCHITECTURE의 디렉터리 구조와 주변 코드에 대어 읽어 문제를 찾지 못함
  - 부채 비율: 5분 ÷ (661줄 × 30분) = 0.03%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: 기본 등급표로 매김 — 테스트 파일이 아닌 실행 코드(`edit_guard.py`, `push_guard.py`, `verdict.py`)가 바뀌었다. 커버리지는 측정 못함이라 판단만으로 매김
  - 근거: `tests/test_edit_guard.py`의 `RerunTest`(다시 수행 통과·막음, 다른 phase 커밋, 확인 절 없음, 코드 블록 안 확인 절), `ExceptionTest`(깨진 stdin, UTF-8 아닌 phase 파일), 세는 파일의 폴더·읽기 전용 시험, `test_deleted_test_file_only_does_not_count`, `test_md_file_passes_without_git`, `test_message_names_test_file_rules`가 바뀐 동작마다 있고, 코드를 되돌리면 실패하는 단언이다
  - 근거: `tests/test_push_guard.py`의 `ExceptionTest`가 `push` 유무 두 갈래를, `tests/test_verdict.py`의 `UnreadableInputTest`가 깨진·객체 아닌·빈 입력과 없는 목록 파일을, `BundleShapeTest`가 세 곳의 꼴을 본다
  - 근거: `plugins/plate/hooks/edit_guard.py:153-154` phase 커밋에서 테스트 파일을 지우기만 한 경우(`--diff-filter=d`)를 보는 시험이 없다. `RerunTest`는 바이트코드와 `.md`만 본다(엣지케이스)
  - 근거: run·cleanup·review 본문의 바뀐 동작은 `tests/test_skill_rules.py`의 글 검사(`test_no_result_relaunch_limit` 등)와 tasks 머리 완료 조건 4의 `돌리지 않음` 줄뿐이고, phase 본문의 새 파일 갈래는 완료 조건 확인으로만 돌렸다(엣지케이스인 여러 새 파일은 돌리지 않음)
  - 등급: B — 테스트가 빠진 동작이 엣지케이스뿐이다(커버리지 측정 못함)
- 기능 적합성
  - 근거: 완료 조건 1 통과: 테스트 묶음 `OK`
  - 근거: 완료 조건 2 통과: 001의 완료 조건 확인을 마지막 커밋에서 다시 돌려 모두 기대대로
  - 근거: 완료 조건 3 통과: 판정 스크립트 `request`·`exit=0`, 액션 SHA 고정
  - 근거: 완료 조건 4 통과: 003의 완료 조건 확인을 다시 돌려 모두 기대대로
  - 근거: 완료 조건 5 통과: ADR-027, ARCHITECTURE 54행, PRD 4·16행
  - 근거: 완료 조건 6 통과: 테스트 다섯 모듈 `OK`, `def section` 없음
  - 등급: A — 완료 조건의 확인이 모두 통과한다

**Sonar way 게이트**
- 새 문제 0개: 3개. 실패
- 새 보안 핫스팟 모두 검토: 7/7. 통과
- 새 줄 커버리지 80% 이상: 측정 못함(잴 새 줄 623줄). 측정 못함
- 새 줄 중복 3% 이하: 측정 못함(잴 새 줄 623줄). 측정 못함
- 게이트: 실패

**소스 문제**
1. 다시 수행의 테스트 셈이 전체 역사에서 같은 제목의 커밋을 찾아, 지난 tasks의 같은 이름 phase 커밋이 테스트를 바꿨으면 이번 phase가 테스트를 바꾸지 않았어도 구현 편집을 통과시킨다. 갈라진 곳 뒤나 이 tasks의 계획 커밋 뒤의 커밋으로 좁혀야 한다 (`plugins/plate/hooks/edit_guard.py:146-150`). 범주: 신뢰성
2. phase 본문의 새 구현 파일 옮기기가 파일이 여럿일 때 임시 자리를 잃거나 같은 이름끼리 덮이고, `git status --porcelain`이 다를 때 되살리는 법을 적지 않는다 (`plugins/plate/skills/phase/SKILL.md:59`). 범주: 신뢰성
3. `STOP`의 글이 "세 번째"를 손으로 적어 `STOP_COUNT`와 따로 논다 (`plugins/plate/hooks/edit_guard.py:30,45`). 범주: 유지보수성
4. phase 커밋에서 테스트 파일을 지우기만 한 경우를 다시 수행의 셈에서 빼는지 보는 시험이 없다 (`plugins/plate/hooks/edit_guard.py:153-154`, `tests/test_edit_guard.py`). 범주: 테스트 적절성

**하네스에서 걸린 것**
- 명령 절의 "커버리지, 중복, 보안 검사: 없음"(ADR-024) 때문에 게이트의 커버리지와 중복이 측정 못함이고, 테스트 적절성은 판단으로만 매겼다.
- tasks 머리 완료 조건 2·4의 확인이 다른 task 머리의 완료 조건을 가리켜(`docs/tasks/001-hook-fixes/plan.md`, `docs/tasks/003-skill-fixes/plan.md`), 그 확인을 돌리려고 그 두 task 머리를 읽었다(1번이 읽게 한 파일이라 기록을 읽은 것은 아니다).
