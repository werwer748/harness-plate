#!/usr/bin/env python3
"""plate의 푸시 훅. Claude Code의 PreToolUse(Bash)에서 돈다.

막는 실패: 에이전트가 끝의 평가와 보고까지 가지 않은 변경을 기본 브랜치에 푸시하는 것.
Bash 명령을 `&&`, `||`, `;`, `|`, 줄바꿈으로 나눠 그 안의 `git push`가 origin의 기본 브랜치를
바꾸거나 지우면 종료 코드 2로 끝나고 stderr의 글이 에이전트에게 간다. heredoc의 본문은 명령으로 보지 않는다.
사람의 푸시는 보지 않는다.
"""

import fnmatch
import json
import os
import re
import shlex
import sys

from edit_guard import git, is_setup

REMOTE = "origin"
PUNCTUATION = "();<>|&\n"
SEPARATORS = set("();|&\n")
ASSIGNMENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
GIT_ARG_OPTIONS = {"-c", "--git-dir", "--work-tree", "--namespace", "--config-env"}
PUSH_ARG_OPTIONS = {"-o", "--push-option", "--repo", "--receive-pack", "--exec"}
REFSPEC_OPTIONS = {  # refspec을 적은 것과 같은 옵션
    "--all": "refs/heads/*",
    "--branches": "refs/heads/*",
    "--mirror": "refs/*",
    "--tags": "refs/tags/*",
}

BLOCK = (
    "plate: 기본 브랜치(`{branch}`)로 푸시하지 않는다: `{command}`\n"
    "끝의 평가와 보고까지 가지 않은 변경이 기본 브랜치에 들어가지 않게 한다. "
    "다른 브랜치로 푸시하고, 기본 브랜치로 합치는 것은 사용자에게 맡긴다.\n"
)


def lexer(text):
    lex = shlex.shlex(text, posix=True, punctuation_chars=PUNCTUATION)
    lex.whitespace = " \t\r"
    lex.whitespace_split = True
    lex.commenters = ""
    return lex


def without_heredocs(command):
    """heredoc의 본문 줄을 뺀 명령 글. 본문은 명령이 아니라 그 명령의 입력이다."""
    out, pending, quote, i = [], [], None, 0
    while i < len(command):
        c = command[i]
        if c == "\\" and quote != "'":  # 뒤의 글자는 따옴표나 `<<`로 읽지 않는다
            out.append(command[i:i + 2])
            i += 2
            continue
        if quote:
            if c == quote:
                quote = None
        elif c in "'\"":
            quote = c
        elif command.startswith("<<", i) and not command.startswith("<<<", i) and command[i - 1:i] != "<":
            strip = command.startswith("<<-", i)  # `<<-`는 본문과 끝 줄 앞의 탭을 뺀다
            j = i + (3 if strip else 2)
            pending.append((lexer(command[j:]).get_token(), strip))
            out.append(command[i:j])
            i = j
            continue
        elif c == "\n" and pending:
            out.append(c)
            i += 1
            for delimiter, strip in pending:  # 본문은 `<<`가 있는 줄의 다음 줄부터 끝 줄까지다
                while i < len(command):
                    end = command.find("\n", i)
                    end = len(command) if end < 0 else end
                    line, i = command[i:end], end + 1
                    if (line.lstrip("\t") if strip else line) == delimiter:
                        break
            pending = []
            continue
        out.append(c)
        i += 1
    return "".join(out)


def segments(command):
    """명령 글을 단순 명령마다의 낱말 목록으로 나눈다. heredoc의 본문, 리다이렉션과 그 대상은 뺀다."""
    try:
        tokens = list(lexer(without_heredocs(command)))
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
    """push 뒤의 낱말에서 (지우는가, 위치 인자 목록, 옵션이 정한 refspec 목록)을 돌려준다."""
    delete, positional, implied = False, [], []
    i = 0
    while i < len(args):
        arg = args[i]
        i += 1
        if arg == "--":
            positional += args[i:]
            break
        if arg == "--delete":
            delete = True
        elif arg in REFSPEC_OPTIONS:
            implied.append(REFSPEC_OPTIONS[arg])
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
    return delete, positional, implied


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


def target_refs(refspecs, delete, branch):
    """refspec마다 원격에서 바뀌거나 지워질 ref. `*`가 든 것은 ref 이름 전체에 견주는 꼴이다."""
    for spec in refspecs:
        spec = spec[1:] if spec.startswith("+") else spec
        if spec == ":":  # 양쪽에 같은 이름으로 있는 브랜치를 모두 보낸다
            spec = "refs/heads/*"
        dst = spec if delete else spec.split(":", 1)[-1]
        if dst in ("HEAD", "@"):
            dst = branch or dst
        if dst:
            yield dst if dst.startswith("refs/") or "*" in dst else "refs/heads/" + dst


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
    delete, positional, implied = push_args(args)
    branch = current_branch(root)
    remote = positional[0] if positional else configured_remote(root, branch)
    if remote != REMOTE:
        return None
    default = default_branch(root)
    refspecs = positional[1:] + implied
    if not refspecs:
        return default if branch == default and not delete else None
    ref = "refs/heads/" + default
    if any(fnmatch.fnmatchcase(ref, target) for target in target_refs(refspecs, delete, branch)):
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
