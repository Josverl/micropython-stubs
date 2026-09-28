from pathlib import Path

from dataclasses import replace
import json

from .catalog import AwesomeCatalogAdapter, CatalogEntry, MimCatalogAdapter, build_inventory
from .model import CatalogSource, PackageIdentity, PortClassification, ReasonCode, RecordDisposition, SourceFamily


FIXTURES = Path(__file__).parent / "fixtures"
AWESOME_SOURCE = "https://raw.githubusercontent.com/mcauser/awesome-micropython/master/readme.md"


def test_awesome_adapter_reads_only_primary_library_links():
    document = (FIXTURES / "awesome" / "readme.md.txt").read_text(encoding="utf-8")

    result = AwesomeCatalogAdapter(AWESOME_SOURCE).parse(document, "2026-09-28T00:00:00Z")

    assert [entry.name for entry in result.entries] == [
        "micropython-joystick-2-unit",
        "IoTy extension",
        "gitlab-package",
        "Official OneWire",
    ]
    assert all(entry.category == "Sensors" for entry in result.entries)
    assert all(entry.observed_at == "2026-09-28T00:00:00Z" for entry in result.entries)
    assert "https://example.invalid/joystick-docs" not in {entry.reference for entry in result.entries}
    assert "https://example.invalid/community" not in {entry.reference for entry in result.entries}
    assert all(entry.category != "Directories and bundled tools" for entry in result.entries)
    assert result.diagnostics == ()


def test_awesome_adapter_reports_library_items_without_links():
    document = """# Fixture

## Libraries

### Invalid

- Missing a package link

## Community

- [Ignored](https://example.invalid/community)
"""

    result = AwesomeCatalogAdapter(AWESOME_SOURCE).parse(document)

    assert result.entries == ()
    assert len(result.diagnostics) == 1
    assert result.diagnostics[0].reason is ReasonCode.INVALID_CATALOG_ENTRY


def test_mim_adapter_discovers_package_pages_from_sitemap():
    document = (FIXTURES / "mim" / "sitemap.xml").read_text(encoding="utf-8")

    result = MimCatalogAdapter().parse_sitemap(document)

    assert [location.key for location in result.locations] == [
        "howmanyoliversarethere+micropython-joystick-2-unit",
        "ntptime",
    ]
    assert all(location.last_modified for location in result.locations)
    assert result.diagnostics == ()


def test_mim_adapter_reports_unrecognized_non_package_sitemap_url():
    result = MimCatalogAdapter().parse_sitemap(
        """<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://checkmim.com/unrecognized</loc></url>
</urlset>"""
    )

    assert result.locations == ()
    assert len(result.diagnostics) == 1
    assert result.diagnostics[0].reason is ReasonCode.INVALID_CATALOG_ENTRY
    assert result.diagnostics[0].reference == "https://checkmim.com/unrecognized"


def test_mim_adapter_parses_community_package_page():
    adapter = MimCatalogAdapter()
    discovery = adapter.parse_sitemap((FIXTURES / "mim" / "sitemap.xml").read_text(encoding="utf-8"))
    location = next(item for item in discovery.locations if item.key.startswith("howmany"))

    result = adapter.parse_package_page(
        location,
        (FIXTURES / "mim" / "community-package.html").read_text(encoding="utf-8"),
    )

    assert result.diagnostics == ()
    assert result.entries[0].reference == "github:howmanyoliversarethere/micropython-joystick-2-unit"
    assert result.entries[0].repository_url == "https://github.com/howmanyoliversarethere/micropython-joystick-2-unit"
    assert dict(result.entries[0].metadata)["license"] == "MIT"
    assert dict(result.entries[0].metadata)["status"] == "VALID"


def test_mim_adapter_parses_official_index_package_page():
    adapter = MimCatalogAdapter()
    discovery = adapter.parse_sitemap((FIXTURES / "mim" / "sitemap.xml").read_text(encoding="utf-8"))
    location = next(item for item in discovery.locations if item.key == "ntptime")

    result = adapter.parse_package_page(
        location,
        (FIXTURES / "mim" / "official-package.html").read_text(encoding="utf-8"),
    )

    assert result.entries[0].reference == "ntptime"
    assert result.entries[0].repository_url is not None
    assert result.entries[0].repository_url.endswith("/micropython/net/ntptime")
    assert dict(result.entries[0].metadata)["version"] == "0.2.2"
    assert result.diagnostics == ()


def test_mim_adapter_reports_pages_without_package_data():
    adapter = MimCatalogAdapter()
    location = adapter.parse_sitemap(
        """<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://checkmim.com/packages/broken</loc></url>
</urlset>"""
    ).locations[0]

    result = adapter.parse_package_page(location, "<html><body>Missing data</body></html>")

    assert result.entries == ()
    assert result.diagnostics[0].reason is ReasonCode.INVALID_CATALOG_ENTRY


def test_mim_adapter_skips_deprecated_page_without_install_reference():
    adapter = MimCatalogAdapter()
    location = adapter.parse_sitemap(
        """<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://checkmim.com/packages/retired-package</loc></url>
</urlset>"""
    ).locations[0]

    result = adapter.parse_package_page(
        location,
        (FIXTURES / "mim" / "deprecated-package.html").read_text(encoding="utf-8"),
    )

    assert result.entries == ()
    assert len(result.diagnostics) == 1
    diagnostic = result.diagnostics[0]
    assert diagnostic.catalog is CatalogSource.MIM
    assert diagnostic.entry_key == "retired-package"
    assert diagnostic.source_url == "https://checkmim.com/packages/retired-package"
    assert diagnostic.disposition is RecordDisposition.SKIP
    assert diagnostic.reason is ReasonCode.DEPRECATED_PACKAGE


def test_mim_adapter_reports_active_page_without_install_reference():
    adapter = MimCatalogAdapter()
    location = adapter.parse_sitemap(
        """<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://checkmim.com/packages/active-package</loc></url>
</urlset>"""
    ).locations[0]
    document = """<script type="application/ld+json">
{"@type":"SoftwareSourceCode","name":"active-package","codeRepository":"https://github.com/example/active-package"}
</script><code>mpremote mip install </code>"""

    result = adapter.parse_package_page(location, document)

    assert result.entries == ()
    assert result.diagnostics[0].disposition is RecordDisposition.ERROR
    assert result.diagnostics[0].reason is ReasonCode.INVALID_CATALOG_ENTRY


def test_mim_adapter_reports_malformed_sitemap():
    result = MimCatalogAdapter().parse_sitemap("<urlset><url>")

    assert result.locations == ()
    assert result.diagnostics[0].reason is ReasonCode.INVALID_CATALOG_ENTRY


def _fixture_catalog_entries() -> tuple[list[CatalogEntry], list]:
    awesome = AwesomeCatalogAdapter(AWESOME_SOURCE).parse(
        (FIXTURES / "awesome" / "readme.md.txt").read_text(encoding="utf-8"),
        "2026-09-28T00:00:00Z",
    )
    mim_adapter = MimCatalogAdapter()
    discovery = mim_adapter.parse_sitemap((FIXTURES / "mim" / "sitemap.xml").read_text(encoding="utf-8"))
    mim_results = [
        mim_adapter.parse_package_page(
            location,
            (FIXTURES / "mim" / filename).read_text(encoding="utf-8"),
        )
        for location, filename in zip(
            discovery.locations,
            ("community-package.html", "official-package.html"),
            strict=True,
        )
    ]
    entries = [*awesome.entries, *(entry for result in mim_results for entry in result.entries)]
    diagnostics = [*awesome.diagnostics, *discovery.diagnostics, *(item for result in mim_results for item in result.diagnostics)]
    return entries, diagnostics


def test_inventory_normalizes_and_deduplicates_cross_catalog_packages():
    entries, diagnostics = _fixture_catalog_entries()

    inventory = build_inventory(entries, diagnostics)

    assert len(inventory.records) == 5
    joystick = next(record for record in inventory.records if "joystick-2-unit" in record.candidate.identity.key)
    assert joystick.candidate.install_reference == "github:howmanyoliversarethere/micropython-joystick-2-unit"
    assert {item.catalog for item in joystick.candidate.provenance} == {
        CatalogSource.AWESOME_MICROPYTHON,
        CatalogSource.MIM,
    }
    assert "https://github.com/HowManyOliversAreThere/micropython-joystick-2-unit" in {
        alias.reference for alias in joystick.candidate.aliases
    }
    assert joystick.disposition is RecordDisposition.DISCOVERED
    assert joystick.reason is None


def test_inventory_deduplicates_within_catalog_and_retains_provenance():
    entries, _ = _fixture_catalog_entries()
    original = next(entry for entry in entries if entry.name == "gitlab-package")
    duplicate = replace(original, category="Alternate category")

    inventory = build_inventory([original, duplicate])

    assert len(inventory.records) == 1
    assert {item.entry_key for item in inventory.records[0].candidate.provenance} == {
        "Sensors:gitlab-package",
        "Alternate category:gitlab-package",
    }


def test_inventory_defers_micropython_lib_without_losing_candidates():
    entries, diagnostics = _fixture_catalog_entries()

    inventory = build_inventory(entries, diagnostics)
    deferred = [record for record in inventory.records if record.disposition is RecordDisposition.DEFERRED]

    assert len(deferred) == 2
    assert all(record.candidate.source_family is SourceFamily.MICROPYTHON_LIB for record in deferred)
    assert all(record.reason is ReasonCode.DEFERRED_INTERNAL_MANIFEST for record in deferred)


def test_inventory_filters_by_catalog_identity_and_classification():
    entries, diagnostics = _fixture_catalog_entries()
    entries.append(
        CatalogEntry(
            catalog=CatalogSource.AWESOME_MICROPYTHON,
            name="ESP32 driver",
            reference="https://github.com/example/esp32-driver",
            description="An ESP32-only driver",
            category="Hardware",
            source_url=AWESOME_SOURCE,
        )
    )
    inventory = build_inventory(entries, diagnostics)
    identity = PackageIdentity.repository("github", "example", "esp32-driver")

    assert len(inventory.filtered(catalog=CatalogSource.MIM).records) == 2
    assert [record.candidate.identity for record in inventory.filtered(identity=identity).records] == [identity]
    specific = inventory.filtered(classification=PortClassification.PORT_SPECIFIC).records
    assert [record.candidate.identity for record in specific] == [identity]
    assert specific[0].classification is not None
    assert specific[0].classification.ports == ("esp32",)


def test_inventory_reports_unsupported_references_with_stable_reason():
    entry = CatalogEntry(
        catalog=CatalogSource.AWESOME_MICROPYTHON,
        name="Documentation",
        reference="https://docs.example.invalid/project/",
        description="Documentation rather than a package",
        category="Other",
        source_url=AWESOME_SOURCE,
    )

    inventory = build_inventory([entry])

    assert inventory.records == ()
    assert inventory.diagnostics[0].reason is ReasonCode.UNSUPPORTED_SOURCE


def test_inventory_json_is_deterministic_and_machine_readable():
    entries, diagnostics = _fixture_catalog_entries()

    forward = build_inventory(entries, diagnostics).to_json()
    reverse = build_inventory(reversed(entries), reversed(diagnostics)).to_json()
    document = json.loads(forward)

    assert forward == reverse
    assert document["schema_version"] == 1
    assert len(document["packages"]) == 5
    assert all("identity" in package and "install_reference" in package for package in document["packages"])
    assert {package["action"] for package in document["packages"]} == {
        "resolve_mip",
        "resolve_single_file",
        None,
    }
