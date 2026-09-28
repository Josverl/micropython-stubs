import hashlib
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
import json
import os
import stat
from dataclasses import dataclass
from pathlib import Path
from threading import Event, Lock
import zipfile

import pytest

from ..model import ReasonCode, RecordDisposition
from ..resolver import (
    ArchiveLimits,
    CacheMode,
    CachedFetcher,
    FetchResponse,
    MipResolver,
    PackageWorkspace,
    ResolverError,
    UrlFetcher,
    plan_mip_reference,
    safe_extract_zip,
)


FIXTURES = Path(__file__).parent.parent / "fixtures" / "mip"


@dataclass
class MemoryFetcher:
    responses: dict[str, FetchResponse]
    calls: int = 0

    def fetch(self, reference: str) -> FetchResponse:
        self.calls += 1
        return self.responses[reference]


class BlockingFetcher:
    def __init__(self, response: FetchResponse) -> None:
        self.response = response
        self.calls = 0
        self.started = Event()
        self.release = Event()
        self._calls_lock = Lock()

    def fetch(self, reference: str) -> FetchResponse:
        _ = reference
        with self._calls_lock:
            self.calls += 1
        self.started.set()
        if not self.release.wait(timeout=2):
            raise TimeoutError("fixture fetch was not released")
        return self.response


def test_plan_github_package_reference():
    planned = plan_mip_reference("github:howmanyoliversarethere/micropython-joystick-2-unit")

    assert planned.logical_reference == "github:howmanyoliversarethere/micropython-joystick-2-unit/package.json"
    assert planned.fetch_reference == (
        "https://raw.githubusercontent.com/howmanyoliversarethere/micropython-joystick-2-unit/HEAD/package.json"
    )
    assert planned.requested_revision is None


def test_plan_provider_file_with_revision():
    planned = plan_mip_reference("github:example/package/src/driver.py@v1.2.0")

    assert planned.fetch_reference == "https://raw.githubusercontent.com/example/package/v1.2.0/src/driver.py"
    assert planned.target_name == "driver.py"
    assert planned.requested_revision == "v1.2.0"


def test_plan_provider_file_encodes_revision_and_path_components():
    planned = plan_mip_reference("github:example/package/drivers/value #1.py@release/1.0")

    assert planned.fetch_reference == ("https://raw.githubusercontent.com/example/package/release%2F1.0/drivers/value%20%231.py")


@pytest.mark.parametrize(
    ("reference", "expected"),
    [
        ("gitlab:example/package@v1", "https://gitlab.com/example/package/-/raw/v1/package.json"),
        ("codeberg:example/package@v1", "https://codeberg.org/api/v1/repos/example/package/raw/package.json?ref=v1"),
    ],
)
def test_plan_supported_provider_packages(reference: str, expected: str):
    assert plan_mip_reference(reference).fetch_reference == expected


def test_plan_index_and_https_references():
    index = plan_mip_reference("collections-defaultdict", "0.1.0")
    url = plan_mip_reference("https://packages.example/driver")

    assert index.fetch_reference == "https://micropython.org/pi/v2/package/py/collections-defaultdict/0.1.0.json"
    assert url.fetch_reference == "https://packages.example/driver/package.json"


def test_unsupported_reference_has_stable_reason():
    resolver = MipResolver(CachedFetcher(Path("unused"), None))

    with pytest.raises(ResolverError) as raised:
        resolver.resolve_reference("https://packages.example/archive.zip")

    assert raised.value.reason is ReasonCode.UNSUPPORTED_SOURCE


def test_cached_fetcher_supports_use_cache_refresh_and_offline(tmp_path: Path):
    reference = "https://packages.example/package.json"
    upstream = MemoryFetcher({reference: FetchResponse(b'{"version":"1"}', reference, "abc123")})
    fetcher = CachedFetcher(tmp_path, upstream)

    first = fetcher.fetch(reference)
    second = fetcher.fetch(reference)
    offline = fetcher.fetch(reference, CacheMode.OFFLINE)
    refreshed = fetcher.fetch(reference, CacheMode.REFRESH)

    assert not first.from_cache
    assert second.from_cache and offline.from_cache
    assert refreshed.resolved_revision == "abc123"
    assert upstream.calls == 2


def test_cached_fetcher_serializes_same_reference_across_threads(tmp_path: Path):
    reference = "https://packages.example/package.json"
    upstream = BlockingFetcher(FetchResponse(b'{"version":"1"}', reference))
    fetcher = CachedFetcher(tmp_path, upstream)

    with ThreadPoolExecutor(max_workers=2) as executor:
        first = executor.submit(fetcher.fetch, reference)
        assert upstream.started.wait(timeout=2)
        second = executor.submit(fetcher.fetch, reference)
        upstream.release.set()
        responses = (first.result(timeout=2), second.result(timeout=2))

    assert upstream.calls == 1
    assert {response.from_cache for response in responses} == {False, True}


def test_cached_fetcher_reports_offline_miss(tmp_path: Path):
    with pytest.raises(ResolverError) as raised:
        CachedFetcher(tmp_path, None).fetch("https://packages.example/missing.json", CacheMode.OFFLINE)

    assert raised.value.reason is ReasonCode.CACHE_MISS


def test_cached_fetcher_detects_modified_body(tmp_path: Path):
    reference = "https://packages.example/package.json"
    upstream = MemoryFetcher({reference: FetchResponse(b"original", reference)})
    fetcher = CachedFetcher(tmp_path, upstream)
    fetcher.fetch(reference)
    body = next(tmp_path.glob("responses/*/*/body"))
    body.write_bytes(b"modified")

    with pytest.raises(ResolverError) as raised:
        fetcher.fetch(reference, CacheMode.OFFLINE)

    assert raised.value.reason is ReasonCode.CACHE_CORRUPT


def test_cached_fetcher_reports_incomplete_entry_as_corrupt(tmp_path: Path):
    reference = "https://packages.example/package.json"
    upstream = MemoryFetcher({reference: FetchResponse(b"original", reference)})
    fetcher = CachedFetcher(tmp_path, upstream)
    fetcher.fetch(reference)
    next(tmp_path.glob("responses/*/*/metadata.json")).unlink()

    with pytest.raises(ResolverError) as raised:
        fetcher.fetch(reference, CacheMode.OFFLINE)

    assert raised.value.reason is ReasonCode.CACHE_CORRUPT


def test_url_fetcher_restricts_local_paths_to_configured_roots(tmp_path: Path):
    allowed_root = tmp_path / "allowed"
    allowed_file = allowed_root / "package.json"
    allowed_file.parent.mkdir()
    allowed_file.write_bytes(b"{}")
    outside_file = tmp_path / "outside.json"
    outside_file.write_bytes(b"{}")
    fetcher = UrlFetcher(local_roots=(allowed_root,))

    assert fetcher.fetch(str(allowed_file)).data == b"{}"
    assert fetcher.fetch(allowed_file.as_uri()).data == b"{}"
    with pytest.raises(ResolverError) as raised:
        fetcher.fetch(str(outside_file))

    assert raised.value.reason is ReasonCode.UNSUPPORTED_REFERENCE


def _fixture_bytes(relative_path: str) -> bytes:
    return (FIXTURES / relative_path).read_bytes()


def _resolver(tmp_path: Path, responses: dict[str, bytes], *, materialize: bool = False) -> MipResolver:
    upstream = MemoryFetcher({reference: FetchResponse(data, reference) for reference, data in responses.items()})
    cache_root = tmp_path / "cache"
    workspace = PackageWorkspace(cache_root) if materialize else None
    return MipResolver(CachedFetcher(cache_root, upstream), workspace=workspace)


def test_resolve_supplied_github_reference_pins_commit_and_replays_offline(tmp_path: Path):
    revision = "61087f6f86236fb2240b53b47eca5fbbdefdfd88"
    revision_url = "https://api.github.com/repos/howmanyoliversarethere/micropython-joystick-2-unit/commits/HEAD"
    manifest_url = f"https://raw.githubusercontent.com/howmanyoliversarethere/micropython-joystick-2-unit/{revision}/package.json"
    source_url = f"https://raw.githubusercontent.com/HowManyOliversAreThere/micropython-joystick-2-unit/{revision}/joystick_2_unit.py"
    upstream = MemoryFetcher(
        {
            revision_url: FetchResponse(json.dumps({"sha": revision}).encode(), revision_url),
            manifest_url: FetchResponse(_fixture_bytes("simple/package.json"), manifest_url),
            source_url: FetchResponse(b"class Joystick2Unit:\n    pass\n", source_url),
        }
    )
    cache_root = tmp_path / "cache"
    reference = "github:howmanyoliversarethere/micropython-joystick-2-unit"

    result = MipResolver(CachedFetcher(cache_root, upstream)).resolve_reference(reference)
    offline = MipResolver(CachedFetcher(cache_root, None)).resolve_reference(reference, mode=CacheMode.OFFLINE)

    assert result.record.disposition is RecordDisposition.CHECK
    assert result.record.resolution is not None
    assert result.record.resolution.resolved_revision == revision
    assert result.record.resolution.package_version == "1.2"
    assert result.record.resolution.manifest_reference == manifest_url
    assert [file.source for file in result.record.resolution.files] == [source_url]
    assert offline.record.resolution == result.record.resolution
    assert upstream.calls == 3


def test_resolve_direct_python_url(tmp_path: Path):
    source_url = "https://fixtures.invalid/driver.py"
    resolver = _resolver(tmp_path, {source_url: b"value = 1\n"})

    result = resolver.resolve_reference(source_url)

    assert result.record.disposition is RecordDisposition.CHECK
    assert result.record.resolution is not None
    assert [file.target for file in result.record.resolution.files] == ["driver.py"]


def test_requested_provider_revision_is_not_replaced_by_manifest_version(tmp_path: Path):
    revision = "a" * 40
    revision_url = "https://api.github.com/repos/example/package/commits/v1"
    manifest_url = f"https://raw.githubusercontent.com/example/package/{revision}/package.json"
    resolver = _resolver(
        tmp_path,
        {
            revision_url: json.dumps({"sha": revision}).encode(),
            manifest_url: json.dumps({"version": "2.0", "urls": []}).encode(),
        },
    )

    result = resolver.resolve_reference("github:example/package@v1")

    assert result.record.resolution is not None
    assert result.record.resolution.requested_revision == "v1"
    assert result.record.resolution.resolved_revision == revision
    assert result.record.resolution.package_version == "2.0"


def test_gitlab_default_branch_resolves_to_immutable_commit(tmp_path: Path):
    revision = "b" * 40
    revision_url = "https://gitlab.com/api/v4/projects/example%2Fpackage/repository/commits?per_page=1"
    source_url = f"https://gitlab.com/example/package/-/raw/{revision}/driver.py"
    resolver = _resolver(
        tmp_path,
        {
            revision_url: json.dumps([{"id": revision}]).encode(),
            source_url: b"value = 1\n",
        },
    )

    result = resolver.resolve_reference("gitlab:example/package/driver.py")

    assert result.record.resolution is not None
    assert result.record.resolution.resolved_revision == revision
    assert result.record.resolution.package_version is None
    assert result.record.resolution.files[0].source == source_url


def test_codeberg_default_branch_resolves_to_immutable_commit(tmp_path: Path):
    revision = "c" * 40
    repository_url = "https://codeberg.org/api/v1/repos/example/package"
    revision_url = "https://codeberg.org/api/v1/repos/example/package/git/commits/main"
    source_url = f"https://codeberg.org/api/v1/repos/example/package/raw/driver.py?ref={revision}"
    resolver = _resolver(
        tmp_path,
        {
            repository_url: json.dumps({"default_branch": "main"}).encode(),
            revision_url: json.dumps({"sha": revision}).encode(),
            source_url: b"value = 1\n",
        },
    )

    result = resolver.resolve_reference("codeberg:example/package/driver.py")

    assert result.record.resolution is not None
    assert result.record.resolution.resolved_revision == revision
    assert result.record.resolution.package_version is None
    assert result.record.resolution.files[0].source == source_url


def test_resolve_mixed_and_mpy_only_payloads(tmp_path: Path):
    mixed_manifest = "https://fixtures.invalid/mixed/package.json"
    mpy_manifest = "https://fixtures.invalid/mpy/package.json"
    resolver = _resolver(
        tmp_path,
        {
            mixed_manifest: _fixture_bytes("mixed/package.json"),
            "https://fixtures.invalid/mixed/source.py": b"value = 1\n",
            "https://fixtures.invalid/mixed/native.mpy": b"M\x06fixture",
            mpy_manifest: _fixture_bytes("mpy-only/package.json"),
            "https://fixtures.invalid/native_only.mpy": b"M\x06only",
        },
    )

    mixed = resolver.resolve_reference(mixed_manifest)
    mpy_only = resolver.resolve_reference(mpy_manifest)

    assert mixed.record.disposition is RecordDisposition.CHECK
    resolution = mixed.record.resolution
    assert resolution is not None
    assert {file.target for file in resolution.files} == {"mixed/source.py", "mixed/native.mpy"}
    assert mpy_only.record.disposition is RecordDisposition.SKIP
    assert mpy_only.record.reason is ReasonCode.MPY_ONLY


@pytest.mark.parametrize(
    ("fixture", "reason"),
    [
        ("malformed/package.json", ReasonCode.INVALID_MANIFEST),
        ("path-traversal/package.json", ReasonCode.UNSAFE_PATH),
        ("collision/package.json", ReasonCode.TARGET_COLLISION),
    ],
)
def test_resolver_reports_invalid_manifest_paths_and_collisions(tmp_path: Path, fixture: str, reason: ReasonCode):
    manifest_url = "https://fixtures.invalid/package.json"
    responses = {manifest_url: _fixture_bytes(fixture)}
    if reason is ReasonCode.TARGET_COLLISION:
        responses.update(
            {
                "https://fixtures.invalid/one.py": b"one = 1\n",
                "https://fixtures.invalid/two.py": b"two = 2\n",
            }
        )
    resolver = _resolver(tmp_path, responses)

    result = resolver.resolve_reference(manifest_url)

    assert result.record.disposition is RecordDisposition.ERROR
    assert result.record.reason is reason


def test_resolver_detects_dependency_cycle(tmp_path: Path):
    revision_a = "a" * 40
    revision_b = "b" * 40
    a_url = f"https://raw.githubusercontent.com/fixtures/cycle-a/{revision_a}/package.json"
    b_url = f"https://raw.githubusercontent.com/fixtures/cycle-b/{revision_b}/package.json"
    resolver = _resolver(
        tmp_path,
        {
            "https://api.github.com/repos/fixtures/cycle-a/commits/v1": json.dumps({"sha": revision_a}).encode(),
            "https://api.github.com/repos/fixtures/cycle-b/commits/v1": json.dumps({"sha": revision_b}).encode(),
            a_url: _fixture_bytes("cycle/a.json"),
            b_url: _fixture_bytes("cycle/b.json"),
            "https://fixtures.invalid/cycle/a.py": b"a = 1\n",
            "https://fixtures.invalid/cycle/b.py": b"b = 1\n",
        },
    )

    result = resolver.resolve_reference("github:fixtures/cycle-a@v1")

    assert result.record.disposition is RecordDisposition.ERROR
    assert result.record.reason is ReasonCode.DEPENDENCY_CYCLE


def test_index_hash_validation_uses_content_addressed_file(tmp_path: Path):
    payload = b"value = 42\n"
    short_hash = hashlib.sha256(payload).hexdigest()[:16]
    manifest = json.dumps({"v": 1, "version": "1.0", "hashes": [["value.py", short_hash]]}).encode()
    manifest_url = "https://micropython.org/pi/v2/package/py/example/latest.json"
    file_url = f"https://micropython.org/pi/v2/file/{short_hash[:2]}/{short_hash}"
    resolver = _resolver(tmp_path, {manifest_url: manifest, file_url: payload})

    result = resolver.resolve_reference("example")

    assert result.record.disposition is RecordDisposition.CHECK
    assert result.record.resolution is not None
    assert result.record.resolution.resolved_revision == "1.0"


def test_index_hash_requires_a_bounded_hex_digest(tmp_path: Path):
    manifest_url = "https://micropython.org/pi/v2/package/py/example/latest.json"
    resolver = _resolver(tmp_path, {manifest_url: json.dumps({"hashes": [["value.py", "bad"]]}).encode()})

    result = resolver.resolve_reference("example")

    assert result.record.disposition is RecordDisposition.ERROR
    assert result.record.reason is ReasonCode.INVALID_MANIFEST


def test_manifest_rejects_unsupported_format_version(tmp_path: Path):
    manifest_url = "https://fixtures.invalid/package.json"
    resolver = _resolver(tmp_path, {manifest_url: json.dumps({"v": 2, "urls": []}).encode()})

    result = resolver.resolve_reference(manifest_url)

    assert result.record.disposition is RecordDisposition.ERROR
    assert result.record.reason is ReasonCode.INVALID_MANIFEST


def test_nested_dependencies_are_inventoried_in_one_closure(tmp_path: Path):
    root_url = "https://fixtures.invalid/nested/package.json"
    provider_revision = "d" * 40
    provider_revision_url = "https://api.github.com/repos/example/dependency/commits/v1.0.0"
    provider_manifest_url = f"https://raw.githubusercontent.com/example/dependency/{provider_revision}/package.json"
    provider_source_url = f"https://raw.githubusercontent.com/example/dependency/{provider_revision}/provider_dependency.py"
    index_manifest_url = "https://micropython.org/pi/v2/package/py/collections-defaultdict/latest.json"
    indexed_payload = b"from collections import defaultdict\n"
    short_hash = hashlib.sha256(indexed_payload).hexdigest()[:16]
    index_manifest = json.loads(_fixture_bytes("nested/index-dependency.json"))
    index_manifest["hashes"][0][1] = short_hash
    index_source_url = f"https://micropython.org/pi/v2/file/{short_hash[:2]}/{short_hash}"
    resolver = _resolver(
        tmp_path,
        {
            root_url: _fixture_bytes("nested/package.json"),
            "https://fixtures.invalid/nested/src/main.py": b"main = True\n",
            provider_revision_url: json.dumps({"sha": provider_revision}).encode(),
            provider_manifest_url: _fixture_bytes("nested/provider-dependency.json"),
            provider_source_url: b"provider = True\n",
            index_manifest_url: json.dumps(index_manifest).encode(),
            index_source_url: indexed_payload,
        },
        materialize=True,
    )

    result = resolver.resolve_reference(root_url)

    assert result.record.disposition is RecordDisposition.CHECK
    assert result.record.resolution is not None
    assert {file.target for file in result.record.resolution.files} == {
        "nested/main.py",
        "nested/provider_dependency.py",
        "collections/defaultdict.py",
    }
    assert len(result.record.resolution.dependencies) == 2
    assert all(edge.resolved_revision for edge in result.record.resolution.dependencies)
    assert result.workspace is not None
    metadata = json.loads((result.workspace / "metadata.json").read_text(encoding="utf-8"))
    assert {dependency["requested_reference"] for dependency in metadata["dependencies"]} == {
        "github:example/dependency",
        "collections-defaultdict",
    }
    assert metadata["package_version"] == "1.0.0"


def test_workspace_materializes_and_cleans_one_package_independently(tmp_path: Path):
    manifest_url = "https://fixtures.invalid/package.json"
    resolver = _resolver(
        tmp_path,
        {
            manifest_url: json.dumps({"version": "1", "urls": [["driver.py", "https://fixtures.invalid/driver.py"]]}).encode(),
            "https://fixtures.invalid/driver.py": b"value = 1\n",
        },
        materialize=True,
    )

    result = resolver.resolve_reference(manifest_url)

    assert result.workspace is not None
    assert (result.workspace / "source" / "driver.py").read_bytes() == b"value = 1\n"
    assert (result.workspace / "metadata.json").is_file()
    identity = result.record.candidate.identity
    workspace = resolver.workspace
    assert workspace is not None
    package_root = workspace.package_root(identity)
    unrelated = workspace.root / "packages" / "unrelated" / "keep.txt"
    unrelated.parent.mkdir(parents=True)
    unrelated.write_text("keep", encoding="utf-8")

    workspace.clean(identity)

    assert not package_root.exists()
    assert unrelated.read_text(encoding="utf-8") == "keep"


def test_workspace_key_changes_when_same_version_payload_changes(tmp_path: Path):
    manifest_url = "https://fixtures.invalid/package.json"
    source_url = "https://fixtures.invalid/driver.py"
    manifest = json.dumps({"version": "1", "urls": [["driver.py", source_url]]}).encode()
    upstream = MemoryFetcher(
        {
            manifest_url: FetchResponse(manifest, manifest_url),
            source_url: FetchResponse(b"value = 1\n", source_url),
        }
    )
    cache_root = tmp_path / "cache"
    resolver = MipResolver(CachedFetcher(cache_root, upstream), workspace=PackageWorkspace(cache_root))

    first = resolver.resolve_reference(manifest_url)
    upstream.responses[source_url] = FetchResponse(b"value = 2\n", source_url)
    second = resolver.resolve_reference(manifest_url, mode=CacheMode.REFRESH)

    assert first.workspace is not None and second.workspace is not None
    assert first.workspace != second.workspace
    assert (first.workspace / "source" / "driver.py").read_bytes() == b"value = 1\n"
    assert (second.workspace / "source" / "driver.py").read_bytes() == b"value = 2\n"


def test_workspace_rebuilds_modified_source_without_corrupting_object(tmp_path: Path):
    manifest_url = "https://fixtures.invalid/package.json"
    source_url = "https://fixtures.invalid/driver.py"
    source = b"value = 1\n"
    resolver = _resolver(
        tmp_path,
        {
            manifest_url: json.dumps({"version": "1", "urls": [["driver.py", source_url]]}).encode(),
            source_url: source,
        },
        materialize=True,
    )

    first = resolver.resolve_reference(manifest_url)
    assert first.workspace is not None
    (first.workspace / "source" / "driver.py").write_bytes(b"tampered\n")

    second = resolver.resolve_reference(manifest_url, mode=CacheMode.OFFLINE)

    second_workspace = second.workspace
    assert second_workspace is not None
    assert second_workspace == first.workspace
    assert (second_workspace / "source" / "driver.py").read_bytes() == source
    object_path = next((tmp_path / "cache" / "objects").rglob(hashlib.sha256(source).hexdigest()))
    assert object_path.read_bytes() == source


def test_mpy_only_package_is_not_materialized(tmp_path: Path):
    manifest_url = "https://fixtures.invalid/mpy/package.json"
    resolver = _resolver(
        tmp_path,
        {
            manifest_url: _fixture_bytes("mpy-only/package.json"),
            "https://fixtures.invalid/native_only.mpy": b"M\x06only",
        },
        materialize=True,
    )

    result = resolver.resolve_reference(manifest_url)

    assert result.record.disposition is RecordDisposition.SKIP
    assert result.record.reason is ReasonCode.MPY_ONLY
    assert result.workspace is None


def _zip_bytes(files: dict[str, bytes], *, symlinks: frozenset[str] = frozenset()) -> bytes:
    output = BytesIO()
    with zipfile.ZipFile(output, "w") as archive:
        for name, content in files.items():
            info = zipfile.ZipInfo(name)
            if name in symlinks:
                info.create_system = 3
                info.external_attr = (stat.S_IFLNK | 0o777) << 16
            archive.writestr(info, content)
    return output.getvalue()


def test_safe_extract_zip_is_atomic_and_rejects_traversal(tmp_path: Path):
    destination = tmp_path / "package"

    files = safe_extract_zip(_zip_bytes({"src/main.py": b"value = 1\n"}), destination)

    assert files == (destination / "src" / "main.py",)
    assert files[0].read_bytes() == b"value = 1\n"

    unsafe_destination = tmp_path / "unsafe"
    with pytest.raises(ResolverError) as raised:
        safe_extract_zip(_zip_bytes({"../outside.py": b"bad = True\n"}), unsafe_destination)

    assert raised.value.reason is ReasonCode.UNSAFE_PATH
    assert not unsafe_destination.exists()
    assert not (tmp_path / "outside.py").exists()


def test_safe_extract_zip_rejects_links_and_size_limit(tmp_path: Path):
    with pytest.raises(ResolverError) as linked:
        safe_extract_zip(
            _zip_bytes({"link.py": b"target.py"}, symlinks=frozenset({"link.py"})),
            tmp_path / "linked",
        )

    assert linked.value.reason is ReasonCode.UNSAFE_PATH
    assert not (tmp_path / "linked").exists()

    with pytest.raises(ResolverError) as oversized:
        safe_extract_zip(
            _zip_bytes({"large.py": b"0123456789"}),
            tmp_path / "oversized",
            limits=ArchiveLimits(max_total_bytes=8),
        )

    assert oversized.value.reason is ReasonCode.LIMIT_EXCEEDED
    assert not (tmp_path / "oversized").exists()


def test_safe_extract_zip_rejects_case_insensitive_collision(tmp_path: Path):
    with pytest.raises(ResolverError) as raised:
        safe_extract_zip(
            _zip_bytes({"package/Main.py": b"one = 1\n", "package/main.py": b"two = 2\n"}),
            tmp_path / "collision",
        )

    assert raised.value.reason is ReasonCode.TARGET_COLLISION
    assert not (tmp_path / "collision").exists()


def test_resolver_rejects_case_insensitive_target_collision(tmp_path: Path):
    manifest_url = "https://fixtures.invalid/package.json"
    manifest = json.dumps(
        {
            "urls": [
                ["package/Main.py", "https://fixtures.invalid/one.py"],
                ["package/main.py", "https://fixtures.invalid/two.py"],
            ]
        }
    ).encode()
    resolver = _resolver(
        tmp_path,
        {
            manifest_url: manifest,
            "https://fixtures.invalid/one.py": b"one = 1\n",
            "https://fixtures.invalid/two.py": b"two = 2\n",
        },
    )

    result = resolver.resolve_reference(manifest_url)

    assert result.record.disposition is RecordDisposition.ERROR
    assert result.record.reason is ReasonCode.TARGET_COLLISION


@pytest.mark.ecosystem_network
@pytest.mark.skipif(
    os.environ.get("MICROPYTHON_STUBS_ECOSYSTEM_NETWORK") != "1",
    reason="set MICROPYTHON_STUBS_ECOSYSTEM_NETWORK=1 to run live ecosystem checks",
)
def test_live_supplied_github_reference(tmp_path: Path):
    cache_root = tmp_path / "cache"
    resolver = MipResolver(CachedFetcher(cache_root, UrlFetcher()))

    result = resolver.resolve_reference("github:howmanyoliversarethere/micropython-joystick-2-unit")

    assert result.record.disposition is RecordDisposition.CHECK
    assert result.record.resolution is not None
    assert [file.target for file in result.record.resolution.files] == ["joystick_2_unit.py"]
