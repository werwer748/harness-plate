# Phase 1: 명령 절의 설치 줄

**목표**: 명령 절이 설치, 빌드, 린트, 테스트 네 줄로 정의되고, plan이 설치 명령도 챙기며, 이 저장소의 명령 절에 설치 줄이 생긴다.

**테스트 먼저**: 아니오 — 스킬 본문과 문서(`.md`)만 고친다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (낱말의 명령 절, 3번의 명령 찾기, 5번의 물음, 적는 규칙의 명령 절 고침)
- `plugins/plate/skills/check/SKILL.md` (낱말의 명령 절, 3번)
- `plugins/plate/skills/retro/SKILL.md` (낱말의 명령 절, 3번)
- `plugins/plate/skills/review/SKILL.md` (낱말의 명령 절, 2번)
- `docs/ARCHITECTURE.md` (`## 명령` 절)

**TODO**
- [ ] 명령 절의 정의가 설치, 빌드, 린트, 테스트 네 줄이 되고, 없는 명령은 "없음"이다 (`plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/review/SKILL.md`의 낱말)
- [ ] plan이 명령 절을 볼 때 설치 명령도 빌드 매니페스트와 코드에서 찾고, 찾지 못하면 묻는다 (`plugins/plate/skills/plan/SKILL.md`의 3번, 5번)
- [ ] check, retro, tasks 끝의 review는 설치 명령을 돌리지 않는다고 적힌다 (`plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/review/SKILL.md`)
- [ ] 이 저장소의 명령 절에 `- 설치: 없음` 줄이 생긴다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: 완료 조건 1의 확인을 모두 돌린다
