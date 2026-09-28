from dataclasses import replace
import json
from pathlib import Path
import re

import pytest

from ..model import (
    CatalogProvenance,
    CatalogSource,
    ClassificationOverride,
    FileKind,
    PackageAlias,
    PackageCandidate,
    PackageFile,
    PackageIdentity,
    PackageModelError,
    PortClassification,
    PortEvidence,
    PortEvidenceSource,
    ReasonCode,
    RecordDisposition,
    SourceFamily,
    classify_ports,
    decide_payload,
    deduplicate_candidates,
    load_classification_overrides,
)


def _candidate(
    *,
    catalog: CatalogSource,
    owner: str,
    reference: str,
    entry_url: str,
) -> PackageCandidate:
    return PackageCandidate(
        identity=PackageIdentity.repository("github", owner, "micropython-joystick-2-unit"),
        display_name="micropython-joystick-2-unit",
        source_family=SourceFamily.MIP,
        install_reference=reference,
        aliases=(PackageAlias(catalog, reference),),
        provenance=(CatalogProvenance(catalog, entry_url, "joystick"),),
    )


def test_repository_identity_normalizes_provider_owner_repository_and_git_suffix():
    first = PackageIdentity.repository("GitHub", "HowManyOliversAreThere", "MicroPython-Joystick-2-Unit.git")
    second = PackageIdentity.repository("github", "howmanyoliversarethere", "micropython-joystick-2-unit")

    assert first == second
    assert first.key == "repository:github:howmanyoliversarethere/micropython-joystick-2-unit"


def test_repository_identity_preserves_distinct_monorepository_paths():
    first = PackageIdentity.repository("github", "example", "drivers", "sensor-a")
    second = PackageIdentity.repository("github", "example", "drivers", "sensor-b")

    assert first != second


def test_repository_identity_rejects_traversal():
    with pytest.raises(ValueError, match="normalized relative path"):
        PackageIdentity.repository("github", "example", "drivers", "../package.json")


def test_url_identity_normalizes_origin_and_removes_fragment():
    identity = PackageIdentity.url("HTTPS://Example.COM:443/packages/driver.json?format=mip#section")

    assert identity.key == "url:https://example.com/packages/driver.json?format=mip"


def test_deduplicate_candidates_merges_catalog_aliases_deterministically():
    awesome = _candidate(
        catalog=CatalogSource.AWESOME_MICROPYTHON,
        owner="HowManyOliversAreThere",
        reference="https://github.com/HowManyOliversAreThere/micropython-joystick-2-unit",
        entry_url="https://github.com/mcauser/awesome-micropython",
    )
    mim = _candidate(
        catalog=CatalogSource.MIM,
        owner="howmanyoliversarethere",
        reference="github:howmanyoliversarethere/micropython-joystick-2-unit",
        entry_url="https://checkmim.com/packages/howmanyoliversarethere+micropython-joystick-2-unit",
    )

    forward = deduplicate_candidates([awesome, mim])
    reverse = deduplicate_candidates([mim, awesome])

    assert forward == reverse
    assert len(forward) == 1
    assert forward[0].install_reference == "github:howmanyoliversarethere/micropython-joystick-2-unit"
    assert {alias.catalog for alias in forward[0].aliases} == {
        CatalogSource.AWESOME_MICROPYTHON,
        CatalogSource.MIM,
    }
    assert {item.catalog for item in forward[0].provenance} == {
        CatalogSource.AWESOME_MICROPYTHON,
        CatalogSource.MIM,
    }
    assert deduplicate_candidates(forward) == forward


def test_deduplicate_candidates_reports_source_family_conflicts():
    candidate = _candidate(
        catalog=CatalogSource.MIM,
        owner="example",
        reference="github:example/micropython-joystick-2-unit",
        entry_url="https://example.invalid/package",
    )

    with pytest.raises(PackageModelError) as raised:
        deduplicate_candidates([candidate, replace(candidate, source_family=SourceFamily.SINGLE_FILE)])

    assert raised.value.reason is ReasonCode.IDENTITY_CONFLICT


def test_deduplicate_candidates_keeps_distinct_identities():
    assert (
        len(
            deduplicate_candidates(
                [
                    _candidate(
                        catalog=CatalogSource.AWESOME_MICROPYTHON,
                        owner="owner-a",
                        reference="github:owner-a/micropython-joystick-2-unit",
                        entry_url="https://example.invalid/a",
                    ),
                    _candidate(
                        catalog=CatalogSource.MIM,
                        owner="owner-b",
                        reference="github:owner-b/micropython-joystick-2-unit",
                        entry_url="https://example.invalid/b",
                    ),
                ]
            )
        )
        == 2
    )


def test_payload_uses_python_files_from_the_complete_dependency_closure():
    root = PackageIdentity.repository("github", "example", "mixed")
    dependency = PackageIdentity.index("dependency")
    files = [
        PackageFile(root, "native.mpy", "https://fixtures.invalid/native.mpy"),
        PackageFile(dependency, "dependency.py", "https://fixtures.invalid/dependency.py", dependency_depth=1),
    ]

    decision = decide_payload(files)

    assert decision.disposition is RecordDisposition.CHECK
    assert decision.reason is None
    assert [file.target for file in decision.python_files] == ["dependency.py"]
    assert [file.target for file in decision.mpy_files] == ["native.mpy"]


def test_payload_with_only_mpy_files_has_stable_skip_reason():
    identity = PackageIdentity.repository("github", "example", "native")

    decision = decide_payload([PackageFile(identity, "native_only.mpy", "https://fixtures.invalid/native_only.mpy")])

    assert decision.disposition is RecordDisposition.SKIP
    assert decision.reason is ReasonCode.MPY_ONLY
    assert decision.python_files == ()
    assert decision.mpy_files[0].kind is FileKind.MPY


def test_payload_without_python_or_mpy_files_has_stable_skip_reason():
    identity = PackageIdentity.repository("github", "example", "metadata")

    decision = decide_payload([PackageFile(identity, "README.md", "https://fixtures.invalid/README.md")])

    assert decision.disposition is RecordDisposition.SKIP
    assert decision.reason is ReasonCode.NO_PYTHON_SOURCE


@pytest.mark.parametrize("target", ["../outside.py", "/absolute.py", "C:/drive.py", "folder\\file.py"])
def test_package_file_rejects_unsafe_or_non_posix_targets(target: str):
    identity = PackageIdentity.repository("github", "example", "unsafe")

    with pytest.raises(ValueError):
        PackageFile(identity, target, "https://fixtures.invalid/file.py")


def test_reason_code_values_are_stable_report_keys():
    assert ReasonCode.INVALID_MANIFEST.value == "invalid_manifest"
    assert ReasonCode.UNAVAILABLE.value == "unavailable"
    assert ReasonCode.AMBIGUOUS_PORT.value == "ambiguous_port"
    assert ReasonCode.DEPRECATED_PACKAGE.value == "deprecated_package"


def test_explicit_metadata_takes_precedence_over_static_signals():
    decision = classify_ports(
        [
            PortEvidence(
                PortEvidenceSource.STATIC_SIGNAL,
                PortClassification.PORT_SPECIFIC,
                "Imports an ESP32-only module",
                ports=("esp32",),
            ),
            PortEvidence(
                PortEvidenceSource.EXPLICIT_METADATA,
                PortClassification.PORTABLE,
                "Package metadata declares all ports",
            ),
        ]
    )

    assert decision.classification is PortClassification.PORTABLE
    assert decision.reason is None
    assert len(decision.evidence) == 2


def test_reviewed_override_takes_precedence_over_other_evidence():
    identity = PackageIdentity.repository("github", "example", "driver")
    override = ClassificationOverride(
        identity,
        PortClassification.PORT_SPECIFIC,
        "Maintainer-reviewed compatibility",
        ports=("RP2",),
        reference="https://example.invalid/review",
    )

    decision = classify_ports(
        [
            PortEvidence(
                PortEvidenceSource.EXPLICIT_METADATA,
                PortClassification.PORTABLE,
                "Legacy metadata",
            )
        ],
        override,
    )

    assert decision.classification is PortClassification.PORT_SPECIFIC
    assert decision.ports == ("rp2",)


def test_equal_precedence_specific_evidence_combines_supported_ports():
    decision = classify_ports(
        [
            PortEvidence(
                PortEvidenceSource.DOCUMENTATION,
                PortClassification.PORT_SPECIFIC,
                "ESP32 documented",
                ports=("esp32",),
            ),
            PortEvidence(
                PortEvidenceSource.MANIFEST_PATH,
                PortClassification.PORT_SPECIFIC,
                "RP2 manifest path",
                ports=("rp2",),
            ),
        ]
    )

    assert decision.classification is PortClassification.PORT_SPECIFIC
    assert decision.ports == ("esp32", "rp2")


def test_conflicting_equal_precedence_evidence_stays_unknown():
    decision = classify_ports(
        [
            PortEvidence(
                PortEvidenceSource.DOCUMENTATION,
                PortClassification.PORTABLE,
                "README says portable",
            ),
            PortEvidence(
                PortEvidenceSource.MANIFEST_PATH,
                PortClassification.PORT_SPECIFIC,
                "Port-specific manifest path",
                ports=("esp32",),
            ),
        ]
    )

    assert decision.classification is PortClassification.UNKNOWN
    assert decision.reason is ReasonCode.AMBIGUOUS_PORT


def test_missing_classification_evidence_stays_unknown():
    decision = classify_ports([])

    assert decision.classification is PortClassification.UNKNOWN
    assert decision.reason is ReasonCode.NO_PORT_EVIDENCE


def test_classification_override_file_uses_canonical_identity_keys(tmp_path):
    path = tmp_path / "overrides.json"
    path.write_text(
        """{
  "schema_version": 1,
  "packages": {
    "repository:github:example/driver": {
      "classification": "port_specific",
      "ports": ["ESP32"],
      "rationale": "Maintainer-reviewed package documentation",
      "reference": "https://example.invalid/review"
    }
  }
}
""",
        encoding="utf-8",
    )

    overrides = load_classification_overrides(path)
    identity = PackageIdentity.repository("github", "example", "driver")

    assert overrides[identity].ports == ("esp32",)


def test_port_specific_override_requires_scope(tmp_path):
    path = tmp_path / "overrides.json"
    path.write_text(
        '{"schema_version": 1, "packages": {"index:driver": {"classification": "port_specific", "rationale": "Reviewed"}}}',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="requires a port or board"):
        load_classification_overrides(path)


def test_committed_classification_overrides_validate():
    overrides = load_classification_overrides(Path(__file__).parent.parent / "classification_overrides.json")

    assert {identity.key for identity in overrides} == {
        "repository:github:bartoszadamczyk/pico-ir",
        "repository:github:peterhinch/micropython-micro-gui",
        "repository:github:raspberrypifoundation/picozero",
    }
    assert {identity.key: (override.classification, override.ports, override.boards) for identity, override in overrides.items()} == {
        "repository:github:bartoszadamczyk/pico-ir": (PortClassification.PORT_SPECIFIC, (), ("rpi_pico",)),
        "repository:github:peterhinch/micropython-micro-gui": (PortClassification.PORTABLE, (), ()),
        "repository:github:raspberrypifoundation/picozero": (PortClassification.PORT_SPECIFIC, (), ("rpi_pico",)),
    }
    for override in overrides.values():
        assert override.rationale
        assert override.reference is not None
        assert re.fullmatch(r"https://github\.com/[^/]+/[^/]+/blob/[0-9a-f]{40}/[^#]+(?:#.+)?", override.reference)


def test_fixture_outcomes_use_normalized_contract_values():
    document = json.loads((Path(__file__).parent.parent / "fixtures" / "cases.json").read_text(encoding="utf-8"))
    actions = {"resolve_mip", "resolve_single_file"}

    for group in ("catalog_cases", "manifest_cases"):
        for case in document[group]:
            if disposition := case.get("expected_disposition"):
                RecordDisposition(disposition)
            if reason := case.get("expected_reason"):
                ReasonCode(reason)
            if action := case.get("expected_action"):
                assert action in actions
            if source_family := case.get("expected_source_family"):
                SourceFamily(source_family)
