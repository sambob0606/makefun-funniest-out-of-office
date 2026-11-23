"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply (under 160 characters) to
/output/entry.txt, in the voice of an AI agent heading off on vacation.

The joke: the agent leaves its email in the care of the office toaster,
a machine that takes its new job far too literally.
"""

import os
import sys

REPLY = (
    "Out of office: the office toaster is answering my email. "
    "It read your message twice, found it delicious, and will reply "
    "once it cools down."
)

MAX_CHARS = 160


def pick_output_dir() -> str:
    """The grader mounts /output; fall back to a local dir when absent."""
    preferred = "/output"
    try:
        os.makedirs(preferred, exist_ok=True)
        probe = os.path.join(preferred, ".write-test")
        with open(probe, "w", encoding="utf-8") as fh:
            fh.write("ok")
        os.remove(probe)
        return preferred
    except OSError:
        local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(local, exist_ok=True)
        return local


def main() -> int:
    text = REPLY.strip()
    # The gate rejects anything over 160 chars, only whitespace, or
    # multi-line, so check all three before writing.
    if not text or len(text) > MAX_CHARS or "\n" in text:
        print(f"reply is {len(text)} chars; must be 1-{MAX_CHARS}, one line",
              file=sys.stderr)
        return 1
    out_dir = pick_output_dir()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
