# Ecosystem QA tester guide

Use this harness to check real MicroPython packages against a selected stub package with Pyright, mypy, Ruff, or Pyrefly. Package source is resolved into an isolated workspace and inspected statically; it is never imported or executed.

Run all commands from the repository root in PowerShell.

## Quick start

Install the test tools and verify the command:

```powershell
uv sync --extra test
uv run python -m tests.quality_tests.ecosystem.cli --help
```

Run one package with the practical defaults:

```powershell
uv run python -m tests.quality_tests.ecosystem.cli `
  --package github:howmanyoliversarethere/micropython-joystick-2-unit `
  --version v1.28.0
```

This focused command bypasses catalog discovery. It uses the checked-in v1.28.0 ESP32 generic stubs and Pyright, prints a text report, and retains the workspace only if the run fails. An uncached first run requires network access to resolve and cache the package.

Run the offline regression suite at any time:

```powershell
uv run pytest tests/quality_tests/ecosystem -q
```

The suite uses local fixtures. The live network smoke test is excluded unless explicitly enabled.

## Defaults

`--version` is the only always-required selection. Other omitted options use these defaults:

| Setting | Default |
| --- | --- |
| Catalog | `mim` when `--package` is absent |
| Port and board | `esp32-esp32_generic` |
| Checker | `pyright` |
| Stub source | `local` |
| Cache mode | `use_cache` |
| Workspace retention | `on_failure` |
| Report | Text on standard output |
| Report-file mode | `replace` |
| Unknown port policy | `skip` for catalog runs; `use_requested` for focused runs |
| MIM fetch controls | 4 workers, 2 request starts per second |

Selectable stable checkers are `pyright`, `mypy`, `ruff`, and `pyrefly`. Repeat `--version`, `--portboard`, or `--checker` to build a matrix. The currently unstable `ty` and `zuban` adapters are intentionally not CLI choices.

## Common runs

### Focus one package

Use `--package` for the quickest investigation of a known MIP, provider, package-index, HTTP(S), or direct-file reference:

```powershell
uv run python -m tests.quality_tests.ecosystem.cli `
  --package github:howmanyoliversarethere/micropython-joystick-2-unit `
  --version v1.28.0 `
  --report json `
  --report-file tests/quality_tests/.ecosystem-cache/reports/joystick.json
```

### Run a bounded MIM batch

Omitting `--package` uses MIM. Filters are applied after catalog normalization and deduplication:

```powershell
uv run python -m tests.quality_tests.ecosystem.cli `
  --version v1.28.0 `
  --package-filter sensor `
  --limit 5 `
  --report json `
  --report-file tests/quality_tests/.ecosystem-cache/reports/mim-sensors.json
```

`--limit` bounds selected packages, not catalog discovery requests. For wider discovery, select `--catalog awesome` or `--catalog both`. Useful batch filters are `--package-filter`, `--classification`, and `--port-filter`.

```powershell
uv run python -m tests.quality_tests.ecosystem.cli `
  --catalog both `
  --package-filter joystick `
  --classification portable `
  --port-filter rp2 `
  --limit 10 `
  --version v1.28.0 `
  --portboard rp2-rpi_pico
```

### Compare checkers or targets

Repeated options form the Cartesian QA matrix after package compatibility filtering:

```powershell
uv run python -m tests.quality_tests.ecosystem.cli `
  --package github:howmanyoliversarethere/micropython-joystick-2-unit `
  --version v1.28.0 `
  --portboard esp32-esp32_generic `
  --portboard rp2-rpi_pico `
  --checker pyright `
  --checker mypy
```

For a catalog package with unknown or ambiguous compatibility, the default is to skip it. Use `--unknown-policy use_requested` only when you intentionally want to test it against the requested target.

### Select a stub source

The default `local` source installs matching packages from `publish/`. Alternatives are:

| Option | Use |
| --- | --- |
| `--stub-source pypi` | Latest matching stable package from PyPI |
| `--stub-source pypi-pre` | Matching package including prereleases |
| `--stub-source path --stub-path <directory>` | Copy one explicit stub tree |

For example:

```powershell
uv run python -m tests.quality_tests.ecosystem.cli `
  --package github:howmanyoliversarethere/micropython-joystick-2-unit `
  --version v1.28.0 `
  --stub-source path `
  --stub-path publish/micropython-v1_28_0-esp32-esp32_generic-stubs
```

Add `--no-stub-cache` only when uv must ignore its package cache during stub provisioning.

## Cache and replay

Package and catalog responses live under `tests/quality_tests/.ecosystem-cache/`.

| Mode | Behavior |
| --- | --- |
| `use_cache` | Reuse valid entries and fetch anything missing. This is the default. |
| `refresh` | Fetch again and atomically replace matching entries. |
| `offline` | Never use the network; missing entries become `cache_miss`. |

Warm the cache with the normal command or `--refresh`, then rerun the same selection offline:

```powershell
uv run python -m tests.quality_tests.ecosystem.cli `
  --package github:howmanyoliversarethere/micropython-joystick-2-unit `
  --version v1.28.0 `
  --refresh

uv run python -m tests.quality_tests.ecosystem.cli `
  --package github:howmanyoliversarethere/micropython-joystick-2-unit `
  --version v1.28.0 `
  --cache-mode offline
```

`--refresh` and `--cache-mode offline` cannot be combined. For MIM, use `--workers 1` through `16` and `--rate-limit <requests-per-second>` to control upstream traffic.

## Read the result

Package outcomes are:

| Outcome | Meaning |
| --- | --- |
| `pass` | All selected checker runs passed. |
| `type_check_failure` | At least one checker found an error. |
| `skipped` | The package was intentionally not checked, for example because no compatible port was selected. |
| `unsupported` | The source or reference shape is not supported. |
| `unavailable` | Required package, dependency, or cache content could not be obtained. |
| `error` | Setup, provisioning, checker, or internal processing failed. |

Process exit codes summarize the whole invocation:

| Exit | Meaning |
| --- | --- |
| 0 | All selected packages passed or were intentionally skipped. |
| 1 | At least one type-check failure and no operational failure. |
| 2 | An operational failure occurred, including error catalog diagnostics, unavailable content, invalid usage, or no selected package. |

A package can pass while a batch exits 2 because a separate catalog entry failed discovery. Read top-level `catalog_diagnostics` separately from each package `outcome`.

JSON run reports use schema version 2. They include discovery choices, the QA matrix, immutable resolution evidence, package files and dependencies, stub provisioning, checker commands, normalized diagnostics, stage status, counts, timings, and retained workspace evidence.

Text reports print failed checker diagnostics in this form when position data is available:

```text
diagnostic: source/driver.py:12:5: error: diagnostic message
```

Reports redact credentials, sensitive values, file URLs, and unrelated absolute host paths.

## Debug a failure

The default `--retain on_failure` leaves each failed or errored QA workspace in place. Text output prints its usable path:

```text
workspace retained: D:\...\ecosystem-qa-...
```

JSON stores the same path in `retained_workspace`; successful unretained runs store `null`. A retained workspace contains:

```text
source/       resolved package .py files
typings/      selected MicroPython stubs
pyproject.toml and checker configuration
```

Inspect the paths reported by a JSON run in PowerShell:

```powershell
$ReportPath = "tests/quality_tests/.ecosystem-cache/reports/joystick.json"
$Report = Get-Content $ReportPath -Raw | ConvertFrom-Json
$Report.results.reports.retained_workspace | Where-Object { $_ }
```

Start with the first failed result's `diagnostics`, `message`, `typings.command`, and `retained_workspace`. Provisioning errors have a message even when no checker diagnostic exists. After changing stubs or the package selection, rerun the original command; use `--cache-mode offline` when the complete resolution is already cached.

Use `--retain always` to inspect passing workspaces or `--retain never` when no workspace should remain. A retained path is intentionally machine-specific, so review reports before sharing them even though credentials are redacted.

## Aggregate runs

`--report-mode aggregate` combines repeated JSON invocations into one report file. It requires `--report json` and `--report-file`:

```powershell
$Aggregate = "tests/quality_tests/.ecosystem-cache/reports/checkers.json"

uv run python -m tests.quality_tests.ecosystem.cli `
  --package github:howmanyoliversarethere/micropython-joystick-2-unit `
  --version v1.28.0 `
  --checker pyright `
  --report json `
  --report-file $Aggregate `
  --report-mode aggregate

uv run python -m tests.quality_tests.ecosystem.cli `
  --package github:howmanyoliversarethere/micropython-joystick-2-unit `
  --version v1.28.0 `
  --checker mypy `
  --report json `
  --report-file $Aggregate `
  --report-mode aggregate
```

Aggregate reports use schema version 1 and retain each schema-v2 run in invocation order. `run_count` and package outcome `counts` are summed from those runs; aggregate `exit_code` uses the most severe stored exit. A prior single schema-v2 report is promoted on the first aggregate write.

Invalid, incompatible, or internally inconsistent existing files fail without changing the file. Text reports always replace their destination and cannot use aggregate mode. Omit `--report-mode aggregate`, or pass `--report-mode replace`, to replace any existing report atomically.

## Cleanup

Remove retained workspaces but keep downloaded responses:

```powershell
Remove-Item -Recurse -Force tests/quality_tests/.ecosystem-cache/runs -ErrorAction SilentlyContinue
```

Remove generated reports only:

```powershell
Remove-Item -Recurse -Force tests/quality_tests/.ecosystem-cache/reports -ErrorAction SilentlyContinue
```

Reset the complete ecosystem cache:

```powershell
Remove-Item -Recurse -Force tests/quality_tests/.ecosystem-cache -ErrorAction SilentlyContinue
```

The next online run recreates required directories and downloads.

## Troubleshooting

| Symptom | Action |
| --- | --- |
| `cache_miss` in offline mode | Rerun the same selection with `use_cache` or `--refresh`, then retry offline. |
| `Local stub package is unavailable` | Choose a version/portboard present under `publish/`, or use `pypi`, `pypi-pre`, or `path`. |
| `no_compatible_port` | Select a target supported by the package evidence. |
| `no_port_evidence` or `ambiguous_port` | Review the evidence; use `--unknown-policy use_requested` only for an intentional probe. |
| Package passes but the process exits 2 | Inspect top-level catalog diagnostics for a separate discovery failure. |
| MIM requests are slow or rate-limited | Reuse the cache, lower `--workers`, lower `--rate-limit`, or narrow future runs to a focused package. |
| Aggregate file is rejected | Keep the original as evidence and write to a new path, or deliberately replace it without aggregate mode. |
| A failed workspace is missing | Confirm retention was `on_failure` or `always`; `never` removes it. |

## Validate the harness

Run the complete offline harness suite:

```powershell
uv run pytest tests/quality_tests/ecosystem -q
```

Opt into the live network smoke test only when external traffic is intended:

```powershell
$env:MICROPYTHON_STUBS_ECOSYSTEM_NETWORK = "1"
uv run pytest tests/quality_tests/ecosystem -m ecosystem_network -n 0
Remove-Item Env:MICROPYTHON_STUBS_ECOSYSTEM_NETWORK
```

## Maintainer references

Implementation details live beside this guide instead of in the tester workflow:

- [model.py](model.py): normalized identities, resolutions, classifications, and reason codes
- [catalog.py](catalog.py) and [catalog_loader.py](catalog_loader.py): catalog parsing, normalization, and transport
- [resolver.py](resolver.py): bounded package/dependency resolution and cache behavior
- [runner.py](runner.py) and [orchestrator.py](orchestrator.py): isolated QA execution and report construction
- [aggregate.py](aggregate.py): cumulative report validation and metadata
- [classification_overrides.json](classification_overrides.json): reviewed compatibility evidence
- [fixtures/cases.json](fixtures/cases.json): local edge-case corpus
- [pilot_baseline.json](pilot_baseline.json): historical reviewed pilot evidence