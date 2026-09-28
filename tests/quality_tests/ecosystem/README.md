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

`QARunReport` preserves package identity, provenance, requested and resolved revisions, stub selection and provisioning command, checker commands, normalized diagnostics, counts, statuses, and timings. `to_json` emits schema version 1; `render_text` emits a concise summary and any setup/checker error. Workspace retention is `never`, `on_failure`, or `always` so failed inputs can be inspected without accumulating successful runs.

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
| 2 | Unsupported, unavailable, internal/setup failure, no selected package, or command usage error. |

JSON reports use schema version 1 and retain each package's runner reports. Text reports show the same outcomes and aggregate counts. One package failure does not stop later packages.

Live pytest cases are marked `ecosystem_network` and excluded by repository defaults. Run them only with both the marker and environment opt-in:

```powershell
$env:MICROPYTHON_STUBS_ECOSYSTEM_NETWORK = "1"
uv run pytest -m ecosystem_network tests/quality_tests/ecosystem -n 0
```

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

## Report vocabulary

Record dispositions are `discovered`, `check`, `skip`, `error`, and `deferred`. Skipped, failed, and deferred records require one of the stable reason codes defined by `ReasonCode`:

```text
mpy_only
no_python_source
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
