# ty failures and expected failures

[Back to type checker test report](typecheck_report.md)

<a id="typecheck-detail-ty-ca5f102067e3"></a>
## - stdlib stdlib_only - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_stdlib_only.py::test_typecheck_stdlib_only[ty-local-stdlib_only---stdlib]

```text
ty found 10 errors and 1 warnings in 3 files.
assert 10 == 0

"check_io.py"(12,29): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"check_ssl.py"(48,24): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"check_ssl.py"(48,44): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"check_ssl.py"(48,55): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
"check_sys/check_stdio.py"(6,0): no-matching-overload: No overload of bound method `IO.write` matches arguments
"check_sys/check_stdio.py"(11,0): no-matching-overload: No overload of bound method `IO.write` matches arguments
"check_sys/check_stdio.py"(28,15): unresolved-attribute: Attribute `readinto` is not defined on `BinaryIO` in union `BinaryIO | Any`
"check_sys/check_stdio.py"(33,20): unresolved-attribute: Attribute `readinto` is not defined on `BinaryIO` in union `BinaryIO | Any`
"check_sys/check_stdio.py"(41,8): no-matching-overload: No overload of bound method `IO.write` matches arguments
"check_sys/check_stdio.py"(42,8): unresolved-attribute: Attribute `readinto` is not defined on `BinaryIO` in union `BinaryIO | Any`
"check_sys/check_stdio.py"(43,8): unresolved-attribute: Attribute `readinto` is not defined on `BinaryIO` in union `BinaryIO | Any`
```

<a id="typecheck-detail-ty-3cceaf1f077c"></a>
## v1.29.0 esp32 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-348035a3ce4d"></a>
## v1.29.0 esp32 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-bluetooth-ty]

```text
ty found 10 errors and 1 warnings in 8 files.
assert 10 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-f145429371c4"></a>
## v1.29.0 esp32 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32-ty]

```text
ty found 3 errors and 4 warnings in 2 files.
assert 3 == 0
```

7 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-53c8d4773419"></a>
## v1.29.0 esp32 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-espnow-ty]

```text
ty found 3 errors and 1 warnings in 2 files.
assert 3 == 0
```

4 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-8df47c05d5f8"></a>
## v1.29.0 esp32 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-micropython-ty]

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-4d03a823d9c3"></a>
## v1.29.0 esp32 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-networking-ty]

```text
ty found 4 errors and 7 warnings in 4 files.
assert 4 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-c91e7751c088"></a>
## v1.29.0 esp32 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-135acccd1e2e"></a>
## v1.29.0 esp32-esp32_generic_c6 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-2f69e3102b4a"></a>
## v1.29.0 esp32-esp32_generic_c6 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-bluetooth-ty]

```text
ty found 10 errors and 1 warnings in 8 files.
assert 10 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-3636e15d0f51"></a>
## v1.29.0 esp32-esp32_generic_c6 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-esp32-ty]

```text
ty found 6 errors and 4 warnings in 4 files.
assert 3 == 0
```

6 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-572896766017"></a>
## v1.29.0 esp32-esp32_generic_c6 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-espnow-ty]

```text
ty found 3 errors and 1 warnings in 2 files.
assert 3 == 0
```

4 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-bc3654cc236a"></a>
## v1.29.0 esp32-esp32_generic_c6 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-micropython-ty]

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-98d9afc44aa5"></a>
## v1.29.0 esp32-esp32_generic_c6 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-networking-ty]

```text
ty found 4 errors and 7 warnings in 4 files.
assert 4 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-6909a76f92f9"></a>
## v1.29.0 esp32-esp32_generic_c6 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-5fa7a8ff91c2"></a>
## v1.29.0 esp32-esp32_generic_s3 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-c0eb20268d4e"></a>
## v1.29.0 esp32-esp32_generic_s3 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-bluetooth-ty]

```text
ty found 10 errors and 1 warnings in 8 files.
assert 10 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-30f9263e0d0e"></a>
## v1.29.0 esp32-esp32_generic_s3 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-esp32-ty]

```text
ty found 4 errors and 4 warnings in 3 files.
assert 3 == 0
```

6 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-3d29f56d4e66"></a>
## v1.29.0 esp32-esp32_generic_s3 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-espnow-ty]

```text
ty found 3 errors and 1 warnings in 2 files.
assert 3 == 0
```

4 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-1647080b5459"></a>
## v1.29.0 esp32-esp32_generic_s3 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-micropython-ty]

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-594e82be2737"></a>
## v1.29.0 esp32-esp32_generic_s3 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-networking-ty]

```text
ty found 4 errors and 7 warnings in 4 files.
assert 4 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-7122d929796c"></a>
## v1.29.0 esp32-esp32_generic_s3 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-271cd8b86577"></a>
## v1.29.0 esp8266 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp8266-micropython-ty]

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-3a2fcf5232ef"></a>
## v1.29.0 esp8266 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp8266-networking-ty]

```text
ty found 4 errors and 7 warnings in 4 files.
assert 4 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-11176c683854"></a>
## v1.29.0 esp8266 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp8266-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-e5371b325318"></a>
## v1.29.0 rp2 asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-asm_pio-ty]

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-62075a18b4ec"></a>
## v1.29.0 rp2 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-09f6f0e2a242"></a>
## v1.29.0 rp2 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-micropython-ty]

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-08b1d7c3d3cf"></a>
## v1.29.0 rp2 rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rp2-ty]

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0
```

8 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-5a13d8e658d7"></a>
## v1.29.0 rp2 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-dd7ee0f13b16"></a>
## v1.29.0 rp2-rpi_pico asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-asm_pio-ty]

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-84bac47a77de"></a>
## v1.29.0 rp2-rpi_pico asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-f7ad84e3fb3d"></a>
## v1.29.0 rp2-rpi_pico micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-micropython-ty]

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-80615def3cb4"></a>
## v1.29.0 rp2-rpi_pico rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-rp2-ty]

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0
```

8 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-a9cafbf6429d"></a>
## v1.29.0 rp2-rpi_pico stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-d1c433596264"></a>
## v1.29.0 rp2-rpi_pico2 asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-asm_pio-ty]

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-2728d14a98ae"></a>
## v1.29.0 rp2-rpi_pico2 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-ae72db2b19ed"></a>
## v1.29.0 rp2-rpi_pico2 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-micropython-ty]

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-c37faaf2402e"></a>
## v1.29.0 rp2-rpi_pico2 rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-rp2-ty]

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0
```

8 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-61300be3ac3f"></a>
## v1.29.0 rp2-rpi_pico2 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-70aa8e4f3b7a"></a>
## v1.29.0 rp2-rpi_pico2_w asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-asm_pio-ty]

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-4113fb6d5a36"></a>
## v1.29.0 rp2-rpi_pico2_w asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-2ec44712092c"></a>
## v1.29.0 rp2-rpi_pico2_w micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-micropython-ty]

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-1d2daa7938a7"></a>
## v1.29.0 rp2-rpi_pico2_w networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-networking-ty]

```text
ty found 4 errors and 7 warnings in 4 files.
assert 4 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-a8cd1e706df5"></a>
## v1.29.0 rp2-rpi_pico2_w rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-rp2-ty]

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0
```

8 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-e0de2afa46ce"></a>
## v1.29.0 rp2-rpi_pico2_w stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-ca428241d499"></a>
## v1.29.0 rp2-rpi_pico_w aioble - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-aioble-ty]

```text
ty found 12 errors and 0 warnings in 9 files.
assert 11 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-6decd13a4df1"></a>
## v1.29.0 rp2-rpi_pico_w asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-asm_pio-ty]

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-2ea9f3a6c423"></a>
## v1.29.0 rp2-rpi_pico_w asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-328672f30765"></a>
## v1.29.0 rp2-rpi_pico_w bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-bluetooth-ty]

```text
ty found 10 errors and 1 warnings in 8 files.
assert 9 == 0
```

10 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-4028b26ebea6"></a>
## v1.29.0 rp2-rpi_pico_w micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-micropython-ty]

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-1b7bd7a8b45d"></a>
## v1.29.0 rp2-rpi_pico_w networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-networking-ty]

```text
ty found 4 errors and 7 warnings in 4 files.
assert 4 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-6eb3effd45a5"></a>
## v1.29.0 rp2-rpi_pico_w rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-rp2-ty]

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0
```

8 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-d89d363a4003"></a>
## v1.29.0 rp2-rpi_pico_w stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-073ff6324364"></a>
## v1.29.0 samd asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-6bc262ee1cd2"></a>
## v1.29.0 samd micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-micropython-ty]

```text
ty found 21 errors and 2 warnings in 4 files.
assert 18 == 0
```

20 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-7bd9c87d6249"></a>
## v1.29.0 samd stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-1c0e835245b6"></a>
## v1.29.0 samd-seeed_wio_terminal asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-seeed_wio_terminal-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-918d20107591"></a>
## v1.29.0 samd-seeed_wio_terminal micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-seeed_wio_terminal-micropython-ty]

```text
ty found 21 errors and 2 warnings in 4 files.
assert 18 == 0
```

20 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-36ef4ca58f5e"></a>
## v1.29.0 samd-seeed_wio_terminal stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-seeed_wio_terminal-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-75763f53fe6f"></a>
## v1.29.0 stm32 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-fb90518fe573"></a>
## v1.29.0 stm32 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-micropython-ty]

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-9905cf0ff099"></a>
## v1.29.0 stm32 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-42739240d0a8"></a>
## v1.29.0 stm32-pybv11 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-pybv11-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-3db3889bc258"></a>
## v1.29.0 stm32-pybv11 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-pybv11-micropython-ty]

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-2acaae7c81e4"></a>
## v1.29.0 stm32-pybv11 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-pybv11-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-40ba38b843d6"></a>
## v1.29.0 unix asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-unix-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-7145b8712d99"></a>
## v1.29.0 unix micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-unix-micropython-ty]

```text
ty found 22 errors and 2 warnings in 5 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-c145fe273b4b"></a>
## v1.29.0 unix stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-unix-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-3267e5b12640"></a>
## v1.29.0 webassembly micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-webassembly-micropython-ty]

```text
ty found 22 errors and 2 warnings in 5 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-2d22baf13466"></a>
## v1.29.0 webassembly stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-webassembly-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-4379a2376c42"></a>
## v1.29.0 webassembly webassembly - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-webassembly-webassembly-ty]

```text
ty found 15 errors and 0 warnings in 7 files.
assert 15 == 0

"check_pyscript/check_config.py"(8,20): unknown-argument: Argument `target` does not match any known parameter of function `display`
"check_pyscript/check_config.py"(8,36): unknown-argument: Argument `append` does not match any known parameter of function `display`
"check_pyscript/check_html.py"(11,37): unknown-argument: Argument `target` does not match any known parameter of function `display`
"check_pyscript/check_html.py"(29,0): unresolved-attribute: Unresolved attribute `onopen` on type `WebSocket`
"check_pyscript/check_html.py"(30,0): unresolved-attribute: Unresolved attribute `onmessage` on type `WebSocket`
"check_pyscript/check_html.py"(31,0): unresolved-attribute: Unresolved attribute `onclose` on type `WebSocket`
"check_pyscript/check_pyworker.py"(5,23): unknown-argument: Argument `target` does not match any known parameter of function `display`
"check_pyscript/check_pyworker.py"(5,40): unknown-argument: Argument `append` does not match any known parameter of function `display`
"check_pyscript/check_when.py"(10,15): too-many-positional-arguments: Too many positional arguments to function `when`: expected 1, got 2
"check_pyscript/check_when.py"(18,15): too-many-positional-arguments: Too many positional arguments to function `when`: expected 1, got 2
"check_pyscript/check_when.py"(28,14): too-many-positional-arguments: Too many positional arguments to function `when`: expected 1, got 2
"check_pyscript/check_workers.py"(6,19): missing-argument: No arguments provided for required parameters `x2`, `x3` of function `create_named_worker`
"check_pyscript/check_workers.py"(6,68): unknown-argument: Argument `type` does not match any known parameter of function `create_named_worker`
```

2 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-16ea3ca16cef"></a>
## v1.29.0 windows asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-windows-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-18163d6a0ffe"></a>
## v1.29.0 windows micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-windows-micropython-ty]

```text
ty found 22 errors and 2 warnings in 5 files.
assert 21 == 0
```

23 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-ce3f92c06743"></a>
## v1.29.0 windows stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-windows-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-0612fe019a9c"></a>
## v1.28.0 esp32 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-cd1e4217bd44"></a>
## v1.28.0 esp32 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-bluetooth-ty]

```text
ty found 10 errors and 1 warnings in 8 files.
assert 10 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-e02cacffbcbc"></a>
## v1.28.0 esp32 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32-ty]

```text
ty found 3 errors and 4 warnings in 2 files.
assert 3 == 0
```

7 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-e2929b3ba323"></a>
## v1.28.0 esp32 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-espnow-ty]

```text
ty found 3 errors and 1 warnings in 2 files.
assert 3 == 0
```

4 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-20c6336eaa40"></a>
## v1.28.0 esp32 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-a479cb7ca7e6"></a>
## v1.28.0 esp32 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-networking-ty]

```text
ty found 5 errors and 7 warnings in 5 files.
assert 5 == 0
```

12 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-762332d3dce4"></a>
## v1.28.0 esp32 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-df3a02a8b88b"></a>
## v1.28.0 esp32-esp32_generic_c6 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-0a564935ed4c"></a>
## v1.28.0 esp32-esp32_generic_c6 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-bluetooth-ty]

```text
ty found 10 errors and 1 warnings in 8 files.
assert 10 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-c6cb82bfc417"></a>
## v1.28.0 esp32-esp32_generic_c6 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-esp32-ty]

```text
ty found 6 errors and 4 warnings in 4 files.
assert 3 == 0
```

6 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-17c18666e24b"></a>
## v1.28.0 esp32-esp32_generic_c6 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-espnow-ty]

```text
ty found 3 errors and 1 warnings in 2 files.
assert 3 == 0
```

4 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-611705b31e71"></a>
## v1.28.0 esp32-esp32_generic_c6 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-04be44620d7d"></a>
## v1.28.0 esp32-esp32_generic_c6 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-networking-ty]

```text
ty found 5 errors and 7 warnings in 5 files.
assert 5 == 0
```

12 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-ade6a494018f"></a>
## v1.28.0 esp32-esp32_generic_c6 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-21a1122455c5"></a>
## v1.28.0 esp32-esp32_generic_s3 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-18977a023b11"></a>
## v1.28.0 esp32-esp32_generic_s3 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-bluetooth-ty]

```text
ty found 10 errors and 1 warnings in 8 files.
assert 10 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-c4a28bf6914c"></a>
## v1.28.0 esp32-esp32_generic_s3 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-esp32-ty]

```text
ty found 4 errors and 4 warnings in 3 files.
assert 3 == 0
```

6 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-68af08d576fa"></a>
## v1.28.0 esp32-esp32_generic_s3 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-espnow-ty]

```text
ty found 3 errors and 1 warnings in 2 files.
assert 3 == 0
```

4 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-323193eb9810"></a>
## v1.28.0 esp32-esp32_generic_s3 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-3a0af584a442"></a>
## v1.28.0 esp32-esp32_generic_s3 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-networking-ty]

```text
ty found 5 errors and 7 warnings in 5 files.
assert 5 == 0
```

12 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-a97892484427"></a>
## v1.28.0 esp32-esp32_generic_s3 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-457ec0b74b8e"></a>
## v1.28.0 esp8266 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp8266-micropython-ty]

```text
ty found 29 errors and 2 warnings in 6 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-ed9208ef9165"></a>
## v1.28.0 esp8266 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp8266-networking-ty]

```text
ty found 5 errors and 7 warnings in 5 files.
assert 5 == 0
```

12 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-ad9278b5abe6"></a>
## v1.28.0 esp8266 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp8266-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-c82030d5044d"></a>
## v1.28.0 rp2 asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-asm_pio-ty]

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-9198c67ebc6d"></a>
## v1.28.0 rp2 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-b005461e577b"></a>
## v1.28.0 rp2 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-82f4c0d25571"></a>
## v1.28.0 rp2 rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rp2-ty]

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0
```

8 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-bfc11448ec64"></a>
## v1.28.0 rp2 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-4a17af158054"></a>
## v1.28.0 rp2-rpi_pico asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico-asm_pio-ty]

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-763c2eb3ff92"></a>
## v1.28.0 rp2-rpi_pico asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-db89d75ecc9b"></a>
## v1.28.0 rp2-rpi_pico micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-2ddec4849921"></a>
## v1.28.0 rp2-rpi_pico rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico-rp2-ty]

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0
```

8 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-61d9bef01cec"></a>
## v1.28.0 rp2-rpi_pico stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-334f4590de1e"></a>
## v1.28.0 rp2-rpi_pico2 asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2-asm_pio-ty]

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-7f2cab394487"></a>
## v1.28.0 rp2-rpi_pico2 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-293d0885310b"></a>
## v1.28.0 rp2-rpi_pico2 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-48126ab46bbc"></a>
## v1.28.0 rp2-rpi_pico2 rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2-rp2-ty]

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0
```

8 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-3689b3ab8318"></a>
## v1.28.0 rp2-rpi_pico2 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-a715e7d8b518"></a>
## v1.28.0 rp2-rpi_pico2_w asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-asm_pio-ty]

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-db91ef32ac8e"></a>
## v1.28.0 rp2-rpi_pico2_w asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-99708c317e21"></a>
## v1.28.0 rp2-rpi_pico2_w micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-421d9b2685ba"></a>
## v1.28.0 rp2-rpi_pico2_w networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-networking-ty]

```text
ty found 5 errors and 7 warnings in 5 files.
assert 5 == 0
```

12 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-9e8cc463a2f3"></a>
## v1.28.0 rp2-rpi_pico2_w rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-rp2-ty]

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0
```

8 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-126d86acef65"></a>
## v1.28.0 rp2-rpi_pico2_w stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-5dd0e57a2b5f"></a>
## v1.28.0 rp2-rpi_pico_w aioble - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-aioble-ty]

```text
ty found 12 errors and 0 warnings in 9 files.
assert 11 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-11c150b240e7"></a>
## v1.28.0 rp2-rpi_pico_w asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-asm_pio-ty]

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-da02b7cdabb1"></a>
## v1.28.0 rp2-rpi_pico_w asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-25c7889b2d8b"></a>
## v1.28.0 rp2-rpi_pico_w bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-bluetooth-ty]

```text
ty found 10 errors and 1 warnings in 8 files.
assert 9 == 0
```

10 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-d6c3c9e0dfff"></a>
## v1.28.0 rp2-rpi_pico_w micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-8d51e1be7871"></a>
## v1.28.0 rp2-rpi_pico_w networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-networking-ty]

```text
ty found 5 errors and 7 warnings in 5 files.
assert 5 == 0
```

12 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-a8f12237d815"></a>
## v1.28.0 rp2-rpi_pico_w rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-rp2-ty]

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0
```

8 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-0dd42bad079c"></a>
## v1.28.0 rp2-rpi_pico_w stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-880b07fb7999"></a>
## v1.28.0 samd asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-dc4e2f392c9f"></a>
## v1.28.0 samd micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 25 == 0
```

27 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-af30f8174103"></a>
## v1.28.0 samd stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-bba3061914ed"></a>
## v1.28.0 samd-seeed_wio_terminal asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-seeed_wio_terminal-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-ccb881d86ad1"></a>
## v1.28.0 samd-seeed_wio_terminal micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-seeed_wio_terminal-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 25 == 0
```

27 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-a61ab7bf1fca"></a>
## v1.28.0 samd-seeed_wio_terminal stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-seeed_wio_terminal-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-292fae9f817d"></a>
## v1.28.0 stm32 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-064082b10ba5"></a>
## v1.28.0 stm32 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-6cc3654b1690"></a>
## v1.28.0 stm32 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-eb19c1eb0969"></a>
## v1.28.0 stm32-pybv11 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-pybv11-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-7f0b116d13f0"></a>
## v1.28.0 stm32-pybv11 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-pybv11-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-8258ff4d2bdb"></a>
## v1.28.0 stm32-pybv11 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-pybv11-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-dbedbf465f9f"></a>
## v1.28.0 unix asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-unix-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-e0dcd430da81"></a>
## v1.28.0 unix micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-unix-micropython-ty]

```text
ty found 29 errors and 2 warnings in 6 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-17b87e618ce0"></a>
## v1.28.0 unix stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-unix-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-ad80be96eff7"></a>
## v1.28.0 webassembly micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-webassembly-micropython-ty]

```text
ty found 29 errors and 2 warnings in 6 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-652475e4938a"></a>
## v1.28.0 webassembly stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-webassembly-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-9e9dc80bf0e3"></a>
## v1.28.0 webassembly webassembly - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-webassembly-webassembly-ty]

```text
ty found 8 errors and 0 warnings in 4 files.
assert 8 == 0

"check_pyscript/check_config.py"(3,5): unresolved-import: Cannot resolve imported module `pyscript.context`
"check_pyscript/check_ffi_storage.py"(22,31): invalid-assignment: Object of type `Storage` is not assignable to `Preferences`
"check_pyscript/check_ffi_storage.py"(22,60): invalid-argument-type: Argument to function `storage` is incorrect: Expected `type[Storage]`, found `<class 'Preferences'>`
"check_pyscript/check_modules.py"(18,58): unknown-argument: Argument `indent` does not match any known parameter of function `stringify`
"check_pyscript/check_web.py"(53,4): not-subscriptable: Cannot delete subscript on object of type `Style` with no `__delitem__` method
"check_pyscript/check_web.py"(55,0): unresolved-attribute: Object of type `Classes` has no attribute `discard`
```

2 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-e1484e72a98a"></a>
## v1.28.0 windows asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-windows-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-65a61adf8dfe"></a>
## v1.28.0 windows micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-windows-micropython-ty]

```text
ty found 29 errors and 2 warnings in 6 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-faf2fa9ac9d3"></a>
## v1.28.0 windows stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-windows-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

41 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-cbd1e3e95409"></a>
## v1.27.0 esp32 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-c046c9ae5b7b"></a>
## v1.27.0 esp32 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-bluetooth-ty]

```text
ty found 10 errors and 1 warnings in 8 files.
assert 10 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-919bdb33f279"></a>
## v1.27.0 esp32 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32-ty]

```text
ty found 3 errors and 4 warnings in 2 files.
assert 3 == 0
```

7 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-f476a6ed2b59"></a>
## v1.27.0 esp32 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-espnow-ty]

```text
ty found 3 errors and 1 warnings in 2 files.
assert 3 == 0
```

4 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-39caa892bbaf"></a>
## v1.27.0 esp32 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-89cbdbdde4a9"></a>
## v1.27.0 esp32 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-networking-ty]

```text
ty found 5 errors and 7 warnings in 5 files.
assert 5 == 0
```

12 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-d64fc6e29a62"></a>
## v1.27.0 esp32 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

38 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-2050d2096e70"></a>
## v1.27.0 esp32-esp32_generic_c6 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-f149e80f5edb"></a>
## v1.27.0 esp32-esp32_generic_c6 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-bluetooth-ty]

```text
ty found 10 errors and 1 warnings in 8 files.
assert 10 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-4cb3ab240f69"></a>
## v1.27.0 esp32-esp32_generic_c6 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-esp32-ty]

```text
ty found 6 errors and 4 warnings in 4 files.
assert 3 == 0
```

6 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-c1ad5ed5d442"></a>
## v1.27.0 esp32-esp32_generic_c6 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-espnow-ty]

```text
ty found 3 errors and 1 warnings in 2 files.
assert 3 == 0
```

4 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-8b3dc16eeca4"></a>
## v1.27.0 esp32-esp32_generic_c6 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-88bc757e26ff"></a>
## v1.27.0 esp32-esp32_generic_c6 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-networking-ty]

```text
ty found 5 errors and 7 warnings in 5 files.
assert 5 == 0
```

12 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-d0e46bf5e96b"></a>
## v1.27.0 esp32-esp32_generic_c6 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

38 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-db396e880883"></a>
## v1.27.0 esp32-esp32_generic_s3 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-64c19888920b"></a>
## v1.27.0 esp32-esp32_generic_s3 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-bluetooth-ty]

```text
ty found 10 errors and 1 warnings in 8 files.
assert 10 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-7f86c1aca6b1"></a>
## v1.27.0 esp32-esp32_generic_s3 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-esp32-ty]

```text
ty found 4 errors and 4 warnings in 3 files.
assert 3 == 0
```

6 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-8dd5b1767a18"></a>
## v1.27.0 esp32-esp32_generic_s3 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-espnow-ty]

```text
ty found 3 errors and 1 warnings in 2 files.
assert 3 == 0
```

4 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-9c4d8003f976"></a>
## v1.27.0 esp32-esp32_generic_s3 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-bcdf8625c110"></a>
## v1.27.0 esp32-esp32_generic_s3 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-networking-ty]

```text
ty found 5 errors and 7 warnings in 5 files.
assert 5 == 0
```

12 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-04d1b4c8da3c"></a>
## v1.27.0 esp32-esp32_generic_s3 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

38 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-1623a6a1c7f6"></a>
## v1.27.0 esp8266 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp8266-micropython-ty]

```text
ty found 29 errors and 2 warnings in 6 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-419944d8e5ab"></a>
## v1.27.0 esp8266 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp8266-networking-ty]

```text
ty found 5 errors and 7 warnings in 5 files.
assert 5 == 0
```

12 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-567b77ae77d3"></a>
## v1.27.0 esp8266 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp8266-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

38 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-3eba7f8ca516"></a>
## v1.27.0 rp2-rpi_pico2 asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2-asm_pio-ty]

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-8d81c6d8b490"></a>
## v1.27.0 rp2-rpi_pico2 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-ec26838444c4"></a>
## v1.27.0 rp2-rpi_pico2 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-6f1b5244ecd8"></a>
## v1.27.0 rp2-rpi_pico2 rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2-rp2-ty]

```text
ty found 9 errors and 0 warnings in 4 files.
assert 8 == 0
```

8 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-0e6e5db884aa"></a>
## v1.27.0 rp2-rpi_pico2 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

38 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-0f4708737836"></a>
## v1.27.0 rp2-rpi_pico2_w asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-asm_pio-ty]

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-edd134a0146a"></a>
## v1.27.0 rp2-rpi_pico2_w asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-47b4df88d38c"></a>
## v1.27.0 rp2-rpi_pico2_w micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-4195907c025a"></a>
## v1.27.0 rp2-rpi_pico2_w networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-networking-ty]

```text
ty found 5 errors and 7 warnings in 5 files.
assert 5 == 0
```

12 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-a6b241e34641"></a>
## v1.27.0 rp2-rpi_pico2_w rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-rp2-ty]

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0
```

8 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-3464ad6cdea4"></a>
## v1.27.0 rp2-rpi_pico2_w stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

38 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-ec89cf5a88fd"></a>
## v1.27.0 rp2-rpi_pico_w aioble - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-aioble-ty]

```text
ty found 12 errors and 0 warnings in 9 files.
assert 11 == 0
```

11 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-f5bbeb79725f"></a>
## v1.27.0 rp2-rpi_pico_w asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-asm_pio-ty]

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0
```

1 shared diagnostic omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-b04f79ae17f6"></a>
## v1.27.0 rp2-rpi_pico_w asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-80a70167defa"></a>
## v1.27.0 rp2-rpi_pico_w bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-bluetooth-ty]

```text
ty found 10 errors and 1 warnings in 8 files.
assert 9 == 0
```

10 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-3705c5a9f415"></a>
## v1.27.0 rp2-rpi_pico_w micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-1d1755137596"></a>
## v1.27.0 rp2-rpi_pico_w networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-networking-ty]

```text
ty found 5 errors and 7 warnings in 5 files.
assert 5 == 0
```

12 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-52f3fed82565"></a>
## v1.27.0 rp2-rpi_pico_w rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-rp2-ty]

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0
```

8 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-77835203908d"></a>
## v1.27.0 rp2-rpi_pico_w stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

38 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-178d7f94838d"></a>
## v1.27.0 samd asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-b51ef055f864"></a>
## v1.27.0 samd micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 25 == 0
```

27 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-4a6414db7d05"></a>
## v1.27.0 samd stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

38 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-9ddd83db8ee2"></a>
## v1.27.0 samd-seeed_wio_terminal asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-seeed_wio_terminal-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-b3735a471884"></a>
## v1.27.0 samd-seeed_wio_terminal micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-seeed_wio_terminal-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 25 == 0
```

27 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-3c92205ab28b"></a>
## v1.27.0 samd-seeed_wio_terminal stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-seeed_wio_terminal-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

38 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-a0cc374de27f"></a>
## v1.27.0 stm32 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-1f5813fef19f"></a>
## v1.27.0 stm32 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-cd2013914c6b"></a>
## v1.27.0 stm32 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

38 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-c5db0d79dffb"></a>
## v1.27.0 stm32-pybv11 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-pybv11-asyncio-ty]

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0
```

24 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-09f3c04edea5"></a>
## v1.27.0 stm32-pybv11 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-pybv11-micropython-ty]

```text
ty found 28 errors and 2 warnings in 5 files.
assert 28 == 0
```

30 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-ty-9aab8306f5e1"></a>
## v1.27.0 stm32-pybv11 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-pybv11-stdlib-ty]

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0
```

38 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

## Shared diagnostics

```text
"check_asm_pio_code.py"(50,23): unresolved-attribute: Module `time` has no member `ticks_ms` (Reported by 13 tests)
"check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms` (Reported by 38 tests)
"check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it (Reported by 43 tests)
"check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any` (Reported by 38 tests)
"check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms` (Reported by 38 tests)
"check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms` (Reported by 38 tests)
"check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it (Reported by 38 tests)
"check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff` (Reported by 38 tests)
"check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff` (Reported by 38 tests)
"check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments (Reported by 38 tests)
"check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it (Reported by 38 tests)
"check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__` (Reported by 38 tests)
"check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART` (Reported by 38 tests)
"check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]` (Reported by 38 tests)
"check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART` (Reported by 38 tests)
"check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite` (Reported by 38 tests)
"check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms` (Reported by 38 tests)
"check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__` (Reported by 38 tests)
"check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART` (Reported by 38 tests)
"check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]` (Reported by 38 tests)
"check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART` (Reported by 38 tests)
"check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite` (Reported by 38 tests)
"check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms` (Reported by 38 tests)
"check_espnow.py"(14,0): undefined-reveal: `reveal_type` used without importing it (Reported by 9 tests)
"check_examples/ble_advertising.py"(85,39): invalid-argument-type: Argument to `UUID.__init__` is incorrect: Expected `int | str`, found `float*` (Reported by 12 tests)
"check_examples/ble_bonding_peripheral.py"(130,12): undefined-reveal: `reveal_type` used without importing it (Reported by 12 tests)
"check_examples/ble_bonding_peripheral.py"(196,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 12 tests)
"check_examples/ble_simple_central.py"(222,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 12 tests)
"check_examples/ble_simple_central.py"(244,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 12 tests)
"check_examples/ble_simple_peripheral.py"(102,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 12 tests)
"check_examples/ble_temperature.py"(99,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 12 tests)
"check_examples/ble_temperature_central.py"(242,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 12 tests)
"check_examples/ble_temperature_central.py"(251,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 12 tests)
"check_examples/ble_uart_peripheral.py"(114,12): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 12 tests)
"check_examples/ble_uart_repl.py"(84,4): unresolved-attribute: Module `os` has no member `dupterm` (Reported by 9 tests)
"check_examples/http_client_ssl.py"(15,12): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead. (Reported by 18 tests)
"check_examples/http_client_ssl.py"(21,10): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead. (Reported by 18 tests)
"check_examples/http_client_ssl.py"(22,16): deprecated: The function `read` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.recv` method instead. (Reported by 18 tests)
"check_examples/http_server_ssl.py"(66,23): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead. (Reported by 18 tests)
"check_examples/http_server_ssl.py"(69,12): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket` (Reported by 18 tests)
"check_examples/http_server_ssl.py"(70,12): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket` (Reported by 18 tests)
"check_examples/http_server_ssl.py"(90,29): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead. (Reported by 18 tests)
"check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free` (Reported by 43 tests)
"check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold` (Reported by 37 tests)
"check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free` (Reported by 37 tests)
"check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc` (Reported by 37 tests)
"check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free` (Reported by 43 tests)
"check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc` (Reported by 43 tests)
"check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free` (Reported by 43 tests)
"check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc` (Reported by 43 tests)
"check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free` (Reported by 43 tests)
"check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc` (Reported by 43 tests)
"check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free` (Reported by 43 tests)
"check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc` (Reported by 43 tests)
"check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free` (Reported by 43 tests)
"check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT` (Reported by 43 tests)
"check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]` (Reported by 43 tests)
"check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]` (Reported by 43 tests)
"check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it (Reported by 43 tests)
"check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3 (Reported by 43 tests)
"check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3 (Reported by 43 tests)
"check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3 (Reported by 43 tests)
"check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_machine/check_Pin.py"(20,4): unresolved-attribute: Module `utime` has no member `sleep_ms` (Reported by 13 tests)
"check_machine/check_Pin.py"(22,4): unresolved-attribute: Module `utime` has no member `sleep_ms` (Reported by 13 tests)
"check_machine/check_Pin.py"(56,4): deprecated: The function `read` is deprecated: Use read_u16() instead. (Reported by 9 tests)
"check_machine/check_Pin.py"(59,4): deprecated: The function `atten` is deprecated: Use ADC.init(atten=atten) instead. (Reported by 9 tests)
"check_machine/check_Pin.py"(61,4): deprecated: The function `width` is deprecated: Use ADC.block().init(bits=bits) instead. (Reported by 3 tests)
"check_machine/check_Pin.py"(64,4): deprecated: The function `read` is deprecated: Use read_u16() instead. (Reported by 9 tests)
"check_machine/check_devices.py"(12,0): unresolved-attribute: Module `os` has no member `mount` (Reported by 9 tests)
"check_machine/check_devices.py"(14,0): unresolved-attribute: Module `os` has no member `umount` (Reported by 9 tests)
"check_machine/check_devices.py"(27,0): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 9 tests)
"check_machine/check_ds18x20.py"(12,0): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 13 tests)
"check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it (Reported by 43 tests)
"check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it (Reported by 43 tests)
"check_micropython/check_viper.py"(10,56): unresolved-reference: Name `ptr` used when not defined (Reported by 27 tests)
"check_micropython/check_viper.py"(10,64): unresolved-reference: Name `uint` used when not defined (Reported by 27 tests)
"check_micropython/check_viper.py"(11,19): unresolved-reference: Name `ptr8` used when not defined (Reported by 27 tests)
"check_micropython/check_viper.py"(12,23): unresolved-reference: Name `ptr16` used when not defined (Reported by 27 tests)
"check_micropython/check_viper.py"(13,19): unresolved-reference: Name `ptr32` used when not defined (Reported by 27 tests)
"check_micropython/check_viper.py"(14,15): unresolved-reference: Name `uint` used when not defined (Reported by 27 tests)
"check_micropython/check_viper.py"(5,23): unresolved-reference: Name `uint` used when not defined (Reported by 27 tests)
"check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount` (Reported by 43 tests)
"check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount` (Reported by 43 tests)
"check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount` (Reported by 43 tests)
"check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount` (Reported by 43 tests)
"check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount` (Reported by 43 tests)
"check_pyscript/check_ffi_storage.py"(23,4): invalid-assignment: Cannot assign to a subscript on an object of type `Preferences` (Reported by 2 tests)
"check_pyscript/check_modules.py"(16,22): too-many-positional-arguments: Too many positional arguments to bound method `Event.remove_listener`: expected 1, got 2 (Reported by 2 tests)
"check_socket.py"(19,0): type-assertion-failure: Type `Unknown` does not match asserted type `bytes` (Reported by 12 tests)
"check_ssl_1.py"(16,42): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 18 tests)
"check_ssl_2.py"(50,20): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead. (Reported by 18 tests)
"check_ssl_2.py"(52,20): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket` (Reported by 18 tests)
"check_ssl_2.py"(53,20): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket` (Reported by 18 tests)
"check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 43 tests)
"check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception` (Reported by 43 tests)
"check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception` (Reported by 43 tests)
"check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms` (Reported by 38 tests)
"check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms` (Reported by 38 tests)
"check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms` (Reported by 43 tests)
"check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff` (Reported by 43 tests)
"check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add` (Reported by 43 tests)
"check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception` (Reported by 43 tests)
"check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms` (Reported by 43 tests)
"check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 32 tests)
"check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 32 tests)
"check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive (Reported by 32 tests)
"check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 43 tests)
"check_time.py"(6,0): unresolved-attribute: Module `utime` has no member `sleep_ms` (Reported by 13 tests)
"check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]` (Reported by 43 tests)
"check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us` (Reported by 43 tests)
"check_time.py"(7,0): unresolved-attribute: Module `utime` has no member `sleep_us` (Reported by 13 tests)
"check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms` (Reported by 43 tests)
"check_time.py"(8,8): unresolved-attribute: Module `utime` has no member `ticks_ms` (Reported by 13 tests)
"check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms` (Reported by 43 tests)
"check_time.py"(9,24): unresolved-attribute: Module `utime` has no member `ticks_ms` (Reported by 13 tests)
"check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff` (Reported by 43 tests)
"check_time.py"(9,8): unresolved-attribute: Module `utime` has no member `ticks_diff` (Reported by 13 tests)
"check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us` (Reported by 43 tests)
"check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff` (Reported by 43 tests)
"check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us` (Reported by 43 tests)
"check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]` (Reported by 43 tests)
"check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]` (Reported by 43 tests)
"check_utils/timer.py"(5,25): unresolved-import: Module `utime` has no member `sleep_ms` (Reported by 9 tests)
"check_utils/timer.py"(5,35): unresolved-import: Module `utime` has no member `ticks_diff` (Reported by 9 tests)
"check_utils/timer.py"(5,47): unresolved-import: Module `utime` has no member `ticks_ms` (Reported by 9 tests)
"check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms` (Reported by 38 tests)
"community_code/sample_1.py"(11,17): unresolved-import: Module `time` has no member `ticks_us` (Reported by 3 tests)
"community_code/sample_1.py"(53,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms` (Reported by 3 tests)
"examples_bluetooth/ble_advertising.py"(85,39): invalid-argument-type: Argument to `UUID.__init__` is incorrect: Expected `int | str`, found `float*` (Reported by 3 tests)
"examples_bluetooth/ble_bonding_peripheral.py"(196,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 3 tests)
"examples_bluetooth/ble_simple_central.py"(222,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 3 tests)
"examples_bluetooth/ble_simple_central.py"(244,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 3 tests)
"examples_bluetooth/ble_simple_peripheral.py"(102,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 3 tests)
"examples_bluetooth/ble_temperature.py"(99,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 3 tests)
"examples_bluetooth/ble_temperature_central.py"(242,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 3 tests)
"examples_bluetooth/ble_temperature_central.py"(251,8): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 3 tests)
"examples_bluetooth/ble_uart_peripheral.py"(114,12): unresolved-attribute: Module `time` has no member `sleep_ms` (Reported by 3 tests)
```
