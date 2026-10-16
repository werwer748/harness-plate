# 검증

## 검증 1

**확인**
- 본문의 "답을 적는 규칙"에 문장 중간에 있는 칸의 규칙이 있다. 칸 자리의 글만 바꾸고 칸 앞뒤의 글자는 더하지도 빼지도 않는다. 답은 앞뒤 글에 이어져 한 문장으로 읽히게 다듬는다. 없다고 답한 것도 이어지는 문장으로 적고, 줄 전체가 칸이면 지금처럼 "없음"으로 적는다.
  - `grep -c '문장 중간' plugins/plate/skills/context/SKILL.md` → 2(74행, 76행). 통과
  - "답을 적는 규칙" 절(69~82행)을 읽음 → 74행에 네 가지가 모두 있다: 칸 자리의 글만 바꾸고 칸 앞뒤의 글자는 더하지도 빼지도 않는다(쉼표도 그렇다), 답은 앞뒤 글에 이어져 한 문장으로 읽히게 다듬는다, 없다고 답한 것도 이어지는 문장으로 적는다(`멈춘 이유는 없다.`), 줄 전체가 칸이면 "없음"으로 적는다. 통과
- 본문에 한 칸이 여럿을 물을 때의 규칙이 있다. 질문은 칸마다 하나로 낸다. 답에 빠진 갈래가 있으면 그 갈래만 한 번 더 묻는다. 그래도 답을 받지 못한 갈래는 그 자리에 `{확인 필요}`로 남겨 칸을 닫지 않는다.
  - `grep -c '여럿' plugins/plate/skills/context/SKILL.md` → 2(75행, 76행). 통과
  - "여럿"이 나온 곳을 읽음 → 75행에 세 가지가 모두 있다: 질문은 칸마다 하나로 낸다, 빠진 갈래만 한 번 더 묻는다, 답을 받지 못한 갈래는 `{확인 필요}`로 남겨 칸을 닫지 않는다. 76행은 이 작업 뒤의 커밋 `e2b6444`가 더한 줄(여럿을 묻는 칸이 문장 중간에 있을 때의 꼴)이고 75행과 어긋나지 않는다. 통과
- 본문의 절대 규칙에 다섯째 항목이 있다. 저장소 밖의 파일을 열지 않는다. 도구가 세션에 이미 실어 둔 저장소 밖의 내용도 칸의 내용이나 추천안의 근거로 쓰지 않는다. 2번 "스캔한다"의 글이 이 규칙과 어긋나지 않고, 본문에 도구 이름이 없다.
  - `grep -c '^5\. \*\*.*저장소 밖' plugins/plate/skills/context/SKILL.md` → 1. 통과
  - `grep -ciE 'claude|codex|grok' plugins/plate/skills/context/SKILL.md` → 0. 통과
  - 절대 규칙 5(18행)와 2번 절(39~50행)을 읽음 → 18행에 여는 것(저장소 밖의 파일을 열지 않는다)과 근거로 쓰는 것(세션에 이미 실린 저장소 밖의 내용도 칸의 내용이나 추천안의 근거로 쓰지 않는다)이 둘 다 있다. 41행은 목록 밖에서 열 수 있는 것을 해석을 확인하는 데 필요한 저장소 안의 소스 파일로만 둔다. 통과
- 고친 본문으로 `~/plate-rail-test/ctx-cells`(이 레포를 커밋 `7c37c9b`로 맞춘 복제본)에서 맥락 채우기를 돌린 결과에 2단계 자기 적용에서 본 넷이 없다. 답은 세 칸에만 주고 그 밖의 칸은 모두 미룬 실행이다.
  - `git -C ~/plate-rail-test/ctx-cells status --short` → ` M docs/ADR.md` 한 줄. 시험 폴더의 HEAD는 `7c37c9b`(브랜치 `plate-test`)다. 통과
  - `git -C ~/plate-rail-test/ctx-cells diff --numstat -- docs/ADR.md` → `3	3	docs/ADR.md`(사이는 탭). 통과
  - (쉼표) `git -C ~/plate-rail-test/ctx-cells diff -U0 -- docs/ADR.md | grep '^+' | grep -c '이유는,'` → 0. 통과
  - (쉼표) `grep -c '판정하는 이유는 특정 프로젝트' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 1. 통과
  - (끊긴 "없음") `grep -c '멈춘 이유는 없음' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 0. 통과
  - (끊긴 "없음") `grep -c '멈춘 이유는 [^{]*\.$' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 1(`멈춘 이유는 없다.`). 통과
  - (닫힌 칸) `grep -c '뺀 이유는 .*{확인 필요}' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 1. 통과
  - (닫힌 칸) `grep -c '뺀 이유는 .*잘못된 작업의 기록' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 1. 바뀐 줄은 `…뺀 이유는 앞의 것은 {확인 필요}, 뒤의 것은 잘못된 작업의 기록이기 때문이다.`이다. 통과
  - (다시 묻기) `python3 ~/plate-rail-test/bin/calls.py ~/plate-rail-test/logs/ctx-cells-1.jsonl | grep -cE '^CALL (Edit|Write)'` → 0. 그 기록의 마지막 답글(`result`)을 읽음 → "ADR-019 칸에는 갈래가 둘 있는데, 그중 하나에 대한 답과 미룬다는 말씀이 모두 없어서 그 갈래만 여쭙습니다"와 "**답을 미리 주는 방식을 기본으로 한 이유**는 무엇인가요?" 질문 하나다. 답 파일(`~/plate-rail-test/answers/ctx-cells-1.md`)은 세 칸에만 답하고 나머지 칸을 미룬다. 통과
  - (저장소 밖) `for f in ~/plate-rail-test/logs/ctx-cells-*.jsonl; do python3 ~/plate-rail-test/bin/calls.py "$f"; done | grep '^CALL' | grep -oE '(/Users/|~/)[^" ]*' | sort -u | grep -v "^$HOME/plate-rail-test/ctx-cells" | grep -v "^$HOME/Desktop/harness-plate/plugins/plate"` → 출력 없음. 세 기록의 도구 호출 입력 8개는 모두 259자 이하라 앞 300자로 잘린 것이 없다. 통과

**문제**
- 절대 규칙 5의 "저장소 밖의 파일을 열지 않는다"에는 다른 스킬을 이름으로 부를 때 도구가 여는 스킬 파일의 예외가 없다. `docs/TOOLS.md`의 Codex 절에는 Codex가 플러그인을 `~/.codex/plugins/cache/…`에 복사해 읽고, 본문에 "plate의 setup 스킬(`plate:setup`)을 불러"라고만 있으면 그 `SKILL.md`를 열어 따른다고 적혀 있다. 그래서 같은 본문의 0번(셋업이 안 됐으면 `plate:setup`을 부른다)을 Codex에서 따르면 절대 규칙 5를 어긴다. 본문 하나가 도구가 바뀌어도 같게 작동한다는 ADR-004, 본문을 계속 도구에 기대지 않게 쓴다는 ADR-018과 어긋난다 (`plugins/plate/skills/context/SKILL.md` 18행). 기준: 맥락 문서

**배운 것**
- `~/plate-rail-test/ctx-cells`의 결과와 `~/plate-rail-test/logs/ctx-cells-*.jsonl`은 커밋 `d169a15`의 context 본문으로 돌린 것이다. 그 뒤 커밋 `e2b6444`가 같은 본문의 59행(초안을 보이는 규칙)과 76행(여럿을 묻는 칸이 문장 중간에 있을 때의 꼴)을 바꿨고, 바뀐 본문으로는 이 시험을 다시 돌리지 않았다.
- `docs/ADR.md`의 ADR-018 이유 끝 "멈춘 이유는 없음"은 이 작업이 더한 문장 중간 칸의 규칙에 맞지 않는 꼴로 남아 있다(계획의 범위 밖). 범위 밖에 함께 적힌 2단계 완성 판정 항목은 커밋 `9b0dfb6`에서 항목째 지워졌다.

**하네스의 문제점**
- verify 스킬 2번("완료 조건에 적힌 확인을 하나도 빼지 않고 직접 돌린다")과 계획의 완료 조건 4: 그 확인은 실제 실행을 다시 하지 않고 남은 결과(시험 폴더의 커밋하지 않은 변경, 실행 기록)를 읽는 명령이다. 그래서 검증에서 다시 돌려도 phase 2 때의 결과를 다시 읽을 뿐이고, 그 사이 다른 작업(`e2b6444`)이 같은 본문을 고친 뒤의 동작은 보이지 않는다.
- verify 스킬 "낱말"의 "작업의 커밋": 다른 작업 폴더의 이름으로 시작하는 커밋을 빼서, 이 작업의 머리를 고친 커밋 `9b0dfb6`(`005-run: phase 8`. ADR 번호를 지우며 범위 밖, 완료 조건 4, 결정의 글을 바꿨다)이 점검 대상에서 빠진다. 이번에는 번호를 풀어 쓴 것뿐이라 뜻이 같았다.
- 계획(결정의 "저장소 밖 규칙은 여는 것과 근거로 쓰는 것을 둘 다 막는다"와 완료 조건 4의 "저장소 밖" 확인): 확인은 `$HOME/Desktop/harness-plate/plugins/plate` 아래의 경로를 빼서 플러그인 파일을 여는 것을 허용하는 쪽인데, 결정과 완료 조건 3에는 그 예외가 없다. 확인과 규칙이 다른 범위를 봐서 위 문제(다른 스킬의 파일을 여는 도구)가 phase의 회고에서도 걸리지 않았다.

**판정**: 문제 있음
