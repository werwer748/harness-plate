# 판정 스크립트와 CI 워크플로 양식의 발견을 고친다

## 목표
정리 점검 2026-10-29의 신뢰성-7(판정 스크립트가 깨진 입력에서 1로 끝난다), 유지보수성-1(등급 묶음의 꼴 세 곳을 견주는 테스트가 없다), 보안-4(CI 워크플로 양식의 액션이 메이저 태그로 걸려 있다)를 고친다.

## 범위 밖
- 워크플로가 받는 plate의 ref를 고정하는 것(ADR-021·022가 감수했다).
- 이 저장소에 CI 워크플로를 두는 것.
- GitHub Actions에서 워크플로를 실제로 돌리는 것.

## 완료 조건
1. 판정 스크립트는 stdin을 JSON 객체로 읽지 못하거나 `--changed-files`의 파일을 읽지 못하면 `request`를 내고 0으로 끝나며, docstring과 ARCHITECTURE가 그것을 적는다(신뢰성-7).
   - 확인: `printf 'not json' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`
   - 확인: `printf '[]' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`
   - 확인: `printf '{"build":"pass","lint":"none","test":"pass","coverage":"skipped","reliability":"A","security":"A","maintainability":"A"}' | python3 plugins/plate/ci/verdict.py --changed-files /nonexistent; echo "exit=$?"` → `request`, `exit=0`
   - 확인: `grep -n '읽지 못하면' plugins/plate/ci/verdict.py docs/ARCHITECTURE.md` → 두 파일에 저마다 한 줄 이상
2. 등급 묶음의 꼴(키 일곱 개와 값의 열거)이 setup 양식의 `--json-schema`, review의 PR 모드 절의 표, 판정 스크립트의 `COMMANDS`·`GRADES`에서 같은지 테스트가 보고, 한 곳이 어긋나면 실패한다(유지보수성-1).
   - 확인: `python3 -m unittest tests.test_verdict.BundleShapeTest -v` → `OK`
   - 확인: 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고, 사본의 `plugins/plate/skills/setup/SKILL.md`에서 `"maintainability":{"type":"string","enum":["A","B","C","D","E","unjudged"]}`를 `"maintainability":{"type":"string","enum":["A","B","C","D","E"]}`로 바꿔 사본에서 `python3 -m unittest tests.test_verdict.BundleShapeTest` → 실패(`FAILED`)
3. setup의 CI 워크플로 양식의 `uses:` 줄이 모두 40자리 커밋 SHA로 고정되고 줄 끝에 그 SHA의 태그를 `# v7`처럼 적으며, 그 SHA가 그 태그가 가리키는 커밋이다(보안-4).
   - 확인: `grep -nE 'uses: ' plugins/plate/skills/setup/SKILL.md` → 모든 줄이 `uses: <소유자>/<이름>@<40자리 16진수> # v<수>` 꼴
   - 확인: 그 줄마다 `git ls-remote https://github.com/<소유자>/<이름> 'refs/tags/<태그>' 'refs/tags/<태그>^{}'`를 돌려, `^{}` 줄이 있으면 그 해시, 없으면 태그 줄의 해시가 줄의 SHA와 같다
4. 테스트 묶음이 모두 통과한다.
   - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 결정
- 판정 스크립트가 읽지 못한 입력은 머지 요청(`request`)으로 보낸다. 이유: 보고서의 고치는 방향이고, 판정 댓글이 남으면서 머지는 사람이 한다(fail-closed). (추천안으로 정함)
- 액션의 SHA는 지금 양식의 메이저 태그(`actions/checkout@v7` 같은 것)가 가리키는 커밋으로 정하고, 수행이 `git ls-remote`로 얻는다. 이유: 동작을 바꾸지 않고 고정만 한다. (추천안으로 정함)
