# Phase 2: run의 LESSONS와 닫힌 검증

**목표**: run이 LESSONS에 같은 뜻의 줄을 겹쳐 넣지 않고, 옛 셋업에서는 위치를 묻고, 닫힌 검증을 다시 만나도 "통과하면"의 1번부터 하며, 옛 셋업의 시험 폴더에서 묻고 멈추는 것이 확인된다.

**읽을 것**
- `docs/LESSONS.md` (하네스의 문제점 절의 `(006-verify, phase 2)` 다섯째 줄(같은 사실이 두 줄)과 `(006-verify, phase 3)` 첫째 줄(옛 셋업), 미룬 문제 절의 `(006-verify, 검증 1)` 마지막 줄(첫 갈래의 결함))
- `plugins/plate/skills/run/SKILL.md` ("검증을 맡긴다"와 "`docs/LESSONS.md`" 절)
- `plugins/plate/skills/setup/SKILL.md` ("문서 지도 구간" 절: 지금의 지도 위의 글)
- `~/plate-rail-test/bin/vfmake.sh` (시험 폴더를 만드는 꼴과 `vrule-base`)
- `~/plate-rail-test/bin/run.sh` (헤드리스 실행의 꼴과 허용 목록)
- `~/plate-rail-test/answers/run-vrule.md` (run에 줄 글 `001`)
- `docs/TOOLS.md` ("Claude Code" 절의 헤드리스 실행과 권한)

**TODO**
- [ ] run "`docs/LESSONS.md`" 절에서, 옮길 줄과 같은 뜻의 줄이 LESSONS의 같은 절에 이미 있으면 더하지 않는다. 회고 절과 검증 절에서 옮길 때 모두, 다른 작업에서 옮긴 줄과 겹칠 때도 같다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] run "`docs/LESSONS.md`" 절에서, 문서 지도 위의 글에 "하네스의 스킬이 위치를 정해 둔 기록은 묻지 않고"가 없는 프로젝트에서 LESSONS를 처음 만들 때는 위치를 묻고, `docs/LESSONS.md`를 추천안으로 내며, setup을 다시 돌리면 다음부터 묻지 않는다고 함께 알린다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] run "검증을 맡긴다"의 첫 갈래가, 닫힌 검증이면 맡기지 않고 "통과하면"의 1번부터 하게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `bin/vfmake.sh`가 시험 폴더 `run-oldsetup`을 만든다. `vrule-base`에 `docs/LESSONS.md`와 문서 지도의 LESSONS 행을 지운 커밋을 얹은 것이다 (`~/plate-rail-test/bin/vfmake.sh`)
- [ ] run과 verify의 본문을 마지막으로 고친 뒤 `run-oldsetup`에서 `/plate:run 001`을 헤드리스로 한 턴 돌린 기록이 `logs/run-oldsetup.jsonl`에 있다. run은 검증이 `verify.md`를 커밋한 뒤 LESSONS를 만들기 전에 위치를 묻고 멈췄고, `docs/LESSONS.md`도 지도의 행도 생기지 않았다 (`~/plate-rail-test/bin/run.sh`)

**통과 조건**
- 완료 조건 4, 5, 6이 참이다.
  - 확인: 완료 조건 4, 5, 6의 확인을 모두 돌린다
