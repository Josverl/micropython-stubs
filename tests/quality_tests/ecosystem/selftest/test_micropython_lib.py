from dataclasses import dataclass
from io import BytesIO
import json
import os
from pathlib import Path
import stat
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

import pytest

from ..catalog import CatalogEntry, build_inventory
from ..catalog_loader import CatalogLoadOptions, NetworkCatalogLoader
from ..micropython_lib import (
    MicropythonLibCatalogAdapter,
    MicropythonLibLimits,
    MicropythonLibManifestError,
    MicropythonLibSnapshot,
    fetch_micropython_lib_snapshot,
)
from ..model import CatalogSource, PortClassification, ReasonCode, RecordDisposition, SourceFamily
from ..orchestrator import CatalogSelection
from ..resolver import CacheMode, CachedFetcher, FetchResponse, MipResolver, UrlFetcher


FIXTURES = Path(__file__).parent.parent / "fixtures" / "micropython-lib"


@dataclass
class MemoryFetcher:
    responses: dict[str, FetchResponse]
    calls: int = 0

    def fetch(self, reference: str, mode: CacheMode | None = None) -> FetchResponse:
        _ = mode
        self.calls += 1
        return self.responses[reference]


def _fixture_archive(revision: str) -> bytes:
    output = BytesIO()
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for source in sorted(FIXTURES.rglob("*")):
            if source.is_file():
                relative = source.relative_to(FIXTURES).as_posix()
                archive.writestr(f"micropython-lib-{revision}/{relative}", source.read_bytes())
    return output.getvalue()


def _archive(entries: dict[str, bytes]) -> bytes:
    output = BytesIO()
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for path, data in entries.items():
            archive.writestr(path, data)
    return output.getvalue()


def test_snapshot_resolves_literal_manifest_and_dependency_closure() -> None:
    snapshot = MicropythonLibSnapshot.from_directory(
        FIXTURES,
        requested_revision="v1.29.0",
        resolved_revision="a" * 40,
    )

    resolution = snapshot.resolve("micropython/net/fixture-demo")

    assert resolution.package.name == "fixture-demo"
    assert resolution.package.version == "1.2.3"
    assert resolution.package.description == "Fixture package."
    assert [(item.name, item.package_path, item.depth) for item in resolution.dependencies] == [
        ("fixture-dependency", "python-stdlib/fixture-dependency", 1)
    ]
    assert [(item.target, item.depth) for item in resolution.files] == [
        ("fixture_demo.py", 0),
        ("fixture_helpers/__init__.py", 0),
        ("fixture_helpers/codec.py", 0),
        ("fixture_dependency.py", 1),
    ]
    assert resolution.classification.classification is PortClassification.UNKNOWN
    assert resolution.classification.reason is ReasonCode.NO_PORT_EVIDENCE


def test_snapshot_derives_unix_port_evidence_from_library_path() -> None:
    snapshot = MicropythonLibSnapshot.from_directory(
        FIXTURES,
        requested_revision="v1.29.0",
        resolved_revision="a" * 40,
    )

    resolution = snapshot.resolve("unix-ffi/fixture-unix")

    assert resolution.classification.classification is PortClassification.PORT_SPECIFIC
    assert resolution.classification.ports == ("unix",)


def test_catalog_adapter_emits_manifest_neutral_records() -> None:
    snapshot = MicropythonLibSnapshot.from_directory(
        FIXTURES,
        requested_revision="v1.29.0",
        resolved_revision="a" * 40,
    )

    parsed = MicropythonLibCatalogAdapter().parse(snapshot)
    inventory = build_inventory(parsed.entries, parsed.diagnostics)

    assert not inventory.diagnostics
    assert len(inventory.records) == 3
    fixture_demo = next(record for record in inventory.records if record.candidate.display_name == "fixture-demo")
    assert fixture_demo.candidate.source_family is SourceFamily.MICROPYTHON_LIB
    assert fixture_demo.candidate.provenance[0].catalog is CatalogSource.MICROPYTHON_LIB
    assert fixture_demo.disposition is RecordDisposition.DISCOVERED
    fixture_dependency = next(record for record in inventory.records if record.candidate.display_name == "fixture-dependency")
    assert fixture_dependency.classification is not None
    assert fixture_dependency.classification.classification is PortClassification.PORTABLE
    fixture_unix = next(record for record in inventory.records if record.candidate.display_name == "fixture-unix")
    assert fixture_unix.classification is not None
    assert fixture_unix.classification.ports == ("unix",)


def test_network_catalog_loader_reads_selected_micropython_lib_revision() -> None:
    requested_revision = "v1.29.0"
    resolved_revision = "c" * 40
    revision_url = f"https://api.github.com/repos/micropython/micropython-lib/commits/{requested_revision}"
    archive_url = f"https://github.com/micropython/micropython-lib/archive/{resolved_revision}.zip"
    fetcher = MemoryFetcher(
        {
            revision_url: FetchResponse(json.dumps({"sha": resolved_revision}).encode(), revision_url),
            archive_url: FetchResponse(_fixture_archive(resolved_revision), archive_url),
        }
    )

    inventory = NetworkCatalogLoader(fetcher).load(
        CatalogLoadOptions(CatalogSelection.MICROPYTHON_LIB, CacheMode.REFRESH, requested_revision)
    )

    assert len(inventory.records) == 3
    assert not inventory.diagnostics
    assert fetcher.calls == 2


def test_network_catalog_loader_preserves_snapshot_failure_reason() -> None:
    requested_revision = "v1.29.0"
    resolved_revision = "c" * 40
    revision_url = f"https://api.github.com/repos/micropython/micropython-lib/commits/{requested_revision}"
    archive_url = f"https://github.com/micropython/micropython-lib/archive/{resolved_revision}.zip"
    fetcher = MemoryFetcher(
        {
            revision_url: FetchResponse(json.dumps({"sha": resolved_revision}).encode(), revision_url),
            archive_url: FetchResponse(
                _archive({f"micropython-lib-{resolved_revision}/../escape.py": b"escaped = True\n"}),
                archive_url,
            ),
        }
    )

    inventory = NetworkCatalogLoader(fetcher).load(
        CatalogLoadOptions(CatalogSelection.MICROPYTHON_LIB, CacheMode.REFRESH, requested_revision)
    )

    assert len(inventory.diagnostics) == 1
    assert inventory.diagnostics[0].reason is ReasonCode.UNSAFE_PATH


def test_snapshot_rejects_dynamic_manifest_code() -> None:
    snapshot = MicropythonLibSnapshot.from_files(
        {
            "micropython/dynamic/manifest.py": b'metadata(version="1.0.0")\nmodule_name = "dynamic.py"\nmodule(module_name)\n',
            "micropython/dynamic/dynamic.py": b"value = 1\n",
        },
        requested_revision="v1.29.0",
        resolved_revision="a" * 40,
    )

    with pytest.raises(MicropythonLibManifestError) as raised:
        snapshot.resolve("micropython/dynamic")

    assert raised.value.reason is ReasonCode.INVALID_MANIFEST
    assert "only literal manifest calls are supported" in str(raised.value)


def test_snapshot_allows_parent_relative_base_path_within_repository() -> None:
    snapshot = MicropythonLibSnapshot.from_files(
        {
            "micropython/components/feature/manifest.py": (b'metadata(version="1.0.0")\npackage("shared", base_path="../common")\n'),
            "micropython/components/common/shared/__init__.py": b"value = 1\n",
        },
        requested_revision="v1.29.0",
        resolved_revision="a" * 40,
    )

    resolution = snapshot.resolve("micropython/components/feature")

    assert [item.target for item in resolution.files] == ["shared/__init__.py"]


def test_unix_ffi_precedence_applies_to_transitive_dependencies() -> None:
    snapshot = MicropythonLibSnapshot.from_files(
        {
            "unix-ffi/root/manifest.py": b'metadata(version="1.0.0")\nrequire("nested")\nmodule("root.py")\n',
            "unix-ffi/root/root.py": b"root = True\n",
            "python-stdlib/nested/manifest.py": b'metadata(version="1.0.0")\nrequire("os")\nmodule("nested.py")\n',
            "python-stdlib/nested/nested.py": b"nested = True\n",
            "unix-ffi/os/manifest.py": b'metadata(version="1.0.0")\nmodule("os.py")\n',
            "unix-ffi/os/os.py": b"unix = True\n",
            "python-stdlib/os/manifest.py": b'metadata(version="1.0.0")\nmodule("os.py")\n',
            "python-stdlib/os/os.py": b"stdlib = True\n",
        },
        requested_revision="v1.29.0",
        resolved_revision="a" * 40,
    )

    resolution = snapshot.resolve("unix-ffi/root")

    assert any(item.package_path == "unix-ffi/os" for item in resolution.dependencies)
    assert not any(item.package_path == "python-stdlib/os" for item in resolution.dependencies)


def test_snapshot_rejects_archive_path_traversal() -> None:
    archive = _archive({"micropython-lib-test/../escape.py": b"escaped = True\n"})

    with pytest.raises(MicropythonLibManifestError) as raised:
        MicropythonLibSnapshot.from_zip(archive, requested_revision="test", resolved_revision="a" * 40)

    assert raised.value.reason is ReasonCode.UNSAFE_PATH


def test_snapshot_rejects_archive_symbolic_link() -> None:
    output = BytesIO()
    link = ZipInfo("micropython-lib-test/micropython/link.py")
    link.create_system = 3
    link.external_attr = (stat.S_IFLNK | 0o777) << 16
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        archive.writestr(link, "target.py")

    with pytest.raises(MicropythonLibManifestError) as raised:
        MicropythonLibSnapshot.from_zip(output.getvalue(), requested_revision="test", resolved_revision="a" * 40)

    assert raised.value.reason is ReasonCode.UNSAFE_PATH


def test_snapshot_rejects_expanded_archive_over_byte_limit() -> None:
    archive = _archive({"micropython-lib-test/micropython/large.py": b"x" * 4096})
    limits = MicropythonLibLimits(max_total_bytes=len(archive) + 1)

    with pytest.raises(MicropythonLibManifestError) as raised:
        MicropythonLibSnapshot.from_zip(
            archive,
            requested_revision="test",
            resolved_revision="a" * 40,
            limits=limits,
        )

    assert raised.value.reason is ReasonCode.LIMIT_EXCEEDED
    assert "Expanded snapshot" in str(raised.value)


def test_snapshot_rejects_dependency_cycle() -> None:
    snapshot = MicropythonLibSnapshot.from_files(
        {
            "micropython/one/manifest.py": b'metadata(version="1")\nrequire("two")\n',
            "micropython/two/manifest.py": b'metadata(version="1")\nrequire("one")\n',
        },
        requested_revision="test",
        resolved_revision="a" * 40,
    )

    with pytest.raises(MicropythonLibManifestError) as raised:
        snapshot.resolve("micropython/one")

    assert raised.value.reason is ReasonCode.DEPENDENCY_CYCLE


@pytest.mark.parametrize(
    ("files", "expected_message"),
    [
        (
            {"micropython/root/manifest.py": b'metadata(version="1")\nrequire("missing")\n'},
            "not found or ambiguous: missing",
        ),
        (
            {
                "micropython/root/manifest.py": b'metadata(version="1")\nrequire("shared")\n',
                "micropython/group-a/shared/manifest.py": b'metadata(version="1")\n',
                "micropython/group-b/shared/manifest.py": b'metadata(version="1")\n',
            },
            "not found or ambiguous: shared",
        ),
    ],
)
def test_snapshot_rejects_missing_or_ambiguous_requirement(
    files: dict[str, bytes],
    expected_message: str,
) -> None:
    snapshot = MicropythonLibSnapshot.from_files(
        files,
        requested_revision="test",
        resolved_revision="a" * 40,
    )

    with pytest.raises(MicropythonLibManifestError) as raised:
        snapshot.resolve("micropython/root")

    assert raised.value.reason is ReasonCode.DEPENDENCY_UNAVAILABLE
    assert expected_message in str(raised.value)


def test_snapshot_rejects_dependency_target_collision() -> None:
    snapshot = MicropythonLibSnapshot.from_files(
        {
            "micropython/root/manifest.py": b'metadata(version="1")\nrequire("one")\nrequire("two")\n',
            "micropython/one/manifest.py": b'metadata(version="1")\nmodule("shared.py")\n',
            "micropython/one/shared.py": b"value = 1\n",
            "micropython/two/manifest.py": b'metadata(version="1")\nmodule("shared.py")\n',
            "micropython/two/shared.py": b"value = 2\n",
        },
        requested_revision="test",
        resolved_revision="a" * 40,
    )

    with pytest.raises(MicropythonLibManifestError) as raised:
        snapshot.resolve("micropython/root")

    assert raised.value.reason is ReasonCode.TARGET_COLLISION


def test_snapshot_catalog_deduplicates_with_mim_and_retains_provenance() -> None:
    revision = "a" * 40
    snapshot = MicropythonLibSnapshot.from_directory(
        FIXTURES,
        requested_revision="v1.29.0",
        resolved_revision=revision,
    )
    snapshot_entry = next(entry for entry in MicropythonLibCatalogAdapter().parse(snapshot).entries if entry.name == "fixture-demo")
    mim_entry = CatalogEntry(
        catalog=CatalogSource.MIM,
        name="fixture-demo",
        reference="fixture-demo",
        description="MIM view of the official package.",
        category="networking",
        source_url="https://checkmim.com/packages/fixture-demo",
        repository_url="https://github.com/micropython/micropython-lib/tree/master/micropython/net/fixture-demo",
    )

    inventory = build_inventory((snapshot_entry, mim_entry))

    assert len(inventory.records) == 1
    candidate = inventory.records[0].candidate
    assert candidate.source_family is SourceFamily.MICROPYTHON_LIB
    assert {item.catalog for item in candidate.provenance} == {CatalogSource.MICROPYTHON_LIB, CatalogSource.MIM}
    assert {alias.reference for alias in candidate.aliases} >= {"fixture-demo", snapshot_entry.reference}


def test_mip_resolver_resolves_official_archive_and_replays_offline(tmp_path: Path) -> None:
    requested_revision = "v1.29.0"
    resolved_revision = "b" * 40
    reference = f"github:micropython/micropython-lib/micropython/net/fixture-demo@{requested_revision}"
    revision_url = f"https://api.github.com/repos/micropython/micropython-lib/commits/{requested_revision}"
    archive_url = f"https://github.com/micropython/micropython-lib/archive/{resolved_revision}.zip"
    upstream = MemoryFetcher(
        {
            revision_url: FetchResponse(json.dumps({"sha": resolved_revision}).encode(), revision_url),
            archive_url: FetchResponse(_fixture_archive(resolved_revision), archive_url),
        }
    )
    cache_root = tmp_path / "cache"

    result = MipResolver(CachedFetcher(cache_root, upstream)).resolve_reference(reference)
    offline = MipResolver(CachedFetcher(cache_root, None)).resolve_reference(reference, mode=CacheMode.OFFLINE)

    assert result.record.disposition is RecordDisposition.CHECK
    assert result.record.resolution is not None
    assert result.record.resolution.requested_revision == requested_revision
    assert result.record.resolution.resolved_revision == resolved_revision
    assert result.record.resolution.package_version == "1.2.3"
    assert [item.target for item in result.record.resolution.files] == [
        "fixture_demo.py",
        "fixture_helpers/__init__.py",
        "fixture_helpers/codec.py",
        "fixture_dependency.py",
    ]
    assert result.record.resolution.dependencies[0].requested_reference.endswith("/python-stdlib/fixture-dependency")
    assert offline.record.resolution == result.record.resolution
    assert upstream.calls == 2


@pytest.mark.ecosystem_network
@pytest.mark.skipif(
    os.environ.get("MICROPYTHON_STUBS_ECOSYSTEM_NETWORK") != "1",
    reason="set MICROPYTHON_STUBS_ECOSYSTEM_NETWORK=1 to run live ecosystem checks",
)
def test_live_selected_micropython_lib_repository_snapshot(tmp_path: Path) -> None:
    fetcher = CachedFetcher(tmp_path / "cache", UrlFetcher())
    snapshot = fetch_micropython_lib_snapshot(
        lambda reference: fetcher.fetch(reference, CacheMode.REFRESH).data,
        "v1.29.0",
    )

    parsed = MicropythonLibCatalogAdapter().parse(snapshot)
    resolutions = tuple(snapshot.resolve(path) for path in snapshot.package_paths)

    assert len(snapshot.package_paths) >= 150
    assert len(parsed.entries) == len(snapshot.package_paths)
    assert not parsed.diagnostics
    assert len(resolutions) == len(snapshot.package_paths)
