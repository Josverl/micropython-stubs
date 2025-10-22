(ruff_config)=
# Linting with Ruff

Ruff is an extremely fast Python linter and code formatter written in Rust. It can replace multiple tools including Flake8, isort, and more. For MicroPython stubs, ruff provides stub-specific linting through its built-in `flake8-pyi` plugin.

## Why use Ruff with MicroPython stubs?

- **Fast**: Ruff is 10-100x faster than other Python linters
- **Comprehensive**: Includes 800+ rules from popular linters
- **Stub-aware**: Built-in support for `.pyi` stub file linting via flake8-pyi rules
- **Easy to configure**: Single configuration file in `pyproject.toml`

## Installation

Install ruff using pip:

```bash
pip install ruff
```

Or add it to your `pyproject.toml`:

```toml
[project.optional-dependencies]
test = [
    "ruff",
    # ... other test dependencies
]
```

## Configuration

Ruff can be configured in your `pyproject.toml` file. For MicroPython stubs, we enable the PYI (flake8-pyi) rules for stub-specific checking:

```toml
[tool.ruff]
line-length = 140
target-version = "py39"

[tool.ruff.lint]
extend-select = [
    "PYI", # flake8-pyi - stub file specific checks
]
ignore = [
    "F401",   # unused import
    "F403",   # import *
    "F821",   # undefined name (can occur in stubs)
    "E402",   # module level import not at top of file - common in test snippets
    "PYI021", # Docstrings should not be included in stubs (but we want them for MicroPython)
    "PYI044", # `from __future__ import annotations` - used in generated stubs
    "PYI048", # Function body must contain exactly one statement - docstrings count
    "PYI011", # Only simple default values allowed for typed arguments - we want actual defaults
    "PYI014", # Only simple default values allowed for arguments - we want actual defaults
    "PYI029", # __str__ and __repr__ are useful in MicroPython stubs
]
```

## Running Ruff

### Check your code

```bash
# Check a single file
ruff check my_file.py

# Check a directory
ruff check src/

# Check with automatic fixes
ruff check --fix src/
```

### Format your code

Ruff can also format your code (similar to Black):

```bash
# Format a file
ruff format my_file.py

# Format a directory
ruff format src/
```

### Check stub files

To check MicroPython stub files:

```bash
# Check a specific stub directory
ruff check stubs/micropython-v1_24_1-esp32-stubs/

# Check all stubs
ruff check stubs/
```

## Integration with the test suite

The MicroPython stubs project includes ruff as one of the linters in the quality test suite. When running tests, ruff will automatically check code snippets and stub files for quality issues.

## IDE Integration

Most modern Python IDEs support Ruff:

### VS Code

Install the Ruff extension from the VS Code marketplace:
- Extension ID: `charliermarsh.ruff`

Configure in `.vscode/settings.json`:
```json
{
    "[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll": true,
            "source.organizeImports": true
        },
        "editor.defaultFormatter": "charliermarsh.ruff"
    }
}
```

### PyCharm

PyCharm supports Ruff through the external tools configuration or via plugins from the JetBrains marketplace.

## Comparison with other linters

For MicroPython stubs, we use multiple complementary linters:
- **Pyright**: Type checking and type inference
- **MyPy**: Alternative type checker with different semantics
- **Ruff**: Fast linting including stub-specific rules

Each serves a different purpose:
- Pyright/MyPy focus on type correctness
- Ruff focuses on code quality, style, and stub-specific best practices

## Further reading

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Ruff rules reference](https://docs.astral.sh/ruff/rules/)
- [flake8-pyi rules](https://docs.astral.sh/ruff/rules/#flake8-pyi-pyi)
