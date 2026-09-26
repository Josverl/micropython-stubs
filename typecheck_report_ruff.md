# ruff failures and expected failures

[Back to type checker test report](typecheck_report.md)

<a id="typecheck-detail-ruff-f2abc670c5e7"></a>
## - stdlib stdlib_only - FAIL

**Test specification:**
> pytest tests/quality_tests/test_stdlib_only.py::test_typecheck_stdlib_only[ruff-local-stdlib_only---stdlib]

```text
ruff found 2 errors and 0 warnings in 1 files.
assert 2 == 0

"check_os/check_files.py"(36,19): Avoid equality comparisons to `True`; use `sub:` for truth checks
"check_os/check_files.py"(54,11): Avoid equality comparisons to `True`; use `sub:` for truth checks
```
