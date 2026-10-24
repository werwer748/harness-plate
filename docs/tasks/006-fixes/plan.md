# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리고 plate 저장소에서 고친다

## 완료 조건
1. `scan`의 인지 복잡도가 어림 67로 기준 15를 넘어, 셸 꼴 하나를 고칠 때 다른 꼴을 깨뜨리기 쉽다 (`plugins/plate/hooks/push_guard.py:62`)
   - 확인: `plugins/plate/hooks/push_guard.py`의 `scan`과 거기서 나눈 함수를 다시 읽어 Sonar의 셈법으로 센 인지 복잡도가 함수마다 15 이하이고, `python3 -m unittest discover -s tests`가 통과한다
2. `push_args`의 인지 복잡도가 어림 24로 기준 15를 넘는다 (`plugins/plate/hooks/push_guard.py:168`)
   - 확인: `plugins/plate/hooks/push_guard.py`의 `push_args`와 거기서 나눈 함수를 다시 읽어 Sonar의 셈법으로 센 인지 복잡도가 함수마다 15 이하이고, `python3 -m unittest discover -s tests`가 통과한다
3. 푸시 훅의 옵션과 설정을 읽는 가지 일곱 곳(따옴표 밖 이스케이프, 환경 변수 앞붙임, `git -c` 같은 git 옵션, `--`, `-o`·`--repo` 같은 push 옵션, 짧은 옵션 묶음의 `-o`, 설정의 원격)에 시험이 없어 깨져도 알 수 없다 (`plugins/plate/hooks/push_guard.py:71`)
   - 확인: `tests/test_push_guard.py`를 읽어 일곱 가지마다 그 가지를 지나는 시험이 있고, `python3 -m unittest discover -s tests`가 통과한다
4. 완료 조건 1의 셋째 확인 `diff -r <복사본> plugins/plate`가 `.gitignore`에 걸린 `__pycache__`를 다른 것으로 내어 실패한다. 추적되는 파일은 같다 (`plugins/plate/hooks/__pycache__`)
   - 확인: `python3 -m unittest discover -s tests`를 돌린 뒤 시험 저장소의 기본 브랜치를 새로 받아, 그 안의 plate 복사본을 `git archive 72dcfcf plugins/plate | tar -x -C <임시 폴더>`로 꺼낸 tasks 끝의 plate와 `diff -r -x __pycache__ <복사본> <임시 폴더>/plugins/plate`로 견주면 아무것도 나오지 않는다
5. 두 매니페스트의 `description`이 0.11.0의 푸시 훅과 CI(review의 PR 모드, 판정 스크립트)를 적지 않는다 (`plugins/plate/.claude-plugin/plugin.json:4`, `plugins/plate/.codex-plugin/plugin.json:4`)
   - 확인: 두 파일의 `description`을 읽어 푸시 훅과 CI(review의 PR 모드, 판정 스크립트)가 적혀 있다
6. 띄운 에이전트에 실린 plate 스킬 본문이 tasks가 고친 저장소의 본문을 따라오지 않는다. 세션에 실린 plate 스킬 본문은 세션을 띄울 때의 것이라 같은 세션에서 띄운 에이전트에는 tasks가 고치기 전의 본문이 실린다는 사실을 적고, 스킬의 절차를 바꾸는 tasks는 그 절차에 기대는 다음 단계를 새 세션에서 이어 간다고 적는다 (`docs/TOOLS.md`)
   - 확인: `docs/TOOLS.md`를 읽어 그 사실과 새 세션에서 이어 간다는 것이 적혀 있다
7. 복사본과 견주는 `diff -r`가 git이 무시하는 `__pycache__`를 다른 것으로 낸다. 테스트와 `--plugin-dir` 세션의 훅이 `plugins/plate/hooks/__pycache__`를 만든다는 것을 적고, `plugins/plate`를 복사본과 견주는 확인은 `diff -r -x __pycache__`로 쓴다 (`docs/ARCHITECTURE.md`)
   - 확인: `docs/ARCHITECTURE.md`를 읽어 그것이 적혀 있다
8. 시험 폴더의 run 허용 목록에 푸시가 없다. run의 허용 목록에 `Bash(git push:*)`를 넣어 장면마다 `RUN_ALLOW`로 더하지 않게 한다 (`~/plate-rail-test/bin/run.sh`)
   - 확인: `~/plate-rail-test/bin/run.sh`를 읽어 run의 허용 목록에 `Bash(git push:*)`가 있다
9. tasks 완료 조건 1, 2, 3, 4, 5, 6이 참이다.
   - 확인: `python3 -m unittest discover -s tests`가 통과하고, 그 가운데 판정 스크립트의 테스트가 세 규칙의 경계를 본다
   - 확인: `docs/tasks/005-publish-verify/done-phase-3.md`의 기록에 적힌 세 장면의 PR마다 `gh pr view <번호> -R werwer748/plate-ci-test --json state,comments`가 자동 머지 장면은 `MERGED`, 머지 요청 장면은 `OPEN`, 닫기 장면은 `CLOSED`를 내고, 셋 모두 평가서 댓글이 있다
   - 확인: 시험 저장소의 기본 브랜치를 새로 받아 그 안의 plate 복사본을 `git archive 72dcfcf plugins/plate | tar -x -C <임시 폴더>`로 꺼낸 tasks 끝의 plate와 `diff -r -x __pycache__ <복사본> <임시 폴더>/plugins/plate`로 견주면 아무것도 나오지 않는다
   - 확인: `docs/tasks/005-publish-verify/`의 `done-phase-2.md`, `done-phase-3.md`, `done-phase-4.md`에 적힌 run 장면의 실행 기록마다 PR을 열지(원격 없는 장면은 합칠지) 묻는 글이 있고, 기록마다 `test <기록> -nt plugins/plate/skills/run/SKILL.md`가 참이다
   - 확인: 그 기록에 적힌 run 장면의 PR마다 `gh pr view <번호> -R werwer748/plate-ci-test --json headRefName,baseRefName,comments`의 머리 브랜치가 `tasks/`로 시작하고 기준 브랜치가 `main`이며, CI 워크플로가 없던 장면의 PR에는 평가서 댓글이 있다
   - 확인: 원격 없는 장면의 시험 폴더에서 `git log --format=%s main`에 그 tasks의 `<이름>: 비움` 커밋이 있다
   - 확인: `python3 -m unittest discover -s tests`가 통과하고, 그 가운데 푸시 훅의 테스트가 이 경우들을 본다
   - 확인: `docs/tasks/005-publish-verify/done-phase-4.md`에 적힌 푸시 훅 장면의 실행 기록에 기본 브랜치로의 `git push`가 훅에 막힌 결과(`is_error`가 `true`)가 있고, `test <기록> -nt <푸시 훅 스크립트>`가 참이다
   - 확인: `docs/tasks/005-publish-verify/done-phase-2.md`에 적힌 setup 장면의 실행 기록에 그 물음과 시크릿 등록 안내가 있고, 그 시험 폴더에 워크플로 파일이 있으며, `test <기록> -nt plugins/plate/skills/setup/SKILL.md`가 참이다
   - 확인: `gh repo view werwer748/harness-plate --json visibility -q .visibility`가 `PUBLIC`
   - 확인: `GIT_TERMINAL_PROMPT=0 git -c credential.helper= ls-remote https://github.com/werwer748/harness-plate.git HEAD`가 자격 증명 없이 해시 한 줄을 낸다
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.11.0`
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `README.md`를 읽어 PR, CI 판정, 푸시 훅, 명령 절의 설치 줄, 공개 저장소가 적혀 있고, 옛 동작(GitHub 원격이 있어도 로컬로 합친다, 비공개 저장소)이 남지 않았다

## 결정
- 시험 저장소의 plate 복사본은 tasks 끝 커밋 `72dcfcf`의 `plugins/plate`와 `diff -r -x __pycache__`로 견주고, 소스 문제 4는 코드가 아니라 이 견주는 법과 완료 조건 7의 문서로 고친다. 푸시 훅을 고치면 푸시 훅 장면을 다시 돌린다. 이유: 이 task가 `plugins/plate`를 고치면 시험 저장소의 복사본과 달라지는데, 복사본은 CI 장면이 그때의 plate로 돌았는지를 보는 것이라 새로 올릴 까닭이 없고 phase는 푸시하지 않는다. 완료 조건 4와 7이 같은 문제를 코드와 문서의 다른 길로 고치라고 해 맞물리지 않았다.
