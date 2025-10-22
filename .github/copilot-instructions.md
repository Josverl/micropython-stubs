# MicroPython-Stubs Repository Guide

## Project Overview

This repository mostly contains **type stubs**, not executable code. 
It hosts 3,000+ stub files (`.pyi`) for MicroPython across multiple versions (v1.17-v1.27), ports (esp32, rp2, stm32, etc.), and boards. These stubs enable IDE autocomplete, type checking, and documentation for MicroPython development.

**Sister Repository**: [micropython-stubber](https://github.com/Josverl/micropython-stubber) - CLI tool (`stubber`) that generates these stubs.

## Repository Structure

```
stubs/                  # Generated stub files (MCU, frozen, doc, merged)
publish/                # Ready-to-install PyPI packages
  micropython-v1_XX_X-{port}-{board}-stubs/
  micropython-stdlib-stubs/
tools/                  # Tooling (board_compare)
scripts/                # Analysis scripts and notebooks
docs/                   # Sphinx documentation source
data/                   # JSON database files (stub-packages.json)
tests/quality_tests/    # Pytest-based stub quality tests
```

## Key Concepts

### Stub Types (Half-Products)
1. **MCU stubs**: Generated on-device, precise but minimal type info (`stubs/micropython-{version}-{port}[-{board}]`)
2. **Frozen stubs**: From manifest files, includes frozen modules (`stubs/micropython-{version}-Frozen/{port}/{board}`)
3. **Doc stubs**: Parsed from MicroPython `.rst` docs, rich typing (`stubs/micropython-{version}-docstubs`)
4. **Merged stubs**: MCU + Doc, precise + rich (`stubs/micropython-{version}-{port}-merged`)
5. **Core stubs**: Manual overrides for problematic modules (`stubs/micropython-core`)

### Naming Convention
`micropython-{flat_version}-{port}-{board}-stubs` where `flat_version` uses underscores (e.g., `v1_24_1`).

## Development Workflows

### Platform Notes
- **Primary**: Windows 
- **Secondary**: Linux 
- **CI/CD** :GitHub Actions workflows use Ubuntu

### Database

#### `data/all_packages.db`
The project uses a SQLite database (`package_data.db`) to store metadata about packages 
and project hashes to detect if a package has changed since it was last published.

This database is generated and maintained by the `micropython-stubber` tool during the publishing process.
It is checked in to the repository to allow scripts and tools to query package information as it cannot be 
regenerated easily.

The database can be queried, but should not be modified directly.
There is also a JSON export of the database at `data/all_modules.json` which can be used for read-only queries without needing SQLite.


### Database Access - IMPORTANT
**SQLite3 CLI tools are NOT installed.** When working with `package_data.db` or database queries:
- ✅ **USE**: Data Store MCP servers (available in this environment)
- ❌ **AVOID**: Writing one-off SQLite scripts/commands that require debugging
- Alternative: Query `all_modules.json` (JSON export of package data) or `data/stub-packages.json`

### Core Tools

#### The `stubber` CLI
From [micropython-stubber](https://github.com/Josverl/micropython-stubber), installed via pip:
```powershell
pip install micropython-stubber  # or --pre for preview versions
```

**Common Commands**:
```powershell
stubber clone --add-stubs              # Clone micropython + micropython-lib repos
stubber get-docstubs --version v1.24.1 # Generate doc stubs
stubber get-frozen --version v1.24.1   # Generate frozen stubs
stubber merge --version v1.24.1        # Merge MCU + doc stubs
stubber build --version v1.24.1        # Build publishable package
```

#### Update Scripts
- **`update_all_modules.py`**: Regenerates `all_modules.json` from `publish/` packages
- **`docs/update_docs.py`**: Updates documentation files

#### Build/Test Tasks
VSCode tasks (`.vscode/tasks.json`):
- `Sphinx: build documentation` - Default build (Ctrl+Shift+B)
- `Sphinx: clean build documentation`

### Typical Development Flow

1. **Update stubs for a version** (using stubber CLI):
   ```bash
   # example: version =  v1.24.1
   stubber get-docstubs --version v1.24.1
   stubber get-frozen --version v1.24.1
   stubber merge --version v1.24.1 --port rp2 --board rpi_pico
   stubber build --version v1.24.1 --port rp2 --board rpi_pico
   ```

2. **Interactive development** (Jupyter notebooks):
   - `Manual stub build chain.ipynb` - Interactive stub generation workflow
   - `scripts/package_db_to_json.ipynb` - Database export operations
   - `scripts/find_undoc_funcs.ipynb` - Documentation analysis

3. **Test stub quality**:
   ```bash
   pytest tests/quality_tests/ -v
   # Clear cache and retest
   pytest tests/quality_tests/ --cache-clear
   # Test specific version/port
   pytest tests/quality_tests/ -k "v1_24_1 and rp2"
   ```

4. **Update documentation**:
   ```bash
   python docs/update_docs.py
   python update_all_modules.py
   ```

5. **Build docs**:
   Run task: `Sphinx: build documentation`

### GitHub Actions (`.github/workflows/`)
- **`update_stubs.yml`**: Daily stub updates using stubber CLI
- **`test_stub_quality.yml`**: Pyright/mypy validation on snippets (15min runtime)
- **`test_runtime_typing.yml`**: Docker-based runtime tests for typing module
- **`publish_explorer.yml`**: Deploys board explorer app
- **`weekly_automation.yml`**: Maintenance tasks
- **`get-doc-stubs.yml`**: Documentation stub generation
- **`update_docs.yml`**: Sphinx documentation build

## Code Conventions

### Python Style
- **Formatter**: Ruff (line-length: 140) ( black was use - is phased out)
- **Linter**: Ruff (extends Black, adds `PYI` for stubs)
- **Type Checker**: Pyright (primary), mypy (secondary)
- **Target**: Python 3.9+ (stubs must be usable from 3.9)

### Stub-Specific Rules (Ruff)
```toml
# From pyproject.toml - these are EXCEPTIONS for MicroPython stubs:
PYI021 = ignore  # Docstrings ARE included (documentation purpose)
PYI011 = ignore  # Allow complex defaults (MicroPython-specific)
PYI014 = ignore  # Allow actual default values (not just ...)
PYI029 = ignore  # __str__/__repr__ useful for MicroPython
```

### File Organization
- Stubs use `.pyi` extension (type stub files)
- Frozen modules may have `.py` source alongside `.pyi`
- Package structure mirrors MicroPython module hierarchy

## Testing Strategy

All tests must use the pytest framework only.


### Quality Tests (`tests/quality_tests/`)
Integration tests validate stub quality using code snippets and type checkers.

**Test Structure**:
- **Parametrized**: Test across versions/ports/boards
- **Stub sources**: `pypi`, `pypi-pre`, `local` (from `publish/`)
- **Snippet folders**: `feat_*/` and `check_*/` directories with test code
- **Caching**: 24-hour cache for stub packages (speed up test runs)
- **Tools**: Uses `uv pip` for fast isolated installs to `typings/` folders

**What tests validate**:
- Type checker output (pyright, mypy)
- `assert_type` verifies inferred types match expectations
- `# type: ignore` comments with `--warn-unused-ignores` ensure errors are caught
- Idiomatic MicroPython code should pass without type errors

### Running Tests
```bash
# All snippet tests
pytest tests/quality_tests/ -m snippets -v

# Clear cache and retest
pytest tests/quality_tests/ --cache-clear

# Specific version/port combination
pytest tests/quality_tests/ -k "v1_24_1 and rp2"

# Single test file
pytest tests/quality_tests/test_snippets.py::test_pyright[local-v1.20.0-stm32-stdlib]
```

### Docker-Based Testing
Runtime validation uses official MicroPython Docker images:

**Example** (`tests/quality_tests/feat_typing/manual_run.ipynb`):
```python
# Test typing module functionality at runtime
image = "micropython/unix:v1.23.0"
!docker run -u 1000 -v {cwd}:/code --rm {image} micropython list_libs.py
```

**Use cases**:
- Validate typing module behavior
- Test MicroPython-specific functionality
- Cross-platform compatibility checks

### Jupyter Notebooks for Testing
Notebooks provide interactive development and testing workflows:

**Key notebooks**:
- **`Manual stub build chain.ipynb`**: Complete stub generation pipeline
  - Run `stubber docstubs`, `frozen`, `merge`, `build` commands
  - Invalidate pytest cache for testing
  - Publish to PyPI (test/production)
  
- **`tests/quality_tests/feat_typing/manual_run.ipynb`**: Docker test runner
  - Execute MicroPython scripts in containers
  - Validate runtime typing behavior

- **`scripts/package_db_to_json.ipynb`**: Database operations
  - Export package data to JSON
  - Query module information

**Benefits of notebooks**:
- Interactive exploration of stub generation
- Quick iteration on test scenarios
- Visual feedback for analysis tasks
- Cell-by-cell execution for debugging

## Important Files

- **`all_modules.json`**: 112k+ line JSON database of all modules across packages (query this instead of SQLite)
- **`data/stub-packages.json`**: PyPI package metadata
- **`pyproject.toml`**: Dependencies, tool configs (black, ruff, pytest)
- **`pyrightconfig.json`**: Pyright settings for this repo

## Common Pitfalls

1. **Don't edit stubs directly in `stubs/`** - they're generated. Edit sources (docs, frozen, core) or fix generation logic in stubber.

2. **Version format matters**: Use `v1_24_1` (flat) in paths/packages, `v1.24.1` for stubber commands.

3. **Multiple stub packages conflict**: Installing multiple versions overwrites files. Use `--target typings` for isolation.

4. **MCU stubs need hardware**: Generating new MCU stubs requires physical board + firmware flash.

5. **Database queries**: Prefer Data Store MCP tools or JSON files over SQLite CLI (not installed).

## Documentation

- **Read the Docs**: https://micropython-stubs.readthedocs.io/
- **Board Explorer**: https://josverl.github.io/micropython-stubs/board-explorer-mpy.html
- **Key docs**:
  - `docs/10_introduction.md` - Stub purpose and benefits
  - `docs/stub_types.md` - Stub generation methods
  - `docs/diy_stubs_files.md` - Creating custom stubs

## IDE Integration

Stubs are PEP 561 stub-only packages installed via pip:
```bash
pip install micropython-rp2-stubs --target ./typings --no-user
```

Configure IDE to use `./typings` as extra paths for type checking (see `docs/22_vscode.md`, `docs/24_pycharm.md`).

## Publishing

Packages published to PyPI follow naming: `micropython-{port}-stubs` or `micropython-{port}-{board}-stubs`.

Version scheme: `{mpy_version}.post{N}` (e.g., `1.24.1.post1` for first stub update of MicroPython 1.24.1).
