#!/bin/bash
# constitution — SessionStart
# 막는 실패: 하네스의 절대 규칙이 세션에 실리지 않아 지켜지지 않는 것.
#   플러그인 루트의 CLAUDE.md·AGENTS.md는 컨텍스트에 자동으로 실리지 않는다.
# 동작: 세션이 시작될 때(새 세션, 재개, /clear, 압축 뒤) 플러그인의 AGENTS.md를 그대로 출력한다.
#   SessionStart 훅의 stdout은 첫 프롬프트 앞에 컨텍스트로 들어간다.
# 한계: 메인 세션에만 실린다(서브에이전트에는 실리지 않는다).
#   출력이 10,000자를 넘으면 Claude Code가 본문 대신 파일 경로와 앞 2,000자만 넣는다.

cat "$(dirname "$0")/../AGENTS.md"
