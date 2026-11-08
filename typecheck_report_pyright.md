# pyright failures and expected failures

[Back to type checker test report](typecheck_report.md)

<a id="typecheck-detail-pyright-e73a404760cb"></a>
## v1.28.0 esp32 espnow - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-espnow-pyright]

```text
pyright found 1 errors and 0 warnings in 8 files.
assert 1 == 0

  Attribute "peers_table" is unknown
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-pyright-44b74672b0e6"></a>
## v1.28.0 esp32-esp32_generic_c6 espnow - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-espnow-pyright]

```text
pyright found 1 errors and 0 warnings in 8 files.
assert 1 == 0

  Attribute "peers_table" is unknown
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-pyright-421be3f954b0"></a>
## v1.28.0 esp32-esp32_generic_s3 espnow - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-espnow-pyright]

```text
pyright found 1 errors and 0 warnings in 8 files.
assert 1 == 0

  Attribute "peers_table" is unknown
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-pyright-0d71cbf91bee"></a>
## v1.28.0 webassembly webassembly - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-webassembly-webassembly-pyright]

```text
pyright found 8 errors and 0 warnings in 15 files.
assert 8 == 0

"check_pyscript/check_config.py"(3,5): Import "pyscript.context" could not be resolved
"check_pyscript/check_ffi_storage.py"(22,31): Type "Storage" is not assignable to declared type "Preferences"
  "Storage" is not assignable to "Preferences"
"check_pyscript/check_ffi_storage.py"(22,60): Argument of type "type[Preferences]" cannot be assigned to parameter "storage_class" of type "type[Storage]" in function "storage"
  "type[Preferences]" is not assignable to "type[Storage]"
  Type "type[Preferences]" is not assignable to type "type[Storage]"
"check_pyscript/check_ffi_storage.py"(23,4): "__setitem__" method not defined on type "Preferences"
"check_pyscript/check_modules.py"(16,22): Expected 0 positional arguments
"check_pyscript/check_modules.py"(18,58): No parameter named "indent"
"check_pyscript/check_web.py"(53,4): "__delitem__" method not defined on type "Style"
"check_pyscript/check_web.py"(55,15): Cannot access attribute "discard" for class "Classes"
  Attribute "discard" is unknown
```

<a id="typecheck-detail-pyright-43b6de36cfd8"></a>
## v1.27.0 esp32 espnow - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-espnow-pyright]

```text
pyright found 1 errors and 0 warnings in 8 files.
assert 1 == 0

  Attribute "peers_table" is unknown
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-pyright-7483e16d975b"></a>
## v1.27.0 esp32-esp32_generic_c6 espnow - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-espnow-pyright]

```text
pyright found 1 errors and 0 warnings in 8 files.
assert 1 == 0

  Attribute "peers_table" is unknown
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-pyright-b7caade69be8"></a>
## v1.27.0 esp32-esp32_generic_s3 espnow - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-espnow-pyright]

```text
pyright found 1 errors and 0 warnings in 8 files.
assert 1 == 0

  Attribute "peers_table" is unknown
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

## Shared diagnostics

```text
"check_espnow.py"(55,8): Cannot access attribute "peers_table" for class "ESPNow" (Reported by 6 tests)
```
