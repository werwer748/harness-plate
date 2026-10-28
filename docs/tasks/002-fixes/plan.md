# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리고 plate 저장소에서 고친다

## 완료 조건
1. 작업 트리를 얻는 예로 든 `git stash create`는 추적하지 않는 새 파일을 넣지 않고 새 파일만 바뀌었으면 아무것도 내지 않아, 새 파일을 만드는 phase의 통과 조건이 이 예를 따르면 그 파일이 없는 트리를 본다. 예를 `cp -R` 사본으로 줄이거나 새 파일이 빠진다는 단서를 단다 (`plugins/plate/skills/plan/SKILL.md:249`)
   - 확인: `plugins/plate/skills/plan/SKILL.md`의 적는 규칙 "조건" 절을 다시 읽어, 작업 트리를 얻는 예로 `git stash create`를 새 파일이 빠진다는 단서 없이 들지 않는다
2. tasks 완료 조건 1, 2, 3이 참이다.
   - 확인: `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건", "결정" 절을 읽어, tasks 완료 조건 1에 백틱으로 적은 다섯 글이 저마다 그 절에 있다. 하나라도 없으면 실패
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사하고, 사본의 `plugins/plate/skills/plan/SKILL.md`에서 글 `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다`가 한 번 있는지 본 뒤(없으면 실패) 그 글을 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`를 돌리면 출력에 `FAIL: test_55_checks_run_on_uncommitted_worktree` 줄이 있다
   - 확인: 같은 방법으로 새로 복사해 글 `지울 글을 본문에 있는 그대로 인용하고`를 빈 글로 바꾸면 출력에 `FAIL: test_56_mutation_checks_quote_text_and_name_test` 줄이 있다
   - 확인: 같은 방법으로 새로 복사해 글 `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고`를 빈 글로 바꾸면 출력에 `FAIL: test_57_quote_earlier_task_text_as_changed` 줄이 있다
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.19.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄이 세 규칙(통과 조건은 커밋 전 작업 트리에서 돎, 지울 글 인용과 실패할 테스트 이름, 앞 task가 바꿀 글을 바뀐 뒤 꼴로 인용)을 저마다 담고, `tests/test_skill_rules.py`의 모듈 docstring의 plan 목록에 #55·#56·#57이 있다. 하나라도 없으면 실패

## 결정
- 없음
