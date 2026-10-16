# Phase 5: 검증 2의 문제를 고친다

**목표**: 검증 2에서 나온 문제를 모두 고친다.

**읽을 것**
- `docs/tasks/007-harness-issues/verify.md`의 `## 검증 2` 절
- `plugins/plate/skills/run/SKILL.md`

**TODO**
- [ ] run 본문 "`docs/LESSONS.md`" 절의 "문서 지도"(273행)는 옛 셋업에서 LESSONS를 처음 만들기 전에 위치를 묻고 `docs/LESSONS.md`를 추천안으로 내지만, 사용자가 추천안이 아닌 위치를 답했을 때 무엇을 하는지는 본문에 없다. 본문의 나머지는 그 문서를 모두 `docs/LESSONS.md`로 가리킨다: 절대 규칙 5(20행)가 직접 고치는 파일을 `docs/LESSONS.md`로 한정하고, 6번(129, 131행), "통과하면"(177, 179행), 같은 뜻의 줄을 거르는 247행, 이미 옮겼는지 보는 248행의 `git log -S'(NNN-slug, 검증 ' -- docs/LESSONS.md`, 지도에 더할 행(276행)이 모두 그 경로다. 그래서 다른 위치를 고르면 run은 절대 규칙 5로 그 파일을 고치지 못하고, 적힌 대로 따르면 지도에 더하는 행이 고른 위치를 가리키지 않으며, 248행의 명령은 고른 위치의 이력을 보지 않아 이 작업이 막은 "옮긴 뒤 지운 줄이 돌아온다"가 그 프로젝트에서는 다시 난다. 다시 돌린 `run-oldsetup`의 물음도 "다른 위치가 좋으면 그 경로를 알려 주세요"라고 다른 답을 청했다(`~/plate-rail-test/logs/run-oldsetup.jsonl`) (`plugins/plate/skills/run/SKILL.md` 20행, 273행)

**통과 조건**
- 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
