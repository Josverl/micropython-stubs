"""Offline parsers and normalized inventory for ecosystem package catalogs."""

from __future__ import annotations

import json
import re
import shlex
from dataclasses import dataclass
from enum import Enum
from html.parser import HTMLParser
from pathlib import PurePosixPath
from typing import Iterable, Mapping
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

from markdown_it import MarkdownIt
from markdown_it.token import Token

from .model import (
    CatalogProvenance,
    CatalogSource,
    ClassificationOverride,
    PackageAlias,
    PackageCandidate,
    PackageIdentity,
    PackageModelError,
    PackageRecord,
    PortClassification,
    PortEvidence,
    PortEvidenceSource,
    ReasonCode,
    RecordDisposition,
    SourceFamily,
    classify_ports,
    deduplicate_candidates,
)


class CatalogAction(str, Enum):
    RESOLVE_MIP = "resolve_mip"
    RESOLVE_SINGLE_FILE = "resolve_single_file"


@dataclass(frozen=True)
class CatalogEntry:
    catalog: CatalogSource
    name: str
    reference: str
    description: str
    category: str
    source_url: str
    observed_at: str | None = None
    repository_url: str | None = None
    metadata: tuple[tuple[str, str], ...] = ()

    @property
    def key(self) -> str:
        return f"{self.category}:{self.name}" if self.category else self.name


@dataclass(frozen=True)
class CatalogDiagnostic:
    catalog: CatalogSource
    entry_key: str
    source_url: str
    disposition: RecordDisposition
    reason: ReasonCode
    detail: str
    reference: str | None = None


@dataclass(frozen=True)
class CatalogParseResult:
    entries: tuple[CatalogEntry, ...]
    diagnostics: tuple[CatalogDiagnostic, ...]


@dataclass(frozen=True)
class MimPackageLocation:
    key: str
    page_url: str
    last_modified: str | None


@dataclass(frozen=True)
class MimDiscoveryResult:
    locations: tuple[MimPackageLocation, ...]
    diagnostics: tuple[CatalogDiagnostic, ...]


@dataclass(frozen=True)
class CatalogInventory:
    records: tuple[PackageRecord, ...]
    diagnostics: tuple[CatalogDiagnostic, ...]

    def filtered(
        self,
        *,
        catalog: CatalogSource | None = None,
        identity: PackageIdentity | None = None,
        classification: PortClassification | None = None,
    ) -> CatalogInventory:
        records = self.records
        if catalog is not None:
            records = tuple(record for record in records if any(item.catalog is catalog for item in record.candidate.provenance))
        if identity is not None:
            records = tuple(record for record in records if record.candidate.identity == identity)
        if classification is not None:
            records = tuple(
                record for record in records if record.classification is not None and record.classification.classification is classification
            )
        diagnostics = self.diagnostics if identity is None and classification is None else ()
        if catalog is not None:
            diagnostics = tuple(item for item in diagnostics if item.catalog is catalog)
        return CatalogInventory(records, diagnostics)

    def to_dict(self) -> dict[str, object]:
        return {
            "schema_version": 1,
            "packages": [_record_to_dict(record) for record in self.records],
            "diagnostics": [_diagnostic_to_dict(item) for item in self.diagnostics],
        }

    def to_json(self, *, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, sort_keys=True) + "\n"


@dataclass(frozen=True)
class _NormalizedCatalogEntry:
    candidate: PackageCandidate
    evidence: tuple[PortEvidence, ...]
    disposition: RecordDisposition
    reason: ReasonCode | None


class AwesomeCatalogAdapter:
    def __init__(self, source_url: str) -> None:
        self.source_url = source_url
        self._markdown = MarkdownIt("commonmark")

    def parse(self, document: str, observed_at: str | None = None) -> CatalogParseResult:
        tokens = self._markdown.parse(document)
        entries: list[CatalogEntry] = []
        diagnostics: list[CatalogDiagnostic] = []
        in_libraries = False
        category = ""
        index = 0

        while index < len(tokens):
            token = tokens[index]
            if token.type == "heading_open" and index + 1 < len(tokens):
                heading = tokens[index + 1].content.strip()
                if token.tag == "h2":
                    if in_libraries and heading.casefold() != "libraries":
                        break
                    in_libraries = heading.casefold() == "libraries"
                    category = ""
                elif in_libraries and token.tag in {"h3", "h4"}:
                    category = heading
                index += 1
            elif in_libraries and token.type == "list_item_open":
                inline, closing_index = _first_item_inline(tokens, index)
                link = _first_link(inline) if inline is not None else None
                if link is None:
                    detail = inline.content.strip() if inline is not None else "list item has no inline content"
                    diagnostics.append(
                        CatalogDiagnostic(
                            catalog=CatalogSource.AWESOME_MICROPYTHON,
                            entry_key=f"{category}:item-{len(entries) + len(diagnostics) + 1}",
                            source_url=self.source_url,
                            disposition=RecordDisposition.ERROR,
                            reason=ReasonCode.INVALID_CATALOG_ENTRY,
                            detail=f"Library list item has no package link: {detail}",
                        )
                    )
                elif not _is_awesome_non_package_reference(link[1]):
                    name, reference = link
                    entries.append(
                        CatalogEntry(
                            catalog=CatalogSource.AWESOME_MICROPYTHON,
                            name=name,
                            reference=reference,
                            description=inline.content if inline is not None else "",
                            category=category,
                            source_url=self.source_url,
                            observed_at=observed_at,
                            repository_url=reference,
                        )
                    )
                index = closing_index
            index += 1

        return CatalogParseResult(tuple(entries), tuple(diagnostics))


class MimCatalogAdapter:
    def __init__(self, sitemap_url: str = "https://checkmim.com/sitemap.xml") -> None:
        self.sitemap_url = sitemap_url

    def parse_sitemap(self, document: str) -> MimDiscoveryResult:
        try:
            root = ET.fromstring(document)
        except ET.ParseError as error:
            return MimDiscoveryResult(
                (),
                (
                    CatalogDiagnostic(
                        catalog=CatalogSource.MIM,
                        entry_key="sitemap",
                        source_url=self.sitemap_url,
                        disposition=RecordDisposition.ERROR,
                        reason=ReasonCode.INVALID_CATALOG_ENTRY,
                        detail=f"Invalid MIM sitemap XML: {error}",
                    ),
                ),
            )

        locations: list[MimPackageLocation] = []
        diagnostics: list[CatalogDiagnostic] = []
        for url_element in (element for element in root.iter() if _local_name(element.tag) == "url"):
            page_url = _child_text(url_element, "loc")
            last_modified = _child_text(url_element, "lastmod") or None
            key = _mim_package_key(page_url)
            if key is None:
                if _is_mim_non_package_url(page_url):
                    continue
                diagnostics.append(
                    CatalogDiagnostic(
                        catalog=CatalogSource.MIM,
                        entry_key="sitemap-entry",
                        source_url=self.sitemap_url,
                        disposition=RecordDisposition.ERROR,
                        reason=ReasonCode.INVALID_CATALOG_ENTRY,
                        detail=f"Unsupported MIM package URL in sitemap: {page_url or '<missing>'}",
                        reference=page_url or None,
                    )
                )
                continue
            locations.append(MimPackageLocation(key, page_url, last_modified))

        return MimDiscoveryResult(tuple(sorted(locations, key=lambda item: item.key.casefold())), tuple(diagnostics))

    def parse_package_page(self, location: MimPackageLocation, document: str) -> CatalogParseResult:
        parser = _MimPageParser()
        parser.feed(document)
        package_data = _software_source_code(parser.json_ld_documents)
        install_reference = _mip_install_reference(parser.code_blocks)
        if package_data is not None and install_reference is None and _is_deprecated_package(package_data):
            name = package_data.get("name")
            if isinstance(name, str) and name.strip():
                repository_url = package_data.get("codeRepository")
                return CatalogParseResult(
                    (),
                    (
                        CatalogDiagnostic(
                            catalog=CatalogSource.MIM,
                            entry_key=location.key,
                            source_url=location.page_url,
                            disposition=RecordDisposition.SKIP,
                            reason=ReasonCode.DEPRECATED_PACKAGE,
                            detail=f"MIM package {name.strip()} is deprecated and has no install reference",
                            reference=repository_url if isinstance(repository_url, str) else None,
                        ),
                    ),
                )
        if package_data is None or install_reference is None:
            missing = []
            if package_data is None:
                missing.append("SoftwareSourceCode JSON-LD")
            if install_reference is None:
                missing.append("mpremote mip install command")
            return CatalogParseResult(
                (),
                (
                    CatalogDiagnostic(
                        catalog=CatalogSource.MIM,
                        entry_key=location.key,
                        source_url=location.page_url,
                        disposition=RecordDisposition.ERROR,
                        reason=ReasonCode.INVALID_CATALOG_ENTRY,
                        detail=f"MIM package page is missing {' and '.join(missing)}",
                    ),
                ),
            )

        name = package_data.get("name")
        repository_url = package_data.get("codeRepository")
        if not isinstance(name, str) or not name.strip() or not isinstance(repository_url, str):
            return CatalogParseResult(
                (),
                (
                    CatalogDiagnostic(
                        catalog=CatalogSource.MIM,
                        entry_key=location.key,
                        source_url=location.page_url,
                        disposition=RecordDisposition.ERROR,
                        reason=ReasonCode.INVALID_CATALOG_ENTRY,
                        detail="MIM SoftwareSourceCode data requires name and codeRepository strings",
                    ),
                ),
            )

        metadata_keys = ("license", "version", "keywords", "dateCreated", "dateModified")
        metadata = tuple((key, str(package_data[key])) for key in metadata_keys if package_data.get(key) is not None)
        if parser.package_status:
            metadata += (("status", parser.package_status),)
        description = package_data.get("description")
        entry = CatalogEntry(
            catalog=CatalogSource.MIM,
            name=name.strip(),
            reference=install_reference,
            description=description if isinstance(description, str) else "",
            category=str(package_data.get("keywords", "")),
            source_url=location.page_url,
            observed_at=location.last_modified,
            repository_url=repository_url,
            metadata=metadata,
        )
        return CatalogParseResult((entry,), ())


def build_inventory(
    entries: Iterable[CatalogEntry],
    diagnostics: Iterable[CatalogDiagnostic] = (),
    overrides: Mapping[PackageIdentity, ClassificationOverride] | None = None,
) -> CatalogInventory:
    """Normalize and deduplicate parsed catalog entries without network access."""
    normalized: list[_NormalizedCatalogEntry] = []
    collected_diagnostics = list(diagnostics)
    for entry in entries:
        try:
            normalized.append(_normalize_catalog_entry(entry))
        except PackageModelError as error:
            collected_diagnostics.append(_entry_diagnostic(entry, error.reason, str(error)))
        except ValueError as error:
            collected_diagnostics.append(_entry_diagnostic(entry, ReasonCode.UNSUPPORTED_REFERENCE, str(error)))

    grouped: dict[PackageIdentity, list[_NormalizedCatalogEntry]] = {}
    for item in normalized:
        grouped.setdefault(item.candidate.identity, []).append(item)

    records: list[PackageRecord] = []
    for identity, items in grouped.items():
        try:
            candidate = deduplicate_candidates(item.candidate for item in items)[0]
        except PackageModelError as error:
            first = items[0].candidate
            collected_diagnostics.append(
                CatalogDiagnostic(
                    catalog=first.provenance[0].catalog,
                    entry_key=first.provenance[0].entry_key,
                    source_url=first.provenance[0].entry_url,
                    disposition=RecordDisposition.ERROR,
                    reason=error.reason,
                    detail=str(error),
                    reference=first.install_reference,
                )
            )
            continue

        evidence = tuple({item for normalized_item in items for item in normalized_item.evidence})
        classification = classify_ports(evidence, (overrides or {}).get(identity))
        active = [item for item in items if item.disposition is RecordDisposition.DISCOVERED]
        disposition = RecordDisposition.DISCOVERED if active else RecordDisposition.DEFERRED
        reason = None if active else ReasonCode.DEFERRED_INTERNAL_MANIFEST
        records.append(
            PackageRecord(
                candidate=candidate,
                classification=classification,
                disposition=disposition,
                reason=reason,
            )
        )

    return CatalogInventory(
        tuple(sorted(records, key=lambda record: record.candidate.identity.key)),
        tuple(sorted(collected_diagnostics, key=_diagnostic_sort_key)),
    )


class _MimPageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.json_ld_documents: list[object] = []
        self.code_blocks: list[str] = []
        self.package_status: str | None = None
        self._capture: str | None = None
        self._buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        content_type = attributes.get("type")
        if tag == "script" and isinstance(content_type, str) and content_type.casefold() == "application/ld+json":
            self._capture = "json"
            self._buffer = []
        elif tag == "code":
            self._capture = "code"
            self._buffer = []
        if status := attributes.get("data-package-status"):
            self.package_status = status

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._capture == "json":
            try:
                self.json_ld_documents.append(json.loads("".join(self._buffer)))
            except json.JSONDecodeError:
                pass
            self._capture = None
            self._buffer = []
        elif tag == "code" and self._capture == "code":
            self.code_blocks.append("".join(self._buffer).strip())
            self._capture = None
            self._buffer = []

    def handle_data(self, data: str) -> None:
        if self._capture is not None:
            self._buffer.append(data)


def _first_item_inline(tokens: list[Token], opening_index: int) -> tuple[Token | None, int]:
    depth = 1
    first_inline: Token | None = None
    index = opening_index + 1
    while index < len(tokens):
        token = tokens[index]
        if token.type == "list_item_open":
            depth += 1
        elif token.type == "list_item_close":
            depth -= 1
            if depth == 0:
                return first_inline, index
        elif depth == 1 and token.type == "inline" and first_inline is None:
            first_inline = token
        index += 1
    return first_inline, len(tokens) - 1


def _first_link(inline: Token) -> tuple[str, str] | None:
    children = inline.children or []
    for index, token in enumerate(children):
        if token.type != "link_open":
            continue
        reference = token.attrGet("href")
        label_parts: list[str] = []
        for child in children[index + 1 :]:
            if child.type == "link_close":
                break
            if child.type in {"text", "code_inline"}:
                label_parts.append(child.content)
        name = "".join(label_parts).strip()
        if isinstance(reference, str) and reference and name:
            return name, reference
    return None


def _software_source_code(documents: list[object]) -> dict[str, object] | None:
    for document in documents:
        if isinstance(document, dict) and document.get("@type") == "SoftwareSourceCode":
            return document
    return None


def _is_deprecated_package(package_data: dict[str, object]) -> bool:
    keywords = package_data.get("keywords")
    if isinstance(keywords, str):
        values = keywords.split(",")
    elif isinstance(keywords, list):
        values = [value for value in keywords if isinstance(value, str)]
    else:
        return False
    return any(value.strip().casefold() == "deprecated" for value in values)


def _mip_install_reference(code_blocks: list[str]) -> str | None:
    for block in code_blocks:
        try:
            arguments = shlex.split(block)
        except ValueError:
            continue
        if len(arguments) == 4 and arguments[:3] == ["mpremote", "mip", "install"]:
            return arguments[3]
    return None


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _child_text(element: ET.Element, name: str) -> str:
    for child in element:
        if _local_name(child.tag) == name:
            return (child.text or "").strip()
    return ""


def _mim_package_key(page_url: str) -> str | None:
    parsed = urlsplit(page_url)
    if parsed.scheme != "https" or parsed.hostname != "checkmim.com":
        return None
    parts = parsed.path.strip("/").split("/")
    if len(parts) != 2 or parts[0] != "packages" or not parts[1]:
        return None
    return unquote(parts[1])


def _is_awesome_non_package_reference(reference: str) -> bool:
    parsed = urlsplit(reference)
    host = (parsed.hostname or "").casefold()
    path = parsed.path.rstrip("/").casefold()
    return (
        (host == "github.com" and (path == "/search" or path.startswith("/topics/")))
        or (host == "gitlab.com" and (path == "/explore" or path.startswith("/explore/")))
        or (host == "codeberg.org" and (path == "/explore" or path.startswith("/explore/")))
        or (host == "pypi.org" and path == "/search")
        or (host == "libraries.io" and path == "/search")
        or host == "docs.micropython.org"
        or (host == "micropython.org" and path == "/webrepl")
    )


def _is_mim_non_package_url(page_url: str) -> bool:
    parsed = urlsplit(page_url)
    return parsed.scheme == "https" and parsed.hostname == "checkmim.com" and parsed.path.rstrip("/") in {"", "/about", "/privacy"}


def _normalize_catalog_entry(entry: CatalogEntry) -> _NormalizedCatalogEntry:
    official = _is_micropython_lib_reference(entry.repository_url or entry.reference)
    normalization_reference = entry.repository_url if official and entry.repository_url else entry.reference
    identity, install_reference, source_family = normalize_package_reference(normalization_reference, official=official)
    if entry.catalog is CatalogSource.MIM and _is_bare_package_name(entry.reference) and not official:
        identity = PackageIdentity.index(entry.reference)

    disposition = RecordDisposition.DISCOVERED
    reason = None
    aliases = tuple(
        PackageAlias(entry.catalog, reference)
        for reference in sorted(
            {entry.reference, normalization_reference, install_reference},
            key=lambda value: (value.casefold(), value),
        )
    )
    provenance = CatalogProvenance(
        catalog=entry.catalog,
        entry_url=entry.source_url,
        entry_key=entry.key,
        observed_at=entry.observed_at,
        metadata=entry.metadata,
    )
    candidate = PackageCandidate(
        identity=identity,
        display_name=entry.name,
        source_family=SourceFamily.MICROPYTHON_LIB if official else source_family,
        install_reference=install_reference,
        aliases=aliases,
        provenance=(provenance,),
    )
    return _NormalizedCatalogEntry(candidate, _classification_evidence(entry), disposition, reason)


def normalize_package_reference(
    reference: str,
    *,
    official: bool = False,
) -> tuple[PackageIdentity, str, SourceFamily]:
    """Normalize a supported package reference for catalog or focused use."""
    reference = reference.strip()
    if not reference:
        raise ValueError("package reference is empty")
    official = official or _is_micropython_lib_reference(reference)
    if _is_bare_package_name(reference):
        return PackageIdentity.index(reference), reference, SourceFamily.MIP

    for provider in ("github", "gitlab", "codeberg"):
        if reference.casefold().startswith(f"{provider}:"):
            return _normalize_provider_reference(reference, provider, official)

    parsed = urlsplit(reference)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError(f"unsupported package reference: {reference}")
    provider_by_host = {
        "github.com": "github",
        "gitlab.com": "gitlab",
        "codeberg.org": "codeberg",
    }
    provider = provider_by_host.get(parsed.hostname.casefold())
    if provider is not None:
        return _normalize_repository_url(reference, provider, official)

    suffix = PurePosixPath(parsed.path).suffix.casefold()
    if suffix in {".py", ".mpy"}:
        return PackageIdentity.url(reference), reference, SourceFamily.SINGLE_FILE
    if suffix == ".json":
        return PackageIdentity.url(reference), reference, SourceFamily.MIP
    raise PackageModelError(ReasonCode.UNSUPPORTED_SOURCE, f"URL is not a supported package or Python file: {reference}")


def _normalize_provider_reference(
    reference: str,
    provider: str,
    official: bool,
) -> tuple[PackageIdentity, str, SourceFamily]:
    body = reference.split(":", 1)[1]
    package, separator, revision = body.rpartition("@")
    if not separator:
        package, revision = body, ""
    parts = package.strip("/").split("/")
    if len(parts) < 2 or not all(parts[:2]):
        raise ValueError(f"invalid {provider} package reference: {reference}")
    owner, repository = parts[:2]
    inner_path = "/".join(parts[2:])
    package_path, family = _package_path_and_family(inner_path)
    identity = PackageIdentity.repository(provider, owner, repository, package_path)
    install_reference = identity.value
    if revision:
        install_reference += f"@{revision}"
    return identity, install_reference, SourceFamily.MICROPYTHON_LIB if official else family


def _normalize_repository_url(
    reference: str,
    provider: str,
    official: bool,
) -> tuple[PackageIdentity, str, SourceFamily]:
    parsed = urlsplit(reference)
    parts = [unquote(part) for part in parsed.path.strip("/").split("/") if part]
    if len(parts) < 2:
        raise ValueError(f"repository URL has no owner and repository: {reference}")
    owner, repository = parts[:2]
    repository = repository[:-4] if repository.casefold().endswith(".git") else repository
    inner_path = ""
    revision = ""
    if len(parts) > 2:
        if provider == "github" and len(parts) >= 5 and parts[2] in {"blob", "tree"}:
            revision = parts[3]
            inner_path = "/".join(parts[4:])
        else:
            raise ValueError(f"unsupported deep {provider} repository URL: {reference}")

    package_path, family = _package_path_and_family(inner_path)
    identity = PackageIdentity.repository(provider, owner, repository, package_path)
    install_reference = identity.value
    if revision:
        install_reference += f"@{revision}"
    return identity, install_reference, SourceFamily.MICROPYTHON_LIB if official else family


def _package_path_and_family(inner_path: str) -> tuple[str, SourceFamily]:
    suffix = PurePosixPath(inner_path).suffix.casefold() if inner_path else ""
    if suffix in {".py", ".mpy"}:
        return inner_path, SourceFamily.SINGLE_FILE
    if PurePosixPath(inner_path).name.casefold() == "package.json":
        parent = PurePosixPath(inner_path).parent.as_posix()
        return "" if parent == "." else parent, SourceFamily.MIP
    return inner_path, SourceFamily.MIP


def _is_bare_package_name(reference: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9_.-]+", reference))


def _is_micropython_lib_reference(reference: str) -> bool:
    lowered = reference.casefold()
    return "github.com/micropython/micropython-lib" in lowered or lowered.startswith("github:micropython/micropython-lib")


_PORT_ALIASES = {
    "esp32": "esp32",
    "esp8266": "esp8266",
    "rp2": "rp2",
    "rp2040": "rp2",
    "stm32": "stm32",
    "pyboard": "stm32",
    "samd": "samd",
    "unix": "unix",
    "webassembly": "webassembly",
}


def _classification_evidence(entry: CatalogEntry) -> tuple[PortEvidence, ...]:
    metadata = dict(entry.metadata)
    if entry.catalog is CatalogSource.MICROPYTHON_LIB:
        library = metadata.get("library")
        if library == "unix-ffi":
            return (
                PortEvidence(
                    source=PortEvidenceSource.MANIFEST_PATH,
                    classification=PortClassification.PORT_SPECIFIC,
                    detail="micropython-lib unix-ffi package path",
                    ports=("unix",),
                    reference=entry.source_url,
                ),
            )
        if library in {"python-stdlib", "python-ecosys"}:
            return (
                PortEvidence(
                    source=PortEvidenceSource.MANIFEST_PATH,
                    classification=PortClassification.PORTABLE,
                    detail=f"micropython-lib {library} package path",
                    reference=entry.source_url,
                ),
            )
    keywords = metadata.get("keywords", "")
    keyword_ports = _ports_in_text(keywords)
    has_keyword_scope = bool(re.search(r"\b(?:only|specific(?:ally)?|for|supports?)\b", keywords.casefold()))
    if keyword_ports and has_keyword_scope:
        return (
            PortEvidence(
                source=PortEvidenceSource.EXPLICIT_METADATA,
                classification=PortClassification.PORT_SPECIFIC,
                detail=f"Catalog keywords: {keywords}",
                ports=keyword_ports,
                reference=entry.source_url,
            ),
        )

    description_ports = _ports_in_text(entry.description)
    lowered = entry.description.casefold()
    has_scope_language = bool(re.search(r"\b(?:only|specific(?:ally)?|for|supports?)\b", lowered))
    if description_ports and has_scope_language:
        return (
            PortEvidence(
                source=PortEvidenceSource.DOCUMENTATION,
                classification=PortClassification.PORT_SPECIFIC,
                detail=f"Catalog description: {entry.description}",
                ports=description_ports,
                reference=entry.source_url,
            ),
        )
    return ()


def _ports_in_text(value: str) -> tuple[str, ...]:
    words = set(re.findall(r"[a-z0-9]+", value.casefold()))
    return tuple(sorted({_PORT_ALIASES[word] for word in words if word in _PORT_ALIASES}))


def _entry_diagnostic(entry: CatalogEntry, reason: ReasonCode, detail: str) -> CatalogDiagnostic:
    return CatalogDiagnostic(
        catalog=entry.catalog,
        entry_key=entry.key,
        source_url=entry.source_url,
        disposition=RecordDisposition.ERROR,
        reason=reason,
        detail=detail,
        reference=entry.reference,
    )


def _diagnostic_sort_key(item: CatalogDiagnostic) -> tuple[str, str, str, str]:
    return item.catalog.value, item.entry_key, item.reason.value, item.reference or ""


def _record_to_dict(record: PackageRecord) -> dict[str, object]:
    classification = record.classification
    return {
        "identity": record.candidate.identity.key,
        "display_name": record.candidate.display_name,
        "source_family": record.candidate.source_family.value,
        "install_reference": record.candidate.install_reference,
        "action": _catalog_action(record.candidate.source_family),
        "disposition": record.disposition.value,
        "reason": record.reason.value if record.reason else None,
        "aliases": [{"catalog": alias.catalog.value, "reference": alias.reference} for alias in record.candidate.aliases],
        "provenance": [
            {
                "catalog": item.catalog.value,
                "entry_url": item.entry_url,
                "entry_key": item.entry_key,
                "observed_at": item.observed_at,
                "metadata": dict(item.metadata),
            }
            for item in record.candidate.provenance
        ],
        "classification": {
            "value": classification.classification.value if classification else PortClassification.UNKNOWN.value,
            "ports": list(classification.ports) if classification else [],
            "boards": list(classification.boards) if classification else [],
            "reason": classification.reason.value if classification and classification.reason else None,
        },
    }


def _catalog_action(source_family: SourceFamily) -> str | None:
    if source_family is SourceFamily.MIP:
        return CatalogAction.RESOLVE_MIP.value
    if source_family is SourceFamily.SINGLE_FILE:
        return CatalogAction.RESOLVE_SINGLE_FILE.value
    return None


def _diagnostic_to_dict(item: CatalogDiagnostic) -> dict[str, object]:
    return {
        "catalog": item.catalog.value,
        "entry_key": item.entry_key,
        "source_url": item.source_url,
        "reference": item.reference,
        "disposition": item.disposition.value,
        "reason": item.reason.value,
        "detail": item.detail,
    }
