# 버전을 0.15.0으로 올리고 문서를 cleanup 스킬에 맞춘다

## 목표
두 매니페스트의 버전이 0.15.0이 되고 설명에 cleanup 스킬이 들어간다. README, PRD, ARCHITECTURE가 cleanup 스킬과 어긋나지 않는다.

## 범위 밖
- 1.0.0, 태그, 릴리스, PRD의 "9단계까지 만든 뒤 1.0.0을 낸다" 줄
- `docs/ADR.md` (다섯 범주에 드는 결정이 없다)
- cleanup 스킬 본문과 `docs/TOOLS.md` (`001-cleanup-skill`이 했다)
- 이 레포의 `AGENTS.md` 문서 지도 (cleanup이 처음 돌 때 그 스킬이 행을 더한다)

## 완료 조건
1. 두 매니페스트의 버전이 0.15.0이고 설명에 cleanup 스킬이 있다(tasks 완료 조건 3).
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.15.0`
   - 확인: `grep -c cleanup plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`가 두 파일 모두 1 이상
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
2. README, PRD, ARCHITECTURE가 cleanup 스킬과 어긋나지 않는다(tasks 완료 조건 3).
   - 확인: `README.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`를 문서마다 따로 읽어, 스킬 수·스킬 목록·부르는 이름·9단계의 상태·디렉터리 구조·규칙 문단의 스킬 목록에서 cleanup과 어긋나는 줄이 없다. 한 문서라도 있으면 실패
   - 확인: `grep -c 'plate:cleanup' README.md`가 2 이상 (Claude Code와 Codex의 부르는 이름)
3. 앞 task가 이룬 것이 그대로다(tasks 완료 조건 1, 2).
   - 확인: `test -f plugins/plate/skills/cleanup/SKILL.md`가 0으로 끝나고, `git diff --name-only $(git log -1 --format=%H -- docs/tasks/001-cleanup-skill/retro.md) HEAD -- plugins/plate/skills/cleanup/SKILL.md docs/TOOLS.md`가 아무것도 내지 않는다
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`

## 결정
- 버전은 0.15.0이다. PR 전에 main이 먼저 0.15.0 이상이 되면 PR에서 다음 마이너로 맞춘다. 이유: tasks 결정
