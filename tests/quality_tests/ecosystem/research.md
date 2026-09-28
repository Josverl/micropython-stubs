# Ecosystem package source research

Research date: 2026-09-28
Beads epic: `micropython-stubs-ut0`
Research spike: `micropython-stubs-ut0.2`

## Decisions

1. Keep catalog discovery separate from package resolution. Awesome MicroPython and MIM produce catalog records; a MIP resolver turns supported references into an installable Python-file inventory.
2. Use a manifest-neutral record between source adapters and the QA runner. MIP `package.json` details must not leak into the checker/workspace layer.
3. The initial implementation resolves community MIP packages from Awesome MicroPython and MIM. It may inventory official `micropython-lib` entries exposed by either catalog, but reports their resolution as deferred. Internal-manifest support belongs to `micropython-stubs-ut0.9`.
4. Force source-package resolution (`py` / `mpy=False`) because the QA target is `.py` source. Record mixed `.py`/`.mpy` payloads, and skip a resolved closure only when it contains no `.py` file.
5. Treat catalog pages, manifests, archives, and source files as untrusted data. Never import package modules. Validate paths, bound recursion and downloads, detect cycles and target collisions, and materialize a package atomically below a git-ignored root.
6. Reuse the existing isolated-workspace, stub-installation, checker-configuration, and checker-execution code in `tests/quality_tests`; do not make the ecosystem layer another checker implementation.

## Catalog sources

### Awesome MicroPython

Authoritative catalog input:

- Repository: <https://github.com/mcauser/awesome-micropython>
- Raw catalog: <https://raw.githubusercontent.com/mcauser/awesome-micropython/master/readme.md>
- Scope: top-level package entries below `## Libraries`; stop before `## Community`.
- License: CC0-1.0.

The input is Markdown, not a package index. Parse a Markdown syntax tree and select the leading link from each library-list item. Do not collect every link with a regular expression: descriptions contain documentation, product, source-file, and secondary links that are not separate packages.

A dated inventory of the `Libraries` section found 801 HTTP links (800 distinct): 748 GitHub, 34 GitLab, and 7 Codeberg links, including 32 GitHub `blob`/`tree` deep links. These are link counts, not package counts, because descriptions can contain additional links. Relevant entry shapes include:

- repository roots that may have an implicit `package.json`;
- explicit `package.json`, directory, or single-file links;
- GitHub, GitLab, and Codeberg repositories;
- deep links into monorepositories;
- official `micropython-lib` links, which are catalogued but deferred;
- C/native-only, application, example, archived, moved, or unavailable repositories;
- descriptions with port hints such as ESP32, ESP8266, RP2, Pyboard, or Pycom.

Store the section/category, display name, description, original URL, and catalog provenance before normalizing a package reference. Repository identity alone is not always sufficient: two deep paths in one monorepository can be distinct package candidates.

The raw endpoint currently returns an ETag and `Cache-Control: max-age=300`. Cache the body and ETag, use a conditional request after the freshness interval, and record the resolved catalog commit when available. Avoid the GitHub API for routine catalog refresh; reserve provider API or `git ls-remote` calls for pinning mutable package refs, with bounded concurrency and optional authenticated credentials supplied outside reports.

### MIM

Authoritative discovery input:

- Site: <https://checkmim.com/>
- Sitemap: <https://checkmim.com/sitemap.xml>
- Package details: `https://checkmim.com/packages/{package-key}`
- Robots policy: `/`, `/packages/`, `/users/`, and `/about` are allowed; account, submission, profile, and administration routes are disallowed.

No documented JSON API was found. The package list and detail pages are server-rendered, and browser inspection observed no package-data API request. Use the XML sitemap for discovery rather than walking `?page=N`; then fetch only new or changed detail pages. The sitemap is served with `Cache-Control: public, max-age=0, s-maxage=3600` and gives every package a `lastmod` value.

The 2026-09-28 sitemap contained 314 package pages:

- 185 owner/repository-style keys such as `howmanyoliversarethere+micropython-joystick-2-unit`;
- 129 bare index-style keys such as `ntptime`, `base64`, and `umqtt.simple`;
- all 314 entries had `lastmod` timestamps.

MIM explicitly contains both community packages and official packages sourced from `micropython-lib`. Detail pages expose factual fields useful to normalization: canonical install command/reference, source repository, author, submitter, license, version, tags, validation status, description, and README content. Observed statuses include `Valid` for a community package and `Human Reviewed` for an official package; treat status as open text rather than a closed enum.

The supplied example page resolves to:

```text
mpremote mip install github:howmanyoliversarethere/micropython-joystick-2-unit
```

Its source link differs in letter case from the install command and from the Awesome entry. Normalize GitHub owner/repository identity case-insensitively while preserving the source spelling and all provenance.

MIM declares site content all rights reserved and publishes no bulk-API terms or rate limit. Keep only factual metadata, links, hashes, and extraction evidence; do not mirror full pages or README text in committed fixtures. Cache detail results by sitemap `lastmod`, identify the client, use low bounded concurrency, honor `Retry-After`, and stop/reduce traffic on 429 or repeated 5xx responses.

Official MIM entries such as `ntptime` use a bare index reference and point into `micropython-lib`. The initial adapter should emit the catalog record with `source_family=micropython-lib` and a deferred-resolution reason. It must not silently treat these as community MIP manifests.

## MIP package semantics

Canonical references are documented at <https://docs.micropython.org/en/latest/reference/packages.html>. The host implementation used as the behavior reference is `repos/micropython/tools/mpremote/mpremote/mip.py`.

| Input | Resolution behavior |
| --- | --- |
| bare name | Resolve `{index}/package/{abi-or-py}/{name}/{version}.json`; version defaults to `latest`. |
| HTTP(S) or provider `.py`/`.mpy` URL | Download one file to its basename. |
| HTTP(S), `github:`, `gitlab:`, or `codeberg:` package reference | Append `/package.json` when no JSON filename is present. |
| provider reference plus `@ref` | Use the branch/tag ref when rewriting provider URLs. |
| local `.json` path | Supported by host `mpremote`; useful for deterministic fixture tests. |

Provider rewrites are:

- `github:org/repo/path` -> `https://raw.githubusercontent.com/org/repo/{ref-or-HEAD}/path`
- `gitlab:org/repo/path` -> `https://gitlab.com/org/repo/-/raw/{ref-or-HEAD}/path`
- `codeberg:org/repo/path` -> `https://codeberg.org/api/v1/repos/org/repo/raw/path?ref={ref-or-HEAD}`

Supported manifest fields are:

- `version`: package metadata; a self-hosted manifest does not use it to pin its own URLs;
- `urls`: `(destination_path, source_url)` pairs; source URLs may be relative to the manifest or absolute/provider-prefixed;
- `deps`: `(package_reference, version_or_ref)` pairs, recursively resolved;
- `hashes`: `(destination_path, short_sha256)` pairs used by the official package index;
- `v`: package-index manifest format version.

The official index is <https://micropython.org/pi/v2>. Its `index.json` format is version 2 and includes package names, current and available versions, license, description, source path, and source/bytecode variants. Source manifests live below `/package/py/{name}/{version}.json`; for example, `ntptime/latest.json` currently resolves version `0.2.2` to a content-addressed `ntptime.py` hash.

For community QA, resolve the complete dependency closure in source mode and retain an edge list. A package qualifies for checking when that closure contributes at least one `.py` file. Record `.mpy` files but never analyze them as Python source. A closure containing only `.mpy` files receives the stable skip reason `mpy_only`.

The official installer is a compatibility oracle, not the implementation to invoke. It writes manifest destination paths directly, has no explicit cycle or target-collision guard, and can leave partial output after a failure. The QA resolver must additionally enforce:

- normalized relative POSIX destination paths with no absolute path or `..` escape;
- allowed schemes/hosts and configurable byte/file/depth limits;
- dependency cycle detection and deterministic duplicate-edge handling;
- collision detection when packages map different content to one destination;
- immutable revision capture where the provider permits it;
- download-to-staging followed by atomic package publication;
- offline cache lookup keyed by canonical reference, resolved revision, and content hash.

Mutable `HEAD`, branch, and `latest` references must be resolved to immutable evidence for each run. Reports should contain the requested ref, resolved commit/version, manifest hash, and file hashes. Reproduction should prefer the immutable form.

## Port classification evidence

MIP `package.json` has no standard port or board field. Catalog descriptions and MIM tags are hints, not authoritative compatibility declarations. The next design task should preserve evidence and classify in this order:

1. explicit package metadata or a reviewed repository override;
2. manifest/source path or documented supported ports;
3. strong static signals such as imports of a port-only module;
4. otherwise `unknown`.

Do not infer that use of common modules such as `machine` makes a package specific to one port. Native/C-only packages and `.mpy`-only packages are unsupported for source QA independently of port classification.

## Existing QA integration

The current suite already separates most downstream concerns:

- `tests/quality_tests/conftest.py::install_stubs` installs local, PyPI, or preview stubs into a shared cache.
- `type_stub_cache_path_fx` fingerprints and locks that cache.
- `snip_path_fx` creates a real-file isolated workspace and copies checker configuration.
- `copy_type_stubs_fx` links or copies the cached stubs to `typings/`.
- `tests/quality_tests/typecheck.py::run_typechecker` dispatches the supported checkers and normalizes diagnostics.

The ecosystem runner should provide downloaded `.py` files as the workspace source instead of a `feat_*` folder, then reuse or extract these helpers. Checker configuration already excludes `typings/` from source analysis. Live catalog tests need a new registered marker and explicit option or command; default pytest must continue to run only deterministic local-fixture tests.

## Fixture policy

Committed fixtures are minimal, synthetic representations of public formats. They contain links and factual metadata, not mirrored third-party source or README bodies. `fixtures/cases.json` is the fixture inventory and expected disposition.

The initial fixture set covers:

- Awesome repository-root, deep-file, non-GitHub, and deferred `micropython-lib` links;
- MIM community and official sitemap/detail records;
- the supplied `github:howmanyoliversarethere/micropython-joystick-2-unit` manifest shape;
- relative and provider URLs, nested dependencies, mixed `.py`/`.mpy`, `.mpy`-only, and malformed manifests.

Parser/resolver implementation may extend these fixtures, but network responses must never be required by unit tests.

## Recommended cache contract

Use `tests/quality_tests/.ecosystem-cache/` as the default persistent root and add it to `tests/quality_tests/.gitignore` when the resolver is implemented. Allow a CLI/environment override so CI can place the cache on a durable volume. Use this layout:

```text
.ecosystem-cache/
	catalogs/{adapter}/{snapshot-id}/body
	catalogs/{adapter}/{snapshot-id}/metadata.json
	objects/sha256/{first-two}/{digest}
	packages/{safe-package-id}/{resolved-revision}/metadata.json
	packages/{safe-package-id}/{resolved-revision}/source/
	locks/{cache-key}.lock
```

`safe-package-id` should be a readable slug plus a digest of the canonical source identity, not an untrusted catalog string. A package metadata record should include:

- requested and canonical references;
- source adapter and catalog provenance;
- requested version/ref and immutable resolved version/revision;
- source manifest URL and SHA-256;
- dependency edges and their resolved identities;
- every destination path, origin URL/hash, media kind, byte count, and SHA-256;
- disposition/skip reason, timestamps, and resolver schema version.

Store downloaded bytes once in the content-addressed object pool. Build each per-package `source/` tree in a sibling staging directory, validate the whole dependency closure, then rename it into place. A package entry is valid only when its metadata and all referenced objects exist and hash correctly. Use a per-key lock compatible with pytest-xdist; a stale or interrupted staging directory is disposable.

Catalog cache metadata should retain the request URL, fetched-at time, ETag, Last-Modified, response status, SHA-256, adapter schema version, and, for MIM, sitemap `lastmod`. Refresh with conditional requests. Follow a small bounded number of HTTPS redirects while recording the redirect chain and final URL; this preserves evidence for moved repositories without silently changing package identity.

Deterministic tests use only `fixtures/` with an injected fetch transport. Normal pytest runs must not access the network. Live catalog/package checks require both an `ecosystem_live` marker and an explicit option such as `--ecosystem-live`; refreshing mutable refs should require a further explicit `--ecosystem-refresh` action. Offline CLI mode should fail with a structured cache-miss result rather than fall back to the network.

## Refresh and failure policy

- Default to cached catalog and package data; make refresh explicit for focused runs and bounded for batch runs.
- Preserve the previous valid catalog snapshot if refresh fails, and report its age.
- Distinguish `unavailable`, `invalid_catalog_entry`, `invalid_manifest`, `unsupported_reference`, `unsafe_path`, `dependency_cycle`, `target_collision`, `no_python_source`, and `mpy_only`.
- Do not log credentials or signed URLs. Authentication is optional input for provider rate limits, never fixture or report data.
- Do not execute setup scripts, package modules, examples, or downloaded tools. Static type checkers receive source paths only.

## Sources

- <https://github.com/mcauser/awesome-micropython>
- <https://checkmim.com/about>
- <https://checkmim.com/robots.txt>
- <https://checkmim.com/sitemap.xml>
- <https://docs.micropython.org/en/latest/reference/packages.html>
- <https://micropython.org/pi/v2/index.json>
- `repos/micropython/tools/mpremote/mpremote/mip.py`
- `repos/micropython/lib/micropython-lib/tools/build.py`
