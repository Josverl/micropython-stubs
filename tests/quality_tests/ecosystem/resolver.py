"""Safe, cache-aware resolution of MicroPython MIP package references."""

from __future__ import annotations

import hashlib
import ipaddress
from io import BytesIO
import json
import os
import re
import shutil
import socket
import stat
from _thread import LockType
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path, PurePosixPath
from threading import Lock
from typing import Callable, Iterable, Protocol
from urllib.parse import quote, urljoin, urlsplit
import urllib.request
import uuid
import zipfile

import fasteners

from .catalog import normalize_package_reference
from .micropython_lib import MicropythonLibLimits, MicropythonLibManifestError, fetch_micropython_lib_snapshot
from .model import (
    CatalogProvenance,
    CatalogSource,
    DependencyDisposition,
    DependencyEdge,
    PackageAlias,
    PackageCandidate,
    PackageFile,
    PackageIdentity,
    PackageModelError,
    PackageRecord,
    PackageResolution,
    PortClassification,
    PortDecision,
    ReasonCode,
    RecordDisposition,
    SourceFamily,
    classify_ports,
    decide_payload,
)


DEFAULT_PACKAGE_INDEX = "https://micropython.org/pi/v2"
_PROVIDER_URLS = {
    "github": "https://raw.githubusercontent.com/{owner}/{repository}/{revision}/{path}",
    "gitlab": "https://gitlab.com/{owner}/{repository}/-/raw/{revision}/{path}",
    "codeberg": "https://codeberg.org/api/v1/repos/{owner}/{repository}/raw/{path}?ref={revision}",
}
_CACHE_THREAD_LOCKS: dict[str, LockType] = {}
_CACHE_THREAD_LOCKS_GUARD = Lock()


class CacheMode(str, Enum):
    USE_CACHE = "use_cache"
    REFRESH = "refresh"
    OFFLINE = "offline"


class ReferenceKind(str, Enum):
    MANIFEST = "manifest"
    FILE = "file"


class ResolverError(RuntimeError):
    def __init__(self, reason: ReasonCode, message: str) -> None:
        super().__init__(message)
        self.reason = reason


@dataclass(frozen=True)
class FetchResponse:
    data: bytes
    final_url: str
    resolved_revision: str | None = None
    from_cache: bool = False


class Fetcher(Protocol):
    def fetch(self, reference: str) -> FetchResponse: ...


AddressResolver = Callable[[str, int], Iterable[str]]


def _resolve_host_addresses(hostname: str, port: int) -> tuple[str, ...]:
    try:
        address_info = socket.getaddrinfo(hostname, port, type=socket.SOCK_STREAM)
    except socket.gaierror as error:
        raise ResolverError(ReasonCode.UNAVAILABLE, f"Unable to resolve fetch destination {hostname}: {error}") from error
    return tuple(sorted({str(item[4][0]) for item in address_info}))


@dataclass(frozen=True)
class DestinationPolicy:
    """Constrain remote fetches to approved hosts and public network addresses."""

    allowed_hosts: frozenset[str] | None = None
    allow_non_global_hosts: frozenset[str] = frozenset()
    resolver: AddressResolver = _resolve_host_addresses

    def __post_init__(self) -> None:
        if self.allowed_hosts is not None:
            object.__setattr__(self, "allowed_hosts", frozenset(_normalize_hostname(host) for host in self.allowed_hosts))
        object.__setattr__(
            self,
            "allow_non_global_hosts",
            frozenset(_normalize_hostname(host) for host in self.allow_non_global_hosts),
        )

    def validate(self, reference: str) -> None:
        parsed = urlsplit(reference)
        if parsed.scheme not in {"http", "https"} or parsed.hostname is None:
            raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, f"Unsupported fetch destination: {reference}")
        hostname = _normalize_hostname(parsed.hostname)
        if self.allowed_hosts is not None and hostname not in self.allowed_hosts:
            raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, f"Fetch destination host is not allowed: {hostname}")
        try:
            port = parsed.port or (443 if parsed.scheme == "https" else 80)
        except ValueError as error:
            raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, f"Invalid fetch destination port: {reference}") from error
        addresses = tuple(self.resolver(hostname, port))
        if not addresses:
            raise ResolverError(ReasonCode.UNAVAILABLE, f"Fetch destination did not resolve to an address: {hostname}")
        if hostname in self.allow_non_global_hosts:
            return
        for value in addresses:
            try:
                address = ipaddress.ip_address(value.split("%", 1)[0])
            except ValueError as error:
                raise ResolverError(ReasonCode.UNAVAILABLE, f"Fetch destination resolved to an invalid address: {value}") from error
            if not address.is_global or address.is_multicast:
                raise ResolverError(
                    ReasonCode.UNSUPPORTED_REFERENCE,
                    f"Fetch destination resolved to a non-public address: {hostname} ({address})",
                )


@dataclass(frozen=True)
class PlannedReference:
    requested_reference: str
    logical_reference: str
    fetch_reference: str
    requested_revision: str | None
    kind: ReferenceKind
    target_name: str | None = None


@dataclass(frozen=True)
class ResolverLimits:
    max_depth: int = 16
    max_files: int = 1024
    max_total_bytes: int = 32 * 1024 * 1024


@dataclass(frozen=True)
class ArchiveLimits:
    max_files: int = 4096
    max_total_bytes: int = 64 * 1024 * 1024


@dataclass(frozen=True)
class ResolvedPayload:
    file: PackageFile
    data: bytes


@dataclass(frozen=True)
class ResolutionResult:
    record: PackageRecord
    payloads: tuple[ResolvedPayload, ...] = ()
    workspace: Path | None = None


@dataclass(frozen=True)
class _PackageOutcome:
    resolved_revision: str | None
    package_version: str | None
    manifest_reference: str | None
    manifest_sha256: str | None


@dataclass
class _ResolutionState:
    payloads: dict[str, ResolvedPayload] = field(default_factory=dict)
    dependencies: list[DependencyEdge] = field(default_factory=list)
    resolved_packages: dict[str, _PackageOutcome] = field(default_factory=dict)
    stack: list[str] = field(default_factory=list)
    total_bytes: int = 0


def plan_mip_reference(
    reference: str,
    revision: str | None = None,
    *,
    index_url: str = DEFAULT_PACKAGE_INDEX,
) -> PlannedReference:
    """Translate a MIP package/file reference into one fetch operation."""
    requested_reference = reference.strip()
    if not requested_reference:
        raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, "package reference is empty")
    reference, embedded_revision = _split_revision(requested_reference)
    if revision is not None and embedded_revision is not None and revision != embedded_revision:
        raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, "conflicting package revisions")
    requested_revision = revision or embedded_revision

    provider = _provider_prefix(reference)
    suffix = _reference_suffix(reference)
    if suffix in {".py", ".mpy"}:
        logical_reference = reference
        fetch_reference = _rewrite_provider(reference, requested_revision) if provider else reference
        return PlannedReference(
            requested_reference,
            logical_reference,
            fetch_reference,
            requested_revision,
            ReferenceKind.FILE,
            _reference_name(reference),
        )

    if provider or _is_http_reference(reference):
        logical_reference = reference if suffix == ".json" else f"{reference.rstrip('/')}/package.json"
        fetch_reference = _rewrite_provider(logical_reference, requested_revision) if provider else logical_reference
    elif suffix == ".json":
        logical_reference = reference
        fetch_reference = reference
    elif ":" not in reference and "/" not in reference and "\\" not in reference:
        version = requested_revision or "latest"
        logical_reference = f"{index_url.rstrip('/')}/package/py/{reference}/{version}.json"
        fetch_reference = logical_reference
    else:
        raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, f"unsupported MIP package reference: {requested_reference}")

    return PlannedReference(
        requested_reference,
        logical_reference,
        fetch_reference,
        requested_revision,
        ReferenceKind.MANIFEST,
    )


class MipResolver:
    def __init__(
        self,
        fetcher: CachedFetcher,
        *,
        index_url: str = DEFAULT_PACKAGE_INDEX,
        limits: ResolverLimits = ResolverLimits(),
        workspace: PackageWorkspace | None = None,
        micropython_lib_revision: str = "HEAD",
    ) -> None:
        self.fetcher = fetcher
        self.index_url = index_url.rstrip("/")
        self.limits = limits
        self.workspace = workspace
        self.micropython_lib_revision = micropython_lib_revision

    def resolve_reference(
        self,
        reference: str,
        *,
        mode: CacheMode = CacheMode.USE_CACHE,
    ) -> ResolutionResult:
        try:
            identity, canonical_reference, source_family = normalize_package_reference(reference)
        except (ValueError, PackageModelError) as error:
            reason = error.reason if isinstance(error, PackageModelError) else ReasonCode.UNSUPPORTED_REFERENCE
            raise ResolverError(reason, str(error)) from error
        aliases = tuple(
            PackageAlias(CatalogSource.DIRECT, value)
            for value in sorted({reference, canonical_reference}, key=lambda value: (value.casefold(), value))
        )
        candidate = PackageCandidate(
            identity=identity,
            display_name=_candidate_name(identity, reference),
            source_family=source_family,
            install_reference=canonical_reference,
            aliases=aliases,
            provenance=(CatalogProvenance(CatalogSource.DIRECT, reference, identity.key),),
        )
        return self.resolve_candidate(candidate, mode=mode)

    def resolve_group(
        self,
        name: str,
        references: tuple[str, ...],
        *,
        classification: PortDecision | None = None,
        mode: CacheMode = CacheMode.USE_CACHE,
    ) -> ResolutionResult:
        group_name = name.strip().casefold()
        group_references = tuple(dict.fromkeys(reference.strip() for reference in references if reference.strip()))
        if not group_name or not group_references:
            raise ValueError("package group name and references must not be empty")

        group_reference = f"group:{group_name}"
        candidate = PackageCandidate(
            identity=PackageIdentity.index(f"group-{group_name}"),
            display_name=group_name,
            source_family=SourceFamily.MIP,
            install_reference=group_reference,
            aliases=(PackageAlias(CatalogSource.DIRECT, group_reference),),
            provenance=(CatalogProvenance(CatalogSource.DIRECT, group_reference, group_reference),),
        )
        selected_classification = classification or classify_ports([])
        state = _ResolutionState()
        try:
            for reference in group_references:
                try:
                    identity, canonical_reference, _ = normalize_package_reference(reference)
                except (ValueError, PackageModelError) as error:
                    reason = error.reason if isinstance(error, PackageModelError) else ReasonCode.UNSUPPORTED_REFERENCE
                    raise ResolverError(reason, f"Invalid package group member {reference}: {error}") from error
                planned = plan_mip_reference(canonical_reference, index_url=self.index_url)
                outcome = self._resolve_package(canonical_reference, None, identity, 1, state, mode)
                state.dependencies.append(
                    DependencyEdge(
                        requested_reference=canonical_reference,
                        requested_revision=planned.requested_revision,
                        depth=1,
                        disposition=DependencyDisposition.RESOLVED,
                        identity=identity,
                        resolved_revision=outcome.resolved_revision,
                    )
                )

            payloads = tuple(sorted(state.payloads.values(), key=lambda payload: payload.file.target))
            resolution = PackageResolution(
                requested_reference=group_reference,
                canonical_reference=group_reference,
                requested_revision=None,
                resolved_revision=None,
                manifest_reference=None,
                manifest_sha256=None,
                dependencies=tuple(state.dependencies),
                files=tuple(payload.file for payload in payloads),
            )
            decision = decide_payload(resolution.files)
            record = PackageRecord(
                candidate=candidate,
                resolution=resolution,
                classification=selected_classification,
                disposition=decision.disposition,
                reason=decision.reason,
            )
            workspace_path = (
                self.workspace.materialize(record, payloads)
                if self.workspace is not None and record.disposition is RecordDisposition.CHECK
                else None
            )
            return ResolutionResult(record, payloads, workspace_path)
        except ResolverError as error:
            return ResolutionResult(
                PackageRecord(
                    candidate=candidate,
                    classification=selected_classification,
                    disposition=RecordDisposition.ERROR,
                    reason=error.reason,
                )
            )

    def resolve_candidate(
        self,
        candidate: PackageCandidate,
        *,
        classification: PortDecision | None = None,
        mode: CacheMode = CacheMode.USE_CACHE,
    ) -> ResolutionResult:
        if candidate.source_family is SourceFamily.MICROPYTHON_LIB:
            return self._resolve_micropython_lib_candidate(candidate, classification, mode)

        classification = classification or classify_ports([])
        state = _ResolutionState()
        try:
            outcome = self._resolve_package(
                candidate.install_reference,
                None,
                candidate.identity,
                0,
                state,
                mode,
            )
            files = tuple(payload.file for payload in state.payloads.values())
            resolution = PackageResolution(
                requested_reference=candidate.install_reference,
                canonical_reference=candidate.install_reference,
                requested_revision=plan_mip_reference(candidate.install_reference, index_url=self.index_url).requested_revision,
                resolved_revision=outcome.resolved_revision,
                manifest_reference=outcome.manifest_reference,
                manifest_sha256=outcome.manifest_sha256,
                dependencies=tuple(state.dependencies),
                files=files,
                package_version=outcome.package_version,
            )
            decision = decide_payload(files)
            record = PackageRecord(
                candidate=candidate,
                resolution=resolution,
                classification=classification,
                disposition=decision.disposition,
                reason=decision.reason,
            )
            payloads = tuple(sorted(state.payloads.values(), key=lambda payload: payload.file.target))
            workspace_path = (
                self.workspace.materialize(record, payloads)
                if self.workspace is not None and record.disposition is RecordDisposition.CHECK
                else None
            )
            return ResolutionResult(record, payloads, workspace_path)
        except ResolverError as error:
            return ResolutionResult(
                PackageRecord(
                    candidate=candidate,
                    classification=classification,
                    disposition=RecordDisposition.ERROR,
                    reason=error.reason,
                )
            )

    def _resolve_micropython_lib_candidate(
        self,
        candidate: PackageCandidate,
        classification: PortDecision | None,
        mode: CacheMode,
    ) -> ResolutionResult:
        try:
            logical_reference, embedded_revision = _split_revision(candidate.install_reference)
            requested_revision = embedded_revision or self.micropython_lib_revision
            repository_reference = "github:micropython/micropython-lib"
            if logical_reference.startswith(f"{repository_reference}/"):
                package_reference = logical_reference.removeprefix(f"{repository_reference}/")
            elif logical_reference == repository_reference:
                raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, "micropython-lib reference must identify a package")
            else:
                package_reference = logical_reference

            snapshot = fetch_micropython_lib_snapshot(
                lambda reference: self.fetcher.fetch(reference, mode).data,
                requested_revision,
                limits=MicropythonLibLimits(
                    max_depth=self.limits.max_depth,
                    max_files=self.limits.max_files,
                    max_total_bytes=self.limits.max_total_bytes,
                ),
            )
            resolved_revision = snapshot.resolved_revision
            source_resolution = snapshot.resolve(package_reference)
            state = _ResolutionState()
            for source_file in source_resolution.files:
                identity = PackageIdentity.repository(
                    "github",
                    "micropython",
                    "micropython-lib",
                    source_file.owner_path,
                )
                self._add_payload(
                    state,
                    identity,
                    source_file.target,
                    snapshot.raw_reference(source_file.source_path),
                    source_file.data,
                    source_file.depth,
                )

            dependencies = tuple(
                DependencyEdge(
                    requested_reference=f"github:micropython/micropython-lib/{item.package_path}",
                    requested_revision=item.requested_version,
                    depth=item.depth,
                    disposition=DependencyDisposition.RESOLVED,
                    identity=PackageIdentity.repository("github", "micropython", "micropython-lib", item.package_path),
                    resolved_revision=resolved_revision,
                )
                for item in source_resolution.dependencies
            )
            manifest_reference = snapshot.raw_reference(source_resolution.package.manifest_path)
            manifest_data = snapshot.files[source_resolution.package.manifest_path]
            payloads = tuple(sorted(state.payloads.values(), key=lambda item: (item.file.dependency_depth, item.file.target)))
            resolution = PackageResolution(
                requested_reference=candidate.install_reference,
                canonical_reference=logical_reference,
                requested_revision=requested_revision,
                resolved_revision=resolved_revision,
                manifest_reference=manifest_reference,
                manifest_sha256=hashlib.sha256(manifest_data).hexdigest(),
                dependencies=dependencies,
                files=tuple(item.file for item in payloads),
                package_version=source_resolution.package.version,
            )
            decision = decide_payload(resolution.files)
            selected_classification = classification or source_resolution.classification
            if (
                selected_classification.classification is PortClassification.UNKNOWN
                and not selected_classification.evidence
                and source_resolution.classification.classification is not PortClassification.UNKNOWN
            ):
                selected_classification = source_resolution.classification
            record = PackageRecord(
                candidate=candidate,
                resolution=resolution,
                classification=selected_classification,
                disposition=decision.disposition,
                reason=decision.reason,
            )
            workspace_path = (
                self.workspace.materialize(record, payloads)
                if self.workspace is not None and record.disposition is RecordDisposition.CHECK
                else None
            )
            return ResolutionResult(record, payloads, workspace_path)
        except (MicropythonLibManifestError, ResolverError) as error:
            return ResolutionResult(
                PackageRecord(
                    candidate=candidate,
                    classification=classification or classify_ports([]),
                    disposition=RecordDisposition.ERROR,
                    reason=error.reason,
                )
            )

    def _resolve_package(
        self,
        reference: str,
        revision: str | None,
        identity: PackageIdentity,
        depth: int,
        state: _ResolutionState,
        mode: CacheMode,
    ) -> _PackageOutcome:
        if depth > self.limits.max_depth:
            raise ResolverError(ReasonCode.LIMIT_EXCEEDED, f"Dependency depth exceeds {self.limits.max_depth}")
        planned = plan_mip_reference(reference, revision, index_url=self.index_url)
        package_key = f"{planned.logical_reference}@{planned.requested_revision or ''}"
        if package_key in state.stack:
            chain = " -> ".join((*state.stack, package_key))
            raise ResolverError(ReasonCode.DEPENDENCY_CYCLE, f"Dependency cycle: {chain}")
        if package_key in state.resolved_packages:
            return state.resolved_packages[package_key]

        state.stack.append(package_key)
        try:
            provider_revision = self._resolve_provider_revision(planned, mode)
            fetch_reference = _resolved_fetch_reference(planned, provider_revision)
            if planned.kind is ReferenceKind.FILE:
                response = self._fetch(fetch_reference, state, mode)
                self._add_payload(
                    state,
                    identity,
                    planned.target_name or _reference_name(planned.logical_reference),
                    fetch_reference,
                    response.data,
                    depth,
                )
                outcome = _PackageOutcome(provider_revision or response.resolved_revision or planned.requested_revision, None, None, None)
            else:
                response = self._fetch(fetch_reference, state, mode)
                manifest_sha256 = hashlib.sha256(response.data).hexdigest()
                manifest = _parse_manifest(response.data, planned.logical_reference)
                manifest_version = manifest.get("version")
                if manifest_version is not None and not isinstance(manifest_version, str):
                    raise ResolverError(ReasonCode.INVALID_MANIFEST, "manifest version must be a string")
                resolved_revision = response.resolved_revision or provider_revision or manifest_version or planned.requested_revision
                self._resolve_manifest_files(manifest, planned, provider_revision, identity, depth, state, mode)
                self._resolve_dependencies(manifest, depth, state, mode)
                outcome = _PackageOutcome(resolved_revision, manifest_version, fetch_reference, manifest_sha256)
            state.resolved_packages[package_key] = outcome
            return outcome
        finally:
            state.stack.pop()

    def _resolve_manifest_files(
        self,
        manifest: dict[str, object],
        planned: PlannedReference,
        provider_revision: str | None,
        identity: PackageIdentity,
        depth: int,
        state: _ResolutionState,
        mode: CacheMode,
    ) -> None:
        for target, source in _manifest_pairs(manifest, "urls"):
            source_reference = _relative_reference(planned.logical_reference, source)
            _validate_target(identity, target, source_reference, depth)
            fetch_reference = self._source_fetch_reference(
                source_reference,
                planned.logical_reference,
                provider_revision,
                mode,
            )
            response = self._fetch(fetch_reference, state, mode)
            self._add_payload(state, identity, target, fetch_reference, response.data, depth)

        for target, short_hash in _manifest_pairs(manifest, "hashes"):
            if re.fullmatch(r"[0-9a-fA-F]{8,64}", short_hash) is None:
                raise ResolverError(ReasonCode.INVALID_MANIFEST, f"Invalid package-index hash for {target}")
            _validate_target(identity, target, short_hash, depth)
            source_reference = f"{self.index_url}/file/{short_hash[:2]}/{short_hash}"
            response = self._fetch(source_reference, state, mode)
            digest = hashlib.sha256(response.data).hexdigest()
            if not digest.startswith(short_hash.casefold()):
                raise ResolverError(ReasonCode.INVALID_MANIFEST, f"Hash mismatch for {target}")
            self._add_payload(state, identity, target, source_reference, response.data, depth)

    def _source_fetch_reference(
        self,
        source_reference: str,
        package_reference: str,
        package_revision: str | None,
        mode: CacheMode,
    ) -> str:
        if _provider_prefix(source_reference) is None:
            return source_reference
        logical_reference, requested_revision = _split_revision(source_reference)
        planned = PlannedReference(
            requested_reference=source_reference,
            logical_reference=logical_reference,
            fetch_reference=_rewrite_provider(logical_reference, requested_revision),
            requested_revision=requested_revision,
            kind=ReferenceKind.FILE,
        )
        if requested_revision is None and _provider_repository(logical_reference) == _provider_repository(package_reference):
            return _resolved_fetch_reference(planned, package_revision)
        return _resolved_fetch_reference(planned, self._resolve_provider_revision(planned, mode))

    def _resolve_provider_revision(self, planned: PlannedReference, mode: CacheMode) -> str | None:
        repository = _provider_repository(planned.logical_reference)
        if repository is None:
            return None
        provider, owner, name = repository
        requested = planned.requested_revision
        if requested is not None and re.fullmatch(r"[0-9a-fA-F]{40,64}", requested):
            return requested.casefold()

        if provider == "github":
            reference = quote(requested or "HEAD", safe="")
            document = self._fetch_provider_document(
                f"https://api.github.com/repos/{quote(owner, safe='')}/{quote(name, safe='')}/commits/{reference}",
                mode,
            )
            return _provider_commit_id(document, "sha", provider)

        if provider == "gitlab":
            project = quote(f"{owner}/{name}", safe="")
            if requested is not None and requested.casefold() != "head":
                reference = quote(requested, safe="")
                document = self._fetch_provider_document(
                    f"https://gitlab.com/api/v4/projects/{project}/repository/commits/{reference}",
                    mode,
                )
            else:
                document = self._fetch_provider_document(
                    f"https://gitlab.com/api/v4/projects/{project}/repository/commits?per_page=1",
                    mode,
                )
                if not isinstance(document, list) or not document:
                    raise ResolverError(ReasonCode.UNAVAILABLE, "GitLab returned no default-branch commit")
                document = document[0]
            return _provider_commit_id(document, "id", provider)

        if requested is None or requested.casefold() == "head":
            repository_document = self._fetch_provider_document(
                f"https://codeberg.org/api/v1/repos/{quote(owner, safe='')}/{quote(name, safe='')}",
                mode,
            )
            if not isinstance(repository_document, dict) or not isinstance(repository_document.get("default_branch"), str):
                raise ResolverError(ReasonCode.UNAVAILABLE, "Codeberg returned no default branch")
            requested = repository_document["default_branch"]
        document = self._fetch_provider_document(
            f"https://codeberg.org/api/v1/repos/{quote(owner, safe='')}/{quote(name, safe='')}/git/commits/{quote(requested, safe='')}",
            mode,
        )
        return _provider_commit_id(document, "sha", provider)

    def _fetch_provider_document(self, reference: str, mode: CacheMode) -> object:
        response = self.fetcher.fetch(reference, mode)
        try:
            return json.loads(response.data.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ResolverError(ReasonCode.UNAVAILABLE, f"Provider revision response is invalid: {reference}") from error

    def _resolve_dependencies(
        self,
        manifest: dict[str, object],
        depth: int,
        state: _ResolutionState,
        mode: CacheMode,
    ) -> None:
        for reference, revision in _manifest_pairs(manifest, "deps"):
            try:
                identity, canonical_reference, _ = normalize_package_reference(reference)
            except (ValueError, PackageModelError) as error:
                reason = error.reason if isinstance(error, PackageModelError) else ReasonCode.UNSUPPORTED_REFERENCE
                raise ResolverError(reason, f"Invalid dependency {reference}: {error}") from error
            outcome = self._resolve_package(canonical_reference, revision or None, identity, depth + 1, state, mode)
            state.dependencies.append(
                DependencyEdge(
                    requested_reference=canonical_reference,
                    requested_revision=revision or None,
                    depth=depth + 1,
                    disposition=DependencyDisposition.RESOLVED,
                    identity=identity,
                    resolved_revision=outcome.resolved_revision,
                )
            )

    def _fetch(self, reference: str, state: _ResolutionState, mode: CacheMode) -> FetchResponse:
        response = self.fetcher.fetch(reference, mode)
        state.total_bytes += len(response.data)
        if state.total_bytes > self.limits.max_total_bytes:
            raise ResolverError(ReasonCode.LIMIT_EXCEEDED, f"Resolved payload exceeds {self.limits.max_total_bytes} bytes")
        return response

    def _add_payload(
        self,
        state: _ResolutionState,
        identity: PackageIdentity,
        target: str,
        source: str,
        data: bytes,
        depth: int,
    ) -> None:
        if len(state.payloads) >= self.limits.max_files and target not in state.payloads:
            raise ResolverError(ReasonCode.LIMIT_EXCEEDED, f"Resolved payload exceeds {self.limits.max_files} files")
        try:
            package_file = PackageFile(
                owner=identity,
                target=target,
                source=source,
                dependency_depth=depth,
                sha256=hashlib.sha256(data).hexdigest(),
                size=len(data),
            )
        except ValueError as error:
            raise ResolverError(ReasonCode.UNSAFE_PATH, str(error)) from error
        existing_target = next(
            (existing_target for existing_target in state.payloads if existing_target.casefold() == package_file.target.casefold()),
            None,
        )
        existing = state.payloads.get(existing_target) if existing_target is not None else None
        if existing is not None:
            if existing.file.target == package_file.target and existing.data == data and existing.file.source == package_file.source:
                return
            raise ResolverError(ReasonCode.TARGET_COLLISION, f"Multiple files target {package_file.target}")
        state.payloads[package_file.target] = ResolvedPayload(package_file, data)


class PackageWorkspace:
    """Materialize immutable package closures under independently cleanable roots."""

    def __init__(self, root: Path) -> None:
        self.root = root

    def package_root(self, identity: PackageIdentity) -> Path:
        name = re.sub(r"[^a-z0-9._-]+", "-", PurePosixPath(identity.value).name.casefold()).strip("-.")
        name = name or "package"
        digest = hashlib.sha256(identity.key.encode("utf-8")).hexdigest()[:12]
        return self.root / "packages" / f"{name[:48]}-{digest}"

    def materialize(self, record: PackageRecord, payloads: tuple[ResolvedPayload, ...]) -> Path:
        if record.resolution is None:
            raise ResolverError(ReasonCode.INVALID_MANIFEST, "resolved package record has no resolution")
        package_root = self.package_root(record.candidate.identity)
        revision_key = _workspace_revision_key(record)
        destination = package_root / revision_key
        lock_path = self.root / "locks" / f"package-{hashlib.sha256(record.candidate.identity.key.encode()).hexdigest()}.lock"
        lock_path.parent.mkdir(parents=True, exist_ok=True)
        with _cache_thread_lock(lock_path), fasteners.InterProcessLock(str(lock_path)):
            metadata = _workspace_metadata(record)
            if self._is_valid(destination, metadata):
                return destination
            _remove_path(destination)

            stage = self.root / ".staging" / f"{package_root.name}-{uuid.uuid4().hex}"
            source_root = stage / "source"
            try:
                source_root.mkdir(parents=True)
                for payload in payloads:
                    object_path = self._store_object(payload)
                    target_path = _safe_child(source_root, payload.file.target)
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(object_path, target_path)
                _atomic_write(stage / "metadata.json", (json.dumps(metadata, indent=2, sort_keys=True) + "\n").encode())
                destination.parent.mkdir(parents=True, exist_ok=True)
                if destination.exists():
                    _remove_path(destination)
                os.replace(stage, destination)
                return destination
            except OSError as error:
                raise ResolverError(ReasonCode.UNAVAILABLE, f"Unable to materialize {destination}: {error}") from error
            finally:
                if stage.exists():
                    shutil.rmtree(stage, ignore_errors=True)

    def clean(self, identity: PackageIdentity) -> None:
        package_root = self.package_root(identity)
        lock_path = self.root / "locks" / f"package-{hashlib.sha256(identity.key.encode()).hexdigest()}.lock"
        lock_path.parent.mkdir(parents=True, exist_ok=True)
        with _cache_thread_lock(lock_path), fasteners.InterProcessLock(str(lock_path)):
            _remove_path(package_root)

    def _store_object(self, payload: ResolvedPayload) -> Path:
        digest = hashlib.sha256(payload.data).hexdigest()
        if payload.file.sha256 is not None and payload.file.sha256 != digest:
            raise ResolverError(ReasonCode.CACHE_CORRUPT, f"Payload hash mismatch: {payload.file.target}")
        object_path = self.root / "objects" / "sha256" / digest[:2] / digest
        if object_path.is_file():
            if hashlib.sha256(object_path.read_bytes()).hexdigest() != digest:
                raise ResolverError(ReasonCode.CACHE_CORRUPT, f"Object hash mismatch: {digest}")
            return object_path
        object_path.parent.mkdir(parents=True, exist_ok=True)
        lock_path = self.root / "locks" / f"object-{digest}.lock"
        with _cache_thread_lock(lock_path), fasteners.InterProcessLock(str(lock_path)):
            if not object_path.is_file():
                _atomic_write(object_path, payload.data)
        return object_path

    def _is_valid(self, destination: Path, expected_metadata: dict[str, object]) -> bool:
        metadata_path = destination / "metadata.json"
        source_root = destination / "source"
        if not metadata_path.is_file() or not source_root.is_dir():
            return False
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            if metadata != expected_metadata:
                return False
            entries = tuple(source_root.rglob("*"))
            if any(path.is_symlink() for path in entries):
                return False
            actual_targets = {path.relative_to(source_root).as_posix() for path in entries if path.is_file()}
            expected_files = expected_metadata.get("files")
            if not isinstance(expected_files, list):
                return False
            expected_targets = {
                str(file_metadata["target"])
                for file_metadata in expected_files
                if isinstance(file_metadata, dict) and isinstance(file_metadata.get("target"), str)
            }
            if actual_targets != expected_targets or len(expected_targets) != len(expected_files):
                return False
            for file_metadata in expected_files:
                if not isinstance(file_metadata, dict):
                    return False
                target = file_metadata.get("target")
                digest = file_metadata.get("sha256")
                if not isinstance(target, str) or not isinstance(digest, str):
                    return False
                file_path = _safe_child(source_root, target)
                if not file_path.is_file() or hashlib.sha256(file_path.read_bytes()).hexdigest() != digest:
                    return False
            return True
        except (OSError, json.JSONDecodeError, ResolverError):
            return False


def safe_extract_zip(
    archive: bytes,
    destination: Path,
    *,
    limits: ArchiveLimits = ArchiveLimits(),
) -> tuple[Path, ...]:
    """Atomically extract a bounded ZIP without links, traversal, or collisions."""
    if destination.exists():
        raise ResolverError(ReasonCode.TARGET_COLLISION, f"Archive destination already exists: {destination}")
    stage = destination.with_name(f".{destination.name}.{uuid.uuid4().hex}.tmp")
    extracted: list[Path] = []
    total_bytes = 0
    try:
        with zipfile.ZipFile(BytesIO(archive)) as package:
            files = [info for info in package.infolist() if not info.is_dir()]
            if len(files) > limits.max_files:
                raise ResolverError(ReasonCode.LIMIT_EXCEEDED, f"Archive exceeds {limits.max_files} files")
            seen: set[str] = set()
            for info in files:
                if stat.S_ISLNK(info.external_attr >> 16):
                    raise ResolverError(ReasonCode.UNSAFE_PATH, f"Archive contains a symbolic link: {info.filename}")
                if info.flag_bits & 0x1:
                    raise ResolverError(ReasonCode.UNSUPPORTED_SOURCE, f"Archive member is encrypted: {info.filename}")
                target = _safe_child(stage, info.filename)
                normalized = target.relative_to(stage).as_posix()
                collision_key = normalized.casefold()
                if collision_key in seen:
                    raise ResolverError(ReasonCode.TARGET_COLLISION, f"Duplicate archive target: {normalized}")
                seen.add(collision_key)
                total_bytes += info.file_size
                if total_bytes > limits.max_total_bytes:
                    raise ResolverError(ReasonCode.LIMIT_EXCEEDED, f"Archive exceeds {limits.max_total_bytes} bytes")
                target.parent.mkdir(parents=True, exist_ok=True)
                with package.open(info) as source, target.open("wb") as output:
                    shutil.copyfileobj(source, output)
                extracted.append(target.relative_to(stage))
        destination.parent.mkdir(parents=True, exist_ok=True)
        os.replace(stage, destination)
        return tuple(destination / path for path in sorted(extracted))
    except (OSError, zipfile.BadZipFile) as error:
        raise ResolverError(ReasonCode.INVALID_MANIFEST, f"Unable to extract archive: {error}") from error
    finally:
        if stage.exists():
            shutil.rmtree(stage, ignore_errors=True)


def _normalize_hostname(hostname: str) -> str:
    normalized = hostname.rstrip(".").casefold()
    if not normalized:
        raise ValueError("destination hostname must not be empty")
    return normalized


class _PolicyRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self, validate: Callable[[str], None]) -> None:
        self.validate = validate

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.validate(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


class UrlFetcher:
    """Fetch bounded HTTP(S) or explicitly rooted local files."""

    def __init__(
        self,
        *,
        local_roots: tuple[Path, ...] = (),
        destination_policy: DestinationPolicy | None = None,
        allow_http: bool = False,
        max_bytes: int = 8 * 1024 * 1024,
        timeout: float = 30.0,
    ) -> None:
        self.local_roots = tuple(root.resolve() for root in local_roots)
        self.destination_policy = destination_policy or DestinationPolicy()
        self.allow_http = allow_http
        self.max_bytes = max_bytes
        self.timeout = timeout

    def _validate_remote_reference(self, reference: str) -> None:
        parsed = urlsplit(reference)
        if parsed.scheme not in {"http", "https"}:
            raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, f"Redirected to unsupported URL: {reference}")
        if parsed.scheme == "http" and not self.allow_http:
            raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, "plain HTTP fetching is disabled")
        if parsed.username is not None or parsed.password is not None:
            raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, "authenticated URLs are not allowed")
        self.destination_policy.validate(reference)

    def fetch(self, reference: str) -> FetchResponse:
        parsed = urlsplit(reference)
        is_windows_path = re.match(r"^[A-Za-z]:[\\/]", reference) is not None
        if parsed.scheme in {"http", "https"}:
            self._validate_remote_reference(reference)
            request = urllib.request.Request(reference, headers={"User-Agent": "micropython-stubs-ecosystem-qa/1"})
            opener = urllib.request.build_opener(_PolicyRedirectHandler(self._validate_remote_reference))
            try:
                with opener.open(request, timeout=self.timeout) as response:
                    data = response.read(self.max_bytes + 1)
                    final_url = response.geturl()
                    resolved_revision = response.headers.get("X-Resolved-Revision")
            except (OSError, ValueError) as error:
                raise ResolverError(ReasonCode.UNAVAILABLE, f"Unable to fetch {reference}: {error}") from error
            if len(data) > self.max_bytes:
                raise ResolverError(ReasonCode.LIMIT_EXCEEDED, f"Response exceeds {self.max_bytes} bytes: {reference}")
            final_scheme = urlsplit(final_url).scheme
            if final_scheme not in {"http", "https"} or (final_scheme == "http" and not self.allow_http):
                raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, f"Redirected to unsupported URL: {final_url}")
            return FetchResponse(data, final_url, resolved_revision)

        if parsed.scheme not in {"", "file"} and not is_windows_path:
            raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, f"Unsupported fetch scheme: {parsed.scheme}")
        if parsed.scheme == "file" and parsed.netloc not in {"", "localhost"}:
            raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, f"Remote file URLs are not allowed: {reference}")
        local_reference = urllib.request.url2pathname(parsed.path) if parsed.scheme == "file" else reference
        path = Path(local_reference).resolve()
        if not any(path.is_relative_to(root) for root in self.local_roots):
            raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, f"Local path is outside configured roots: {path}")
        try:
            data = path.read_bytes()
        except OSError as error:
            raise ResolverError(ReasonCode.UNAVAILABLE, f"Unable to read {path}: {error}") from error
        if len(data) > self.max_bytes:
            raise ResolverError(ReasonCode.LIMIT_EXCEEDED, f"File exceeds {self.max_bytes} bytes: {path}")
        return FetchResponse(data, path.as_uri(), hashlib.sha256(data).hexdigest())


class CachedFetcher:
    """Persist fetch responses by requested URL for deterministic offline replay."""

    def __init__(self, root: Path, upstream: Fetcher | None, *, max_bytes: int = 8 * 1024 * 1024) -> None:
        self.root = root
        self.upstream = upstream
        self.max_bytes = max_bytes

    def fetch(self, reference: str, mode: CacheMode = CacheMode.USE_CACHE) -> FetchResponse:
        cache_key = hashlib.sha256(reference.encode("utf-8")).hexdigest()
        entry_path = self.root / "responses" / cache_key[:2] / cache_key
        lock_path = self.root / "locks" / f"response-{cache_key}.lock"
        lock_path.parent.mkdir(parents=True, exist_ok=True)
        with _cache_thread_lock(lock_path), fasteners.InterProcessLock(str(lock_path)):
            if mode is not CacheMode.REFRESH:
                cached = self._read(entry_path, reference)
                if cached is not None:
                    return cached
            if mode is CacheMode.OFFLINE:
                raise ResolverError(ReasonCode.CACHE_MISS, f"No cached response for {reference}")
            if self.upstream is None:
                raise ResolverError(ReasonCode.UNAVAILABLE, f"No fetcher configured for {reference}")
            response = self.upstream.fetch(reference)
            if len(response.data) > self.max_bytes:
                raise ResolverError(ReasonCode.LIMIT_EXCEEDED, f"Response exceeds {self.max_bytes} bytes: {reference}")
            self._write(entry_path, reference, response)
            return response

    def _read(self, entry_path: Path, reference: str) -> FetchResponse | None:
        body_path = entry_path / "body"
        metadata_path = entry_path / "metadata.json"
        if not body_path.exists() and not metadata_path.exists():
            return None
        if not body_path.is_file() or not metadata_path.is_file():
            raise ResolverError(ReasonCode.CACHE_CORRUPT, f"Incomplete cache entry for {reference}")
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            data = body_path.read_bytes()
        except (OSError, json.JSONDecodeError) as error:
            raise ResolverError(ReasonCode.CACHE_CORRUPT, f"Unreadable cache entry for {reference}: {error}") from error
        if not isinstance(metadata, dict):
            raise ResolverError(ReasonCode.CACHE_CORRUPT, f"Cache metadata is not an object for {reference}")
        final_url = metadata.get("final_url")
        resolved_revision = metadata.get("resolved_revision")
        if (
            metadata.get("reference") != reference
            or metadata.get("sha256") != hashlib.sha256(data).hexdigest()
            or metadata.get("size") != len(data)
            or not isinstance(final_url, str)
            or (resolved_revision is not None and not isinstance(resolved_revision, str))
        ):
            raise ResolverError(ReasonCode.CACHE_CORRUPT, f"Cache entry hash mismatch for {reference}")
        return FetchResponse(
            data=data,
            final_url=final_url,
            resolved_revision=resolved_revision,
            from_cache=True,
        )

    def _write(self, entry_path: Path, reference: str, response: FetchResponse) -> None:
        entry_path.mkdir(parents=True, exist_ok=True)
        metadata = {
            "reference": reference,
            "final_url": response.final_url,
            "resolved_revision": response.resolved_revision,
            "sha256": hashlib.sha256(response.data).hexdigest(),
            "size": len(response.data),
        }
        _atomic_write(entry_path / "body", response.data)
        _atomic_write(entry_path / "metadata.json", (json.dumps(metadata, indent=2, sort_keys=True) + "\n").encode())


def _cache_thread_lock(lock_path: Path) -> LockType:
    key = os.path.normcase(str(lock_path.resolve()))
    with _CACHE_THREAD_LOCKS_GUARD:
        lock = _CACHE_THREAD_LOCKS.get(key)
        if lock is None:
            lock = Lock()
            _CACHE_THREAD_LOCKS[key] = lock
        return lock


def _atomic_write(path: Path, data: bytes) -> None:
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        temporary.write_bytes(data)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def _split_revision(reference: str) -> tuple[str, str | None]:
    if _provider_prefix(reference) is None or "@" not in reference:
        return reference, None
    package, revision = reference.rsplit("@", 1)
    if not package or not revision:
        raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, f"invalid provider revision: {reference}")
    return package, revision


def _provider_prefix(reference: str) -> str | None:
    prefix = reference.split(":", 1)[0].casefold()
    return prefix if prefix in _PROVIDER_URLS else None


def _rewrite_provider(reference: str, revision: str | None) -> str:
    provider = _provider_prefix(reference)
    if provider is None:
        return reference
    parts = reference.split(":", 1)[1].split("/")
    if len(parts) < 3 or not all(parts[:3]):
        raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, f"invalid {provider} reference: {reference}")
    owner, repository = parts[:2]
    path = "/".join(parts[2:])
    return _PROVIDER_URLS[provider].format(
        owner=quote(owner, safe=""),
        repository=quote(repository, safe=""),
        revision=quote(revision or "HEAD", safe=""),
        path=quote(path, safe="/"),
    )


def _provider_repository(reference: str) -> tuple[str, str, str] | None:
    provider = _provider_prefix(reference)
    if provider is None:
        return None
    logical_reference, _ = _split_revision(reference)
    parts = logical_reference.split(":", 1)[1].split("/")
    if len(parts) < 2 or not all(parts[:2]):
        raise ResolverError(ReasonCode.UNSUPPORTED_REFERENCE, f"invalid {provider} reference: {reference}")
    return provider, parts[0].casefold(), parts[1].casefold()


def _resolved_fetch_reference(planned: PlannedReference, resolved_revision: str | None) -> str:
    if _provider_prefix(planned.logical_reference) is not None and resolved_revision is not None:
        return _rewrite_provider(planned.logical_reference, resolved_revision)
    return planned.fetch_reference


def _provider_commit_id(document: object, field: str, provider: str) -> str:
    value = document.get(field) if isinstance(document, dict) else None
    if not isinstance(value, str) or re.fullmatch(r"[0-9a-fA-F]{40,64}", value) is None:
        raise ResolverError(ReasonCode.UNAVAILABLE, f"{provider} returned no immutable commit")
    return value.casefold()


def _is_http_reference(reference: str) -> bool:
    return urlsplit(reference).scheme in {"http", "https"}


def _reference_suffix(reference: str) -> str:
    path = urlsplit(reference).path if _is_http_reference(reference) else reference
    return Path(path).suffix.casefold()


def _reference_name(reference: str) -> str:
    path = urlsplit(reference).path if _is_http_reference(reference) else reference.split("@", 1)[0]
    return Path(path).name


def _candidate_name(identity: PackageIdentity, reference: str) -> str:
    if identity.kind.value == "index":
        return identity.value
    name = PurePosixPath(identity.value).name
    return name or reference


def _parse_manifest(data: bytes, reference: str) -> dict[str, object]:
    try:
        document = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ResolverError(ReasonCode.INVALID_MANIFEST, f"Invalid JSON manifest {reference}: {error}") from error
    if not isinstance(document, dict):
        raise ResolverError(ReasonCode.INVALID_MANIFEST, f"Manifest must be an object: {reference}")
    manifest_format = document.get("v")
    if manifest_format is not None and (type(manifest_format) is not int or manifest_format != 1):
        raise ResolverError(ReasonCode.INVALID_MANIFEST, f"Unsupported manifest format in {reference}: {manifest_format!r}")
    for field_name in ("urls", "hashes", "deps"):
        _manifest_pairs(document, field_name)
    return document


def _manifest_pairs(manifest: dict[str, object], field_name: str) -> tuple[tuple[str, str], ...]:
    value = manifest.get(field_name, ())
    if not isinstance(value, (list, tuple)):
        raise ResolverError(ReasonCode.INVALID_MANIFEST, f"manifest {field_name} must be an array")
    pairs: list[tuple[str, str]] = []
    for item in value:
        if not isinstance(item, (list, tuple)) or len(item) != 2 or not all(isinstance(part, str) for part in item):
            raise ResolverError(ReasonCode.INVALID_MANIFEST, f"manifest {field_name} entries must be string pairs")
        pairs.append((item[0], item[1]))
    return tuple(pairs)


def _relative_reference(manifest_reference: str, source: str) -> str:
    if _provider_prefix(source) is not None or _is_http_reference(source):
        return source
    if _provider_prefix(manifest_reference) is not None:
        return f"{manifest_reference.rpartition('/')[0]}/{source}"
    if _is_http_reference(manifest_reference):
        return urljoin(manifest_reference, source)
    return str((Path(manifest_reference).parent / source).resolve())


def _validate_target(identity: PackageIdentity, target: str, source: str, depth: int) -> None:
    try:
        PackageFile(identity, target, source, dependency_depth=depth)
    except ValueError as error:
        raise ResolverError(ReasonCode.UNSAFE_PATH, str(error)) from error


def _safe_child(root: Path, relative_path: str) -> Path:
    if "\\" in relative_path:
        raise ResolverError(ReasonCode.UNSAFE_PATH, f"Path must use POSIX separators: {relative_path}")
    parts = relative_path.split("/")
    if not relative_path or any(part in {"", ".", ".."} for part in parts) or (len(parts[0]) >= 2 and parts[0][1] == ":"):
        raise ResolverError(ReasonCode.UNSAFE_PATH, f"Unsafe relative path: {relative_path}")
    target = root.joinpath(*parts)
    try:
        target.resolve().relative_to(root.resolve())
    except ValueError as error:
        raise ResolverError(ReasonCode.UNSAFE_PATH, f"Path escapes destination: {relative_path}") from error
    return target


def _remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink(missing_ok=True)
    elif path.exists():
        shutil.rmtree(path)


def _workspace_revision_key(record: PackageRecord) -> str:
    assert record.resolution is not None
    label = record.resolution.resolved_revision or "content"
    evidence = "\n".join(
        (
            label,
            record.resolution.manifest_sha256 or "",
            *(f"{file.target}:{file.sha256 or ''}" for file in sorted(record.resolution.files, key=lambda item: item.target)),
        )
    )
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", label).strip("-.") or "content"
    digest = hashlib.sha256(evidence.encode()).hexdigest()[:12]
    return f"{slug[:48]}-{digest}"


def _workspace_metadata(record: PackageRecord) -> dict[str, object]:
    assert record.resolution is not None
    return {
        "schema_version": 1,
        "identity": record.candidate.identity.key,
        "install_reference": record.candidate.install_reference,
        "disposition": record.disposition.value,
        "reason": record.reason.value if record.reason else None,
        "requested_reference": record.resolution.requested_reference,
        "requested_revision": record.resolution.requested_revision,
        "resolved_revision": record.resolution.resolved_revision,
        "package_version": record.resolution.package_version,
        "manifest_reference": record.resolution.manifest_reference,
        "manifest_sha256": record.resolution.manifest_sha256,
        "dependencies": [
            {
                "requested_reference": dependency.requested_reference,
                "requested_revision": dependency.requested_revision,
                "depth": dependency.depth,
                "disposition": dependency.disposition.value,
                "identity": dependency.identity.key if dependency.identity else None,
                "resolved_revision": dependency.resolved_revision,
                "reason": dependency.reason.value if dependency.reason else None,
            }
            for dependency in record.resolution.dependencies
        ],
        "files": [
            {
                "owner": file.owner.key,
                "target": file.target,
                "source": file.source,
                "dependency_depth": file.dependency_depth,
                "sha256": file.sha256,
                "size": file.size,
                "kind": file.kind.value,
            }
            for file in record.resolution.files
        ],
    }
