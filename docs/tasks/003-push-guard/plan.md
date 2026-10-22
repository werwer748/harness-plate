# 기본 브랜치 푸시 막기

## 목표
셋업된 프로젝트에서 에이전트가 Bash로 기본 브랜치에 푸시하면 plate의 훅이 막고 까닭을 알린다.

## 범위 밖
- 사람의 푸시를 막는 것(git pre-push 훅, GitHub 브랜치 보호 규칙)
- 파일 편집 도구의 훅(`edit_guard.py`)의 동작을 바꾸는 것

## 완료 조건
1. 셋업된 프로젝트에서 에이전트의 Bash 호출이 기본 브랜치로 푸시하면, 훅이 종료 코드 2로 막고 까닭을 stderr로 알린다. 막는 경우는 기본 브랜치에 있는 채 대상 없이 하는 push, 기본 브랜치를 가리키는 push, 기본 브랜치를 지우는 push(`--delete`, `:main` 꼴), `&&`나 `;`로 이어진 명령 안의 push, `git -C <폴더>` 안의 push(그 폴더의 기본 브랜치를 본다)다. 다른 브랜치로의 푸시, origin 밖 원격으로의 푸시, 셋업 안 된 프로젝트(`AGENTS.md`에 문서 지도 구간이 없다)의 푸시는 막지 않는다.
   - 확인: `python3 -m unittest discover -s tests`가 통과한다
   - 확인: 푸시 훅의 테스트 파일을 읽어 위의 경우마다 테스트가 있다
2. `plugins/plate/hooks/hooks.json`이 Bash의 PreToolUse에 푸시 훅을 건다. 스크립트 파일이 없으면 `python3`를 부르지 않고 0으로 끝나는 꼴은 `edit_guard.py`를 거는 것과 같다.
   - 확인: `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"`가 `Bash`를 담은 matcher를 낸다
   - 확인: `plugins/plate/hooks/hooks.json`의 그 명령을 읽어 스크립트가 없을 때 0으로 끝나는 꼴이다
3. `docs/PRD.md`의 목표와 `docs/ARCHITECTURE.md`의 기술 스택, 디렉터리 구조, 막는 장치가 푸시 훅을 적는다.
   - 확인: 두 문서의 그 절들을 읽는다
4. tasks 완료 조건 1의 단위 테스트가 그대로 통과한다. 이 task도 `tests/`를 고친다.
   - 확인: `python3 -m unittest discover -s tests`가 통과하고, 판정 스크립트의 테스트가 그대로 있다

## 결정
- 푸시는 plate의 Claude Code 훅으로 막고, 사람의 푸시는 막지 않는다. 이유: 보호 경로(`.git`, `.husky`)를 건드리지 않고, git 훅은 clone에 따라가지 않으며 `--no-verify`로 건너뛰므로 어차피 막을 수 있는 것은 에이전트 쪽이다.
- 기본 브랜치는 origin의 HEAD가 가리키는 브랜치이고, 그것이 없으면 `main`, `main`도 없으면 `master`다. 이유: run과 review가 쓰는 뜻과 같게 한다.
