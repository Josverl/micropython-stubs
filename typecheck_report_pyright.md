# pyright failures and expected failures

[Back to type checker test report](typecheck_report.md)

<a id="typecheck-detail-pyright-1fa048b7f28a"></a>
## v1.29.0 webassembly webassembly - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-webassembly-webassembly-pyright]

```text
pyright found 15 errors and 0 warnings in 15 files.
assert 15 == 0

"check_pyscript/check_config.py"(8,20): No parameter named "target"
"check_pyscript/check_config.py"(8,36): No parameter named "append"
"check_pyscript/check_html.py"(11,37): No parameter named "target"
"check_pyscript/check_html.py"(29,3): Cannot assign to attribute "onopen" for class "WebSocket"
  Attribute "onopen" is unknown
"check_pyscript/check_html.py"(30,3): Cannot assign to attribute "onmessage" for class "WebSocket"
  Attribute "onmessage" is unknown
"check_pyscript/check_html.py"(31,3): Cannot assign to attribute "onclose" for class "WebSocket"
  Attribute "onclose" is unknown
"check_pyscript/check_pyworker.py"(5,23): No parameter named "target"
"check_pyscript/check_pyworker.py"(5,40): No parameter named "append"
"check_pyscript/check_when.py"(10,15): Expected 1 positional argument
"check_pyscript/check_when.py"(18,15): Expected 1 positional argument
"check_pyscript/check_when.py"(28,14): Expected 1 positional argument
"check_pyscript/check_workers.py"(6,19): Arguments missing for parameters "x2", "x3"
"check_pyscript/check_workers.py"(6,68): No parameter named "type"
```

2 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

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

<a id="typecheck-detail-pyright-5313c9f7e03e"></a>
## v1.28.0 esp32 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-networking-pyright]

```text
pyright found 1 errors and 0 warnings in 13 files.
assert 1 == 0
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

<a id="typecheck-detail-pyright-0d147449ab85"></a>
## v1.28.0 esp32-esp32_generic_c6 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-networking-pyright]

```text
pyright found 1 errors and 0 warnings in 13 files.
assert 1 == 0
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

<a id="typecheck-detail-pyright-d2648bdabab5"></a>
## v1.28.0 esp32-esp32_generic_s3 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-networking-pyright]

```text
pyright found 1 errors and 0 warnings in 13 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-pyright-6128ab2c941d"></a>
## v1.28.0 esp8266 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp8266-networking-pyright]

```text
pyright found 1 errors and 0 warnings in 13 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-pyright-b8baf368ed8a"></a>
## v1.28.0 rp2-rpi_pico2_w networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-networking-pyright]

```text
pyright found 1 errors and 0 warnings in 13 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-pyright-fe8fdebae595"></a>
## v1.28.0 rp2-rpi_pico_w networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-networking-pyright]

```text
pyright found 1 errors and 0 warnings in 13 files.
assert 1 == 0
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
"check_pyscript/check_modules.py"(18,58): No parameter named "indent"
"check_pyscript/check_web.py"(53,4): "__delitem__" method not defined on type "Style"
"check_pyscript/check_web.py"(55,15): Cannot access attribute "discard" for class "Classes"
  Attribute "discard" is unknown
```

2 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

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

<a id="typecheck-detail-pyright-1171d6c03212"></a>
## v1.27.0 esp32 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-networking-pyright]

```text
pyright found 1 errors and 0 warnings in 13 files.
assert 1 == 0
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

<a id="typecheck-detail-pyright-12fdaba458c1"></a>
## v1.27.0 esp32-esp32_generic_c6 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-networking-pyright]

```text
pyright found 1 errors and 0 warnings in 13 files.
assert 1 == 0
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

<a id="typecheck-detail-pyright-3f8436d7c2a8"></a>
## v1.27.0 esp32-esp32_generic_s3 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-networking-pyright]

```text
pyright found 1 errors and 0 warnings in 13 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-pyright-f75d203219e0"></a>
## v1.27.0 esp8266 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp8266-networking-pyright]

```text
pyright found 1 errors and 0 warnings in 13 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-pyright-ba7d86d2eee0"></a>
## v1.27.0 rp2-rpi_pico2_w networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-networking-pyright]

```text
pyright found 1 errors and 0 warnings in 13 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-pyright-4e154065a691"></a>
## v1.27.0 rp2-rpi_pico_w networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-networking-pyright]

```text
pyright found 1 errors and 0 warnings in 13 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

## Shared diagnostics

```text
"check_espnow.py"(53,8): Cannot access attribute "peers_table" for class "ESPNow" (Reported by 6 tests)
"check_pyscript/check_ffi_storage.py"(23,4): "__setitem__" method not defined on type "Preferences" (Reported by 2 tests)
"check_pyscript/check_modules.py"(16,22): Expected 0 positional arguments (Reported by 2 tests)
"check_socket.py"(19,12): "assert_type" mismatch: expected "bytes" but received "Unknown" (Reported by 12 tests)
```
