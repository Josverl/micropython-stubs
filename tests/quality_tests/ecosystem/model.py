"""Normalized records shared by ecosystem catalog and package tooling."""

from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping
from urllib.parse import urlsplit, urlunsplit


class IdentityKind(str, Enum):
    REPOSITORY = "repository"
    INDEX = "index"
    URL = "url"


class CatalogSource(str, Enum):
    AWESOME_MICROPYTHON = "awesome_micropython"
    MIM = "mim"
    MICROPYTHON_LIB = "micropython_lib"
    DIRECT = "direct"


class SourceFamily(str, Enum):
    MIP = "mip"
    SINGLE_FILE = "single_file"
    MICROPYTHON_LIB = "micropython_lib"
    UNKNOWN = "unknown"


class FileKind(str, Enum):
    PYTHON = "py"
    MPY = "mpy"
    OTHER = "other"


class RecordDisposition(str, Enum):
    DISCOVERED = "discovered"
    CHECK = "check"
    SKIP = "skip"
    ERROR = "error"
    DEFERRED = "deferred"


class ReasonCode(str, Enum):
    MPY_ONLY = "mpy_only"
    NO_PYTHON_SOURCE = "no_python_source"
    DEPRECATED_PACKAGE = "deprecated_package"
    DEFERRED_INTERNAL_MANIFEST = "deferred_internal_manifest"
    UNSUPPORTED_REFERENCE = "unsupported_reference"
    UNSUPPORTED_SOURCE = "unsupported_source"
    INVALID_CATALOG_ENTRY = "invalid_catalog_entry"
    INVALID_MANIFEST = "invalid_manifest"
    UNAVAILABLE = "unavailable"
    DEPENDENCY_UNAVAILABLE = "dependency_unavailable"
    UNSAFE_PATH = "unsafe_path"
    DEPENDENCY_CYCLE = "dependency_cycle"
    TARGET_COLLISION = "target_collision"
    LIMIT_EXCEEDED = "limit_exceeded"
    CACHE_MISS = "cache_miss"
    CACHE_CORRUPT = "cache_corrupt"
    IDENTITY_CONFLICT = "identity_conflict"
    NO_COMPATIBLE_PORT = "no_compatible_port"
    AMBIGUOUS_PORT = "ambiguous_port"
    NO_PORT_EVIDENCE = "no_port_evidence"


class DependencyDisposition(str, Enum):
    PENDING = "pending"
    RESOLVED = "resolved"
    SKIPPED = "skipped"
    ERROR = "error"


class PortClassification(str, Enum):
    PORTABLE = "portable"
    PORT_SPECIFIC = "port_specific"
    UNKNOWN = "unknown"


class PortEvidenceSource(str, Enum):
    STATIC_SIGNAL = "static_signal"
    DOCUMENTATION = "documentation"
    MANIFEST_PATH = "manifest_path"
    EXPLICIT_METADATA = "explicit_metadata"
    REVIEWED_OVERRIDE = "reviewed_override"


_PORT_EVIDENCE_PRECEDENCE = {
    PortEvidenceSource.STATIC_SIGNAL: 10,
    PortEvidenceSource.DOCUMENTATION: 20,
    PortEvidenceSource.MANIFEST_PATH: 20,
    PortEvidenceSource.EXPLICIT_METADATA: 30,
    PortEvidenceSource.REVIEWED_OVERRIDE: 40,
}


class PackageModelError(ValueError):
    def __init__(self, reason: ReasonCode, message: str) -> None:
        super().__init__(message)
        self.reason = reason


@dataclass(frozen=True)
class PackageIdentity:
    """Stable package identity independent of catalog aliases and revisions."""

    kind: IdentityKind
    value: str

    @property
    def key(self) -> str:
        return f"{self.kind.value}:{self.value}"

    @classmethod
    def repository(
        cls,
        provider: str,
        owner: str,
        repository: str,
        package_path: str = "",
    ) -> PackageIdentity:
        provider = _identity_component(provider, "provider").casefold()
        owner = _identity_component(owner, "owner").casefold()
        repository = _identity_component(repository, "repository")
        if repository.casefold().endswith(".git"):
            repository = repository[:-4]
        repository = repository.casefold()

        value = f"{provider}:{owner}/{repository}"
        if package_path:
            value = f"{value}/{_normalized_package_path(package_path)}"
        return cls(IdentityKind.REPOSITORY, value)

    @classmethod
    def index(cls, name: str) -> PackageIdentity:
        return cls(IdentityKind.INDEX, _identity_component(name, "package name").casefold())

    @classmethod
    def url(cls, url: str) -> PackageIdentity:
        parsed = urlsplit(url.strip())
        scheme = parsed.scheme.casefold()
        if scheme not in {"http", "https"} or not parsed.hostname:
            raise ValueError("url identity requires an absolute HTTP(S) URL")
        if parsed.username is not None or parsed.password is not None:
            raise ValueError("url identity must not contain credentials")

        host = parsed.hostname.casefold()
        if ":" in host:
            host = f"[{host}]"
        port = parsed.port
        if port is not None and (scheme, port) not in {("http", 80), ("https", 443)}:
            host = f"{host}:{port}"
        normalized = urlunsplit((scheme, host, parsed.path or "/", parsed.query, ""))
        return cls(IdentityKind.URL, normalized)

    @classmethod
    def parse(cls, key: str) -> PackageIdentity:
        kind_value, separator, value = key.partition(":")
        if not separator or not value:
            raise ValueError(f"invalid package identity: {key!r}")
        try:
            kind = IdentityKind(kind_value)
        except ValueError as error:
            raise ValueError(f"unknown package identity kind: {kind_value!r}") from error
        if kind is IdentityKind.INDEX:
            identity = cls.index(value)
        elif kind is IdentityKind.URL:
            identity = cls.url(value)
        else:
            provider, provider_separator, location = value.partition(":")
            location_parts = location.split("/")
            if not provider_separator or len(location_parts) < 2:
                raise ValueError(f"invalid repository identity: {key!r}")
            identity = cls.repository(provider, location_parts[0], location_parts[1], "/".join(location_parts[2:]))
        if identity.key != key:
            raise ValueError(f"package identity must be canonical: {identity.key!r}")
        return identity


@dataclass(frozen=True)
class PackageAlias:
    catalog: CatalogSource
    reference: str


@dataclass(frozen=True)
class CatalogProvenance:
    catalog: CatalogSource
    entry_url: str
    entry_key: str
    observed_at: str | None = None
    metadata: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class PackageCandidate:
    identity: PackageIdentity
    display_name: str
    source_family: SourceFamily
    install_reference: str
    aliases: tuple[PackageAlias, ...]
    provenance: tuple[CatalogProvenance, ...]

    def __post_init__(self) -> None:
        if not self.display_name.strip() or not self.install_reference.strip():
            raise ValueError("package candidate names and references must not be empty")
        if not self.aliases or not self.provenance:
            raise ValueError("package candidate requires aliases and provenance")
        if not any(alias.reference == self.install_reference for alias in self.aliases):
            raise ValueError("package candidate aliases must include its install reference")


@dataclass(frozen=True)
class DependencyEdge:
    requested_reference: str
    requested_revision: str | None
    depth: int
    disposition: DependencyDisposition = DependencyDisposition.PENDING
    identity: PackageIdentity | None = None
    resolved_revision: str | None = None
    reason: ReasonCode | None = None

    def __post_init__(self) -> None:
        if self.depth < 1:
            raise ValueError("dependency depth must be at least one")
        if self.disposition in {DependencyDisposition.SKIPPED, DependencyDisposition.ERROR} and self.reason is None:
            raise ValueError("skipped and failed dependencies require a reason")
        if self.disposition in {DependencyDisposition.PENDING, DependencyDisposition.RESOLVED} and self.reason is not None:
            raise ValueError("pending and resolved dependencies cannot have a failure reason")


@dataclass(frozen=True)
class PackageFile:
    owner: PackageIdentity
    target: str
    source: str
    dependency_depth: int = 0
    sha256: str | None = None
    size: int | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "target", _normalized_relative_path(self.target, "file target"))
        if not self.source.strip():
            raise ValueError("file source must not be empty")
        if self.dependency_depth < 0:
            raise ValueError("dependency depth must not be negative")
        if self.size is not None and self.size < 0:
            raise ValueError("file size must not be negative")

    @property
    def kind(self) -> FileKind:
        suffix = PurePosixPath(self.target).suffix.casefold()
        if suffix == ".py":
            return FileKind.PYTHON
        if suffix == ".mpy":
            return FileKind.MPY
        return FileKind.OTHER


@dataclass(frozen=True)
class PackageResolution:
    requested_reference: str
    canonical_reference: str
    requested_revision: str | None
    resolved_revision: str | None
    manifest_reference: str | None
    manifest_sha256: str | None
    dependencies: tuple[DependencyEdge, ...]
    files: tuple[PackageFile, ...]
    package_version: str | None = None


@dataclass(frozen=True)
class PayloadDecision:
    disposition: RecordDisposition
    reason: ReasonCode | None
    python_files: tuple[PackageFile, ...]
    mpy_files: tuple[PackageFile, ...]


@dataclass(frozen=True)
class PortEvidence:
    source: PortEvidenceSource
    classification: PortClassification
    detail: str
    ports: tuple[str, ...] = ()
    boards: tuple[str, ...] = ()
    reference: str | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "ports", _normalized_names(self.ports, "port"))
        object.__setattr__(self, "boards", _normalized_names(self.boards, "board"))
        if not self.detail.strip():
            raise ValueError("classification evidence requires detail")
        _validate_classification_scope(self.classification, self.ports, self.boards)


@dataclass(frozen=True)
class PortDecision:
    classification: PortClassification
    ports: tuple[str, ...]
    boards: tuple[str, ...]
    evidence: tuple[PortEvidence, ...]
    reason: ReasonCode | None = None

    def __post_init__(self) -> None:
        if self.classification is PortClassification.UNKNOWN and self.reason is None:
            raise ValueError("unknown port decisions require a reason")
        if self.classification is not PortClassification.UNKNOWN and self.reason is not None:
            raise ValueError("classified port decisions cannot have an unknown reason")


@dataclass(frozen=True)
class ClassificationOverride:
    identity: PackageIdentity
    classification: PortClassification
    rationale: str
    ports: tuple[str, ...] = ()
    boards: tuple[str, ...] = ()
    reference: str | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "ports", _normalized_names(self.ports, "port"))
        object.__setattr__(self, "boards", _normalized_names(self.boards, "board"))
        if not self.rationale.strip():
            raise ValueError("classification override requires a rationale")
        _validate_classification_scope(self.classification, self.ports, self.boards)

    def as_evidence(self) -> PortEvidence:
        return PortEvidence(
            source=PortEvidenceSource.REVIEWED_OVERRIDE,
            classification=self.classification,
            detail=self.rationale,
            ports=self.ports,
            boards=self.boards,
            reference=self.reference,
        )


@dataclass(frozen=True)
class PackageRecord:
    candidate: PackageCandidate
    resolution: PackageResolution | None = None
    classification: PortDecision | None = None
    disposition: RecordDisposition = RecordDisposition.DISCOVERED
    reason: ReasonCode | None = None

    def __post_init__(self) -> None:
        if self.disposition in {RecordDisposition.SKIP, RecordDisposition.ERROR, RecordDisposition.DEFERRED} and self.reason is None:
            raise ValueError("skipped, failed, and deferred records require a reason")
        if self.disposition is RecordDisposition.CHECK and self.resolution is None:
            raise ValueError("checkable records require a resolution")


def decide_payload(files: Iterable[PackageFile]) -> PayloadDecision:
    """Select checker inputs from an entire resolved dependency closure."""
    ordered = tuple(sorted(files, key=_package_file_sort_key))
    python_files = tuple(file for file in ordered if file.kind is FileKind.PYTHON)
    mpy_files = tuple(file for file in ordered if file.kind is FileKind.MPY)
    if python_files:
        return PayloadDecision(RecordDisposition.CHECK, None, python_files, mpy_files)
    if mpy_files:
        return PayloadDecision(RecordDisposition.SKIP, ReasonCode.MPY_ONLY, (), mpy_files)
    return PayloadDecision(RecordDisposition.SKIP, ReasonCode.NO_PYTHON_SOURCE, (), ())


def classify_ports(
    evidence: Iterable[PortEvidence],
    override: ClassificationOverride | None = None,
) -> PortDecision:
    """Classify a package using only the highest-precedence available evidence."""
    collected = list(evidence)
    if override is not None:
        collected.append(override.as_evidence())
    ordered = tuple(sorted(collected, key=_port_evidence_sort_key))
    if not ordered:
        return PortDecision(PortClassification.UNKNOWN, (), (), (), ReasonCode.NO_PORT_EVIDENCE)

    highest_precedence = max(_PORT_EVIDENCE_PRECEDENCE[item.source] for item in ordered)
    decisive = tuple(item for item in ordered if _PORT_EVIDENCE_PRECEDENCE[item.source] == highest_precedence)
    classifications = {item.classification for item in decisive}
    if len(classifications) != 1:
        return PortDecision(PortClassification.UNKNOWN, (), (), ordered, ReasonCode.AMBIGUOUS_PORT)

    classification = next(iter(classifications))
    ports = tuple(sorted({port for item in decisive for port in item.ports}))
    boards = tuple(sorted({board for item in decisive for board in item.boards}))
    return PortDecision(classification, ports, boards, ordered)


def load_classification_overrides(path: Path) -> dict[PackageIdentity, ClassificationOverride]:
    """Load reviewed package classifications from the versioned JSON format."""
    document = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict) or document.get("schema_version") != 1:
        raise ValueError("classification overrides require schema_version 1")
    packages = document.get("packages")
    if not isinstance(packages, dict):
        raise ValueError("classification overrides require a packages object")

    overrides: dict[PackageIdentity, ClassificationOverride] = {}
    for identity_key, raw_override in packages.items():
        if not isinstance(identity_key, str) or not isinstance(raw_override, dict):
            raise ValueError("classification override entries must be objects keyed by package identity")
        identity = PackageIdentity.parse(identity_key)
        override = _classification_override_from_mapping(identity, raw_override)
        overrides[identity] = override
    return overrides


def deduplicate_candidates(candidates: Iterable[PackageCandidate]) -> tuple[PackageCandidate, ...]:
    """Merge catalog candidates by identity with order-independent output."""
    grouped: dict[PackageIdentity, list[PackageCandidate]] = {}
    for candidate in candidates:
        grouped.setdefault(candidate.identity, []).append(candidate)

    merged = [_merge_candidate_group(identity, records) for identity, records in grouped.items()]
    return tuple(sorted(merged, key=lambda candidate: candidate.identity.key))


def _merge_candidate_group(identity: PackageIdentity, records: list[PackageCandidate]) -> PackageCandidate:
    source_families = {record.source_family for record in records if record.source_family is not SourceFamily.UNKNOWN}
    if len(source_families) > 1:
        values = ", ".join(sorted(family.value for family in source_families))
        raise PackageModelError(ReasonCode.IDENTITY_CONFLICT, f"conflicting source families for {identity.key}: {values}")
    source_family = next(iter(source_families), SourceFamily.UNKNOWN)

    aliases = {alias for record in records for alias in record.aliases}
    provenance = {item for record in records for item in record.provenance}
    references = {record.install_reference for record in records}

    return PackageCandidate(
        identity=identity,
        display_name=min((record.display_name for record in records), key=lambda value: (value.casefold(), value)),
        source_family=source_family,
        install_reference=min(references, key=_reference_sort_key),
        aliases=tuple(sorted(aliases, key=lambda alias: (alias.catalog.value, alias.reference.casefold(), alias.reference))),
        provenance=tuple(
            sorted(
                provenance,
                key=lambda item: (item.catalog.value, item.entry_url, item.entry_key, item.observed_at or "", item.metadata),
            )
        ),
    )


def _reference_sort_key(reference: str) -> tuple[int, str, str]:
    lowered = reference.casefold()
    is_provider_reference = lowered.startswith(("github:", "gitlab:", "codeberg:"))
    is_bare_index_name = "://" not in lowered and ":" not in lowered
    rank = 0 if is_provider_reference or is_bare_index_name else 1
    return rank, lowered, reference


def _package_file_sort_key(file: PackageFile) -> tuple[int, str, str, str]:
    return file.dependency_depth, file.owner.key, file.target, file.source


def _port_evidence_sort_key(evidence: PortEvidence) -> tuple[int, str, str, tuple[str, ...], tuple[str, ...], str]:
    return (
        -_PORT_EVIDENCE_PRECEDENCE[evidence.source],
        evidence.source.value,
        evidence.classification.value,
        evidence.ports,
        evidence.boards,
        evidence.reference or "",
    )


def _classification_override_from_mapping(
    identity: PackageIdentity,
    raw_override: Mapping[str, object],
) -> ClassificationOverride:
    allowed_keys = {"classification", "rationale", "ports", "boards", "reference"}
    unknown_keys = set(raw_override) - allowed_keys
    if unknown_keys:
        keys = ", ".join(sorted(unknown_keys))
        raise ValueError(f"override for {identity.key} has unknown fields: {keys}")
    try:
        classification = PortClassification(str(raw_override["classification"]))
        rationale = str(raw_override["rationale"])
    except KeyError as error:
        raise ValueError(f"override for {identity.key} is missing {error.args[0]}") from error

    ports = _string_sequence(raw_override.get("ports", ()), "ports")
    boards = _string_sequence(raw_override.get("boards", ()), "boards")
    reference_value = raw_override.get("reference")
    if reference_value is not None and not isinstance(reference_value, str):
        raise ValueError(f"override reference for {identity.key} must be a string")
    return ClassificationOverride(identity, classification, rationale, ports, boards, reference_value)


def _string_sequence(value: object, label: str) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{label} must be an array of strings")
    return tuple(value)


def _normalized_names(values: Iterable[str], label: str) -> tuple[str, ...]:
    normalized = {value.strip().casefold() for value in values}
    if "" in normalized:
        raise ValueError(f"{label} names must not be empty")
    return tuple(sorted(normalized))


def _validate_classification_scope(
    classification: PortClassification,
    ports: tuple[str, ...],
    boards: tuple[str, ...],
) -> None:
    if classification is PortClassification.UNKNOWN:
        raise ValueError("unknown is a decision result, not classification evidence")
    if classification is PortClassification.PORTABLE and (ports or boards):
        raise ValueError("portable classification cannot name ports or boards")
    if classification is PortClassification.PORT_SPECIFIC and not (ports or boards):
        raise ValueError("port-specific classification requires a port or board")


def _identity_component(value: str, label: str) -> str:
    value = value.strip()
    if not value or "/" in value or "\\" in value:
        raise ValueError(f"{label} must be one non-empty path component")
    return value


def _normalized_package_path(value: str) -> str:
    return _normalized_relative_path(value, "package_path")


def _normalized_relative_path(value: str, label: str) -> str:
    if "\\" in value:
        raise ValueError(f"{label} must use POSIX separators")
    parts = value.split("/")
    if not value or any(part in {"", ".", ".."} for part in parts) or (len(parts[0]) >= 2 and parts[0][1] == ":"):
        raise ValueError(f"{label} must be a normalized relative path")
    path = PurePosixPath(value)
    if path.is_absolute():
        raise ValueError(f"{label} must be a normalized relative path")
    return path.as_posix()
