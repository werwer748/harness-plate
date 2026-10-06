# TODO: 레일 2단계 (맥락 채우기 스킬)

**읽는 법**
- 설계와 규격은 [plan.md](plan.md)에 있다. 항목을 하다가 "무엇을, 어떤 규격으로"가 필요하면 그 파일의 해당 절을 읽는다.
- 위에서부터 한 항목씩 한다. 확인이 통과한 항목만 `[x]`로 바꾼다.
- 묶음(A~E) 하나가 끝나면 이 파일을 갱신하고 결과를 보고한다. 컨텍스트가 길어졌으면 거기서 세션을 끊는다. 다음 세션은 첫 미완료 항목부터 잇는다.
- plan.md와 다르게 해야 하거나 막히면 고치기 전에 묻는다. plan.md "구현 중 사용자에게 물을 것"의 항목은 그 지점에 닿았을 때 묻는다.
- 커밋은 `context` 브랜치에 로컬로만 한다. 푸시하지 않는다.

## A. 준비

- [x] A1. 현재 브랜치가 `context`인지 확인
- [x] A2. DESIGN.md 규격(google-labs-code/design.md)을 다시 읽어 `typography` 토큰의 형태와 토큰 참조 문법을 확인하고 plan.md "아직 확인하지 못한 것"에 반영. `typography`를 어떻게 옮길지 정해지지 않으면 묻는다 (확인이 끝나 "확인해 둔 사실"로 옮겼다. 옮기는 방식은 물어 정했다: 원장 77, 78. 토큰 파일을 읽다가 나온 물음 넷은 B6에서 묻도록 plan.md "구현 중 사용자에게 물을 것"에 적었다)
- [x] A3. 헤드리스 여러 턴이 두 도구에서 되는지 빈 폴더에서 확인(`claude -p --resume`, `codex exec resume`)하고 명령 형태를 plan.md "확인해 둔 사실"에 기록
- [x] A4. 두 매니페스트의 version을 0.5.0으로 올림

## B. 맥락 스킬 본문

- [x] B1. 이름과 설명만 있는 껍데기 `plugins/plate/skills/context/SKILL.md` 작성
- [x] B2. 확인: Claude Code에서 `/plate:context`, Codex에서 설치본을 갱신한 뒤 `$plate:context`가 보임
- [x] B3. 낱말(남은 칸, 대상 문서, 적힌 사실·해석·의도)과 절대 규칙 작성 (plan.md "맥락 스킬 규격")
- [x] B4. 절차 0~4 작성
- [x] B5. 답을 적는 규칙, 칸의 분류 표, ADR 후보의 범주 작성
- [x] B6. DESIGN의 토큰 규칙 작성. 네 범주 밖 토큰과 본문 Colors·Typography 절의 묻는 방식은 사용자에게 물어 정한다 (일곱 가지를 물어 정했다: 원장 79~85)
- [x] B7. 확인: 본문에 도구 이름이 없고 동작으로만 쓰여 있음
- [x] B8. 커밋

## C. 셋업 스킬 수정

- [x] C1. 재실행 물음: 문서 지도 구간이 있으면 화면이 있는 프로젝트인지 묻지 않음 (plan.md "셋업 스킬 수정" 1)
- [x] C2. 끝 물음: 남은 칸이 있는 문서가 있으면 이어서 채울지 묻고, 묻지 않는 경우 셋을 적음 (plan.md "셋업 스킬 수정" 2)
- [x] C3. Codex 설치본 갱신 뒤 1단계 판정 D1, D2, D4, D5, D6을 다시 돌림. 끝 물음에는 "채우지 않는다"를 미리 준다 (새 폴더 `c3-empty-*`, `c3-ev-*`에서 돌렸다. 빈 폴더와 excel-viewer 복제본 모두 두 도구의 결과가 바이트 단위로 같고 1단계의 결과와도 같다. 다시 돌려도 변화가 없고, 빈 폴더를 다시 돌릴 때 화면이 있는지 묻지 않는다. 두 도구 모두 끝 물음의 답대로 채우기로 넘어가지 않았다)
- [x] C4. 커밋

## D. 완성 판정 (D1~D11은 plan.md "완성 판정 기준"의 표 번호와 같다. 12번은 E4에서 한다)

- [x] D0. 시험 폴더 8쌍과 답 파일 준비. Codex 설치본을 최신 스킬로 갱신 (빈 폴더의 셋업 결과는 두 도구가 바이트 단위로 같아서 `ctx-full`, `ctx-part`, `ctx-turn`은 C3의 `c3-empty-*`를 복사해 만들었고, `ctx-ev`는 `c3-ev-*`를 복사했다. `ctx-badak`과 `ctx-fin`은 복제본에 셋업을 실제로 돌렸다. `ctx-badak`은 루트 `DESIGN.md`를 지운 변형이다(원장 86). 셋업 직후를 폴더마다 커밋해 두었다. 답 파일은 `/tmp/plate-rail-test/answers/`, 판정 도구는 `/tmp/plate-rail-test/bin/`에 있다)
- [x] D1. `ctx-full`: 답을 모두 주면 세 문서가 채워지고 남은 칸이 0개 (두 도구 통과. 기계 판정 모두 같음. 글자가 다른 곳은 다듬은 표현 넷이다)
- [x] D2. `ctx-part`: 미룬 칸이 `{확인 필요}`가 되고 두 도구에서 같은 칸 (두 도구 통과. PRD의 사용자, ARCHITECTURE의 데이터 흐름, ADR-001의 트레이드오프)
- [x] D3. `ctx-part`: 다시 부르면 남은 칸만 바뀜 (두 도구 통과. `git diff`가 세 파일에서 한 줄씩이다)
- [x] D4. `ctx-full`: 다시 불러도 변화 없음 (두 도구 통과)
- [ ] D5. `ctx-ev`: 출처 경로, ADR 후보의 범주, `README.md`·`TODO.md` 미변경 (Claude Code는 끝났다. Codex는 PRD와 ARCHITECTURE를 쓴 뒤 사용 한도 오류로 끊겼다. 끊긴 결과는 `partial-ctx-ev-codex`에 두고 폴더는 셋업 직후로 되돌렸다. Codex를 다시 돌려야 한다)
- [ ] D6. `ctx-badak`: `docs/DESIGN.md`의 토큰이 `src/app/global.css`의 이름과 값 그대로 (Claude Code는 끝났고 토큰 대조를 통과했다: 색 31개, 모서리 8개, 글꼴 2개의 이름·값·순서가 같다. Codex는 PRD와 ARCHITECTURE를 쓴 뒤 한도 오류로 끊겼다. `partial-ctx-badak-codex`에 두고 되돌렸다. Codex를 다시 돌려야 한다)
- [ ] D7. `ctx-fin`: 기존 세 문서는 그대로이고 `docs/DESIGN.md`만 채워짐 (Claude Code는 통과했다. Codex는 `docs/DESIGN.md`를 다 쓴 뒤 한도 오류로 끝났다. 그 파일은 토큰 대조를 통과했고 Claude Code의 결과와 세 줄만 다르다(`name` 위의 출처 주석, `omitted`의 주석 글, Typography 항목의 표현). `partial-ctx-fin-codex`에 두고 되돌렸다. 실행이 오류로 끝났으니 Codex를 다시 돌린다)
- [x] D8. `ctx-nosetup`: 셋업을 묻고 이어서 채움. 셋업 결과가 setup 단독 결과와 같음. 실패하면 원장 60을 사용자에게 다시 묻는다 (두 도구 통과. `AGENTS.md`, `CLAUDE.md`, `.gitkeep`이 setup 단독 결과와 같다)
- [x] D9. `ctx-chain`: setup의 끝 물음에서 context로 이어짐. 실패하면 원장 60을 사용자에게 다시 묻는다 (두 도구 통과)
- [ ] D10. `ctx-turn`: 여러 턴에서 질문이 하나씩 나옴, 승인 전 쓰지 않음, 도중에 그만하면 답한 칸만 쓰임 (Claude Code는 통과했다: 다섯 턴. 질문이 턴마다 하나, 넷째 턴까지 `git status`가 비어 있고, 승인 뒤 `docs/PRD.md`의 두 줄만 바뀌었다. Codex는 한도 오류로 시작하지 못했다. `/tmp/plate-rail-test/bin/codex_rest.sh`가 판정 5, 6, 7, 10의 Codex 실행을 한 번에 돌린다)
- [x] D11. `ctx-full`: setup을 다시 돌려도 화면 여부를 묻지 않고 변화 없음 (두 도구 통과)
- [ ] D13. D1, D2, D5, D6, D7의 두 도구 결과를 기계 판정과 뜻 대조 표로 정리해 사용자에게 보여 줌 (기계 판정은 `python3 /tmp/plate-rail-test/bin/judge.py <폴더A> <폴더B>`, 토큰 대조는 `tokencheck.py <폴더> <토큰 파일> [--ask radius=rounded]`로 한다)
- [ ] D14. 실패한 항목이 있었으면 스킬을 고치고 그 항목을 다시 통과시킴. 커밋
  - 여기서 사용자에게 물을 것 1: 기존 프로젝트의 해석 칸(기술 스택, 패턴과 규칙)은 도구마다 항목 수와 출처 경로가 다르게 나온다(excel-viewer의 패턴과 규칙이 Claude Code 9개, 끊기기 전의 Codex 2개). 원장 66의 기계 기준을 해석 칸에도 적용할지, 스킬을 더 좁힐지
  - 고칠 후보 2: Claude Code만 DESIGN 앞머리의 `name` 위에 `# 출처: docs/PRD.md`를 붙였다. 출처 주석은 토큰 파일에서 옮긴 범주에만 붙인다고 본문에 적으면 된다
  - 물을 것 3: setup 스킬에서 `AGENTS.md`가 없을 때 Codex만 새 파일의 첫 줄을 빈 줄로 둔다(plan.md "확인해 둔 사실"). 2단계에서 고칠지

## E. 자기 적용과 마무리

- [ ] E1. `README.md`와 두 매니페스트의 설명에 context 스킬을 더함
- [ ] E2. `docs/PRD.md`와 `docs/ARCHITECTURE.md`를 2단계 상태로 고침
- [ ] E3. `docs/ADR.md`에 2단계의 결정을 plan.md의 결정 원장(40번부터)을 근거로 더함. 이유와 트레이드오프 중 기록이 없는 칸은 `{확인 필요}`로 둔다
- [ ] E4. 판정 12: 이 레포에서 `plate:context`를 사용자와 대화형으로 돌려 `docs/ADR.md`의 `{확인 필요}` 칸을 채움. 적힌 내용이 바뀌지 않았는지 `git diff`로 확인
- [ ] E5. 확인: ADR의 각 항목이 결정 원장 번호에 대응 / 지도 표의 위치와 실제 파일이 일치. 커밋
- [ ] E6. 체크리스트 결과를 보고하고 두 가지를 따로 확인받음: `context`를 `main`에 병합하고 푸시할지 / 3단계(계획) 질문 라운드를 열지
