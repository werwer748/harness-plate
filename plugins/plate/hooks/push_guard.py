#!/usr/bin/env python3
"""plate의 푸시 훅. Claude Code의 PreToolUse(Bash)에서 돈다.

막는 실패: 에이전트가 끝의 평가와 보고까지 가지 않은 변경을 기본 브랜치에 푸시하는 것.
Bash 명령을 `&&`, `||`, `;`, `|`, 줄바꿈으로 나눠 그 안의 `git push`가 origin의 기본 브랜치를
바꾸거나 지우면 종료 코드 2로 끝나고 stderr의 글이 에이전트에게 간다. 사람의 푸시는 보지 않는다.
"""

import json
import os
import re
import shlex
import sys

from edit_guard import git, is_setup

REMOTE = "origin"
SEPARATORS = set("();|&\n")
ASSIGNMENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
GIT_ARG_OPTIONS = {"-c", "--git-dir", "--work-tree", "--namespace", "--config-env"}
PUSH_ARG_OPTIONS = {"-o", "--push-option", "--repo", "--receive-pack", "--exec"}

BLOCK = (
    "plate: 기본 브랜치(`{branch}`)로 푸시하지 않는다: `{command}`\n"
    "끝의 평가와 보고까지 가지 않은 변경이 기본 브랜치에 들어가지 않게 한다. "
    "다른 브랜치로 푸시하고, 기본 브랜치로 합치는 것은 사용자에게 맡긴다.\n"
)


def segments(command):
    """명령 글을 단순 명령마다의 낱말 목록으로 나눈다. 리다이렉션과 그 대상은 뺀다."""
    lex = shlex.shlex(command, posix=True, punctuation_chars="();<>|&\n")
    lex.whitespace = " \t\r"
    lex.whitespace_split = True
    lex.commenters = ""
    try:
        tokens = list(lex)
    except ValueError:  # 닫히지 않은 따옴표: 셸도 돌리지 않는다
        return []
    parts, words, skip = [], [], False
    for token in tokens:
        if skip:
            skip = False
        elif set(token) <= SEPARATORS:
            parts.append(words)
            words = []
        elif set(token) <= set("<>&|") and ("<" in token or ">" in token):
            if words and words[-1].isdigit():  # `2>&1`의 `2`
                words.pop()
            skip = True
        else:
            words.append(token)
    parts.append(words)
    return [words for words in parts if words]


def push_call(words, cwd):
    """`git push` 꼴이면 (git이 도는 폴더, push 뒤의 낱말)을, 아니면 None을 돌려준다."""
    i = 0
    while i < len(words) and ASSIGNMENT.match(words[i]):
        i += 1
    if i >= len(words) or os.path.basename(words[i]) != "git":
        return None
    i += 1
    folder = cwd
    while i < len(words) and words[i].startswith("-"):
        option = words[i]
        i += 1
        if option == "-C" and i < len(words):
            folder = os.path.join(folder, os.path.expanduser(words[i]))
            i += 1
        elif option in GIT_ARG_OPTIONS:
            i += 1
    if i >= len(words) or words[i] != "push":
        return None
    return folder, words[i + 1:]


def push_args(args):
    """push 뒤의 낱말에서 (지우는가, 위치 인자 목록)을 돌려준다."""
    delete, positional = False, []
    i = 0
    while i < len(args):
        arg = args[i]
        i += 1
        if arg == "--":
            positional += args[i:]
            break
        if arg == "--delete":
            delete = True
        elif arg in PUSH_ARG_OPTIONS:
            i += 1
        elif arg.startswith("--"):
            pass
        elif arg.startswith("-") and len(arg) > 1:
            for k, letter in enumerate(arg[1:]):
                if letter == "d":
                    delete = True
                elif letter == "o":  # 뒤는 -o의 값이다. 붙어 있지 않으면 다음 낱말이 값이다
                    if not arg[k + 2:]:
                        i += 1
                    break
        else:
            positional.append(arg)
    return delete, positional


def current_branch(root):
    name = git(root, "symbolic-ref", "--quiet", "--short", "HEAD")
    return name.strip() if name else None


def default_branch(root):
    """origin의 HEAD가 가리키는 브랜치. 없으면 `main`, `main`도 없으면 `master`."""
    head = (git(root, "symbolic-ref", "--quiet", "--short", "refs/remotes/origin/HEAD") or "").strip()
    if head.startswith(REMOTE + "/"):
        return head[len(REMOTE) + 1:]
    for ref in ("refs/heads/main", "refs/remotes/origin/main"):
        if git(root, "rev-parse", "--verify", "--quiet", ref) is not None:
            return "main"
    return "master"


def configured_remote(root, branch):
    """대상 없이 하는 push가 가는 원격."""
    keys = ["remote.pushDefault"]
    if branch:
        keys = ["branch.%s.pushRemote" % branch] + keys + ["branch.%s.remote" % branch]
    for key in keys:
        value = git(root, "config", "--get", key)
        if value and value.strip():
            return value.strip()
    return REMOTE


def target_branches(refspecs, delete, branch):
    """refspec마다 원격에서 바뀌거나 지워질 브랜치 이름."""
    for spec in refspecs:
        spec = spec[1:] if spec.startswith("+") else spec
        dst = spec if delete else spec.split(":", 1)[-1]
        if dst in ("HEAD", "@"):
            dst = branch or dst
        if dst.startswith("refs/heads/"):
            dst = dst[len("refs/heads/"):]
        if dst:
            yield dst


def blocked_branch(words, cwd):
    """이 단순 명령이 기본 브랜치로 가는 push면 그 브랜치 이름을, 아니면 None을 돌려준다."""
    call = push_call(words, cwd)
    if not call:
        return None
    folder, args = call
    top = git(folder, "rev-parse", "--show-toplevel") if os.path.isdir(folder) else None
    if not top or not is_setup(top.strip()):
        return None
    root = top.strip()
    delete, positional = push_args(args)
    branch = current_branch(root)
    remote = positional[0] if positional else configured_remote(root, branch)
    if remote != REMOTE:
        return None
    default = default_branch(root)
    refspecs = positional[1:]
    if not refspecs:
        return default if branch == default and not delete else None
    if default in target_branches(refspecs, delete, branch):
        return default
    return None


def check(data):
    """막으면 에이전트에게 줄 글을, 통과시키면 None을 돌려준다."""
    command = (data.get("tool_input") or {}).get("command")
    if not isinstance(command, str):
        return None
    cwd = data.get("cwd") or os.getcwd()
    for words in segments(command):
        branch = blocked_branch(words, cwd)
        if branch:
            return BLOCK.format(branch=branch, command=" ".join(words))
    return None


def main():
    message = check(json.load(sys.stdin))
    if message:
        sys.stderr.write(message)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
