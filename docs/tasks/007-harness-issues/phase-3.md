# Phase 3: LESSONS 정리와 버전

**목표**: 다룬 18줄이 LESSONS에서 지워지고 두 매니페스트가 0.8.1이다.

**읽을 것**
- `docs/LESSONS.md` (지울 18줄이 있는 하네스의 문제점 절과 미룬 문제 절)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (버전)

**TODO**
- [x] `docs/LESSONS.md`의 하네스의 문제점 절에서 이 작업이 다룬 17줄(앞이 `(004-context-rules, 검증 1)`인 셋, `(006-verify, phase 1)`~`(006-verify, phase 6)`인 열하나, `(006-verify, 검증 1)`인 셋)이 지워지고, 미룬 문제 절에서 `(006-verify, 검증 1) run 본문 "검증을 맡긴다"의 첫 갈래는 …` 줄이 지워진다. 이 작업을 실행하며 더해진 줄과 다른 줄은 그대로다 (`docs/LESSONS.md`)
- [x] 두 매니페스트의 버전이 0.8.1이다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)

**통과 조건**
- 완료 조건 7, 8이 참이다.
  - 확인: 완료 조건 7, 8의 확인을 모두 돌린다

## 한 일
- `docs/LESSONS.md`의 하네스의 문제점 절에서 이 작업이 다룬 17줄(앞이 `(004-context-rules, 검증 1)`인 셋, `(006-verify, phase 1)`~`(006-verify, phase 6)`인 열하나, `(006-verify, 검증 1)`인 셋)이 지워지고, 미룬 문제 절에서 `(006-verify, 검증 1) run 본문 "검증을 맡긴다"의 첫 갈래는 …` 줄이 지워진다. 이 작업을 실행하며 더해진 줄과 다른 줄은 그대로다: 하네스의 문제점 절의 10~26행(17줄)과 미룬 문제 절의 run 첫 갈래 줄을 지웠다. 하네스의 문제점 절에는 `(007-harness-issues, phase 2)` 세 줄만 남았고, 프로젝트에서 배운 것 절과 미룬 문제 절의 나머지 다섯 줄은 그대로다 (`docs/LESSONS.md`)
- 두 매니페스트의 버전이 0.8.1이다: 두 파일의 `"version": "0.8.0",`을 `"version": "0.8.1",`로 바꿨다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)

## 확인 결과
- 완료 조건 7, 8이 참이다.
  - 완료 조건 7: `git diff 1f8e2ab -- docs/LESSONS.md | grep '^-- '` → 18줄. `(006-verify, phase 1)`~`(006-verify, phase 6)` 열하나, `(004-context-rules, 검증 1)` 셋, `(006-verify, 검증 1)` 계획을 가리킨 셋(phase 5, 완료 조건 12, 완료 조건 4)으로 하네스의 문제점 절에 있던 17줄과, 미룬 문제 절의 `(006-verify, 검증 1) run 본문 "검증을 맡긴다"의 첫 갈래는 …` 줄이다. 같은 diff의 `^+` 줄은 이 작업 phase 2가 더한 `(007-harness-issues, phase 2)` 세 줄뿐이다. 통과
  - 완료 조건 8: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.8.1",`. 통과

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
없음

## 회고 1: 확인만

**확인**
- 완료 조건 7, 8이 참이다.
  - 완료 조건 7: `git diff 1f8e2ab -- docs/LESSONS.md | grep '^-- '` → 18줄. `1f8e2ab`의 LESSONS에서 하네스의 문제점 절 10~26행에 있던 17줄(`(006-verify, phase 1)`~`(006-verify, phase 6)` 열하나, `(004-context-rules, 검증 1)` 셋, `(006-verify, 검증 1)` 셋)과 미룬 문제 절의 `(006-verify, 검증 1) run 본문 "검증을 맡긴다"의 첫 갈래는 …` 줄이다. 같은 diff의 더한 줄은 `(007-harness-issues, phase 2)` 세 줄뿐이고, 프로젝트에서 배운 것 절 네 줄과 미룬 문제 절의 나머지 다섯 줄은 그대로다. 통과
  - 완료 조건 8: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.8.1",`. 통과

**문제**
- 없음

**판정**: 통과
