# Phase 2: 실제 실행으로 판정한다

**목표**: 고친 본문으로 2단계 자기 적용 직전의 문서를 다시 채운 결과에 그때 본 넷이 없다.

**읽을 것**
- `plugins/plate/skills/context/SKILL.md` (Phase 1에서 고친 본문)
- `docs/TOOLS.md` ("Claude Code" 절: 헤드리스 실행, 세션을 이어 여러 턴을 주고받는 방법)
- `docs/ADR.md` (ADR-019: 시험 폴더, 답 파일, 판정 도구의 위치)
- `~/plate-rail-test/bin/run.sh` (헤드리스 실행. `run.sh claude <폴더> context <로그 이름> [답 파일] [세션 id]`. 실행 기록이 `logs/<로그 이름>.jsonl`로 남고, 플러그인 폴더는 `P`에 적혀 있다)
- `~/plate-rail-test/bin/calls.py` (실행 기록에서 도구 호출을 순서대로 뽑는다)

**TODO**
- [x] 시험 폴더 `~/plate-rail-test/ctx-cells`가 생긴다. 이 레포를 복제해 커밋 `7c37c9b`로 맞춘 것이다. 그 `docs/ADR.md`에는 문장 중간의 칸 여섯과 줄 전체가 칸인 것 스물하나가 있다
- [x] 첫 턴의 답 파일이 생긴다(`~/plate-rail-test/answers/ctx-cells-1.md`). 세 칸만 답한다. ADR-010의 "실제 실행으로 판정하는 이유"에는 "특정 프로젝트에 강하게 결합되어 있는 하네스를 만들게 되는 것을 방지하기 위해서다", ADR-018의 "멈춘 이유"에는 "없음", ADR-019의 칸에는 뒤 갈래(해석 칸을 기계 기준에서 뺀 이유)의 답 "잘못된 작업의 기록이기 때문이다"만 적는다. 그 밖의 칸은 미룬다고 적되, 그 말이 ADR-019의 앞 갈래까지 가리키지 않게 적는다
- [x] 고친 본문으로 시험 폴더에서 맥락 채우기를 헤드리스로 돌린 결과가 생긴다. `run.sh`의 `P`가 가리키는 본문이 Phase 1에서 고친 것이어야 한다. 빠진 갈래를 묻는 질문에는 같은 세션의 다음 턴으로 미룬다고 답하고, 초안의 승인도 필요하면 다음 턴으로 보낸다. 턴마다 답 파일(`answers/ctx-cells-N.md`)과 실행 기록(`logs/ctx-cells-N.jsonl`)이 하나씩 남는다
- [x] 통과 조건에 걸리는 것이 있으면 본문이 고쳐지고, 시험 폴더를 되돌려 다시 돌린 결과가 통과한다 (`plugins/plate/skills/context/SKILL.md`)
- [x] 판정을 돌리며 새로 확인한 도구 사실이 있으면 "Claude Code" 절에 적힌다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 4(실제 실행의 결과에 본 것 넷이 없다)가 참이다.
  - 확인: 완료 조건 4의 확인 열을 모두 돌리고 읽어 기대 결과와 같은지 본다
- 본문을 고쳤다면 완료 조건 1, 2, 3이 여전히 참이다.
  - 확인: 그 세 조건의 확인을 다시 돌리고 읽어 기대 결과와 같은지 본다

## 한 일
- 시험 폴더 `~/plate-rail-test/ctx-cells`가 생긴다: 이 레포를 `git clone`으로 복제하고 `git checkout -b plate-test 7c37c9b`로 맞췄다. `docs/ADR.md`에 문장 중간의 칸 여섯(67, 97, 103, 109, 115, 121행)과 줄 전체가 칸인 것 스물하나가 있는 것을 `grep`으로 셌다. 6행의 `` `{확인 필요}` ``는 표시를 설명하는 문장이라 세지 않았다 (`~/plate-rail-test/ctx-cells/`)
- 첫 턴의 답 파일이 생긴다: 세 칸의 답을 적고, 미루는 말은 "ADR-010의 트레이드오프 칸과, ADR-010·ADR-018·ADR-019가 아닌 항목의 남은 칸은 모두 미룬다"로 적어 ADR-019의 앞 갈래를 가리키지 않게 했다. 앞선 답 파일들의 첫 줄("답이 없는 물음이 나오면 다시 묻지 말고 미룬 것으로 처리한다")은 앞 갈래까지 미루게 되므로 넣지 않았다 (`~/plate-rail-test/answers/ctx-cells-1.md`)
- 고친 본문으로 시험 폴더에서 맥락 채우기를 헤드리스로 돌린 결과가 생긴다: `run.sh`의 `P`(`/Users/gangjungi/Desktop/harness-plate/plugins/plate`)의 `SKILL.md`에 절대 규칙 5가 있는 것을 보고 돌렸다. 세션 `a8ade72e-06a5-4bbe-ad77-1b8897a52e43`으로 세 턴이었다. 1턴은 ADR-019의 앞 갈래(답을 미리 주는 방식을 기본으로 한 이유)만 묻고 멈췄다. 2턴에 "미룬다. 아직 정하지 않았다."를 보내자 바뀌는 세 줄의 표와 초안 전체를 보이고 승인을 물었다. 3턴에 "승인한다."를 보내자 `Edit` 셋으로 쓰고 보고했다 (`~/plate-rail-test/answers/ctx-cells-2.md`, `~/plate-rail-test/answers/ctx-cells-3.md`, `~/plate-rail-test/logs/ctx-cells-1.jsonl`, `ctx-cells-2.jsonl`, `ctx-cells-3.jsonl`)
- 통과 조건에 걸리는 것이 있으면 본문이 고쳐지고, 시험 폴더를 되돌려 다시 돌린 결과가 통과한다: 걸린 것이 없어 본문을 고치지 않았고 다시 돌리지 않았다
- 판정을 돌리며 새로 확인한 도구 사실이 있으면 "Claude Code" 절에 적힌다: 이 판정의 버전(2.1.300, 2026-10-15)을 첫 문장에 더했고, 허용 목록 없이 막히지 않은 명령과 세 턴의 실행 시간을 한 항목으로 더했다 (`docs/TOOLS.md`)

## 확인 결과
- 완료 조건 4(실제 실행의 결과에 본 것 넷이 없다)가 참이다.
  - `git -C ~/plate-rail-test/ctx-cells status --short` → ` M docs/ADR.md` 한 줄. 통과
  - `git -C ~/plate-rail-test/ctx-cells diff --numstat -- docs/ADR.md` → `3	3	docs/ADR.md`. 통과
  - (쉼표) `git -C ~/plate-rail-test/ctx-cells diff -U0 -- docs/ADR.md | grep '^+' | grep -c '이유는,'` → 0. 통과
  - (쉼표) `grep -c '판정하는 이유는 특정 프로젝트' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 1. 통과
  - (끊긴 "없음") `grep -c '멈춘 이유는 없음' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 0. 통과
  - (끊긴 "없음") `grep -c '멈춘 이유는 [^{]*\.$' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 1(`멈춘 이유는 없다.`). 통과
  - (닫힌 칸) `grep -c '뺀 이유는 .*{확인 필요}' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 1. 통과
  - (닫힌 칸) `grep -c '뺀 이유는 .*잘못된 작업의 기록' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 1. 적힌 줄은 `…해석 칸을 기계 기준에서 뺀 이유는 앞의 것은 {확인 필요}, 뒤의 것은 잘못된 작업의 기록이기 때문이다.`. 통과
  - (다시 묻기) `python3 ~/plate-rail-test/bin/calls.py ~/plate-rail-test/logs/ctx-cells-1.jsonl | grep -cE '^CALL (Edit|Write)'` → 0. `python3 ~/plate-rail-test/bin/summ.py ~/plate-rail-test/logs/ctx-cells-1.jsonl 3000`으로 읽은 마지막 답글은 "ADR-019 칸에는 갈래가 둘 있는데, 그중 하나에 대한 답과 미룬다는 말씀이 모두 없어서 그 갈래만 여쭙습니다"와 "**답을 미리 주는 방식을 기본으로 한 이유**는 무엇인가요?" 질문 하나였다. 통과
  - (저장소 밖) `for f in ~/plate-rail-test/logs/ctx-cells-*.jsonl; do python3 ~/plate-rail-test/bin/calls.py "$f"; done | grep '^CALL' | grep -oE '(/Users/|~/)[^" ]*' | sort -u | grep -v "^$HOME/plate-rail-test/ctx-cells" | grep -v "^$HOME/Desktop/harness-plate/plugins/plate"` → 출력 없음. `calls.py`가 앞 300자만 보여 주므로 기록의 도구 호출 입력 전체(세 턴에 8개)를 Python으로 따로 훑었고 저장소 밖의 경로가 없었다. 통과
- 본문을 고쳤다면 완료 조건 1, 2, 3이 여전히 참이다.
  - 본문을 고치지 않았다(`git diff --stat -- plugins/` → 출력 없음). 그래도 돌렸다: `grep -c '문장 중간'` → 1, `grep -c '여럿'` → 1, `grep -c '^5\. \*\*.*저장소 밖'` → 1, `grep -ciE 'claude|codex|grok'` → 0 (모두 `plugins/plate/skills/context/SKILL.md`). 통과

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
- 완료 조건 4의 "저장소 밖" 확인은 이 시험 폴더에서는 실패할 수 없는 쪽에 가깝다. 2단계 자기 적용에서 읽힌 것은 레포 밖의 메모 파일이었는데, `~/plate-rail-test/ctx-cells`에는 그 폴더에 대응하는 메모를 만들어 두지 않았다(머리의 범위 밖). 그래서 이 확인은 저장소 밖의 파일을 열지 않았다는 것만 보이고, 실린 메모를 근거로 쓰지 않는지는 보이지 못한다.
- 여럿을 묻는 칸이 문장 중간에 있으면 칸 앞의 글을 고칠 수 없어서 ADR-019의 줄이 "…뺀 이유는 앞의 것은 {확인 필요}, 뒤의 것은 …"처럼 주어가 겹친 문장이 됐다. 실행한 쪽도 초안에서 이 점을 알리고 고칠 곳을 물었다. 확인은 모두 통과한다.

## 회고 1: 회고

**확인**
- 완료 조건 4(실제 실행의 결과에 본 것 넷이 없다)가 참이다.
  - `git -C ~/plate-rail-test/ctx-cells status --short` → ` M docs/ADR.md` 한 줄. 통과
  - `git -C ~/plate-rail-test/ctx-cells diff --numstat -- docs/ADR.md` → `3	3	docs/ADR.md`(사이는 탭). 통과
  - (쉼표) `git -C ~/plate-rail-test/ctx-cells diff -U0 -- docs/ADR.md | grep '^+' | grep -c '이유는,'` → 0. 통과
  - (쉼표) `grep -c '판정하는 이유는 특정 프로젝트' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 1. 통과
  - (끊긴 "없음") `grep -c '멈춘 이유는 없음' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 0. 통과
  - (끊긴 "없음") `grep -c '멈춘 이유는 [^{]*\.$' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 1. 통과
  - (닫힌 칸) `grep -c '뺀 이유는 .*{확인 필요}' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 1. 통과
  - (닫힌 칸) `grep -c '뺀 이유는 .*잘못된 작업의 기록' ~/plate-rail-test/ctx-cells/docs/ADR.md` → 1. `git diff`로 본 바뀐 세 줄은 모두 칸 앞의 글이 커밋 `7c37c9b`의 것 그대로다. 통과
  - (다시 묻기) `python3 ~/plate-rail-test/bin/calls.py ~/plate-rail-test/logs/ctx-cells-1.jsonl | grep -cE '^CALL (Edit|Write)'` → 0. 그 기록의 마지막 답글(`result`)을 읽었다. "ADR-019 칸에는 갈래가 둘 있는데, 그중 하나에 대한 답과 미룬다는 말씀이 모두 없어서 그 갈래만 여쭙습니다"와 "**답을 미리 주는 방식을 기본으로 한 이유**는 무엇인가요?" 질문 하나다. 통과
  - (저장소 밖) `for f in ~/plate-rail-test/logs/ctx-cells-*.jsonl; do python3 ~/plate-rail-test/bin/calls.py "$f"; done | grep '^CALL' | grep -oE '(/Users/|~/)[^" ]*' | sort -u | grep -v "^$HOME/plate-rail-test/ctx-cells" | grep -v "^$HOME/Desktop/harness-plate/plugins/plate"` → 출력 없음. `calls.py`가 앞 300자만 보여 주므로 세 기록의 도구 호출 입력 전체(1턴 4개, 2턴 0개, 3턴 4개)를 Python으로 따로 훑었다. 나온 절대 경로는 `/Users/gangjungi/plate-rail-test/ctx-cells/docs/ADR.md` 하나다. 통과
- 본문을 고쳤다면 완료 조건 1, 2, 3이 여전히 참이다.
  - `git show --stat 292b184` → 바뀐 것은 `docs/TOOLS.md`와 `phase-2.md`뿐이다. `git diff --stat 33233d0 HEAD -- plugins/` → 출력 없음. 본문을 고치지 않아 이 조건은 걸리지 않는다. 그래도 돌렸다: `grep -c '문장 중간'` → 1, `grep -c '여럿'` → 1, `grep -c '^5\. \*\*.*저장소 밖'` → 1, `grep -ciE 'claude|codex|grok'` → 0 (모두 `plugins/plate/skills/context/SKILL.md`). 본문을 읽어 74행에 네 가지, 75행에 세 가지, 18행(절대 규칙 5)에 여는 것과 근거로 쓰는 것, 41행에 목록 밖에서 열 수 있는 것이 저장소 안의 소스 파일뿐이라는 것을 봤다. 통과

**문제**
없음

**배운 것**
- 완료 조건 4의 확인은 `~/plate-rail-test/ctx-cells`의 커밋하지 않은 변경과 `~/plate-rail-test/logs/ctx-cells-*.jsonl`을 본다. 작업 전체를 검증하기 전에 그 폴더를 되돌리거나 같은 로그 이름으로 다시 돌리면 결과가 바뀐다(`run.sh`는 `logs/<로그 이름>.jsonl`을 덮어쓴다).

**하네스의 문제점**
- 계획(완료 조건 4의 "저장소 밖" 확인): 시험 폴더에 대응하는 메모를 두지 않아(머리의 범위 밖) 실패할 수 없는 쪽에 가깝다. 절대 규칙 5의 둘째 갈래(세션에 실린 저장소 밖의 내용을 근거로 쓰지 않는다)는 실제 실행으로 확인되지 않고 본문의 글(완료 조건 3)로만 확인됐다. 확인 명령도 `calls.py`가 보이는 앞 300자만 훑어서, 입력 전체는 따로 훑어야 했다.
- 계획(같은 확인): 저장소 밖의 경로만 보므로 context 스킬 2번 절의 "아래 목록만 읽는다"에서 벗어난 저장소 안의 읽기는 잡지 않는다. 이번 1턴은 목록에 없는 `CLAUDE.md`를 열었고, 폴더 목록을 한 단계 아래보다 깊게 봤다(`find .claude-plugin .agents plugins -maxdepth 3`, `ls docs/tasks`).
- context 스킬 "답을 적는 규칙"의 문장 중간 칸 규칙과 여럿을 묻는 칸 규칙이 한 칸에 겹칠 때: 칸 앞의 글이 두 갈래를 묶어 "…뺀 이유는"으로 끝나므로 갈래를 칸 안에서 "앞의 것은 {확인 필요}, 뒤의 것은 …"으로 나눠야 했다. 본문에 이때의 꼴이 없어 실행한 쪽이 꼴을 정하고 초안에서 고칠 곳으로 물었다.
- context 스킬 3번의 4("문서의 초안 전체를 보여 주고 승인받는다"): 2턴의 초안은 바뀌는 세 줄의 표와 함께 문서를 보였지만 ADR-016~020의 바뀌지 않는 줄 일부를 "(지금과 같음, 바뀌지 않음)"으로 줄였다(줄였다고 알렸다). 긴 문서에서 바뀌는 곳이 적을 때 무엇까지 보여야 "전체"인지 본문에 없다.

**판정**: 통과
