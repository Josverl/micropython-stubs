# Ruff Linter Integration Summary

## Overview
This implementation adds Ruff as a third linter for checking MicroPython stubs, alongside Pyright and MyPy.

## Changes Made

### 1. Dependencies
- Added `ruff` to `pyproject.toml` test dependencies
- Added `ruff` to `requirements-test.txt`

### 2. Core Implementation
- **`tests/quality_tests/typecheck_ruff.py`**: New module implementing ruff checking with pyright-compatible output format
  - Converts ruff JSON output to pyright format for consistency
  - Supports the same error filtering mechanism as other linters
  
- **`tests/quality_tests/typecheck.py`**: Updated to support ruff as a linter option
  - Added import for `check_with_ruff`
  - Added ruff case in `run_typechecker` function

### 3. Test Files
- **`tests/quality_tests/test_ruff.py`**: Dedicated test file for ruff (following test_mypy.py pattern)
- **`tests/quality_tests/test_snippets.py`**: Added "ruff" to linter parametrization
- **`tests/quality_tests/feat_ruff/`**: Created test directory with sample files

### 4. Configuration
- **`pyproject.toml`**: Enhanced ruff configuration
  - Enabled PYI (flake8-pyi) rules for stub-specific linting
  - Added appropriate ignores for MicroPython stub characteristics:
    - PYI021: Allow docstrings in stubs
    - PYI044: Allow `from __future__ import annotations`
    - PYI048: Allow multiple statements in function bodies (for docstrings)
    - PYI011/PYI014: Allow complex default values
    - PYI029: Allow `__str__` and `__repr__` definitions

- **`tests/quality_tests/_configs/pyproject.toml`**: Added ruff configuration for test directories

### 5. Documentation
- **`docs/29_ruff.md`**: Comprehensive documentation covering:
  - Why use Ruff with MicroPython stubs
  - Installation instructions
  - Configuration examples
  - Usage guide
  - IDE integration
  - Comparison with other linters
  
- **`docs/index.md`**: Added ruff documentation to the table of contents
- **`README.md`**: Added Ruff badge

## Testing
✅ Ruff runs successfully on stub files
✅ Configuration correctly ignores MicroPython-specific patterns
✅ Integration with typecheck infrastructure works
✅ Module can be imported and used standalone

## Benefits
1. **Speed**: Ruff is 10-100x faster than traditional Python linters
2. **Stub-aware**: Built-in flake8-pyi rules catch stub-specific issues
3. **Comprehensive**: 800+ rules covering code quality, style, and best practices
4. **Consistent**: Uses same error reporting format as other linters in the test suite

## Usage

### Command Line
```bash
# Check stub files
ruff check stubs/micropython-preview-docstubs/

# Check with fixes
ruff check --fix stubs/

# Format code
ruff format .
```

### In Test Suite
Ruff is automatically included when running the snippet tests:
```bash
pytest -m snippets
```

## Future Enhancements
- Consider running ruff in CI/CD pipeline
- Add ruff-specific test cases for edge cases
- Potentially use ruff's auto-fix capabilities in development workflow
