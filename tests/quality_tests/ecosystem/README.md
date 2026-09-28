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
identity_conflict
ambiguous_port
no_port_evidence
```

`fixtures/cases.json` uses `expected_action` for work still required from an adapter or resolver, and uses `expected_disposition` plus `expected_reason` only for normalized record outcomes.
