"""Constrained, non-executing interpretation of micropython-lib manifests."""

from __future__ import annotations

import ast
from collections.abc import Callable
from dataclasses import dataclass
import hashlib
from io import BytesIO
import json
from pathlib import Path, PurePosixPath
import re
import stat
from typing import Mapping
from urllib.parse import quote
import zipfile

from .catalog import CatalogDiagnostic, CatalogEntry, CatalogParseResult
from .model import (
    CatalogSource,
    PortClassification,
    PortDecision,
    PortEvidence,
    PortEvidenceSource,
    ReasonCode,
    RecordDisposition,
    classify_ports,
)


_BASE_LIBRARIES = ("micropython", "python-stdlib", "python-ecosys")
_ALL_LIBRARIES = (*_BASE_LIBRARIES, "unix-ffi")
_METADATA_FIELDS = {"version", "description", "license", "author", "stdlib", "pypi", "pypi_publish"}
_REVISION_URL = "https://api.github.com/repos/micropython/micropython-lib/commits/{revision}"
_ARCHIVE_URL = "https://github.com/micropython/micropython-lib/archive/{revision}.zip"


class MicropythonLibManifestError(ValueError):
    def __init__(self, reason: ReasonCode, message: str) -> None:
        super().__init__(message)
        self.reason = reason


@dataclass(frozen=True)
class MicropythonLibLimits:
    max_depth: int = 16
    max_files: int = 4096
    max_total_bytes: int = 64 * 1024 * 1024


@dataclass(frozen=True)
class MicropythonLibPackage:
    name: str
    package_path: str
    manifest_path: str
    version: str | None
    description: str | None
    license: str | None
    author: str | None
    stdlib: bool
    pypi: str | None
    pypi_publish: str | None


@dataclass(frozen=True)
class MicropythonLibSourceFile:
    owner_path: str
    target: str
    source_path: str
    data: bytes
    depth: int


@dataclass(frozen=True)
class MicropythonLibDependency:
    name: str
    requested_version: str | None
    package_path: str
    depth: int


@dataclass(frozen=True)
class MicropythonLibResolution:
    package: MicropythonLibPackage
    files: tuple[MicropythonLibSourceFile, ...]
    dependencies: tuple[MicropythonLibDependency, ...]
    classification: PortDecision


@dataclass(frozen=True)
class _Requirement:
    name: str
    version: str | None
    library: str | None


@dataclass(frozen=True)
class _DeclaredFile:
    target: str
    source_path: str


@dataclass(frozen=True)
class _Manifest:
    package: MicropythonLibPackage
    requirements: tuple[_Requirement, ...]
    files: tuple[_DeclaredFile, ...]


class MicropythonLibSnapshot:
    """A selected micropython-lib tree interpreted as inert source data."""

    def __init__(
        self,
        files: Mapping[str, bytes],
        *,
        requested_revision: str,
        resolved_revision: str,
        limits: MicropythonLibLimits = MicropythonLibLimits(),
    ) -> None:
        if not requested_revision.strip() or not resolved_revision.strip():
            raise ValueError("micropython-lib revisions must not be empty")
        normalized: dict[str, bytes] = {}
        total_bytes = 0
        for path, data in files.items():
            normalized_path = _normalized_path(path, "snapshot file")
            if normalized_path in normalized:
                raise MicropythonLibManifestError(ReasonCode.TARGET_COLLISION, f"Duplicate snapshot file: {normalized_path}")
            if not isinstance(data, bytes):
                raise TypeError("micropython-lib snapshot files must contain bytes")
            normalized[normalized_path] = data
            total_bytes += len(data)
        if len(normalized) > limits.max_files:
            raise MicropythonLibManifestError(ReasonCode.LIMIT_EXCEEDED, f"Snapshot exceeds {limits.max_files} files")
        if total_bytes > limits.max_total_bytes:
            raise MicropythonLibManifestError(ReasonCode.LIMIT_EXCEEDED, f"Snapshot exceeds {limits.max_total_bytes} bytes")

        self.files = normalized
        self.requested_revision = requested_revision
        self.resolved_revision = resolved_revision
        self.limits = limits
        self._manifest_cache: dict[str, _Manifest] = {}
        self._manifest_paths = tuple(sorted(path for path in normalized if PurePosixPath(path).name == "manifest.py"))
        self._packages_by_name: dict[str, list[str]] = {}
        for manifest_path in self._manifest_paths:
            package_path = PurePosixPath(manifest_path).parent.as_posix()
            self._packages_by_name.setdefault(PurePosixPath(package_path).name, []).append(package_path)

    @classmethod
    def from_directory(
        cls,
        root: Path,
        *,
        requested_revision: str,
        resolved_revision: str,
        limits: MicropythonLibLimits = MicropythonLibLimits(),
    ) -> MicropythonLibSnapshot:
        if not root.is_dir():
            raise ValueError(f"micropython-lib snapshot root does not exist: {root}")
        files: dict[str, bytes] = {}
        for source in sorted(root.rglob("*")):
            if source.is_symlink():
                raise MicropythonLibManifestError(ReasonCode.UNSAFE_PATH, f"Snapshot contains a symbolic link: {source}")
            if source.is_file():
                files[source.relative_to(root).as_posix()] = source.read_bytes()
        return cls(
            files,
            requested_revision=requested_revision,
            resolved_revision=resolved_revision,
            limits=limits,
        )

    @classmethod
    def from_files(
        cls,
        files: Mapping[str, bytes],
        *,
        requested_revision: str,
        resolved_revision: str,
        limits: MicropythonLibLimits = MicropythonLibLimits(),
    ) -> MicropythonLibSnapshot:
        return cls(
            files,
            requested_revision=requested_revision,
            resolved_revision=resolved_revision,
            limits=limits,
        )

    @classmethod
    def from_zip(
        cls,
        data: bytes,
        *,
        requested_revision: str,
        resolved_revision: str,
        limits: MicropythonLibLimits = MicropythonLibLimits(),
    ) -> MicropythonLibSnapshot:
        if len(data) > limits.max_total_bytes:
            raise MicropythonLibManifestError(ReasonCode.LIMIT_EXCEEDED, "Compressed snapshot exceeds the byte limit")
        try:
            archive = zipfile.ZipFile(BytesIO(data))
        except (OSError, zipfile.BadZipFile) as error:
            raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, "micropython-lib snapshot is not a ZIP archive") from error
        with archive:
            members = tuple(item for item in archive.infolist() if not item.is_dir())
            if len(members) > limits.max_files:
                raise MicropythonLibManifestError(ReasonCode.LIMIT_EXCEEDED, f"Snapshot exceeds {limits.max_files} files")
            if sum(item.file_size for item in members) > limits.max_total_bytes:
                raise MicropythonLibManifestError(ReasonCode.LIMIT_EXCEEDED, "Expanded snapshot exceeds the byte limit")

            parsed_paths = tuple(_archive_path(item) for item in members)
            roots = {path.parts[0] for path in parsed_paths}
            if len(roots) != 1 or any(len(path.parts) < 2 for path in parsed_paths):
                raise MicropythonLibManifestError(ReasonCode.UNSAFE_PATH, "Snapshot must contain one repository root directory")
            files: dict[str, bytes] = {}
            for member, path in zip(members, parsed_paths, strict=True):
                relative_path = PurePosixPath(*path.parts[1:]).as_posix()
                if not relative_path.casefold().endswith(".py"):
                    continue
                if member.flag_bits & 0x1:
                    raise MicropythonLibManifestError(ReasonCode.UNSAFE_PATH, f"Encrypted snapshot member: {member.filename}")
                mode = member.external_attr >> 16
                if stat.S_ISLNK(mode):
                    raise MicropythonLibManifestError(ReasonCode.UNSAFE_PATH, f"Symbolic-link snapshot member: {member.filename}")
                if relative_path in files:
                    raise MicropythonLibManifestError(ReasonCode.TARGET_COLLISION, f"Duplicate snapshot file: {relative_path}")
                files[relative_path] = archive.read(member)
        return cls(
            files,
            requested_revision=requested_revision,
            resolved_revision=resolved_revision,
            limits=limits,
        )

    @property
    def package_paths(self) -> tuple[str, ...]:
        return tuple(PurePosixPath(path).parent.as_posix() for path in self._manifest_paths)

    def package(self, package_reference: str) -> MicropythonLibPackage:
        return self._manifest(self._resolve_package_path(package_reference)).package

    def raw_reference(self, path: str) -> str:
        normalized = _normalized_path(path, "source path")
        encoded = "/".join(quote(part, safe="") for part in PurePosixPath(normalized).parts)
        return f"https://raw.githubusercontent.com/micropython/micropython-lib/{quote(self.resolved_revision, safe='')}/{encoded}"

    def resolve(self, package_reference: str) -> MicropythonLibResolution:
        root_path = self._resolve_package_path(package_reference)
        root_manifest = self._manifest(root_path)
        root_library = PurePosixPath(root_path).parts[0]
        library_order = ("unix-ffi", *_BASE_LIBRARIES) if root_library == "unix-ffi" else _BASE_LIBRARIES
        payloads: dict[str, MicropythonLibSourceFile] = {}
        dependencies: dict[tuple[str, str], MicropythonLibDependency] = {}
        completed: set[str] = set()
        stack: list[str] = []

        def visit(package_path: str, depth: int) -> None:
            if depth > self.limits.max_depth:
                raise MicropythonLibManifestError(
                    ReasonCode.LIMIT_EXCEEDED,
                    f"Dependency depth exceeds {self.limits.max_depth}",
                )
            if package_path in stack:
                chain = " -> ".join((*stack, package_path))
                raise MicropythonLibManifestError(ReasonCode.DEPENDENCY_CYCLE, f"Dependency cycle: {chain}")
            if package_path in completed:
                return

            stack.append(package_path)
            manifest = self._manifest(package_path)
            try:
                for declared in manifest.files:
                    source = MicropythonLibSourceFile(
                        owner_path=package_path,
                        target=declared.target,
                        source_path=declared.source_path,
                        data=self.files[declared.source_path],
                        depth=depth,
                    )
                    existing = payloads.get(source.target)
                    if existing is not None and existing.data != source.data:
                        raise MicropythonLibManifestError(
                            ReasonCode.TARGET_COLLISION,
                            f"Packages map different content to {source.target}",
                        )
                    if existing is None or source.depth < existing.depth:
                        payloads[source.target] = source

                for requirement in manifest.requirements:
                    dependency_path = self._requirement_path(requirement, library_order)
                    dependency = MicropythonLibDependency(requirement.name, requirement.version, dependency_path, depth + 1)
                    dependencies[(requirement.name, dependency_path)] = dependency
                    visit(dependency_path, depth + 1)
            finally:
                stack.pop()
            completed.add(package_path)

        visit(root_path, 0)
        return MicropythonLibResolution(
            package=root_manifest.package,
            files=tuple(sorted(payloads.values(), key=lambda item: (item.depth, item.target, item.source_path))),
            dependencies=tuple(sorted(dependencies.values(), key=lambda item: (item.depth, item.package_path, item.name))),
            classification=_classification(root_path),
        )

    def _resolve_package_path(self, package_reference: str) -> str:
        normalized = _normalized_path(package_reference.removesuffix("/manifest.py"), "package reference")
        if f"{normalized}/manifest.py" in self.files:
            return normalized
        matches = self._packages_by_name.get(normalized, [])
        if len(matches) == 1:
            return matches[0]
        if not matches:
            raise MicropythonLibManifestError(ReasonCode.UNAVAILABLE, f"micropython-lib package not found: {package_reference}")
        raise MicropythonLibManifestError(
            ReasonCode.INVALID_MANIFEST,
            f"Ambiguous micropython-lib package name {package_reference!r}: {', '.join(sorted(matches))}",
        )

    def _requirement_path(self, requirement: _Requirement, library_order: tuple[str, ...]) -> str:
        matches = self._packages_by_name.get(requirement.name, [])
        if requirement.library is not None:
            order = (requirement.library,)
        else:
            order = library_order
        for library in order:
            library_matches = [path for path in matches if PurePosixPath(path).parts[0] == library]
            if len(library_matches) == 1:
                return library_matches[0]
            if len(library_matches) > 1:
                break
        raise MicropythonLibManifestError(
            ReasonCode.DEPENDENCY_UNAVAILABLE,
            f"Required micropython-lib package not found or ambiguous: {requirement.name}",
        )

    def _manifest(self, package_path: str) -> _Manifest:
        if package_path not in self._manifest_cache:
            self._manifest_cache[package_path] = self._parse_manifest(package_path)
        return self._manifest_cache[package_path]

    def _parse_manifest(self, package_path: str) -> _Manifest:
        manifest_path = f"{package_path}/manifest.py"
        try:
            source = self.files[manifest_path].decode("utf-8")
        except KeyError as error:
            raise MicropythonLibManifestError(ReasonCode.UNAVAILABLE, f"Manifest not found: {manifest_path}") from error
        except UnicodeDecodeError as error:
            raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, f"Manifest is not UTF-8: {manifest_path}") from error
        try:
            tree = ast.parse(source, filename=manifest_path)
        except SyntaxError as error:
            raise MicropythonLibManifestError(
                ReasonCode.INVALID_MANIFEST, f"Invalid manifest syntax in {manifest_path}: {error}"
            ) from error

        metadata: dict[str, object] | None = None
        requirements: list[_Requirement] = []
        files: list[_DeclaredFile] = []
        for node in tree.body:
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                continue
            if not isinstance(node, ast.Expr) or not isinstance(node.value, ast.Call) or not isinstance(node.value.func, ast.Name):
                raise MicropythonLibManifestError(
                    ReasonCode.INVALID_MANIFEST,
                    f"{manifest_path}:{node.lineno}: only literal manifest calls are supported",
                )
            call = node.value
            function = call.func.id
            arguments, keywords = _literal_call(call, manifest_path)
            if function == "metadata":
                if metadata is not None or requirements or files:
                    raise MicropythonLibManifestError(
                        ReasonCode.INVALID_MANIFEST,
                        f"{manifest_path}:{node.lineno}: metadata() must be the first manifest call",
                    )
                if arguments or set(keywords) - _METADATA_FIELDS:
                    raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, f"Invalid metadata() call in {manifest_path}")
                metadata = keywords
            else:
                if metadata is None:
                    raise MicropythonLibManifestError(
                        ReasonCode.INVALID_MANIFEST,
                        f"{manifest_path}:{node.lineno}: metadata() must be the first manifest call",
                    )
                if function == "require":
                    requirements.append(_parse_requirement(arguments, keywords, manifest_path))
                elif function == "module":
                    files.append(self._parse_module(package_path, arguments, keywords, manifest_path))
                elif function == "package":
                    files.extend(self._parse_package_files(package_path, arguments, keywords, manifest_path))
                else:
                    raise MicropythonLibManifestError(
                        ReasonCode.INVALID_MANIFEST,
                        f"{manifest_path}:{node.lineno}: unsupported manifest function {function}()",
                    )

        if metadata is None:
            raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, f"Manifest does not call metadata(): {manifest_path}")
        package = _package_metadata(package_path, manifest_path, metadata)
        unique_files = {(item.target, item.source_path): item for item in files}
        return _Manifest(
            package,
            tuple(requirements),
            tuple(sorted(unique_files.values(), key=lambda item: (item.target, item.source_path))),
        )

    def _parse_module(
        self,
        package_path: str,
        arguments: tuple[object, ...],
        keywords: dict[str, object],
        manifest_path: str,
    ) -> _DeclaredFile:
        values = _bind_call(arguments, keywords, ("module_path", "base_path", "opt"), 1, {"base_path": ".", "opt": None}, manifest_path)
        module_path = _string(values["module_path"], "module path", manifest_path)
        if PurePosixPath(module_path).suffix.casefold() != ".py":
            raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, f"module() requires a .py file in {manifest_path}")
        base_path = _string(values["base_path"], "module base path", manifest_path)
        source_path = _join_path(package_path, base_path, module_path)
        self._require_source(source_path, manifest_path)
        return _DeclaredFile(_normalized_path(module_path, "module target"), source_path)

    def _parse_package_files(
        self,
        package_path: str,
        arguments: tuple[object, ...],
        keywords: dict[str, object],
        manifest_path: str,
    ) -> tuple[_DeclaredFile, ...]:
        values = _bind_call(
            arguments,
            keywords,
            ("package_path", "files", "base_path", "opt"),
            1,
            {"files": None, "base_path": ".", "opt": None},
            manifest_path,
        )
        target_root = _normalized_path(_string(values["package_path"], "package path", manifest_path), "package target")
        base_path = _string(values["base_path"], "package base path", manifest_path)
        source_root = _join_path(package_path, base_path, target_root)
        selected = values["files"]
        if selected is None:
            prefix = f"{source_root}/"
            source_paths = tuple(path for path in self.files if path.startswith(prefix) and path.casefold().endswith(".py"))
            relative_paths = tuple(path[len(prefix) :] for path in source_paths)
        else:
            if not isinstance(selected, (list, tuple)) or not all(isinstance(item, str) for item in selected):
                raise MicropythonLibManifestError(
                    ReasonCode.INVALID_MANIFEST, f"package() files must be literal strings in {manifest_path}"
                )
            relative_paths = tuple(_normalized_path(item, "package file") for item in selected)
            source_paths = tuple(_join_path(source_root, item) for item in relative_paths)
        if not source_paths:
            raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, f"package() selects no Python files in {manifest_path}")
        declarations: list[_DeclaredFile] = []
        for relative_path, source_path in zip(relative_paths, source_paths, strict=True):
            if PurePosixPath(relative_path).suffix.casefold() != ".py":
                raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, f"package() requires .py files in {manifest_path}")
            self._require_source(source_path, manifest_path)
            declarations.append(_DeclaredFile(f"{target_root}/{relative_path}", source_path))
        return tuple(declarations)

    def _require_source(self, source_path: str, manifest_path: str) -> None:
        if source_path not in self.files:
            raise MicropythonLibManifestError(
                ReasonCode.INVALID_MANIFEST,
                f"Manifest {manifest_path} references missing source file {source_path}",
            )


class MicropythonLibCatalogAdapter:
    """Project one immutable repository snapshot into normalized catalog entries."""

    def parse(self, snapshot: MicropythonLibSnapshot) -> CatalogParseResult:
        entries: list[CatalogEntry] = []
        diagnostics: list[CatalogDiagnostic] = []
        for package_path in snapshot.package_paths:
            manifest_path = f"{package_path}/manifest.py"
            source_url = snapshot.raw_reference(manifest_path)
            try:
                package = snapshot.package(package_path)
            except MicropythonLibManifestError as error:
                diagnostics.append(
                    CatalogDiagnostic(
                        catalog=CatalogSource.MICROPYTHON_LIB,
                        entry_key=package_path,
                        source_url=source_url,
                        disposition=RecordDisposition.ERROR,
                        reason=error.reason,
                        detail=str(error),
                        reference=package_path,
                    )
                )
                continue
            library = PurePosixPath(package_path).parts[0]
            reference = f"github:micropython/micropython-lib/{package_path}@{snapshot.resolved_revision}"
            metadata = {
                "library": library,
                "manifest_sha256": hashlib.sha256(snapshot.files[manifest_path]).hexdigest(),
            }
            for name in ("version", "license", "author", "pypi", "pypi_publish"):
                value = getattr(package, name)
                if value is not None:
                    metadata[name] = value
            if package.stdlib:
                metadata["stdlib"] = "true"
            entries.append(
                CatalogEntry(
                    catalog=CatalogSource.MICROPYTHON_LIB,
                    name=package.name,
                    reference=reference,
                    description=package.description or "",
                    category=library,
                    source_url=source_url,
                    observed_at=None,
                    repository_url=(f"https://github.com/micropython/micropython-lib/tree/{snapshot.resolved_revision}/{package_path}"),
                    metadata=tuple(sorted(metadata.items())),
                )
            )
        return CatalogParseResult(tuple(entries), tuple(diagnostics))


def fetch_micropython_lib_snapshot(
    fetch: Callable[[str], bytes],
    requested_revision: str,
    *,
    limits: MicropythonLibLimits = MicropythonLibLimits(),
) -> MicropythonLibSnapshot:
    """Fetch and pin one selected repository revision using an injected transport."""
    requested_revision = requested_revision.strip()
    if not requested_revision:
        raise ValueError("micropython-lib revision must not be empty")
    if re.fullmatch(r"[0-9a-fA-F]{40}", requested_revision):
        resolved_revision = requested_revision.casefold()
    else:
        revision_url = _REVISION_URL.format(revision=quote(requested_revision, safe=""))
        try:
            document = json.loads(fetch(revision_url).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise MicropythonLibManifestError(ReasonCode.UNAVAILABLE, "Invalid micropython-lib revision response") from error
        if not isinstance(document, dict) or not isinstance(document.get("sha"), str):
            raise MicropythonLibManifestError(ReasonCode.UNAVAILABLE, "micropython-lib revision response has no commit")
        resolved_revision = document["sha"].casefold()
        if re.fullmatch(r"[0-9a-f]{40}", resolved_revision) is None:
            raise MicropythonLibManifestError(ReasonCode.UNAVAILABLE, "micropython-lib revision response has an invalid commit")
    archive_url = _ARCHIVE_URL.format(revision=resolved_revision)
    return MicropythonLibSnapshot.from_zip(
        fetch(archive_url),
        requested_revision=requested_revision,
        resolved_revision=resolved_revision,
        limits=limits,
    )


def _literal_call(call: ast.Call, manifest_path: str) -> tuple[tuple[object, ...], dict[str, object]]:
    try:
        arguments = tuple(ast.literal_eval(argument) for argument in call.args)
        if any(keyword.arg is None for keyword in call.keywords):
            raise ValueError
        keywords = {str(keyword.arg): ast.literal_eval(keyword.value) for keyword in call.keywords}
    except (ValueError, TypeError) as error:
        raise MicropythonLibManifestError(
            ReasonCode.INVALID_MANIFEST,
            f"{manifest_path}:{call.lineno}: only literal manifest calls are supported",
        ) from error
    if len(keywords) != len(call.keywords):
        raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, f"Duplicate keyword in {manifest_path}:{call.lineno}")
    return arguments, keywords


def _bind_call(
    arguments: tuple[object, ...],
    keywords: dict[str, object],
    parameters: tuple[str, ...],
    required: int,
    defaults: Mapping[str, object],
    manifest_path: str,
) -> dict[str, object]:
    if len(arguments) > len(parameters) or set(keywords) - set(parameters):
        raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, f"Invalid manifest call in {manifest_path}")
    values = dict(defaults)
    for name, value in zip(parameters, arguments, strict=False):
        values[name] = value
    for name, value in keywords.items():
        if name in parameters[: len(arguments)]:
            raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, f"Duplicate argument {name} in {manifest_path}")
        values[name] = value
    missing = [name for name in parameters[:required] if name not in values]
    if missing:
        raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, f"Missing argument {missing[0]} in {manifest_path}")
    return values


def _parse_requirement(
    arguments: tuple[object, ...],
    keywords: dict[str, object],
    manifest_path: str,
) -> _Requirement:
    values = _bind_call(
        arguments,
        keywords,
        ("name", "version", "pypi", "library"),
        1,
        {"version": None, "pypi": None, "library": None},
        manifest_path,
    )
    name = _string(values["name"], "requirement name", manifest_path)
    version = _optional_string(values["version"], "requirement version", manifest_path)
    library = _optional_string(values["library"], "requirement library", manifest_path)
    if library is not None and library not in _ALL_LIBRARIES:
        raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, f"Unknown requirement library {library!r} in {manifest_path}")
    return _Requirement(name, version, library)


def _package_metadata(package_path: str, manifest_path: str, metadata: Mapping[str, object]) -> MicropythonLibPackage:
    version = _optional_string(metadata.get("version"), "metadata version", manifest_path)
    description = _optional_string(metadata.get("description"), "metadata description", manifest_path)
    license_name = _optional_string(metadata.get("license"), "metadata license", manifest_path)
    author = _optional_string(metadata.get("author"), "metadata author", manifest_path)
    pypi = _optional_string(metadata.get("pypi"), "metadata pypi", manifest_path)
    pypi_publish = _optional_string(metadata.get("pypi_publish"), "metadata pypi_publish", manifest_path)
    stdlib = metadata.get("stdlib", False)
    if not isinstance(stdlib, bool):
        raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, f"metadata stdlib must be boolean in {manifest_path}")
    return MicropythonLibPackage(
        name=PurePosixPath(package_path).name,
        package_path=package_path,
        manifest_path=manifest_path,
        version=version,
        description=description,
        license=license_name,
        author=author,
        stdlib=stdlib,
        pypi=pypi,
        pypi_publish=pypi_publish,
    )


def _classification(package_path: str) -> PortDecision:
    library = PurePosixPath(package_path).parts[0]
    if library == "unix-ffi":
        evidence = PortEvidence(
            source=PortEvidenceSource.MANIFEST_PATH,
            classification=PortClassification.PORT_SPECIFIC,
            detail="micropython-lib unix-ffi package path",
            ports=("unix",),
            reference=package_path,
        )
        return classify_ports((evidence,))
    if library in {"python-stdlib", "python-ecosys"}:
        evidence = PortEvidence(
            source=PortEvidenceSource.MANIFEST_PATH,
            classification=PortClassification.PORTABLE,
            detail=f"micropython-lib {library} package path",
            reference=package_path,
        )
        return classify_ports((evidence,))
    return classify_ports(())


def _string(value: object, label: str, manifest_path: str) -> str:
    if not isinstance(value, str) or not value:
        raise MicropythonLibManifestError(ReasonCode.INVALID_MANIFEST, f"{label} must be a non-empty string in {manifest_path}")
    return value


def _optional_string(value: object, label: str, manifest_path: str) -> str | None:
    if value is None:
        return None
    return _string(value, label, manifest_path)


def _join_path(base: str, *relative_parts: str) -> str:
    resolved = list(PurePosixPath(_normalized_path(base, "manifest base path")).parts)
    for value in relative_parts:
        path = PurePosixPath(value.replace("\\", "/"))
        if path.is_absolute():
            raise MicropythonLibManifestError(ReasonCode.UNSAFE_PATH, f"Unsafe manifest path: {value}")
        for part in path.parts:
            if part in {"", "."}:
                continue
            if part == "..":
                if not resolved:
                    raise MicropythonLibManifestError(ReasonCode.UNSAFE_PATH, f"Unsafe manifest path: {value}")
                resolved.pop()
            else:
                resolved.append(part)
    if not resolved:
        raise MicropythonLibManifestError(ReasonCode.UNSAFE_PATH, "Manifest path escapes the snapshot root")
    return PurePosixPath(*resolved).as_posix()


def _normalized_path(value: str, label: str) -> str:
    path = PurePosixPath(value.replace("\\", "/"))
    if path.is_absolute() or not path.parts or any(part in {"", ".", ".."} for part in path.parts):
        raise MicropythonLibManifestError(ReasonCode.UNSAFE_PATH, f"Unsafe {label}: {value}")
    return path.as_posix()


def _archive_path(member: zipfile.ZipInfo) -> PurePosixPath:
    if "\\" in member.filename:
        raise MicropythonLibManifestError(ReasonCode.UNSAFE_PATH, f"Unsafe snapshot member: {member.filename}")
    path = PurePosixPath(member.filename)
    if path.is_absolute() or not path.parts or any(part in {"", ".", ".."} for part in path.parts):
        raise MicropythonLibManifestError(ReasonCode.UNSAFE_PATH, f"Unsafe snapshot member: {member.filename}")
    return path
