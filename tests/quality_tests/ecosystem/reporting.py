"""Path-independent and credential-safe ecosystem QA report helpers."""

from __future__ import annotations

import re
from collections.abc import Iterable
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Mapping, cast
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from .model import PackageResolution

REPORT_SCHEMA_VERSION = 2

_URL_PATTERN = re.compile(r"(?i)\b(?:file|https?)://[^\s<>\"']+")
_WINDOWS_PATH_PATTERN = re.compile(r"(?<![\w:])[A-Za-z]:[\\/][^\s,;:]*")
_POSIX_PATH_PATTERN = re.compile(r"(?<![:\w])/(?:[^/\s]+/)+[^\s,;]*")
_SENSITIVE_ASSIGNMENT_PATTERN = re.compile(
    r"(?i)\b(token|secret|password|passwd|credential|signature|api[_-]?key|access[_-]?key|authorization|auth)=([^\s&]+)"
)
_SENSITIVE_NAMES = frozenset(
    {
        "accesskey",
        "accesskeyid",
        "apikey",
        "auth",
        "authorization",
        "credential",
        "password",
        "passwd",
        "secret",
        "sig",
        "signature",
        "token",
    }
)


def resolution_to_dict(resolution: PackageResolution) -> dict[str, object]:
    manifest = None
    if resolution.manifest_reference is not None or resolution.manifest_sha256 is not None:
        manifest = {
            "reference": resolution.manifest_reference,
            "sha256": resolution.manifest_sha256,
        }
    return {
        "requested_reference": resolution.requested_reference,
        "canonical_reference": resolution.canonical_reference,
        "requested_revision": resolution.requested_revision,
        "resolved_revision": resolution.resolved_revision,
        "package_version": resolution.package_version,
        "manifest": manifest,
        "dependencies": [
            {
                "requested_reference": dependency.requested_reference,
                "requested_revision": dependency.requested_revision,
                "resolved_revision": dependency.resolved_revision,
                "depth": dependency.depth,
                "disposition": dependency.disposition.value,
                "identity": dependency.identity.key if dependency.identity else None,
                "reason": dependency.reason.value if dependency.reason else None,
            }
            for dependency in resolution.dependencies
        ],
        "files": [
            {
                "owner": file.owner.key,
                "target": file.target,
                "source": file.source,
                "dependency_depth": file.dependency_depth,
                "kind": file.kind.value,
                "sha256": file.sha256,
                "size": file.size,
            }
            for file in resolution.files
        ],
    }


def resolution_text(resolution: PackageResolution, *, indent: str = "") -> list[str]:
    lines = [
        f"{indent}revision: requested={resolution.requested_revision or '-'} resolved={resolution.resolved_revision or '-'} "
        f"package_version={resolution.package_version or '-'}"
    ]
    if resolution.manifest_reference is None and resolution.manifest_sha256 is None:
        lines.append(f"{indent}manifest: none")
    else:
        lines.append(f"{indent}manifest: {resolution.manifest_reference or '-'} sha256={resolution.manifest_sha256 or '-'}")
    lines.append(f"{indent}closure: {len(resolution.dependencies)} dependencies, {len(resolution.files)} files")
    for dependency in resolution.dependencies:
        lines.append(
            f"{indent}  dependency[{dependency.depth}]: {dependency.requested_reference} "
            f"requested={dependency.requested_revision or '-'} resolved={dependency.resolved_revision or '-'} "
            f"{dependency.disposition.value}"
        )
    for file in resolution.files:
        lines.append(
            f"{indent}  file[{file.kind.value}]: {file.target} sha256={file.sha256 or '-'} "
            f"size={file.size if file.size is not None else '-'} source={file.source}"
        )
    return lines


def sanitize_report_document(
    document: dict[str, object],
    *,
    preserved_paths: Iterable[Path] = (),
) -> dict[str, object]:
    return cast(dict[str, object], _sanitize_value(document, preserved_paths=_safe_preserved_paths(preserved_paths)))


def sanitize_report_command(command: Iterable[str]) -> tuple[str, ...]:
    sanitized = _sanitize_value(list(command))
    if not isinstance(sanitized, list):
        raise TypeError("sanitized report command must remain a list")
    return tuple(str(argument) for argument in sanitized)


def sanitize_report_text(text: str, *, preserved_paths: Iterable[Path] = ()) -> str:
    paths = _safe_preserved_paths(preserved_paths)
    path_placeholders = {f"REPORTPATH{index}PLACEHOLDER": path for index, path in enumerate(sorted(paths, key=len, reverse=True))}
    for placeholder, path in path_placeholders.items():
        text = text.replace(path, placeholder)

    urls: list[str] = []

    def replace_url(match: re.Match[str]) -> str:
        urls.append(_sanitize_url(match.group(0)))
        return f"REPORTURL{len(urls) - 1}PLACEHOLDER"

    sanitized = _URL_PATTERN.sub(replace_url, text)
    sanitized = _SENSITIVE_ASSIGNMENT_PATTERN.sub(lambda match: f"{match.group(1)}=<redacted>", sanitized)
    sanitized = _WINDOWS_PATH_PATTERN.sub("<path>", sanitized)
    sanitized = _POSIX_PATH_PATTERN.sub("<path>", sanitized)
    for index, url in enumerate(urls):
        sanitized = sanitized.replace(f"REPORTURL{index}PLACEHOLDER", url)
    for placeholder, path in path_placeholders.items():
        sanitized = sanitized.replace(placeholder, path)
    return sanitized


def _sanitize_value(
    value: object,
    *,
    key: str | None = None,
    preserved_paths: frozenset[str] = frozenset(),
) -> object:
    if key is not None and _is_sensitive_name(key):
        return "<redacted>"
    if isinstance(value, str):
        if value in preserved_paths:
            return value
        if _is_absolute_path(value):
            return "<path>"
        return sanitize_report_text(value, preserved_paths=(Path(path) for path in preserved_paths))
    if isinstance(value, Path):
        if str(value) in preserved_paths:
            return str(value)
        return "<path>"
    if isinstance(value, Mapping):
        return {
            str(item_key): _sanitize_value(item_value, key=str(item_key), preserved_paths=preserved_paths)
            for item_key, item_value in value.items()
        }
    if isinstance(value, tuple):
        return [_sanitize_value(item, preserved_paths=preserved_paths) for item in value]
    if isinstance(value, list):
        return [_sanitize_value(item, preserved_paths=preserved_paths) for item in value]
    return value


def _safe_preserved_paths(paths: Iterable[Path]) -> frozenset[str]:
    return frozenset(path for item in paths if (path := str(item)) and _SENSITIVE_ASSIGNMENT_PATTERN.search(path) is None)


def _sanitize_url(reference: str) -> str:
    parsed = urlsplit(reference)
    if parsed.scheme.casefold() == "file":
        return "<path>"
    if parsed.scheme.casefold() not in {"http", "https"}:
        return sanitize_report_text(reference)
    hostname = parsed.hostname or ""
    if ":" in hostname and not hostname.startswith("["):
        hostname = f"[{hostname}]"
    try:
        port = f":{parsed.port}" if parsed.port is not None else ""
    except ValueError:
        port = ""
    query = urlencode(
        [(name, "<redacted>" if _is_sensitive_name(name) else value) for name, value in parse_qsl(parsed.query, keep_blank_values=True)]
    )
    fragment = _SENSITIVE_ASSIGNMENT_PATTERN.sub(lambda match: f"{match.group(1)}=<redacted>", parsed.fragment)
    return urlunsplit((parsed.scheme, f"{hostname}{port}", parsed.path, query, fragment))


def _is_absolute_path(value: str) -> bool:
    return PureWindowsPath(value).is_absolute() or PurePosixPath(value).is_absolute()


def _is_sensitive_name(name: str) -> bool:
    normalized = re.sub(r"[^a-z0-9]", "", name.casefold())
    return normalized in _SENSITIVE_NAMES or any(
        normalized.endswith(suffix)
        for suffix in ("token", "secret", "password", "credential", "signature", "apikey", "accesskey", "accesskeyid")
    )
