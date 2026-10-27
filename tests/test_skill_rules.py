"""release-prep tasks가 고친 스킬 규칙의 글이 본문의 제자리에 남아 있는지 시험한다.

이슈마다(run의 #34·#35·#38·#40·#44·#46·#47·#48·#51, plan의 #37·#41·#46·#52·#53, phase의 #42·#51, check의 #51,
retro의 #49·#50·#51, review의 #51, eval의 #36·#50·#51) 그 규칙을 이루는
글이 그 본문의 그 절에 있는지 본다. 글이 빠지거나 다른 절로 옮겨지면 실패한다.
모든 스킬의 앞머리가 Agent Skills 규격의 한도(description 1024자, name 64자) 안에 있는지도 본다.
"""

import re
import unittest
from pathlib import Path

SKILLS = Path(__file__).resolve().parent.parent / "plugins" / "plate" / "skills"


def read(skill):
    return (SKILLS / skill / "SKILL.md").read_text(encoding="utf-8")


def section(text, heading):
    """`## {heading}` 절의 본문(다음 `## ` 절 앞까지)을 돌려준다. 코드 블록 안의 `## `은 건너뛴다."""
    fence = None
    start = False
    out = []
    for line in text.split("\n"):
        marker = re.match(r"^(`{3,})", line)
        if marker:
            if fence is None:
                fence = marker.group(1)
            elif line.strip() == fence:
                fence = None
        elif fence is None and line.startswith("## "):
            if start:
                break
            if line[3:].strip() == heading:
                start = True
                continue
        if start:
            out.append(line)
    if not start:
        raise AssertionError("절이 없다: ## %s" % heading)
    return "\n".join(out)


def subsection(text, heading):
    """`## {heading}`이나 `### {heading}` 절의 본문(같은 깊이나 더 얕은 다음 머리 앞까지)을 돌려준다.
    코드 블록 안의 머리는 건너뛴다."""
    fence = None
    level = None
    out = []
    for line in text.split("\n"):
        marker = re.match(r"^(`{3,})", line)
        head = re.match(r"^(#{2,3}) (.*)$", line) if fence is None else None
        if marker:
            if fence is None:
                fence = marker.group(1)
            elif line.strip() == fence:
                fence = None
        elif head:
            depth = len(head.group(1))
            if level is not None and depth <= level:
                break
            if level is None and head.group(2).strip() == heading:
                level = depth
                continue
        if level is not None:
            out.append(line)
    if level is None:
        raise AssertionError("절이 없다: %s" % heading)
    return "\n".join(out)


def part(body, name):
    """절 안의 `**{name}**` 줄에서 다음 굵은 머리 줄 앞까지를 돌려준다."""
    match = re.search(r"^\*\*%s\*\*\n(.*?)(?=^\*\*[^*\n]+\*\*$|\Z)" % re.escape(name), body, re.S | re.M)
    if match is None:
        raise AssertionError("굵은 머리가 없다: **%s**" % name)
    return match.group(1)


def front_matter(skill):
    """`SKILL.md` 앞머리(`---`와 `---` 사이)의 `키: 값` 줄을 사전으로 돌려준다."""
    lines = read(skill).split("\n")
    if lines[0] != "---":
        raise AssertionError("앞머리가 없다: %s" % skill)
    fields = {}
    for line in lines[1:]:
        if line == "---":
            return fields
        key, sep, value = line.partition(": ")
        if not sep or not re.match(r"^[a-z-]+$", key):
            raise AssertionError("한 줄 `키: 값` 꼴이 아닌 앞머리 줄이다(%s): %r" % (skill, line))
        fields[key] = value
    raise AssertionError("앞머리가 닫히지 않았다: %s" % skill)


def skill_names():
    return sorted(p.parent.name for p in SKILLS.glob("*/SKILL.md"))


class DescriptionTest(unittest.TestCase):
    """Agent Skills 규격의 한도를 본다. Codex는 1024자를 넘는 description을 잘라 끝의 부르는 말과
    쓰지 않을 때를 모델에게 싣지 않는다(release-prep의 코드 평가 1, run이 1142자였다)."""

    def test_skills_exist(self):
        self.assertGreaterEqual(len(skill_names()), 10)

    def test_description_at_most_1024_chars(self):
        for skill in skill_names():
            with self.subTest(skill=skill):
                description = front_matter(skill)["description"]
                self.assertTrue(description.strip(), "description이 비었다")
                self.assertLessEqual(len(description), 1024)

    def test_name_matches_folder_and_limit(self):
        for skill in skill_names():
            with self.subTest(skill=skill):
                name = front_matter(skill)["name"]
                self.assertEqual(name, skill)
                self.assertLessEqual(len(name), 64)

    def test_description_ends_with_when_not_to_use(self):
        # 길이를 줄이다 끝의 "쓰지 않는다" 문장을 잃으면 실패한다.
        for skill in skill_names():
            with self.subTest(skill=skill):
                self.assertRegex(front_matter(skill)["description"], r"쓰지 않는다\.$")

    def test_run_description_keeps_triggers(self):
        description = front_matter("run")["description"]
        for phrase in ('"실행해줘"', '"phase 진행하자"', '"이어서 하자"', '"끝까지 돌려줘"', "계획이 없는 요청에는 쓰지 않는다"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, description)


class RunRulesTest(unittest.TestCase):
    def setUp(self):
        self.text = read("run")

    def test_34_plan_fix_answers_are_logged_as_stop(self):
        body = section(self.text, "`RUNLOG.md`")
        self.assertIn('"멈춘다"에서 물은 것은 계획을 고칠 안의 승인까지 모두 `멈춤`이다', body)
        self.assertIn("멈춘 자리에서 물은 것도 `멈춤`이고 `고칠 phase`가 아니다", body)
        self.assertIn("`고칠 phase`는 8번에서 task 하나씩의 고칠 phase 안을 물은 것뿐이다", body)

    def test_35_unknown_time_has_no_unit(self):
        body = section(self.text, "`RUNLOG.md`")
        self.assertIn("돌아오지 않은 값은 단위 없이 `모름`으로 적는다", body)
        self.assertIn("`시간 모름초`가 아니다", body)

    def test_38_fix_phase_todo_includes_docs(self):
        body = section(self.text, "8. 고칠 phase를 더한다")
        self.assertIn("고칠 동작을 적은 맥락 문서와 README의 줄도 그 TODO에 넣는다", body)

    def test_38_narrowing_the_plan_stops(self):
        body = section(self.text, "8. 고칠 phase를 더한다")
        self.assertIn("목표나 완료 조건을 바꾸거나 좁혀야 하는지 본다", body)
        self.assertIn('실행 방식과 상관없이 "멈춘다"로 간다', body)
        stop = section(self.text, "멈춘다")
        self.assertIn("회고의 문제를 고치려면 계획 파일(tasks 머리, task 머리)의 목표나 완료 조건을 바꾸거나 좁혀야 한다(8번)", stop)

    def test_40_permission_check_before_first_agent(self):
        body = section(self.text, "1. 시작 조건을 본다")
        self.assertIn("먼저 권한을 본다", body)
        self.assertIn("첫 에이전트를 띄우기 전에 한 번 본다", body)
        self.assertIn("plan 모드가 켜져 있거나", body)
        self.assertIn("물은 자리가 `권한`인 줄을 더한다", body)
        self.assertIn("`권한`", section(self.text, "`RUNLOG.md`"))

    def test_44_runlog_commit_after_retro(self):
        body = section(self.text, "7. task 회고를 맡긴다")
        self.assertIn("그 자리에서 `RUNLOG.md`만 한 커밋으로 넣는다", body)
        self.assertIn("메시지는 `NNN-slug: RUNLOG`다", body)

    def test_tools_md_commit_rule_in_one_place(self):
        # 커밋 자리마다 같은 괄호 글을 되풀이하지 않고 "`RUNLOG.md`" 절 한 곳에 둔다(release-prep 코드 평가 1의 소스 문제 2).
        rule = "아직 커밋하지 않은 `docs/TOOLS.md`"
        self.assertEqual(self.text.count(rule), 1)
        runlog = section(self.text, "`RUNLOG.md`")
        self.assertIn(rule + "는 이 스킬이 `RUNLOG.md`를 넣는 커밋마다 함께 넣는다", runlog)
        follow = '(사용량 까닭을 적은 `docs/TOOLS.md`는 "`RUNLOG.md`" 절을 따른다)'
        for heading in ("6. 통과한 phase의 이름을 바꾼다", "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "멈춘다", "코드 평가를 맡긴다", "하네스 eval을 맡긴다", "비운다"):
            with self.subTest(heading=heading):
                self.assertIn(follow, subsection(self.text, heading))

    def test_44_runlog_commit_after_review_and_eval(self):
        runlog = section(self.text, "`RUNLOG.md`")
        self.assertIn("그 자리에서 `RUNLOG.md`만 넣는 커밋으로 넣는다", runlog)
        end = section(self.text, "tasks 끝")
        self.assertEqual(end.count("그 자리에서 `RUNLOG.md`만 한 커밋으로 넣는다"), 2)


    def test_46_fix_file_checked_by_time_or_hash_stops(self):
        body = section(self.text, "8. 고칠 phase를 더한다")
        self.assertIn("고칠 파일이 task 머리나 tasks 머리의 완료 조건이 돌린 시각이나 본문 해시로 보는 파일이면", body)
        self.assertIn("고친 뒤 그 확인을 다시 참으로 둘 길(고친 본문으로 다시 돌리는 TODO나 phase)이 계획에 있는지도 본다", body)
        self.assertIn("이 경우도 계획을 바꾸게 하는 문제다", body)
        stop = section(self.text, "멈춘다")
        self.assertIn("고칠 파일이 완료 조건이 돌린 시각이나 본문 해시로 보는 파일인데 고친 뒤 그 확인을 다시 참으로 둘 길이 계획에 없을 때도 든다(8번)", stop)

    def test_47_no_command_substitution_in_git_commands(self):
        self.assertIsNone(re.search(r"git[^`\n]*\$\(", self.text))
        body = section(self.text, "8. 고칠 phase를 더한다")
        self.assertIn("먼저 `git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md`로 마지막 회고 절을 더한 커밋의 해시를 얻고", body)
        self.assertIn("그 해시를 넣어 `git log --format='%h %s' {해시}..HEAD -- docs/tasks/`를 따로 불러 찾는다", body)
        terms = section(self.text, "낱말")
        self.assertIn("먼저 `git merge-base {기본 브랜치} HEAD`로 갈라진 곳의 해시를 얻고", terms)
        self.assertIn("그 해시를 넣어 `git diff --name-only {해시} HEAD`를 따로 부른다", terms)

    def test_48_one_decision_line_per_plan_fix(self):
        body = section(self.text, "멈춘다")
        self.assertIn("계획 수정마다 결정 줄 하나다", body)
        self.assertIn("커밋하기 전에 이번 수정의 결정 줄이 task 머리(tasks 머리를 고쳤으면 tasks 머리에도)에 있는지 보고", body)
        self.assertLess(body.index("커밋하기 전에 이번 수정의 결정 줄이"), body.index("고친 계획 파일과 `RUNLOG.md`만 커밋한다"))

    def test_51_marker_line_ends_every_hand_off_block(self):
        for heading in ("4. 수행을 맡긴다", "5. 확인을 맡긴다", "7. task 회고를 맡긴다", "코드 평가를 맡긴다", "하네스 eval을 맡긴다"):
            with self.subTest(heading=heading):
                blocks = re.findall(r"^```\n(.*?)\n```$", subsection(self.text, heading), re.S | re.M)
                self.assertEqual(len(blocks), 1)
                self.assertEqual(blocks[0].split("\n")[-1], "부른 쪽: plate:run")
        self.assertIn("`고칠 문제:` 줄은", section(self.text, "4. 수행을 맡긴다"))
        self.assertIn("**표지 줄**: 맡기는 글 코드 블록의 마지막 줄 `부른 쪽: plate:run`", section(self.text, "낱말"))

class PlanRulesTest(unittest.TestCase):
    def setUp(self):
        self.text = read("plan")

    def test_37_branch_checks_in_conditions(self):
        body = part(section(self.text, "적는 규칙"), "조건")
        self.assertIn("갈래마다 그 갈래를 차려 돌리는 확인을 둔다", body)
        self.assertIn("그 줄이 담아야 할 갈래", body)
        self.assertIn("`git clone --bare`로 만든 저장소로 채우고", body)
        self.assertIn("푸시로 채우지 않는다", body)

    def test_37_draft_check(self):
        body = section(self.text, "6. 초안을 보여 주고 승인받는다")
        self.assertIn("갈래마다 돌리는 확인이 있는지 본다", body)

    def test_41_conditions_from_earlier_phase_output(self):
        body = part(section(self.text, "적는 규칙"), "TODO")
        self.assertIn('"앞 phase의 산출물에 대어 조건을 맞춘다"', body)
        self.assertIn('"앞 phase의 결과로 정한다"', body)
        draft = section(self.text, "6. 초안을 보여 주고 승인받는다")
        self.assertIn("뒤 phase의 실행 조건(허용 목록, 차례)이 앞 phase의 산출물의 동작에 기대는지 본다", draft)


    def test_46_rerun_results_compared_by_body_hash(self):
        body = part(section(self.text, "적는 규칙"), "조건")
        self.assertIn("돌려 본 결과가 지금 본문의 것인지는 커밋 시각이 아니라 돌릴 때 적은 본문 해시(`git hash-object <경로>`)와 `git rev-parse HEAD:<경로>`로 견준다", body)

    def test_52_earlier_task_changes_named_by_section_and_text(self):
        body = part(section(self.text, "적는 규칙"), "phase의 파일")
        self.assertIn("앞 task의 변경에 기대면 이슈 번호만으로 가리키지 않고, 그 파일의 경로와 절 이름과 바뀐 글을 찾을 수 있게 적는다", body)

    def test_53_draft_check_for_run_scenes(self):
        body = section(self.text, "6. 초안을 보여 주고 승인받는다")
        self.assertIn("돌려 보는 확인(임시 복제본이나 시험 저장소에서 스킬과 장면을 돌리는 확인)마다 세 가지를 본다", body)
        self.assertIn("그 차림이 앞 단계(예: 회고 통과, 고칠 것이 나오는 자리)를 지나 기대한 자리에 닿는지", body)
        self.assertIn("기대가 해결 방식이 아니라 관찰할 결과로 적혔는지", body)
        self.assertIn("결정과 TODO가 같은 멈출 자리를 말하는지", body)

class PhaseRulesTest(unittest.TestCase):
    def test_42_does_not_read_earlier_phase_records(self):
        body = section(read("phase"), "1. 읽는다")
        self.assertIn("앞 phase의 결과가 필요하면 계획의 읽을 것에 적힌 산출물 파일만 읽는다", body)
        self.assertIn("필요하면 읽지 않고, 무엇이 왜 필요했는지를", body)


REPORT_SECTIONS = (
    ("phase", "6. 다섯 줄을 돌려준다"),
    ("check", "8. 세 줄을 돌려준다"),
    ("retro", "9. 세 줄을 돌려준다"),
    ("review", "9. 네 줄을 돌려준다"),
    ("eval", "8. 세 줄을 돌려준다"),
)


class CallerMarkerTest(unittest.TestCase):
    """#51: run이 띄운 호출은 표지 줄이나 작업 트리의 스킬 줄로 가르고, 둘 다 없을 때만 직접 부른 꼴로 보고한다."""

    def test_51_direct_report_only_without_marker(self):
        for skill, heading in REPORT_SECTIONS:
            with self.subTest(skill=skill):
                body = section(read(skill), heading)
                self.assertIn("맡은 글에 `부른 쪽: plate:run` 줄도 작업 트리의 스킬 줄", body)
                self.assertIn("`작업 트리의 {경로}를 읽어 그 절차를 따른다.`로 시작하는 줄)도 없을 때만 사용자가 직접 부른 것으로 보고", body)
                self.assertNotIn("사용자가 직접 불렀으면", body)


class RetroRulesTest(unittest.TestCase):
    def test_49_friction_problem_only_for_remaining_lines_judged_problem(self):
        body = section(read("retro"), "5. tasks 끝에 볼 것을 모은다")
        self.assertIn('확인 절 "하네스에서 걸린 것"의 `남은 것:`으로 시작하는 줄은 이번 회고 절 "남은 것"에서 "문제"로 판정한 것만 모으고', body)
        self.assertIn('"문제 아님"으로 판정한 줄은 모으지 않는다', body)

    def test_50_stop_list_includes_permission(self):
        body = section(read("retro"), "5. tasks 끝에 볼 것을 모은다")
        self.assertIn("물은 자리가 `멈춤`이 아닌 줄(권한, 실행 방식,", body)


class EvalRulesTest(unittest.TestCase):
    def test_50_runlog_commits_in_rule_table(self):
        body = section(read("eval"), "3. 기준마다 근거를 적고 등급을 매긴다")
        for message in ("`NNN-slug: RUNLOG`", "`<tasks 이름>: RUNLOG`"):
            with self.subTest(message=message):
                self.assertIn("| %s | run | `RUNLOG.md`와 사용량 까닭을 적은 `docs/TOOLS.md` |" % message, body)

    def test_50_permission_is_a_set_question(self):
        body = section(read("eval"), "낱말")
        self.assertIn("모두(`권한`, `실행 방식`,", body)

    def test_36_moved_remaining_lines_count_only_when_retro_says_problem(self):
        body = section(read("eval"), "2. 실패를 모아 MAST 유형으로 나눈다")
        self.assertIn("`남은 것:`으로 시작하는 줄", body)
        self.assertIn('"문제"로 판정된 것만 실패로 센다', body)
        self.assertIn('"문제 아님"으로 판정됐거나 회고가 모으지 않은 줄은 실패가 아니다', body)


if __name__ == "__main__":
    unittest.main()
