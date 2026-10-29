# 회고

## 회고 1

**확인**
- 1. 판정 스크립트는 stdin을 JSON 객체로 읽지 못하거나 `--changed-files`의 파일을 읽지 못하면 `request`를 내고 0으로 끝나며, docstring과 ARCHITECTURE가 그것을 적는다(신뢰성-7).
  - `printf 'not json' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`. 통과
  - `printf '[]' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`. 통과
  - `printf '{"build":"pass","lint":"none","test":"pass","coverage":"skipped","reliability":"A","security":"A","maintainability":"A"}' | python3 plugins/plate/ci/verdict.py --changed-files /nonexistent; echo "exit=$?"` → `request`, `exit=0`. 통과
  - `grep -n '읽지 못하면' plugins/plate/ci/verdict.py docs/ARCHITECTURE.md` → `verdict.py:21`, `verdict.py:22`, `ARCHITECTURE.md:57`. 두 파일에 저마다 한 줄 이상. 통과
- 2. 등급 묶음의 꼴이 setup 양식의 `--json-schema`, review의 PR 모드 절의 표, 판정 스크립트의 `COMMANDS`·`GRADES`에서 같은지 테스트가 보고, 한 곳이 어긋나면 실패한다(유지보수성-1).
  - `python3 -m unittest tests.test_verdict.BundleShapeTest -v` → `Ran 3 tests`, `OK`. 통과
  - 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고, 사본의 `plugins/plate/skills/setup/SKILL.md`에서 그 글(한 번 나옴을 assert로 봄)을 `"maintainability":{"type":"string","enum":["A","B","C","D","E"]}`로 바꿔 사본에서 `python3 -m unittest tests.test_verdict.BundleShapeTest` → `FAILED (failures=2)`. 통과
- 3. setup의 CI 워크플로 양식의 `uses:` 줄이 모두 40자리 커밋 SHA로 고정되고 줄 끝에 태그를 적으며, 그 SHA가 그 태그가 가리키는 커밋이다(보안-4).
  - `grep -nE 'uses: ' plugins/plate/skills/setup/SKILL.md` → 352, 365, 399, 411, 415행 다섯 줄. `grep -vcE 'uses: [^/ ]+/[^@ ]+@[0-9a-f]{40} # v[0-9]+$'`로 센 어긋난 줄 `0`. 통과
  - `git ls-remote https://github.com/actions/checkout 'refs/tags/v7' 'refs/tags/v7^{}'` → `3d3c42e5aac5ba805825da76410c181273ba90b1`(`^{}` 없음), 352·411행과 같다. `anthropics/claude-code-action` v1 → `^{}` 줄 `d70510b174a1244958df0b03166a54912811f3e6`, 365행과 같다. `actions/upload-artifact` v7 → `cf430e030ddbb5b0abf93d22962f4752f3646cd9`, 399행과 같다. `actions/download-artifact` v8 → `9000827ccba6bdab643e8b6fd33ac0654aef8333`, 415행과 같다. 통과
- 4. 테스트 묶음이 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 229 tests`, 마지막 줄 `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 229 tests in 19.578s`, `OK`. 통과
- 테스트 먼저 기록: phase 1
  - `done-phase-1.md`의 "한 일"의 테스트 먼저 → 실패 출력(`python3 -m unittest tests.test_verdict.UnreadableInputTest` → `FAILED (failures=7)`)이 먼저, 통과 출력(`python3 -m unittest tests.test_verdict -v` → `Ran 21 tests`, `OK`)이 그 뒤에 있다. 통과

**남은 것**
- phase 1: `--changed-files`의 파일을 읽지 못하면 묶음의 판정이 `close`여도 `request`를 낸다 → 문제 아님 (완료 조건 1과 tasks 머리의 결정(읽지 못한 입력은 머지 요청, fail-closed)대로이고 ARCHITECTURE 57행도 그렇게 적는다. `build: fail` 묶음으로 돌려 `request`를 확인했고, 머지는 일어나지 않는다)
- phase 1: 묶음이 객체이면 키의 값 꼴은 검사하지 않는다 → 문제 아님 (`{}`, `{"build":[1],"coverage":{}}`를 넣어 돌려 예외 없이 `request`, `exit=0`. `verdict`가 `get`과 값 비교만 해 머지로 새지 않는다)
- phase 2: 값의 열거는 테스트 안의 상수와 견주고, `verdict.py`의 docstring의 값과 `verdict()` 안의 비교 글자는 견주지 않는다 → 문제 아님 (완료 조건 2가 정한 세 곳(setup 양식, review 표, `COMMANDS`·`GRADES`)은 모두 견준다)
- phase 2: `review_shape`가 표의 적는 꼴에 기대어, 꼴이 같아도 표의 글이 바뀌면 테스트가 실패할 수 있다 → 문제 아님 (틀린 통과가 아니라 지나친 실패의 위험이고, 지금 꼴에서 통과와 어긋남에서의 실패를 직접 돌려 봤다)
- phase 3: SHA를 오늘 태그의 커밋으로 고정해 새 판을 받으려면 손으로 바꿔야 하고 갱신 장치는 두지 않았다 → 문제 아님 (task 머리의 결정은 "동작을 바꾸지 않고 고정만 한다"이다)
- phase 3: 이미 셋업을 마친 대상 프로젝트의 워크플로는 바뀌지 않는다 → 문제 아님 (완료 조건 3과 목표는 setup의 양식만 정한다)
- phase 3: 워크플로를 GitHub Actions에서 돌려 보지 않았다 → 문제 아님 (task 머리의 범위 밖)

**문제**
없음

**판정**: 통과
