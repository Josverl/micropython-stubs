# mypy failures and expected failures

[Back to type checker test report](typecheck_report.md)

<a id="typecheck-detail-mypy-6f7045ba54ea"></a>
## v1.28.0 esp32 espnow - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-espnow-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-3bebe7e67a81"></a>
## v1.28.0 esp32 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-networking-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-db019f0fe5c8"></a>
## v1.28.0 esp32-esp32_generic_c6 espnow - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-espnow-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-5403956fde1f"></a>
## v1.28.0 esp32-esp32_generic_c6 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-networking-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-f2ad3fd93473"></a>
## v1.28.0 esp32-esp32_generic_s3 espnow - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-espnow-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-2e709d33356f"></a>
## v1.28.0 esp32-esp32_generic_s3 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-networking-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-6dfe5108f536"></a>
## v1.28.0 esp8266 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp8266-networking-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-7ef5e0bdcac4"></a>
## v1.28.0 rp2-rpi_pico2_w networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-networking-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-bf9889fab817"></a>
## v1.28.0 rp2-rpi_pico_w networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-networking-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-a4aaf11c99e5"></a>
## v1.28.0 webassembly webassembly - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-webassembly-webassembly-mypy]

```text
mypy found 7 errors and 0 warnings in 0 files.
assert 6 == 0

"check_pyscript/check_modules.py"(18,0): Unexpected keyword argument "indent" for "stringify"
"stringify" defined in "pyscript.flatted"
"check_pyscript/check_ffi_storage.py"(22,0): Argument 2 to "storage" has incompatible type "type[Preferences]"; expected "type[Storage]"
"check_pyscript/check_ffi_storage.py"(23,0): Unsupported target for indexed assignment ("Preferences")
"check_pyscript/check_config.py"(3,0): Cannot find implementation or library stub for module named "pyscript.context"
See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
"check_pyscript/check_web.py"(53,0): "Style" has no attribute "__delitem__"; maybe "__getitem__" or "__setitem__"?
"check_pyscript/check_web.py"(55,0): "Classes" has no attribute "discard"
```

<a id="typecheck-detail-mypy-fa0a30f2bd9d"></a>
## v1.27.0 esp32 espnow - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-espnow-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-aacc843a49ac"></a>
## v1.27.0 esp32 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-networking-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-82f8c7957d76"></a>
## v1.27.0 esp32-esp32_generic_c6 espnow - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-espnow-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-1c850ac5bd5f"></a>
## v1.27.0 esp32-esp32_generic_c6 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-networking-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-eb5db22bfe1b"></a>
## v1.27.0 esp32-esp32_generic_s3 espnow - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-espnow-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-37d0cd6cf15b"></a>
## v1.27.0 esp32-esp32_generic_s3 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-networking-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-7add3893d207"></a>
## v1.27.0 esp8266 networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp8266-networking-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-ae9878e898f7"></a>
## v1.27.0 rp2-rpi_pico2_w networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-networking-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-mypy-87843aaec01c"></a>
## v1.27.0 rp2-rpi_pico_w networking - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-networking-mypy]

```text
mypy found 1 errors and 0 warnings in 0 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

## Shared diagnostics

```text
"check_espnow.py"(53,0): "ESPNow" has no attribute "peers_table" (Reported by 6 tests)
"check_socket.py"(19,0): Expression is of type "Any", not "bytes" (Reported by 12 tests)
```
