# Phase 3: 워크플로 양식의 액션을 커밋 SHA로 고정한다

**목표**: 보안-4가 고쳐져, CI 워크플로 양식의 액션이 모두 커밋 SHA로 고정된다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)만 고친다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (보안-4의 근거, 좁힌 범위, 2라운드 판정)
- `plugins/plate/skills/setup/SKILL.md`의 CI 워크플로 양식 (`uses:` 줄 넷)
- `docs/ADR.md`의 ADR-021·022 (plate를 기본 브랜치에서 받는 것은 감수)

**TODO**
- [x] 양식의 `uses:` 줄마다 지금 태그가 가리키는 커밋을 `git ls-remote`로 얻어, `@` 뒤를 40자리 SHA로 바꾸고 줄 끝에 `# {태그}`를 붙인다. 태그 이름과 그 밖의 줄은 그대로다 (`plugins/plate/skills/setup/SKILL.md`)
- [x] `tests/`에서 바뀐 `uses:` 줄의 옛 글(`@v7`, `@v1`, `@v8`)을 찾아(`git grep -n -e '@v7' -e '@v1' -e '@v8' -- tests/`), 걸리는 테스트가 있으면 새 글을 지키게 고친다 (`tests/`)

**통과 조건**
- 모든 `uses:` 줄이 SHA로 고정된다(완료 조건 3).
  - 확인: `grep -nE 'uses: ' plugins/plate/skills/setup/SKILL.md` → 모든 줄이 `uses: <소유자>/<이름>@<40자리 16진수> # v<수>` 꼴
  - 확인: 그 줄마다 `git ls-remote https://github.com/<소유자>/<이름> 'refs/tags/<태그>' 'refs/tags/<태그>^{}'`를 돌려, `^{}` 줄이 있으면 그 해시, 없으면 태그 줄의 해시가 줄의 SHA와 같다
- 앞 phase의 동작이 그대로다(완료 조건 1·2).
  - 확인: `python3 -m unittest tests.test_verdict -v` → `OK`
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- 양식의 `uses:` 줄마다 지금 태그가 가리키는 커밋을 `git ls-remote`로 얻어, `@` 뒤를 40자리 SHA로 바꾸고 줄 끝에 `# {태그}`를 붙인다: 다섯 줄을 바꿨다. `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7`(352, 411행), `anthropics/claude-code-action@d70510b174a1244958df0b03166a54912811f3e6 # v1`(365행, 주석 태그라 `^{}`의 커밋 해시), `actions/upload-artifact@cf430e030ddbb5b0abf93d22962f4752f3646cd9 # v7`(399행), `actions/download-artifact@9000827ccba6bdab643e8b6fd33ac0654aef8333 # v8`(415행). 들여쓰기와 그 밖의 줄은 그대로다 (`plugins/plate/skills/setup/SKILL.md`)
- `tests/`에서 바뀐 `uses:` 줄의 옛 글을 찾아 걸리는 테스트를 고친다: `git grep -n -e '@v7' -e '@v1' -e '@v8' -- tests/` → 출력 없음. 걸리는 테스트가 없어 고친 것이 없다 (`tests/`)

## 확인 결과
- 모든 `uses:` 줄이 SHA로 고정된다(완료 조건 3).
  - `grep -nE 'uses: ' plugins/plate/skills/setup/SKILL.md` → 352, 365, 399, 411, 415행 다섯 줄이 모두 `uses: <소유자>/<이름>@<40자리 16진수> # v<수>` 꼴. `grep -vcE 'uses: [^/ ]+/[^@ ]+@[0-9a-f]{40} # v[0-9]+$'`로 어긋난 줄 수를 세어 `0`. 통과
  - `git ls-remote https://github.com/actions/checkout 'refs/tags/v7' 'refs/tags/v7^{}'` → `3d3c42e5aac5ba805825da76410c181273ba90b1 refs/tags/v7`(`^{}` 줄 없음), 줄의 SHA와 같다. `anthropics/claude-code-action` v1 → `^{}` 줄 `d70510b174a1244958df0b03166a54912811f3e6`, 같다. `actions/upload-artifact` v7 → `cf430e030ddbb5b0abf93d22962f4752f3646cd9`(`^{}` 없음), 같다. `actions/download-artifact` v8 → `9000827ccba6bdab643e8b6fd33ac0654aef8333`(`^{}` 없음), 같다. 통과
- 앞 phase의 동작이 그대로다(완료 조건 1·2).
  - `python3 -m unittest tests.test_verdict -v` → `Ran 24 tests`, `OK`. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 229 tests in 20.502s`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- 읽을 것은 `uses:` 줄을 넷으로 적었으나 실제로는 다섯 줄이다(`actions/checkout`이 352행과 411행에 두 번). 다섯 줄을 모두 바꿨다.

## 남은 것
- SHA는 오늘(2026-10-29) 태그가 가리키는 커밋으로 고정했다. 액션의 새 판을 받으려면 SHA를 손으로 바꿔야 하고, 그것을 알리거나 갱신하는 장치(Dependabot 같은 것)는 두지 않았다(범위 밖).
- 이미 셋업을 마친 대상 프로젝트의 `.github/workflows/plate-review.yml`은 바뀌지 않는다. 양식만 고쳤다.
- 워크플로를 GitHub Actions에서 돌려 보지 않았다(task 머리의 범위 밖).

## 하네스에서 걸린 것
- 읽을 것의 "`uses:` 줄 넷"이 실제 다섯 줄과 달랐다(같은 액션이 두 잡에 있다).

## 확인 1

**통과 조건**
- 모든 `uses:` 줄이 SHA로 고정된다(완료 조건 3).
  - `grep -nE 'uses: ' plugins/plate/skills/setup/SKILL.md` → 352, 365, 399, 411, 415행 다섯 줄이 모두 `uses: <소유자>/<이름>@<40자리 16진수> # v<수>` 꼴(`grep -vcE 'uses: [^/ ]+/[^@ ]+@[0-9a-f]{40} # v[0-9]+$'`로 센 어긋난 줄 `0`). 통과
  - `git ls-remote https://github.com/actions/checkout 'refs/tags/v7' 'refs/tags/v7^{}'` → `3d3c42e5aac5ba805825da76410c181273ba90b1`(`^{}` 줄 없음), 352·411행과 같다. `anthropics/claude-code-action` v1 → `^{}` 줄 `d70510b174a1244958df0b03166a54912811f3e6`, 365행과 같다. `actions/upload-artifact` v7 → `cf430e030ddbb5b0abf93d22962f4752f3646cd9`, 399행과 같다. `actions/download-artifact` v8 → `9000827ccba6bdab643e8b6fd33ac0654aef8333`, 415행과 같다. 통과
- 앞 phase의 동작이 그대로다(완료 조건 1·2).
  - `python3 -m unittest tests.test_verdict -v` → `Ran 24 tests`, `OK`. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 229 tests`, 마지막 줄 `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 229 tests`, `OK`. 통과

**남은 것**
- 워크플로를 GitHub Actions에서 돌려 보지 않았다(task 머리의 범위 밖). → 통과 조건은 `uses:` 줄의 꼴과 SHA·태그의 일치만 보고 워크플로의 실행 동작은 보지 않아 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 워크플로를 GitHub Actions에서 돌려 보지 않았다(task 머리의 범위 밖이고, 완료 조건에 `돌리지 않음` 줄은 없다).

**판정**: 통과
