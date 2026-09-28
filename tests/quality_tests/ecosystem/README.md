# Ecosystem package contract

This directory defines the normalized records shared by catalog ingestion, package resolution, and stub QA. The source adapters may differ, but downstream code consumes the models in `model.py`.

## Processing stages

1. A catalog adapter emits a `PackageCandidate` with one canonical identity, its install reference, every observed alias, and catalog provenance.
2. `deduplicate_candidates` merges candidates with the same identity. Its result is deterministic and independent of input order.
3. A resolver emits one `PackageResolution` for the requested package and its complete dependency closure.
4. `decide_payload` selects `.py` checker inputs and records `.mpy` files without analyzing them.
5. `classify_ports` records a portable, port-specific, or unknown decision with all supporting evidence.
6. `PackageRecord` combines these stages with a stable disposition and optional reason code for reports.

Catalog adapters and resolvers must not import or execute third-party modules.

## Catalog ingestion

`catalog.py` is deliberately transport-free. Callers fetch or cache source documents; adapters only parse supplied text:

- `AwesomeCatalogAdapter.parse` reads the first link from each top-level list item in the Markdown `Libraries` section. Secondary documentation links and later sections are excluded.
- `MimCatalogAdapter.parse_sitemap` discovers package detail pages and their `lastmod` values.
- `MimCatalogAdapter.parse_package_page` reads `SoftwareSourceCode` JSON-LD plus the rendered `mpremote mip install` command.
- `build_inventory` normalizes references, defers `micropython-lib`, deduplicates aliases, applies reviewed classification overrides, and returns stable package records and diagnostics.

Provider owner/repository spelling is canonicalized in the primary install reference while original catalog URLs and references remain aliases. Unsupported or malformed entries become diagnostics with stable reason codes; one bad entry does not abort the catalog.

`CatalogInventory.filtered` selects records by source catalog, canonical package identity, and known port classification without downloading package content. `to_dict` and `to_json` emit schema version 1 with deterministic package/diagnostic order. Adapter actions are `resolve_mip` and `resolve_single_file`; deferred sources have no resolver action.

## Package identity

Canonical keys have one of these forms:

```text
repository:{provider}:{owner}/{repository}[/{package-root-or-file}]
index:{package-name}
url:{normalized-http-or-https-url}
```

Repository providers, owners, and repository names are case-insensitive and normalized with `casefold`; a trailing `.git` is removed. A path within a repository remains case-sensitive. It identifies a package root or a direct file and excludes mutable branch/tag/revision data. Adapters should map an implicit or explicit root `package.json` to the repository root, not append `package.json` to the identity.

Index names are case-insensitive. URL identities normalize the scheme, host, and default port and discard fragments while retaining path and query data. Provider repository identities are preferred over URL identities when a source adapter can establish them reliably.

Aliases preserve original spelling and catalog ownership. Provenance preserves the catalog entry URL/key and observation time. Deduplication unions both sets and chooses a provider-style or bare-index install reference before a general URL. Conflicting non-unknown source families fail with `identity_conflict`; they are never silently merged.

## Resolution and payload

`PackageResolution` records:

- requested and canonical references;
- requested and immutable resolved revisions;
- package metadata version separately from the resolved provider revision;
- manifest reference and SHA-256;
- dependency edges with depth, identity, revision, disposition, and reason;
- file inventory for the entire dependency closure.

Every `PackageFile` records the owning package, normalized install target, source, dependency depth, optional hash, and size. Targets must be relative POSIX paths without empty, dot, parent, drive, or absolute components.

Payload policy is closure-based:

- one or more `.py` files: disposition `check`; only those files go to type checkers;
- no `.py` but one or more `.mpy` files: disposition `skip`, reason `mpy_only`;
- neither `.py` nor `.mpy`: disposition `skip`, reason `no_python_source`;
- mixed payload: check `.py`, retain `.mpy` only as inventory.

Therefore a bytecode-only root with a source dependency is checkable because its resolved closure contains Python source.

## MIP resolver and cache

`resolver.py` resolves provider, HTTP(S), package-index, and direct `.py`/`.mpy` references. Manifest `urls`, `hashes`, and `deps` are followed recursively into one bounded closure. Resolution reads bytes and JSON only; package modules and manifest-supplied code are never imported or executed.

Fetch transport is injected. `UrlFetcher` supports bounded HTTPS responses and local files restricted to configured roots. `CachedFetcher` provides three explicit modes:

| Mode | Behavior |
| --- | --- |
| `use_cache` | Reuse a valid response entry, otherwise fetch and cache it. |
| `refresh` | Bypass the response entry, fetch again, and replace it atomically. |
| `offline` | Read a valid response entry only; report `cache_miss` rather than use the network. |

The gitignored `tests/quality_tests/.ecosystem-cache/` layout is:

```text
responses/<prefix>/<request-sha256>/{body,metadata.json}
objects/sha256/<prefix>/<content-sha256>
packages/<sanitized-name>-<identity-digest>/<revision>-<closure-digest>/{source,metadata.json}
locks/
.staging/
```

Response and object hashes are validated before reuse. Package paths combine a readable sanitized component with a digest, and workspace keys include manifest and payload hashes so a mutable source cannot reuse stale files merely by retaining its version label. `PackageWorkspace.clean(identity)` removes only that package's materialized revisions; shared response and object entries remain available to other packages.

GitHub, GitLab, and Codeberg references are resolved through their cached provider APIs before package content is fetched. Mutable branch, tag, and default-branch references therefore produce a full commit in `resolved_revision`; the manifest `version` remains separate as `package_version`. Manifest and provider payload URLs are rewritten to that commit. Run one refresh or cached online resolution before the first offline replay so the provider revision response and pinned content are present; references that already contain a full commit do not require a revision lookup.

ZIP extraction is atomic and bounded by file count and total uncompressed bytes. Absolute/parent/drive paths, backslashes, symbolic links, encrypted members, and case-insensitive target collisions are rejected before the staged directory is published.

All default resolver tests use local fixtures and injected responses. The live smoke test is additionally marked `ecosystem_network` and skipped unless `MICROPYTHON_STUBS_ECOSYSTEM_NETWORK=1` is set explicitly.

## Isolated package QA

`runner.py` converts a resolved record into explicit `QACase` instances and checks each case in a fresh temporary workspace:

```text
source/       # resolved .py payload only
typings/      # selected MicroPython stubs
pyproject.toml and checker configuration
```

`.mpy` inventory entries are never copied into checker source. `plan_qa_matrix` tests portable packages against every requested port/board, limits port-specific packages to compatible selections, and skips an empty intersection with `no_compatible_port`. An unknown classification skips with its evidence reason unless the caller explicitly selects `use_requested`.

Stub sources are `local`, `pypi`, `pypi-pre`, and an explicit filesystem `path`. The runner provisions `typings/`, narrows the existing quality-test checker configuration to `source/`, and dispatches through the existing Pyright, mypy, Ruff, Pyrefly, ty, or Zuban adapters. Installed stubs are search inputs and are excluded from package-source analysis. Package modules are written as bytes and are never imported or executed.

`QARunReport` preserves package identity, provenance, requested and resolved revisions, package version, manifest hash, dependency and payload inventory, stub selection and provisioning command, checker commands, normalized diagnostics, counts, statuses, and timings. JSON and text renderers emit schema version 2 evidence. Serialized commands, provenance, references, diagnostics, and error messages redact URL credentials, sensitive query/metadata values, file URLs, and absolute host paths. Workspace retention is reported as a boolean; its machine-specific path remains available only on the in-memory report for local debugging. Retention is `never`, `on_failure`, or `always` so failed inputs can be inspected without accumulating successful runs.

## Focused and batch commands

The command module requires either a direct package or an explicit catalog selection. A direct package bypasses catalog discovery:

```powershell
uv run python -m tests.quality_tests.ecosystem.cli `
  --package github:howmanyoliversarethere/micropython-joystick-2-unit `
  --version v1.28.0 `
  --portboard rp2-rpi_pico `
  --stub-source local `
  --checker pyright `
  --cache-mode use_cache `
  --report json `
  --report-file results/ecosystem-joystick.json
```

Repeat `--version`, `--portboard`, or `--checker` to build a matrix. Stub sources are `local`, `pypi`, `pypi-pre`, and `path`; the last requires `--stub-path`. `--retain on_failure` preserves failed QA workspaces, and `--no-stub-cache` forwards a cache bypass to uv stub provisioning.

Batch mode accepts `awesome`, `mim`, or `both` and applies filters after normalized cross-catalog deduplication:

```powershell
uv run python -m tests.quality_tests.ecosystem.cli `
  --catalog both `
  --package-filter sensor `
  --classification portable `
  --port-filter rp2 `
  --limit 25 `
  --version v1.28.0 `
  --portboard rp2-rpi_pico `
  --stub-source pypi `
  --checker pyright `
  --refresh `
  --workers 4 `
  --rate-limit 2
```

`--workers` bounds concurrent MIM page fetches from 1 through 16. Package resolution and QA remain deterministically isolated, while `--rate-limit` spaces all upstream catalog and package request starts. `--refresh` replaces matching response-cache entries; `--cache-mode offline` forbids upstream requests and reports cache misses as unavailable. These modes cannot be combined.

Package outcomes are `pass`, `type_check_failure`, `unsupported`, `unavailable`, `skipped`, and `error`. Exit codes are stable:

| Exit | Meaning |
| --- | --- |
| 0 | All selected packages passed or were intentionally skipped. |
| 1 | At least one type-check failure and no operational failure. |
| 2 | Error catalog diagnostics, unsupported or unavailable packages, internal/setup failure, no selected package, or command usage error. |

JSON reports use schema version 2. Both JSON and text record the focused or batch discovery selection, cache mode, requested version/port/checker matrix, run policies, immutable package revision and manifest hash, complete dependency/payload closure, typings provisioning, checker outcomes, stage status, and aggregate counts. Resolved closure evidence is stored once per package; each matrix entry retains only its provisioning and checker run. Skipped and unavailable packages explicitly report stages that did not run. One package failure does not stop later packages.

Live pytest cases are marked `ecosystem_network` and excluded by repository defaults. Run them only with both the marker and environment opt-in:

```powershell
$env:MICROPYTHON_STUBS_ECOSYSTEM_NETWORK = "1"
uv run pytest -m ecosystem_network tests/quality_tests/ecosystem -n 0
```

## Pilot baseline

`pilot_baseline.json` is the reviewed, path-independent baseline from the 2026-09-28 pilot. Raw CLI reports remain under the gitignored `tests/quality_tests/.ecosystem-cache/reports/` directory because durations and upstream outcomes are run-specific. Schema-v2 report renderers exclude credentials and machine-specific paths so a report can be retained as reproducibility evidence when needed.

The fixture corpus exercises both catalog adapters plus every agreed edge case: portable, port-specific, and unknown classification; cross-catalog duplicates; dependency closures; malformed, unsafe, cyclic, colliding, or unavailable inputs; mixed `.py`/`.mpy`; and `.mpy`-only closures. The full offline gate produced 103 passes with the one live network smoke test deselected. Package source was parsed and copied for static analysis only; no package module was imported or executed.

The live pilot used MicroPython v1.28.0 RP2 Pico stubs and Pyright:

| Run | Selected result | Catalog diagnostics | Process exit | Wall time |
| --- | --- | ---: | ---: | ---: |
| Direct joystick refresh | pass | 0 | 0 | 10.670 s |
| Both catalogs, joystick filter, refresh | pass | 14 | 2 | 97.557 s |
| Same batch, offline replay | pass | 14 | 2 | 10.630 s |

The batch selected one canonical joystick package with both Awesome MicroPython and MIM provenance, proving cross-catalog deduplication. Its checker passed one Python source file with no diagnostics. The process still returned 2 because the full catalog snapshot contained seven Awesome non-package links, four deprecated MIM entries without install references, and three non-package MIM sitemap URLs. These unsupported shapes are tracked by `micropython-stubs-ut0.10` and `micropython-stubs-ut0.11`; they are not stub defects and do not change the selected package's pass result.

The pilot found no actionable stub defect in the selected package. Separate follow-ups cover immutable provider revisions (`micropython-stubs-ut0.12`), complete reproducibility evidence in generated reports (`micropython-stubs-ut0.13`), and the reviewed compatibility evidence needed to reduce 892 unknown classifications (`micropython-stubs-ut0.14`).

The refreshed cache contained 318 responses and 12,531,076 body bytes. No failed workspace was retained. Broad validation remains a manual, review-triggered operation for now: the first bounded refresh took 97.6 seconds and MIM publishes neither a bulk API nor rate-limit terms. Reconsider scheduled CI only after the catalog-shape follow-ups are resolved and two refresh runs demonstrate stable runtime and network cost.

## Operations and maintenance

Prerequisites are the repository `uv` environment, the selected checker, and matching stubs. The commands below use checked-in local packages, so only catalog and package inputs require network access:

```powershell
uv sync
uv run pyright --version
Test-Path publish/micropython-stdlib-stubs
Test-Path publish/micropython-v1_28_0-rp2-rpi_pico-stubs
```

Reproduce the direct pilot:

```powershell
uv run python -m tests.quality_tests.ecosystem.cli `
  --package github:howmanyoliversarethere/micropython-joystick-2-unit `
  --version v1.28.0 `
  --portboard rp2-rpi_pico `
  --stub-source local `
  --checker pyright `
  --refresh `
  --retain on_failure `
  --report json `
  --report-file tests/quality_tests/.ecosystem-cache/reports/direct-joystick.json
```

Reproduce the bounded, deduplicated batch:

```powershell
uv run python -m tests.quality_tests.ecosystem.cli `
  --catalog both `
  --package-filter joystick-2-unit `
  --limit 1 `
  --version v1.28.0 `
  --portboard rp2-rpi_pico `
  --stub-source local `
  --checker pyright `
  --unknown-policy use_requested `
  --refresh `
  --workers 4 `
  --rate-limit 4 `
  --retain on_failure `
  --report json `
  --report-file tests/quality_tests/.ecosystem-cache/reports/batch-joystick.json
```

After one successful refresh, replace `--refresh` with `--cache-mode offline` to guarantee zero upstream requests. An absent response becomes `unavailable [cache_miss]`; offline mode never falls back to the network. Use `use_cache` for normal manual runs, and reserve refresh for an intentional snapshot update.

The cache and temporary QA workspaces live below `tests/quality_tests/.ecosystem-cache/`. Successful workspaces are removed automatically. `--retain on_failure` keeps failed workspaces under `runs/` for inspection, while `--retain always` keeps every workspace. Remove retained runs without discarding downloaded responses, or reset the entire cache:

```powershell
Remove-Item -Recurse -Force tests/quality_tests/.ecosystem-cache/runs
Remove-Item -Recurse -Force tests/quality_tests/.ecosystem-cache
```

Read the top-level package `outcome` independently from `catalog_diagnostics`. A package can pass while the process exits 2 because discovery was incomplete. Exit 1 is reserved for checker failures when no operational failure occurred. Reports record catalog provenance, requested and resolved package references, stub provisioning, checker commands, diagnostics, counts, timings, and whether a workspace was retained. The retained path is available only in memory for local debugging.

Classification overrides belong in `classification_overrides.json` only after review of explicit repository or package evidence. Include a rationale and durable reference, then run:

```powershell
uv run pytest tests/quality_tests/ecosystem/test_model.py tests/quality_tests/ecosystem/test_catalog.py tests/quality_tests/ecosystem/test_runner.py -q -n 0
```

Ordinary pytest remains network-free because `ecosystem_network` is excluded in the repository defaults. Keep raw reports and caches uncommitted; update `pilot_baseline.json` only from a reviewed run, preserving factual aggregate data rather than local absolute paths or mirrored third-party content.

## Port classification

Evidence is evaluated in this order; only the highest available level decides the classification:

| Precedence | Evidence source |
| --- | --- |
| 40 | reviewed repository override |
| 30 | explicit package metadata |
| 20 | package documentation or manifest/source path |
| 10 | strong static signal such as an import exclusive to a port |

Equal-precedence port-specific evidence is combined, allowing a package to support multiple named ports or boards. Equal-precedence evidence that disagrees between portable and port-specific yields `unknown` with `ambiguous_port`. No evidence yields `unknown` with `no_port_evidence`. Lower-precedence signals remain attached for reporting but cannot overturn stronger evidence.

`classification_overrides.json` is the reviewed override store. It is keyed by canonical package identity:

```json
{
  "schema_version": 1,
  "packages": {
    "repository:github:example/driver": {
      "classification": "port_specific",
      "ports": ["esp32"],
      "boards": [],
      "rationale": "Maintainer-reviewed compatibility statement",
      "reference": "https://example.invalid/review"
    }
  }
}
```

Portable overrides cannot name ports or boards. Port-specific overrides must name at least one port or board. Unknown is a classifier result, not valid evidence or an override value.

The initial reviewed corpus deliberately gives each source catalog both outcomes. `micropython-micro-gui` appears in Awesome MicroPython and MIM, and its maintainer explicitly describes it as portable between hosts. Awesome's `pico-ir` and MIM's `picozero` explicitly target Raspberry Pi Pico, so both use the conservative `rpi_pico` board scope. A shared MicroPython module such as `machine`, `network`, or `framebuf` is not evidence of a port or board by itself.

Review and expiry policy:

1. Resolve every catalog alias to its canonical identity and verify which catalogs currently contain it.
2. Accept an override only from an explicit maintainer or official package statement. Portable evidence must claim portability or name multiple supported host families; port-specific evidence must name the supported port or board.
3. Cite the exact upstream document using a provider URL pinned to a full commit and summarize the relevant claim in the rationale. Choose the narrowest scope the evidence supports.
4. Re-review each entry during the annual ecosystem refresh and no later than 12 months after the last substantive Git change to that entry. Use Git history as the review record.
5. Re-review immediately when a repository moves or is archived, a catalog changes the package identity, the cited document becomes unavailable, or current documentation or releases contradict the override.
6. An entry expires when its review deadline passes or its evidence is unavailable or contradicted. Remove it so classification returns to `unknown`; add it again only after recording new commit-pinned evidence.

## Report vocabulary

Record dispositions are `discovered`, `check`, `skip`, `error`, and `deferred`. Skipped, failed, and deferred records require one of the stable reason codes defined by `ReasonCode`:

```text
mpy_only
no_python_source
deprecated_package
deferred_internal_manifest
unsupported_reference
unsupported_source
invalid_catalog_entry
invalid_manifest
unavailable
dependency_unavailable
unsafe_path
dependency_cycle
target_collision
limit_exceeded
cache_miss
cache_corrupt
identity_conflict
no_compatible_port
ambiguous_port
no_port_evidence
```

`fixtures/cases.json` uses `expected_action` for work still required from an adapter or resolver, and uses `expected_disposition` plus `expected_reason` only for normalized record outcomes.
