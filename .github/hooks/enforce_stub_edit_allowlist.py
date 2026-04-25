#!/usr/bin/env python3
"""PreToolUse hook to restrict edit operations to allowed stub folders."""

from __future__ import annotations

import json
import re
import sys
from typing import Any, Iterable

ALLOWED_PREFIXES = (
    "reference/micropython/",
    "reference/_mpy_shed/",
)

EDIT_TOOL_HINTS = (
    "apply_patch",
    "replace_string_in_file",
    "multi_replace_string_in_file",
    "create_file",
    "edit_notebook_file",
    "edit",
    "write",
    "rename",
    "delete",
)

PATH_KEYS = {
    "filepath",
    "file_path",
    "path",
    "new_path",
    "old_path",
    "targetpath",
}

PATCH_PATH_RE = re.compile(r"^\*\*\*\s+(?:Update|Add|Delete)\s+File:\s+(.+?)\s*$", re.MULTILINE)


def _emit(decision: str, reason: str) -> None:
    out = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
            "permissionDecisionReason": reason,
        }
    }
    sys.stdout.write(json.dumps(out))


def _normalize_path(raw: str) -> str:
    p = raw.strip().strip('"\'')
    p = p.replace('\\', '/')
    # Convert absolute paths to a relative-ish form if possible.
    marker = '/reference/'
    lower = p.lower()
    idx = lower.find(marker)
    if idx != -1:
        p = p[idx + 1 :]
    # Strip drive letters and leading slashes for stable prefix checks.
    p = re.sub(r'^[a-zA-Z]:', '', p)
    p = p.lstrip('/').lower()
    return p


def _extract_patch_paths(patch_text: str) -> list[str]:
    return [m.group(1).strip() for m in PATCH_PATH_RE.finditer(patch_text)]


def _collect_paths(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        for k, v in value.items():
            k_norm = str(k).lower()
            if k_norm in PATH_KEYS and isinstance(v, str):
                yield v
            elif k_norm == 'input' and isinstance(v, str):
                for p in _extract_patch_paths(v):
                    yield p
            else:
                yield from _collect_paths(v)
    elif isinstance(value, list):
        for item in value:
            yield from _collect_paths(item)


def _is_edit_tool(payload: dict[str, Any]) -> bool:
    tool_name_candidates = (
        payload.get("tool"),
        payload.get("toolName"),
        payload.get("name"),
        payload.get("recipient_name"),
        payload.get("tool_name"),
    )
    for candidate in tool_name_candidates:
        if isinstance(candidate, str):
            c = candidate.lower()
            if any(hint in c for hint in EDIT_TOOL_HINTS):
                return True

    blob = json.dumps(payload).lower()
    return any(hint in blob for hint in EDIT_TOOL_HINTS)


def _is_allowed(path: str) -> bool:
    norm = _normalize_path(path)
    return any(norm.startswith(prefix) for prefix in ALLOWED_PREFIXES)


def main() -> int:
    raw = sys.stdin.read().strip()
    if not raw:
        return 0

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        # Non-JSON input: fail open to avoid blocking all work unexpectedly.
        return 0

    if not _is_edit_tool(payload):
        _emit("allow", "Not an edit operation")
        return 0

    paths = sorted(set(_collect_paths(payload)))

    if not paths:
        _emit(
            "ask",
            "Edit operation detected, but no target path was found for allowlist validation.",
        )
        return 0

    blocked = [p for p in paths if not _is_allowed(p)]
    if blocked:
        _emit(
            "deny",
            "Blocked by stub edit allowlist. Allowed folders: reference/micropython/**, reference/_mpy_shed/**. "
            + "Requested path(s): "
            + ", ".join(blocked[:5]),
        )
        return 0

    _emit("allow", "Edit path is within allowed stub folders")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
