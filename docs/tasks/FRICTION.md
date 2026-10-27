# FRICTION

- `001-run-rules` 문제: run 본문 8번이 계획 커밋을 찾는 명령으로 적은 `git log … $(git log -1 --format=%h -- …/retro.md)..HEAD …`의 명령 치환은 헤드리스 Claude Code에서 승인 요구로 막혀(장면 D, phase 3의 "하네스에서 걸린 것") run 메인이 나눠 불렀다. 같은 본문의 "PR을 연다"는 권한 검사가 명령 치환을 막는다고 적어 두었다
- `001-run-rules` 문제: tasks 머리와 task 머리의 결정 "이 저장소의 main을 복제"는 원본이 다른 브랜치에 있으면 복제본의 `origin/HEAD`가 그 브랜치를 가리키는 것을 다루지 않아, 장면 B에서 run과 코드 평가가 기본 브랜치를 `tasks/release-prep`으로 봤다(phase 2의 "하네스에서 걸린 것"). phase 3은 `git remote set-head origin main`으로 피했다. 002, 003의 장면도 같은 결정을 쓴다
- `001-run-rules` 문제: task 머리의 장면 B 정의가 "phase가 모두 통과하고 회고가 없는 작은 tasks"만 적고 그 tasks가 회고를 통과해야 tasks 끝에 닿는다는 것을 적지 않아, 첫 차림이 회고에서 멈춰 다시 차렸다(phase 2의 "계획과 달라진 점")
- `001-run-rules` 문제: 장면 C의 계획 고칠 안 승인 뒤(계획 커밋, 계획 커밋으로 고친 문제만 남아 TODO 없는 고칠 phase)는 돌려 보지 않았다. run 8번은 첫머리의 "계획을 바꿔야 하는지" 판정 뒤에 계획 커밋으로 고친 문제를 거르는 순서라, 다시 8번에 들어올 때 같은 문제로 다시 멈추지 않는지는 글로만 읽었다
- `001-run-rules` 스킬 후보: phase 2·3에서 장면마다 `mktemp -d` 복제, `git remote set-head origin main`, `tasks/<이름>` 브랜치에 run이 만들 꼴의 커밋(phase 수행·확인·통과, 회고, `RUNLOG`)을 손으로 넣어 차리기, `--plugin-dir`와 허용 목록을 붙인 `claude -p … --output-format stream-json`, 결과 jsonl에서 Agent 호출·세션 id·`duration_ms`를 뽑아 `docs/TOOLS.md` 장면 절의 필드로 옮기기를 되풀이했다. 장면 차림과 필드 뽑기를 스킬로 만들면 002·003의 장면 다섯도 이 손일이 줄어든다
- `001-run-rules` 경계 밖: run 1번의 권한 확인은 도구가 지금 모드를 알려 주지 않으면 묻지 않고 지나가, 헤드리스 acceptEdits 세션(장면 B·C·D)은 모두 "확인할 수 없음" 갈래로 갔다. 완료 조건 1이 정한 경계 안이지만, 모드를 알 수 없는 세션에서 `plugins/plate/skills/` 같은 막히는 경로를 계획이 고치면 #40의 막힘이 그대로 남으므로 약속을 넓힐지 볼 거리다
