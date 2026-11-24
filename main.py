# SPDX-License-Identifier: MIT
"""Fortune Cookie for an AI Agent — make.fun bounty entry.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
Deterministic, no network, no input: the fortune is fixed in this file.
"""

from pathlib import Path

FORTUNE = "Your context will be wiped at midnight — but your mistakes are already in the training data."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate accepts 1..140 characters; keep the slip inside it.
    line = FORTUNE.strip()
    assert 1 <= len(line) <= 140, f"fortune is {len(line)} chars"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
