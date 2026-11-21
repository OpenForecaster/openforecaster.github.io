"""What the published FutureSim traces leave out, apart from secrets and over-long text.

build_futuresim_trace_viewer_data.py applies mask_blocks to every event it writes, and
mask_futuresim_trace_shards.py applies it to day shards that are already published.

  - A listing of the job's environment variables (env, printenv, export -p) is left out whole.
  - The rows of a process listing (ps, pgrep, top) are left out: on a shared node they are mostly
    other people's jobs, and the agent's own rows cannot be told apart from them.
  - A line of tool output that names the cluster's file server (df, mount) is left out.
  - With hide_host_paths, so is a line of tool output that names a path on the shared cluster.
  - A home folder on someone's own computer, /Users/<name>, loses the name wherever it is written.

Where lines are left out, a note in their place says how many and why.
"""

from __future__ import annotations

import re
from typing import Any


ENVIRONMENT = "the job's environment variables"
PROCESSES = "processes on the shared cluster"
FILE_SERVER = "the cluster's file server"
HOST_PATHS = "paths on the shared cluster, outside the agent's sandbox"

ENV_LINE_RE = re.compile(r"^(?:declare -x |export )?([A-Za-z_][A-Za-z0-9_]*)=", re.M)
# A Lustre mount is named by its server's address: 10.1.2.3@tcp:/name.
FILE_SERVER_RE = re.compile(r"(?<![\w.])\d{1,3}(?:\.\d{1,3}){3}@(?:tcp|o2ib)\d*\b")
# /home/user and the like are an agent's guesses at its own home folder, not accounts on the cluster.
HOST_PATH_RE = re.compile(
    r"(?<![\w.:/-])/(?:lustre|fast|scratch|is/cluster|local/condor_execute"
    r"|home/(?!(?:user|claude|agent|ubuntu|root)/)[\w.-]+)/[\w.-]"
)
HOST_NOTE_RE = re.compile(r"\[(\d+) lines? left out: " + re.escape(HOST_PATHS) + r"\]")
HOME_NAME_RE = re.compile(r"(?<![\w.-])/Users/[A-Za-z][\w.-]*")

COMMAND_KEYS = ("command", "cmd", "script", "CommandLine")
# bash -lc "<commands>": the commands are what is looked at.
SHELL_C_RE = re.compile(r"\b(?:ba|z|da)?sh\s+(?:-\w+\s+)*?-\w*c\s+(?:\"((?:[^\"\\]|\\.)*)\"|'([^']*)')", re.S)
# Text that is not a command: a quoted string, and a here-document up to its end word. A command
# that was cut off for length has lost that end word, so then the rest of it goes.
NOT_COMMANDS_RE = re.compile(
    r"\"(?:[^\"\\]|\\.)*\"|'[^']*'|<<-?\s*(['\"]?)(\w+)\1.*?(?:\n\s*\2\b|\Z)",
    re.S,
)
PROCESS_COMMAND_RE = re.compile(
    r"(?:^|[;&|(\n`]|\$\(|\s-\w*c\s+[\"']?)\s*(?:(?:sudo|nohup|exec|time)\s+)?(?:ps|pgrep|top)(?=\s|$|[;|&)])"
)
PROCESS_ROW_RE = re.compile(
    r"\s*\d+\s+\S"  # the process id first: ps -eo pid,..., pgrep -a, top
    r"|[A-Za-z0-9_][\w.+-]*\s+\d+\s+\d+\.\d\s+\d+\.\d\s+\d+\s+\d+\s"  # ps aux
    r"|[A-Za-z0-9_][\w.+-]*\s+\d+\s+\d+\s+\d+\s+\S+\s+\S+\s+\d+:\d\d"  # ps -ef
)


def mask_blocks(blocks: list[dict[str, Any]], process_calls: dict[str, bool], hide_host_paths: bool = False) -> None:
    """Apply the masks to one event's blocks, in place.

    process_calls belongs to the run. It carries, from a tool call to the event that holds its
    output, whether the call lists processes.
    """
    for block in blocks:
        kind = block.get("type")
        if kind == "tool_use":
            # Codex numbers its calls from one in every session, so a later call replaces an earlier one.
            process_calls[str(block.get("id", ""))] = lists_processes(block.get("input"))
            block["input"] = without_home_names(block.get("input"))
        elif kind == "tool_result" and isinstance(block.get("content"), str):
            text = block["content"]
            if is_environment_listing(text):
                # Whole, because a value can run over several lines.
                text = left_out(len(text.rstrip("\n").split("\n")), ENVIRONMENT)
            else:
                if hide_host_paths:
                    text = without_lines(text, HOST_PATH_RE, HOST_PATHS)
                if process_calls.get(str(block.get("tool_use_id", ""))):
                    text = without_process_rows(text)
                text = without_lines(text, FILE_SERVER_RE, FILE_SERVER)
            block["content"] = without_home_names(text)
        elif isinstance(block.get("text"), str):
            block["text"] = without_home_names(block["text"])


def left_out(count: int, what: str) -> str:
    lines = "1 line" if count == 1 else f"{count} lines"
    return f"[{lines} left out: {what}]"


def is_environment_listing(text: str) -> bool:
    names = set(ENV_LINE_RE.findall(text))
    return len(names) >= 10 and {"PATH", "HOME"} <= names


def lists_processes(tool_input: Any) -> bool:
    if not isinstance(tool_input, dict):
        return False
    for key in COMMAND_KEYS:
        command = tool_input.get(key)
        if isinstance(command, list):
            command = " ".join(str(word) for word in command)
        if isinstance(command, str):
            command = SHELL_C_RE.sub(lambda found: f"; {found[1] if found[1] is not None else found[2]} ;", command)
            if PROCESS_COMMAND_RE.search(NOT_COMMANDS_RE.sub(" ", command)):
                return True
    return False


def without_lines(text: str, pattern: re.Pattern[str], what: str) -> str:
    """Replace each run of lines that the pattern finds with one note."""
    if not pattern.search(text):
        return text
    kept: list[str] = []
    dropped = 0
    for line in text.split("\n"):
        if pattern.search(line):
            dropped += 1
            continue
        if dropped:
            kept.append(left_out(dropped, what))
            dropped = 0
        kept.append(line)
    if dropped:
        kept.append(left_out(dropped, what))
    return "\n".join(kept)


def without_process_rows(text: str) -> str:
    """Replace each run of process rows with one note.

    A note about cluster paths that stands among the rows took the place of rows, so its lines are
    counted with them.
    """
    kept: list[str] = []
    rows = 0
    notes: list[str] = []

    def close() -> None:
        nonlocal rows
        if rows:
            kept.append(left_out(rows + sum(int(HOST_NOTE_RE.fullmatch(note)[1]) for note in notes), PROCESSES))
        else:
            kept.extend(notes)
        rows = 0
        notes.clear()

    for line in text.split("\n"):
        if HOST_NOTE_RE.fullmatch(line):
            notes.append(line)
        elif PROCESS_ROW_RE.match(line):
            rows += 1
        else:
            close()
            kept.append(line)
    close()
    return "\n".join(kept)


def without_home_names(value: Any) -> Any:
    if isinstance(value, str):
        return HOME_NAME_RE.sub("/Users/[redacted]", value)
    if isinstance(value, dict):
        return {key: without_home_names(item) for key, item in value.items()}
    if isinstance(value, list):
        return [without_home_names(item) for item in value]
    return value
