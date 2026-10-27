# 코드베이스를 살펴 정리 거리를 보고하는 cleanup 스킬을 더한다

**이름**: cleanup

## 요청
PRD 9단계: 정리·리팩터링. 코드베이스를 정기·비정기로 살펴 정리하는 스킬을 둔다. 이것을 만든 뒤 1.0.0을 낸다. (작업 브랜치는 worktree /Users/hugo/Desktop/harness-plate-cleanup 의 tasks/cleanup. 다른 세션이 main 쪽에서 열린 이슈 #26~#32를 고치고 있으니 그 범위는 건드리지 않는다.)

## 목표
`plate:cleanup`을 부르면 서브에이전트 여섯이 저마다 기준 하나를 맡아 저장소를 살피고, 2라운드 교차 검토를 거쳐 `docs/cleanup/YYYY-MM-DD.md`에 보고서를 쓴다. 그런 다음 발견으로 tasks를 만들지 묻고, 동의하면 `plate:plan`으로 넘겨 작업 사이클을 다시 탄다. 이 동작은 임시 복제본에서 두 장면으로 돌려 확인하고 `docs/TOOLS.md`에 남긴다. 플러그인 버전은 0.15.0이 되고, 맥락 문서와 README가 이 스킬에 맞춰진다.

## 범위 밖
- 1.0.0으로 버전을 올리는 것, PRD의 1.0 줄을 고치는 것, 태그와 릴리스. 이 tasks와 이슈 수정이 모두 main에 들어간 뒤 별도 릴리스 tasks에서 한다
- 정기 실행의 계기(run의 권유, 도구의 예약 실행). 수동으로만 부른다
- 스킬이 코드를 직접 고치는 것
- 발견을 `docs/BACKLOG.md`에 더하는 것과 run의 BACKLOG 규칙을 바꾸는 것
- 이슈 #26~#32와 그것이 고칠 스킬(plan, run, review, eval, check, retro)의 본문
- Codex와 Grok Build에서 확인하는 것(ADR-018)

## 완료 조건
1. `plugins/plate/skills/cleanup/SKILL.md`가 있고, 여섯 기준·2라운드 교차 검토·보고서 위치·문서 지도 행·tasks로 만들지 묻고 plan으로 넘기는 절차를 적는다.
   - 확인: `test -f plugins/plate/skills/cleanup/SKILL.md`가 0으로 끝난다
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
2. 임시 복제본에서 두 장면으로 돌린 결과가 `docs/TOOLS.md`에 있다. 장면 1(tasks로 만들지 않음)은 보고서와 지도 행만 커밋되고 다른 파일은 바뀌지 않으며, 장면 2(만든다)는 `plate:plan`이 불린다. 기록은 SKILL.md의 마지막 커밋 뒤에 돌린 것이다.
   - 확인: `docs/TOOLS.md`의 새 절을 읽어, 두 장면이 저마다 Claude Code 버전, 돌린 시각, 세션 id, 결과(장면 1: 커밋된 파일 목록과 보고서의 여섯 기준 절, 장면 2: `plate:plan` 호출 줄)를 적었다. 하나라도 없으면 실패
   - 확인: 그 절에 적힌 돌린 시각이 `git log -1 --format=%cI -- plugins/plate/skills/cleanup/SKILL.md`보다 늦다
3. 두 매니페스트의 버전이 0.15.0이고 cleanup 스킬을 설명에 담는다. 테스트가 통과하고, 맥락 문서와 README가 cleanup 스킬과 어긋나지 않는다.
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.15.0`
   - 확인: `grep -c cleanup plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`가 두 파일 모두 1 이상
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`를 문서마다 따로 읽어 cleanup 스킬(9단계를 만들었다, 디렉터리 구조, 스킬 목록과 부르는 이름)과 어긋나는 줄이 없다

## 결정
- 스킬 이름은 `cleanup`이다. 이유: PRD의 "정리"와 브랜치 이름에 맞고, 기존 스킬처럼 한 낱말이다
- 스킬은 살피고 보고서를 쓴 뒤 tasks로 만들지 묻고, 동의하면 고른 발견을 `plate:plan`에 넘긴다. 코드는 직접 고치지 않는다. 이유: 사용자의 말 "보고서 … 이후 끝내는게 아니고 해당 작업을 통해 tasks를 구성할지 묻고 동의한다면 다시 작업사이클을 타는 쪽으로"
- 기준은 여섯이고 서브에이전트가 하나씩 맡는다: 보안, 성능, 신뢰성(오류 처리, 테스트 공백), 유지보수성(중복, 복잡도, 죽은 코드, 구조), 기능 적합성(PRD와 코드), 기존 작업 정합성(ADR, BACKLOG, 열린 이슈, 지난 tasks 기록). 이유: review의 범주에 맞추면서 성능, 기존 작업, 기능을 따로 세운다
- 논의는 2라운드다. 1라운드에는 여섯이 따로 찾아 근거(파일:줄)와 함께 적는다. 2라운드에는 저마다 다른 다섯의 발견을 받아 동의, 반박, 중복, 충돌을 달고, 메인이 모아 보고서를 쓴다. 이유: 반박받은 발견을 걸러 내고, 도구에 기대지 않는다
- 보고서는 살필 때마다 `docs/cleanup/YYYY-MM-DD.md`에 새로 쓰고, 처음 쓸 때 문서 지도에 행을 더한다. 다음 정리 때 지난 보고서를 읽어 다시 나온 것을 표시한다. 이유: 지난 보고서와 견줄 수 있고, `docs/tasks/`를 비워도 남는다
- tasks로 만들지 않은 발견은 그 보고서에 "미룸"으로만 남긴다. 이유: run의 BACKLOG 규칙을 건드리지 않고, 오래된 부채가 자동으로 지워지지 않는다
- 정기 실행의 계기는 두지 않고 수동으로만 부른다. 이유: 사용자의 말 "비정기적인 확인 이니까 틀에 묶기보다는 자유도를 좀 주고 추후에 변경하는게 나을꺼같아"
- 살피는 범위는 기본이 저장소 전체의 코드 파일과 결과물인 마크다운(review와 같은 정의)이고, `docs/tasks/`와 도구가 만든 파일은 뺀다. 부를 때 경로를 주면 그것만 본다. 이유: review는 tasks가 바꾼 것만 보므로 그 밖의 쌓인 부채를 보는 것이 이 스킬의 몫이다
- 확인은 이 레포를 `mktemp -d`에 복제한 곳(main)에서 worktree의 plugins/plate를 `--plugin-dir`로 실어 헤드리스로 돌린다. 장면 2는 장면 1의 세션을 묻는 자리에서 갈라 잇는다. 이유: 이 레포를 더럽히지 않고 두 갈래를 모두 돌린다
- 버전은 0.15.0이다. PR 전에 main이 먼저 0.15.0 이상이 되면 PR에서 다음 마이너로 맞춘다. 이유: 1.0.0은 별도 릴리스 tasks에서 한다

## task 목록
- `001-cleanup-skill`: cleanup 스킬 본문이 생기고, 임시 복제본에서 두 장면으로 돌린 결과가 `docs/TOOLS.md`에 남는다
- `002-docs-release`: 버전이 0.15.0이 되고, 매니페스트·README·PRD·ARCHITECTURE가 cleanup 스킬에 맞춰진다
- `003-fixes`: tasks 끝에서 고치기로 한 것이 고쳐진다
