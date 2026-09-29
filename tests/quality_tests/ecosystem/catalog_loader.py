"""Cached, bounded loading for live ecosystem catalogs."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from threading import Lock
import time
from typing import Callable, Mapping, Protocol

from .catalog import (
    AwesomeCatalogAdapter,
    CatalogDiagnostic,
    CatalogEntry,
    CatalogInventory,
    CatalogParseResult,
    MimCatalogAdapter,
    MimPackageLocation,
    build_inventory,
)
from .micropython_lib import MicropythonLibCatalogAdapter, MicropythonLibManifestError, fetch_micropython_lib_snapshot
from .model import CatalogSource, ClassificationOverride, PackageIdentity, ReasonCode, RecordDisposition
from .orchestrator import CatalogSelection
from .progress import NullProgressReporter, ProgressReporter
from .resolver import CacheMode, FetchResponse, Fetcher, ResolverError


AWESOME_CATALOG_URL = "https://raw.githubusercontent.com/mcauser/awesome-micropython/master/readme.md"
MIM_SITEMAP_URL = "https://checkmim.com/sitemap.xml"
MAX_CATALOG_WORKERS = 16


class CachedCatalogFetcher(Protocol):
    def fetch(self, reference: str, mode: CacheMode = CacheMode.USE_CACHE) -> FetchResponse: ...


class RateLimitedFetcher:
    """Space upstream request starts across all catalog and package workers."""

    def __init__(
        self,
        upstream: Fetcher,
        requests_per_second: float,
        *,
        clock: Callable[[], float] = time.monotonic,
        sleeper: Callable[[float], None] = time.sleep,
    ) -> None:
        if requests_per_second <= 0 or requests_per_second > 100:
            raise ValueError("requests per second must be greater than 0 and at most 100")
        self.upstream = upstream
        self.interval = 1.0 / requests_per_second
        self.clock = clock
        self.sleeper = sleeper
        self._lock = Lock()
        self._last_started: float | None = None

    def fetch(self, reference: str) -> FetchResponse:
        with self._lock:
            now = self.clock()
            if self._last_started is not None:
                delay = self._last_started + self.interval - now
                if delay > 0:
                    self.sleeper(delay)
                    now = self.clock()
            self._last_started = now
        return self.upstream.fetch(reference)


@dataclass(frozen=True)
class CatalogLoadOptions:
    catalogs: CatalogSelection = CatalogSelection.BOTH
    cache_mode: CacheMode = CacheMode.USE_CACHE
    micropython_lib_revision: str = "HEAD"

    def __post_init__(self) -> None:
        if not self.micropython_lib_revision.strip():
            raise ValueError("micropython-lib revision must not be empty")


class NetworkCatalogLoader:
    def __init__(
        self,
        fetcher: CachedCatalogFetcher,
        *,
        max_workers: int = 4,
        progress: ProgressReporter | None = None,
    ) -> None:
        if not 1 <= max_workers <= MAX_CATALOG_WORKERS:
            raise ValueError(f"catalog workers must be between 1 and {MAX_CATALOG_WORKERS}")
        self.fetcher = fetcher
        self.max_workers = max_workers
        self.progress = progress or NullProgressReporter()
        self._catalog_total = 0

    def load(
        self,
        options: CatalogLoadOptions,
        *,
        overrides: Mapping[PackageIdentity, ClassificationOverride] | None = None,
    ) -> CatalogInventory:
        entries: list[CatalogEntry] = []
        diagnostics: list[CatalogDiagnostic] = []
        self.progress.start_catalog(options.catalogs.value)
        self._catalog_total = len(options.catalogs.sources)
        self.progress.set_catalog_total(self._catalog_total)
        try:
            if CatalogSource.AWESOME_MICROPYTHON in options.catalogs.sources:
                result = self._load_awesome(options.cache_mode)
                entries.extend(result.entries)
                diagnostics.extend(result.diagnostics)
            if CatalogSource.MIM in options.catalogs.sources:
                result = self._load_mim(options.cache_mode)
                entries.extend(result.entries)
                diagnostics.extend(result.diagnostics)
            if CatalogSource.MICROPYTHON_LIB in options.catalogs.sources:
                result = self._load_micropython_lib(options.cache_mode, options.micropython_lib_revision)
                entries.extend(result.entries)
                diagnostics.extend(result.diagnostics)
            return build_inventory(entries, diagnostics, overrides)
        finally:
            self.progress.finish_catalog()

    def _load_awesome(self, mode: CacheMode) -> CatalogParseResult:
        adapter = AwesomeCatalogAdapter(AWESOME_CATALOG_URL)
        try:
            document = self.fetcher.fetch(AWESOME_CATALOG_URL, mode).data.decode("utf-8")
            return adapter.parse(document)
        except Exception as error:
            return CatalogParseResult((), (_load_diagnostic(CatalogSource.AWESOME_MICROPYTHON, "catalog", AWESOME_CATALOG_URL, error),))
        finally:
            self.progress.advance_catalog("Awesome MicroPython")

    def _load_mim(self, mode: CacheMode) -> CatalogParseResult:
        adapter = MimCatalogAdapter(MIM_SITEMAP_URL)
        try:
            sitemap = self.fetcher.fetch(MIM_SITEMAP_URL, mode).data.decode("utf-8")
            discovery = adapter.parse_sitemap(sitemap)
        except Exception as error:
            return CatalogParseResult((), (_load_diagnostic(CatalogSource.MIM, "sitemap", MIM_SITEMAP_URL, error),))
        finally:
            self.progress.advance_catalog("MIM sitemap")

        entries: list[CatalogEntry] = []
        diagnostics = list(discovery.diagnostics)
        self._catalog_total += len(discovery.locations)
        self.progress.set_catalog_total(self._catalog_total)
        with ThreadPoolExecutor(max_workers=self.max_workers, thread_name_prefix="ecosystem-catalog") as executor:
            futures = {
                executor.submit(self._load_mim_page, adapter, location, mode): (index, location)
                for index, location in enumerate(discovery.locations)
            }
            results: dict[int, CatalogParseResult] = {}
            for future in as_completed(futures):
                index, location = futures[future]
                result = future.result()
                results[index] = result
                self.progress.advance_catalog(location.key)
            for index in range(len(discovery.locations)):
                result = results[index]
                entries.extend(result.entries)
                diagnostics.extend(result.diagnostics)
        return CatalogParseResult(tuple(entries), tuple(diagnostics))

    def _load_mim_page(
        self,
        adapter: MimCatalogAdapter,
        location: MimPackageLocation,
        mode: CacheMode,
    ) -> CatalogParseResult:
        try:
            document = self.fetcher.fetch(location.page_url, mode).data.decode("utf-8")
            return adapter.parse_package_page(location, document)
        except Exception as error:
            return CatalogParseResult((), (_load_diagnostic(CatalogSource.MIM, location.key, location.page_url, error),))

    def _load_micropython_lib(self, mode: CacheMode, requested_revision: str) -> CatalogParseResult:
        source_url = "https://github.com/micropython/micropython-lib"
        try:
            snapshot = fetch_micropython_lib_snapshot(
                lambda reference: self.fetcher.fetch(reference, mode).data,
                requested_revision,
            )
            return MicropythonLibCatalogAdapter().parse(snapshot)
        except Exception as error:
            return CatalogParseResult(
                (),
                (_load_diagnostic(CatalogSource.MICROPYTHON_LIB, requested_revision, source_url, error),),
            )
        finally:
            self.progress.advance_catalog("micropython-lib")


def _load_diagnostic(catalog: CatalogSource, key: str, source_url: str, error: Exception) -> CatalogDiagnostic:
    if isinstance(error, (MicropythonLibManifestError, ResolverError)):
        reason = error.reason
    elif isinstance(error, UnicodeDecodeError):
        reason = ReasonCode.INVALID_CATALOG_ENTRY
    else:
        reason = ReasonCode.UNAVAILABLE
    return CatalogDiagnostic(
        catalog=catalog,
        entry_key=key,
        source_url=source_url,
        disposition=RecordDisposition.ERROR,
        reason=reason,
        detail=str(error),
    )
