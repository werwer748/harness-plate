# TODO: 레일 1단계 (플러그인 뼈대 + 셋업 스킬)

**읽는 법**
- 설계와 규격은 [plan.md](plan.md)에 있다. 항목을 하다가 "무엇을, 어떤 규격으로"가 필요하면 그 파일의 해당 절을 읽는다.
- 위에서부터 한 항목씩 한다. 확인이 통과한 항목만 `[x]`로 바꾼다.
- 묶음(A~E) 하나가 끝나면 이 파일을 갱신하고 결과를 보고한다. 컨텍스트가 길어졌으면 거기서 세션을 끊는다. 다음 세션은 첫 미완료 항목부터 잇는다.
- plan.md와 다르게 해야 하거나 막히면 고치기 전에 묻는다.
- 커밋은 `rail` 브랜치에 로컬로만 한다. 푸시하지 않는다.

## A. 레포 준비

- [x] A1. `git init` → `git remote add origin https://github.com/werwer748/harness-plate.git` → `git fetch origin` (GitHub 레포가 지워져 있어서, 비공개로 다시 만들고 옛 파일 스냅샷 3c8bcb6을 `main`에 푸시한 뒤 fetch했다. plan.md "확인해 둔 사실" 참고)
- [x] A2. `git tag legacy-0.3.0 origin/main` (로컬 태그, 푸시하지 않음)
- [x] A3. `git switch -c rail --no-track origin/main` 뒤 추적 파일을 전부 지우고 커밋. `plan.md`와 `TODO.md`는 추적하지 않는 파일이라 남는다
- [x] A4. 확인: `git ls-files`가 비어 있음 / `git show legacy-0.3.0:HANDOFF.md`가 읽힘 / 현재 브랜치가 `rail` / `plan.md`와 `TODO.md`가 그대로 있음

## B. 매니페스트

- [x] B1. Codex 매니페스트 형식을 공식 문서와 superpowers 예시로 확인하고, 확인한 필드를 plan.md "아직 확인하지 못한 것"에 반영 (확인이 끝나 "확인해 둔 사실"로 옮겼다)
- [x] B2. `.claude-plugin/marketplace.json`, `plugins/plate/.claude-plugin/plugin.json`(version 0.4.0) 작성. 옛 형식은 태그에서 가져온다
- [x] B3. `.agents/plugins/marketplace.json`, `plugins/plate/.codex-plugin/plugin.json` 작성
- [x] B4. 이름과 설명만 있는 껍데기 `plugins/plate/skills/setup/SKILL.md` 작성
- [x] B5. 확인(Claude Code): `claude --plugin-dir plugins/plate` 세션에 `/plate:setup`이 보임
- [x] B6. 확인(Codex): `codex plugin marketplace add <이 폴더>` → `codex plugin list`에 plate가 보임 → `codex plugin add`로 설치됨
- [x] B7. Codex에서의 스킬 호출 이름을 확인해 plan.md에 기록 (`$plate:setup`)
- [x] B8. 커밋

## C. 셋업 스킬 본문

- [x] C1. 절차 4단계와 절대 규칙 작성 (plan.md "셋업 스킬 규격")
- [x] C2. 판정 기준을 목록으로 작성: 같은 역할 문서의 이름 목록, UI 프로젝트 기준
- [x] C3. 양식 4종을 본문에 넣음: PRD·ARCHITECTURE·ADR은 태그의 옛 init 스킬에서, DESIGN은 Google 규격의 절 구성으로
- [x] C4. 문서 지도 구간을 plan.md의 글 그대로 넣음
- [x] C5. 확인: 본문에 도구 이름이 없고 동작으로만 쓰여 있음
- [x] C6. 커밋

## D. 완성 판정 (plan.md "완성 판정 기준"의 표 번호와 같다)

- [x] D0. 시험 폴더 준비: 빈 폴더 2개, excel-viewer 로컬 복제본 3개. Codex 설치본을 최신 스킬로 갱신
- [x] D1. 빈 폴더에 정해진 파일만 생김 (두 도구 각각)
- [x] D2. 빈 폴더 결과가 두 도구에서 한 글자도 다르지 않음 (`diff -r`가 비어 있음)
- [x] D3. `CLAUDE.md` 내용이 `@AGENTS.md` 한 줄
- [x] D4. excel-viewer 복제본(옮기기 승인): 내용 이동, 기존 `AGENTS.md` 보존, `README.md`·`TODO.md` 미변경
- [x] D5. excel-viewer 결과가 두 도구에서 파일 목록·위치·지도 구간이 같음
- [x] D6. 다시 돌려도 변화 없음
- [x] D7. 거절 경로: 기존 `CLAUDE.md` 내용이 남음. `@AGENTS.md` 줄이 이미 있으면 바뀌지 않고, 없으면 맨 위에 그 줄만 더해짐
- [x] D8. Claude Code 서브에이전트에도 문서 지도가 실림
- [x] D9. 실패한 항목이 있었으면 스킬을 고치고 그 항목을 다시 통과시킴. 커밋 (실패한 항목이 없어 스킬을 고치지 않았다. 시험은 `/tmp/plate-rail-test`에서 다시 돌린 결과다. E1에서 `.gitkeep`이 "모든 파일은 줄바꿈으로 끝난다"는 문장과 부딪힌다는 지적이 나와 스킬 문구에 예외를 적었고, 새 빈 폴더 2개에서 두 도구의 결과가 전과 같음을 다시 확인했다)

## E. 자기 셋업과 마무리

- [x] E1. 이 레포(`rail`)에서 셋업을 돌림
- [x] E2. `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`를 plan.md의 결정 원장을 근거로 채움. 추측은 적지 않는다 (ADR의 이유·트레이드오프 중 기록이 없는 칸은 `{확인 필요}`로 두었다)
- [x] E3. `plan.md`와 `TODO.md`의 최종 위치를 문서 지도 규칙에 따라 사용자에게 묻고 옮김 (`docs/tasks/001-setup/`으로 옮겼다. 지도에 행은 더하지 않는다. v1.0이 되면 모두 지운다)
- [x] E4. `README.md`에 두 도구의 설치 명령을 적음
- [x] E5. 확인: 지도 표의 위치와 실제 파일이 일치 / ADR의 각 항목이 결정 원장 번호에 대응. 커밋
- [x] E6. 체크리스트 결과를 보고하고 두 가지를 따로 확인받음: `rail`을 `main`으로 바꾸고 푸시할지 / 2단계(맥락 채우기) 질문 라운드를 열지 (답: `main`으로 푸시한다 / 2단계 질문 라운드는 새 세션에서 연다)
