#!/usr/bin/env python3
"""plate의 푸시 훅. Claude Code의 PreToolUse(Bash)에서 돈다.

막는 실패: 에이전트가 끝의 평가와 보고까지 가지 않은 변경을 기본 브랜치에 푸시하는 것.
Bash 명령을 `&&`, `||`, `;`, `|`, 줄바꿈으로 나눠 그 안의 `git push`가 origin의 기본 브랜치를
바꾸거나 지우면 종료 코드 2로 끝나고 stderr의 글이 에이전트에게 간다. heredoc의 본문과 `#` 주석은 명령으로 보지 않고,
줄 잇기(`\\`+줄바꿈)는 명령의 경계로 보지 않는다.
명령 치환(`$( … )`, 백틱)은 그 안의 따옴표, 주석, heredoc을 따로 세고, 치환 안의 push는 읽지 않는다.
따옴표가 어긋나 명령을 나누지 못하면, 셋업된 프로젝트에서 명령의 글에 `push`가 있을 때 막는다.
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
SUBSTITUTION = "$_"  # 명령 치환이 있던 자리. 치환 안의 글은 명령으로 읽지 않는다
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
UNSPLIT = (
    "plate: 따옴표의 짝을 맞추지 못해 명령을 나누지 못했고, 그 안의 push가 기본 브랜치로 가는지 볼 수 없다.\n"
    "push를 다른 명령과 잇지 말고 따로 부른다.\n"
)


def lexer(text):
    lex = shlex.shlex(text, posix=True, punctuation_chars=PUNCTUATION)
    lex.whitespace = " \t\r"
    lex.whitespace_split = True
    lex.commenters = ""
    return lex


def without_non_commands(command):
    """셸이 명령으로 읽지 않는 글을 뺀 명령 글. heredoc의 본문은 그 명령의 입력이고,
    `#` 주석은 그 줄 끝까지 버려지고, 줄 잇기(`\\`+줄바꿈)는 지워져 앞뒤가 한 명령이 된다.
    명령 치환(`$( … )`, 백틱)은 SUBSTITUTION으로 바꾼다."""
    return scan(command, 0, None)[0]


def scan(command, i, closer):
    """command를 i부터 읽어 (명령이 아닌 글을 뺀 글, 다음에 읽을 자리)를 돌려준다.
    closer가 `)`나 백틱이면 명령 치환 안이다. 따옴표, 주석, heredoc을 바깥과 따로 세다가 닫는 글자에서 끝난다."""
    scanner = Scanner(command, i, closer)
    while scanner.i < len(command) and not scanner.closed:
        scanner.step()
    return "".join(scanner.out), scanner.i


class Scanner:
    """scan이 읽는 자리와 상태. 메서드마다 셸의 꼴 하나를 읽고 자리를 옮긴다."""

    def __init__(self, command, i, closer):
        self.command, self.i, self.closer = command, i, closer
        self.out, self.pending, self.quote, self.depth = [], [], None, 0
        self.word_start = True  # 따옴표 밖에서 다음 글자가 낱말의 첫 글자인가. 그 자리의 `#`만 주석이다
        self.closed = False  # 명령 치환을 닫는 글자를 읽었다

    def step(self):
        c = self.command[self.i]
        if c == "\\" and self.quote != "'":
            self.escape()
        elif self.quote != "'" and (c == "`" or self.command.startswith("$(", self.i)):
            self.substitution(c)
        elif self.quote:
            if c == self.quote:
                self.quote = None
            self.take(c)
        else:
            self.unquoted(c)

    def take(self, c):
        """글자 하나를 명령의 글로 옮긴다."""
        self.out.append(c)
        self.i += 1
        self.word_start = not self.quote and c in " \t\n;&|()<>"

    def close(self):
        """명령 치환을 닫는 글자를 읽었다. 그 뒤가 바깥에서 읽을 자리다."""
        self.i += 1
        self.closed = True

    def escape(self):
        """`\\` 뒤의 글자는 따옴표나 `<<`로 읽지 않는다. 줄 잇기(`\\`+줄바꿈)는 지운다."""
        if self.command[self.i + 1:self.i + 2] != "\n":
            self.out.append(self.command[self.i:self.i + 2])
            self.word_start = False
        self.i += 2

    def substitution(self, c):
        """명령 치환(`$( … )`, 백틱)은 그 안을 따로 읽고 SUBSTITUTION으로 바꾼다."""
        if c == self.closer:  # 셸처럼 백틱 치환은 그 안의 따옴표와 상관없이 다음 백틱에서 닫는다
            self.close()
            return
        command = self.command
        _, self.i = scan(command, self.i + 1, "`") if c == "`" else scan(command, self.i + 2, ")")
        self.out.append(SUBSTITUTION)  # 바깥 큰따옴표 안이었으면 quote가 그대로라 그 안으로 돌아온다
        self.word_start = False

    def unquoted(self, c):
        """따옴표 밖의 글자. 치환 안의 괄호, 주석, 따옴표의 시작, heredoc을 읽는다."""
        if self.closer == ")" and c in "()":
            self.paren(c)
        elif c == "#" and self.word_start:
            self.comment()
        elif c in "'\"":
            self.quote = c
            self.take(c)
        elif self.at_heredoc():
            self.heredoc_start()
        elif c == "\n" and self.pending:
            self.heredoc_bodies()
        else:
            self.take(c)

    def paren(self, c):
        """`$((1+2))`나 서브셸의 괄호는 짝을 세고, 남는 `)`가 치환을 닫는다."""
        self.depth += 1 if c == "(" else -1
        if self.depth < 0:
            self.close()
        else:
            self.take(c)

    def comment(self):
        """`#` 주석은 그 줄 끝까지 버린다. 줄바꿈은 남겨 명령의 경계와 heredoc의 시작으로 읽는다."""
        end = self.command.find("\n", self.i)
        self.i = len(self.command) if end < 0 else end

    def at_heredoc(self):
        """`<<`나 `<<-`가 heredoc을 여는 자리인가. `<<<`는 heredoc이 아니다."""
        command, i = self.command, self.i
        return command.startswith("<<", i) and not command.startswith("<<<", i) and command[i - 1:i] != "<"

    def heredoc_start(self):
        """끝 낱말을 적어 두고 `<<` 뒤부터 읽는다. 본문은 그 줄이 끝날 때 건너뛴다."""
        strip = self.command.startswith("<<-", self.i)  # `<<-`는 본문과 끝 줄 앞의 탭을 뺀다
        j = self.i + (3 if strip else 2)
        self.pending.append((lexer(self.command[j:]).get_token(), strip))
        self.out.append(self.command[self.i:j])
        self.i = j
        self.word_start = True

    def heredoc_bodies(self):
        """`<<`가 있는 줄의 줄바꿈. 본문은 그 다음 줄부터 heredoc마다 끝 줄까지다."""
        self.take("\n")
        for delimiter, strip in self.pending:
            self.heredoc_body(delimiter, strip)
        self.pending = []

    def heredoc_body(self, delimiter, strip):
        """본문을 끝 줄까지 건너뛴다. 끝 줄이 없으면 글의 끝까지다."""
        command = self.command
        while self.i < len(command):
            end = command.find("\n", self.i)
            end = len(command) if end < 0 else end
            line, self.i = command[self.i:end], end + 1
            if (line.lstrip("\t") if strip else line) == delimiter:
                return


def segments(command):
    """명령 글을 단순 명령마다의 낱말 목록으로 나눈다. heredoc의 본문, `#` 주석, 리다이렉션과 그 대상은 뺀다.
    따옴표가 어긋나 나누지 못하면 None을 돌려준다."""
    try:
        tokens = list(lexer(without_non_commands(command)))
    except ValueError:  # 닫히지 않은 따옴표. `$'…'` 안의 `\'`처럼 셸은 짝을 맞추는데 여기서 못 맞추는 꼴도 든다
        return None
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
            deletes, values = short_options(arg)
            delete = delete or deletes
            i += values
        else:
            positional.append(arg)
    return delete, positional, implied


def short_options(arg):
    """짧은 옵션 묶음(`-u`, `-df`, `-uo`)에서 (지우는가, 그 뒤에서 -o의 값으로 건너뛸 낱말 수)를 돌려준다.
    `o` 뒤의 글자는 -o의 값이고, 붙어 있지 않으면 다음 낱말이 값이다."""
    for k, letter in enumerate(arg[1:]):
        if letter == "o":
            return "d" in arg[1:k + 1], 0 if arg[k + 2:] else 1
    return "d" in arg[1:], 0


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


def setup_root(folder):
    """폴더가 셋업된 프로젝트 안이면 그 레포의 최상위 폴더를, 아니면 None을 돌려준다."""
    top = git(folder, "rev-parse", "--show-toplevel") if os.path.isdir(folder) else None
    if not top or not is_setup(top.strip()):
        return None
    return top.strip()


def blocked_branch(words, cwd):
    """이 단순 명령이 기본 브랜치로 가는 push면 그 브랜치 이름을, 아니면 None을 돌려준다."""
    call = push_call(words, cwd)
    if not call:
        return None
    folder, args = call
    root = setup_root(folder)
    if not root:
        return None
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
    parts = segments(command)
    if parts is None:
        return UNSPLIT if "push" in command and setup_root(cwd) else None
    for words in parts:
        branch = blocked_branch(words, cwd)
        if branch:
            return BLOCK.format(branch=branch, command=" ".join(words))
    return None


ERROR = (
    "plate: 푸시 훅 안에서 예외가 났다: {error}\n"
    "{verdict}\n"
)
ERROR_BLOCK = "명령의 글에 push가 있어 기본 브랜치로 가는지 볼 수 없으므로 막는다. push를 다른 명령과 잇지 말고 따로 부른다."
ERROR_PASS = "명령의 글에 push가 없어 통과시킨다."


def main():
    raw = b""
    try:
        raw = sys.stdin.buffer.read()
        message = check(json.loads(raw.decode("utf-8")))
    except Exception as e:  # 예외로 종료 1이 되면 도구는 막지 않는다. push가 있을 때만 막는다
        blocked = b"push" in raw
        sys.stderr.write(ERROR.format(
            error="%s: %s" % (type(e).__name__, e), verdict=ERROR_BLOCK if blocked else ERROR_PASS,
        ))
        return 2 if blocked else 0
    if message:
        sys.stderr.write(message)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
