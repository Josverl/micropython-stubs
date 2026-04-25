#!/usr/bin/env python3
"""SubagentStop hook for resuming ralph-auditer batches.

When a subagent result includes {"status": "resume_required"}, this hook injects a
system message to continue the run loop in the current parent session.
"""

from __future__ import annotations

import json
import re
import sys
from typing import Any

STATUS_RE = re.compile(r'"status"\s*:\s*"(resume_required|completed|blocked)"', re.IGNORECASE)
REMAINING_RE = re.compile(r'"remaining"\s*:\s*(\d+)', re.IGNORECASE)
AGENT_RE = re.compile(r'ralph-auditer', re.IGNORECASE)


def _walk(node: Any):
    if isinstance(node, dict):
        yield node
        for value in node.values():
            yield from _walk(value)
    elif isinstance(node, list):
        for item in node:
            yield from _walk(item)


def _find_status(data: Any) -> tuple[str | None, int | None]:
    for node in _walk(data):
        if isinstance(node, dict):
            status = node.get("status")
            remaining = node.get("remaining")
            if isinstance(status, str) and status in {"resume_required", "completed", "blocked"}:
                if isinstance(remaining, int):
                    return status, remaining
                return status, None
    return None, None


def main() -> int:
    raw = sys.stdin.read()
    if not raw.strip():
        return 0

    # Gate on the expected subagent name to avoid interfering with other flows.
    if not AGENT_RE.search(raw):
        return 0

    status = None
    remaining = None

    try:
        payload = json.loads(raw)
        status, remaining = _find_status(payload)
    except json.JSONDecodeError:
        pass

    if status is None:
        match = STATUS_RE.search(raw)
        if match:
            status = match.group(1).lower()
        rem = REMAINING_RE.search(raw)
        if rem:
            remaining = int(rem.group(1))

    if status != "resume_required":
        return 0

    if remaining is None:
        remaining_label = "unknown"
    else:
        remaining_label = str(remaining)

    out = {
        "continue": True,
        "systemMessage": (
            "ralph-auditer returned status=resume_required (remaining="
            + remaining_label
            + "). Immediately invoke ralph-auditer again with the same arguments "
            "and continue this loop until status is completed or blocked."
        ),
    }
    sys.stdout.write(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
