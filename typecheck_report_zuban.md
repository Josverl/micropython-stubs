# zuban failures and expected failures

[Back to type checker test report](typecheck_report.md)

<a id="typecheck-detail-zuban-c3a186f04ce3"></a>
## - stdlib stdlib_only - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_stdlib_only.py::test_typecheck_stdlib_only[zuban-local-stdlib_only---stdlib]

```text
zuban found 1394 errors and 0 warnings in 53 files.
assert 1394 == 0

"check_io.py"(12,29): Argument 1 to "BufferedWriter" has incompatible type "TextIOWrapper[_WrappedBuffer]"; expected "RawIOBase"
"check_sys/check_stdio.py"(6,17): Argument 1 to "write" of "IO" has incompatible type "bytes"; expected "str"
"check_sys/check_stdio.py"(11,17): Argument 1 to "write" of "IO" has incompatible type "bytes"; expected "str"
"check_sys/check_stdio.py"(28,15): Item "BinaryIO" of "BinaryIO | Any" has no attribute "readinto"
"check_sys/check_stdio.py"(33,20): Item "BinaryIO" of "BinaryIO | Any" has no attribute "readinto"
"check_sys/check_stdio.py"(41,8): No overload variant of "write" of "IO" matches argument types "bytearray", "int"
"check_sys/check_stdio.py"(42,8): Item "BinaryIO" of "BinaryIO | Any" has no attribute "readinto"
"check_sys/check_stdio.py"(43,8): Item "BinaryIO" of "BinaryIO | Any" has no attribute "readinto"
```

1386 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-b097a539839c"></a>
## v1.29.0 esp32 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-asyncio-zuban]

```text
zuban found 1479 errors and 0 warnings in 64 files.
assert 1479 == 0
```

1479 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-0c84fc0b8920"></a>
## v1.29.0 esp32 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-bluetooth-zuban]

```text
zuban found 1478 errors and 0 warnings in 64 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3273e6b60212"></a>
## v1.29.0 esp32 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32-zuban]

```text
zuban found 1480 errors and 0 warnings in 65 files.
assert 1480 == 0
```

1480 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-93a71b4768a5"></a>
## v1.29.0 esp32 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-espnow-zuban]

```text
zuban found 1478 errors and 0 warnings in 64 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-0f256041e8f3"></a>
## v1.29.0 esp32 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-machine-zuban]

```text
zuban found 1478 errors and 0 warnings in 63 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-461ab1174a4a"></a>
## v1.29.0 esp32 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-micropython-zuban]

```text
zuban found 1491 errors and 0 warnings in 65 files.
assert 1491 == 0
```

1491 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-cb9a7ed70102"></a>
## v1.29.0 esp32 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-networking-zuban]

```text
zuban found 1478 errors and 0 warnings in 63 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-e0544c2555c6"></a>
## v1.29.0 esp32 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-stdlib-zuban]

```text
zuban found 1484 errors and 0 warnings in 68 files.
assert 1484 == 0
```

1484 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-2a8436aa15d9"></a>
## v1.29.0 esp32-esp32_generic_c6 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-asyncio-zuban]

```text
zuban found 1479 errors and 0 warnings in 64 files.
assert 1479 == 0
```

1479 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-f14f360ae35f"></a>
## v1.29.0 esp32-esp32_generic_c6 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-bluetooth-zuban]

```text
zuban found 1478 errors and 0 warnings in 64 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-1f12a0a4e5d1"></a>
## v1.29.0 esp32-esp32_generic_c6 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-esp32-zuban]

```text
zuban found 1483 errors and 0 warnings in 67 files.
assert 1480 == 0
```

1480 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-5d4572238d6e"></a>
## v1.29.0 esp32-esp32_generic_c6 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-espnow-zuban]

```text
zuban found 1478 errors and 0 warnings in 64 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-6e4e81ce3634"></a>
## v1.29.0 esp32-esp32_generic_c6 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-machine-zuban]

```text
zuban found 1478 errors and 0 warnings in 63 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3f5bb4c76bb0"></a>
## v1.29.0 esp32-esp32_generic_c6 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-micropython-zuban]

```text
zuban found 1491 errors and 0 warnings in 65 files.
assert 1491 == 0
```

1491 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-a552e0bf377e"></a>
## v1.29.0 esp32-esp32_generic_c6 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-networking-zuban]

```text
zuban found 1478 errors and 0 warnings in 63 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-a428b98e8d0b"></a>
## v1.29.0 esp32-esp32_generic_c6 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-stdlib-zuban]

```text
zuban found 1484 errors and 0 warnings in 68 files.
assert 1484 == 0
```

1484 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-14cba949dbac"></a>
## v1.29.0 esp32-esp32_generic_s3 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-asyncio-zuban]

```text
zuban found 1479 errors and 0 warnings in 64 files.
assert 1479 == 0
```

1479 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-7fdebb598482"></a>
## v1.29.0 esp32-esp32_generic_s3 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-bluetooth-zuban]

```text
zuban found 1478 errors and 0 warnings in 64 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-989af76684c2"></a>
## v1.29.0 esp32-esp32_generic_s3 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-esp32-zuban]

```text
zuban found 1481 errors and 0 warnings in 66 files.
assert 1480 == 0
```

1480 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-695f60dd6c44"></a>
## v1.29.0 esp32-esp32_generic_s3 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-espnow-zuban]

```text
zuban found 1478 errors and 0 warnings in 64 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-cb231f65107a"></a>
## v1.29.0 esp32-esp32_generic_s3 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-machine-zuban]

```text
zuban found 1478 errors and 0 warnings in 63 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-ba219b867d0e"></a>
## v1.29.0 esp32-esp32_generic_s3 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-micropython-zuban]

```text
zuban found 1491 errors and 0 warnings in 65 files.
assert 1491 == 0
```

1491 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-d93c55005444"></a>
## v1.29.0 esp32-esp32_generic_s3 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-networking-zuban]

```text
zuban found 1478 errors and 0 warnings in 63 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-a1c02992239e"></a>
## v1.29.0 esp32-esp32_generic_s3 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-stdlib-zuban]

```text
zuban found 1484 errors and 0 warnings in 68 files.
assert 1484 == 0
```

1484 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-2e169a35efd1"></a>
## v1.29.0 esp8266 esp8266 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp8266-esp8266-zuban]

```text
zuban found 1458 errors and 0 warnings in 60 files.
assert 1458 == 0
```

1458 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-4426bcd0eaca"></a>
## v1.29.0 esp8266 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp8266-machine-zuban]

```text
zuban found 1458 errors and 0 warnings in 60 files.
assert 1458 == 0
```

1458 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-340f3b7a73fa"></a>
## v1.29.0 esp8266 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp8266-micropython-zuban]

```text
zuban found 1471 errors and 0 warnings in 62 files.
assert 1471 == 0
```

1471 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-8aa078f4bc81"></a>
## v1.29.0 esp8266 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp8266-networking-zuban]

```text
zuban found 1458 errors and 0 warnings in 60 files.
assert 1458 == 0
```

1458 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-9ee5e4f5842c"></a>
## v1.29.0 esp8266 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp8266-stdlib-zuban]

```text
zuban found 1464 errors and 0 warnings in 65 files.
assert 1464 == 0
```

1464 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-0893cbd5af79"></a>
## v1.29.0 rp2 asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-asm_pio-zuban]

```text
zuban found 1481 errors and 0 warnings in 63 files.
assert 1481 == 0
```

1481 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-03db235ecc73"></a>
## v1.29.0 rp2 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-asyncio-zuban]

```text
zuban found 1481 errors and 0 warnings in 63 files.
assert 1481 == 0
```

1481 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-52d085bf0eef"></a>
## v1.29.0 rp2 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-machine-zuban]

```text
zuban found 1480 errors and 0 warnings in 62 files.
assert 1480 == 0
```

1480 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-787fcea18029"></a>
## v1.29.0 rp2 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-micropython-zuban]

```text
zuban found 1493 errors and 0 warnings in 64 files.
assert 1493 == 0
```

1493 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-f50e61aa1002"></a>
## v1.29.0 rp2 rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rp2-zuban]

```text
zuban found 1481 errors and 0 warnings in 63 files.
assert 1481 == 0
```

1481 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-6443ad734d11"></a>
## v1.29.0 rp2 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-stdlib-zuban]

```text
zuban found 1486 errors and 0 warnings in 67 files.
assert 1486 == 0
```

1486 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-9f7c71e2eccd"></a>
## v1.29.0 rp2-rpi_pico asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-asm_pio-zuban]

```text
zuban found 1447 errors and 0 warnings in 63 files.
assert 1447 == 0
```

1447 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-be502393f062"></a>
## v1.29.0 rp2-rpi_pico asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-asyncio-zuban]

```text
zuban found 1447 errors and 0 warnings in 63 files.
assert 1447 == 0
```

1447 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-472302f312ef"></a>
## v1.29.0 rp2-rpi_pico machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-machine-zuban]

```text
zuban found 1446 errors and 0 warnings in 62 files.
assert 1446 == 0
```

1446 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-2079fef46009"></a>
## v1.29.0 rp2-rpi_pico micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-micropython-zuban]

```text
zuban found 1459 errors and 0 warnings in 64 files.
assert 1459 == 0
```

1459 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-a5d61dea5bbb"></a>
## v1.29.0 rp2-rpi_pico rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-rp2-zuban]

```text
zuban found 1447 errors and 0 warnings in 63 files.
assert 1447 == 0
```

1447 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-1a80e0aa3a1c"></a>
## v1.29.0 rp2-rpi_pico stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-stdlib-zuban]

```text
zuban found 1452 errors and 0 warnings in 67 files.
assert 1452 == 0
```

1452 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-870557673959"></a>
## v1.29.0 rp2-rpi_pico2 asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-asm_pio-zuban]

```text
zuban found 1447 errors and 0 warnings in 63 files.
assert 1447 == 0
```

1447 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-d12aa6838ec9"></a>
## v1.29.0 rp2-rpi_pico2 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-asyncio-zuban]

```text
zuban found 1447 errors and 0 warnings in 63 files.
assert 1447 == 0
```

1447 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-5f130b0c18b9"></a>
## v1.29.0 rp2-rpi_pico2 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-machine-zuban]

```text
zuban found 1446 errors and 0 warnings in 62 files.
assert 1446 == 0
```

1446 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3133e941364f"></a>
## v1.29.0 rp2-rpi_pico2 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-micropython-zuban]

```text
zuban found 1459 errors and 0 warnings in 64 files.
assert 1459 == 0
```

1459 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-479fb4b50687"></a>
## v1.29.0 rp2-rpi_pico2 rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-rp2-zuban]

```text
zuban found 1447 errors and 0 warnings in 63 files.
assert 1447 == 0
```

1447 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-6c8f767f89c7"></a>
## v1.29.0 rp2-rpi_pico2 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-stdlib-zuban]

```text
zuban found 1452 errors and 0 warnings in 67 files.
assert 1452 == 0
```

1452 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-cfb6b5091b55"></a>
## v1.29.0 rp2-rpi_pico2_w asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-asm_pio-zuban]

```text
zuban found 1481 errors and 0 warnings in 63 files.
assert 1481 == 0
```

1481 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-42698395dcde"></a>
## v1.29.0 rp2-rpi_pico2_w asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-asyncio-zuban]

```text
zuban found 1481 errors and 0 warnings in 63 files.
assert 1481 == 0
```

1481 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-fa3b8104617d"></a>
## v1.29.0 rp2-rpi_pico2_w machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-machine-zuban]

```text
zuban found 1480 errors and 0 warnings in 62 files.
assert 1480 == 0
```

1480 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-5df1bfef7dcd"></a>
## v1.29.0 rp2-rpi_pico2_w micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-micropython-zuban]

```text
zuban found 1493 errors and 0 warnings in 64 files.
assert 1493 == 0
```

1493 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-d88afde133fd"></a>
## v1.29.0 rp2-rpi_pico2_w networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-networking-zuban]

```text
zuban found 1480 errors and 0 warnings in 62 files.
assert 1480 == 0
```

1480 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-dac47cfc2b4e"></a>
## v1.29.0 rp2-rpi_pico2_w rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-rp2-zuban]

```text
zuban found 1481 errors and 0 warnings in 63 files.
assert 1481 == 0
```

1481 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-be5c23de5987"></a>
## v1.29.0 rp2-rpi_pico2_w stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-stdlib-zuban]

```text
zuban found 1486 errors and 0 warnings in 67 files.
assert 1486 == 0
```

1486 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3cc7a4be24ba"></a>
## v1.29.0 rp2-rpi_pico_w aioble - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-aioble-zuban]

```text
zuban found 1483 errors and 0 warnings in 63 files.
assert 1483 == 0
```

1483 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-9c03f445da3f"></a>
## v1.29.0 rp2-rpi_pico_w asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-asm_pio-zuban]

```text
zuban found 1481 errors and 0 warnings in 63 files.
assert 1481 == 0
```

1481 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-f9337b44060a"></a>
## v1.29.0 rp2-rpi_pico_w asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-asyncio-zuban]

```text
zuban found 1481 errors and 0 warnings in 63 files.
assert 1481 == 0
```

1481 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-a75715d548d4"></a>
## v1.29.0 rp2-rpi_pico_w bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-bluetooth-zuban]

```text
zuban found 1480 errors and 0 warnings in 63 files.
assert 1480 == 0
```

1480 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-b51da807a06d"></a>
## v1.29.0 rp2-rpi_pico_w machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-machine-zuban]

```text
zuban found 1480 errors and 0 warnings in 62 files.
assert 1480 == 0
```

1480 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-746d48a779ac"></a>
## v1.29.0 rp2-rpi_pico_w micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-micropython-zuban]

```text
zuban found 1493 errors and 0 warnings in 64 files.
assert 1493 == 0
```

1493 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-9ee6368cf56a"></a>
## v1.29.0 rp2-rpi_pico_w networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-networking-zuban]

```text
zuban found 1480 errors and 0 warnings in 62 files.
assert 1480 == 0
```

1480 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-08e96d5007f2"></a>
## v1.29.0 rp2-rpi_pico_w rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-rp2-zuban]

```text
zuban found 1481 errors and 0 warnings in 63 files.
assert 1481 == 0
```

1481 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-9279f7f05325"></a>
## v1.29.0 rp2-rpi_pico_w stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-stdlib-zuban]

```text
zuban found 1486 errors and 0 warnings in 67 files.
assert 1486 == 0
```

1486 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-904c0dc8e69b"></a>
## v1.29.0 samd asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-asyncio-zuban]

```text
zuban found 1435 errors and 0 warnings in 59 files.
assert 1435 == 0
```

1435 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-9b53bf757812"></a>
## v1.29.0 samd machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-machine-zuban]

```text
zuban found 1434 errors and 0 warnings in 58 files.
assert 1434 == 0
```

1434 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-927ef62f5604"></a>
## v1.29.0 samd micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-micropython-zuban]

```text
zuban found 1447 errors and 0 warnings in 60 files.
assert 1447 == 0
```

1447 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-729f28aa71da"></a>
## v1.29.0 samd samd - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-samd-zuban]

```text
zuban found 1434 errors and 0 warnings in 58 files.
assert 1434 == 0
```

1434 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-5ea24e44c76b"></a>
## v1.29.0 samd stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-stdlib-zuban]

```text
zuban found 1440 errors and 0 warnings in 63 files.
assert 1440 == 0
```

1440 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-d2eb1de721c1"></a>
## v1.29.0 samd-seeed_wio_terminal asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-seeed_wio_terminal-asyncio-zuban]

```text
zuban found 1435 errors and 0 warnings in 59 files.
assert 1435 == 0
```

1435 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-88b35f83cd6a"></a>
## v1.29.0 samd-seeed_wio_terminal machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-seeed_wio_terminal-machine-zuban]

```text
zuban found 1434 errors and 0 warnings in 58 files.
assert 1434 == 0
```

1434 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-e59cf6c5cf49"></a>
## v1.29.0 samd-seeed_wio_terminal micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-seeed_wio_terminal-micropython-zuban]

```text
zuban found 1447 errors and 0 warnings in 60 files.
assert 1447 == 0
```

1447 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-fd08e4b0f0d0"></a>
## v1.29.0 samd-seeed_wio_terminal samd - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-seeed_wio_terminal-samd-zuban]

```text
zuban found 1434 errors and 0 warnings in 58 files.
assert 1434 == 0
```

1434 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3916c4434364"></a>
## v1.29.0 samd-seeed_wio_terminal stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-seeed_wio_terminal-stdlib-zuban]

```text
zuban found 1440 errors and 0 warnings in 63 files.
assert 1440 == 0
```

1440 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-1e3735fd74b8"></a>
## v1.29.0 stm32 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-asyncio-zuban]

```text
zuban found 1455 errors and 0 warnings in 62 files.
assert 1455 == 0
```

1455 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3cf1126f91f5"></a>
## v1.29.0 stm32 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-machine-zuban]

```text
zuban found 1454 errors and 0 warnings in 61 files.
assert 1454 == 0
```

1454 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-e8c6850e2c21"></a>
## v1.29.0 stm32 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-micropython-zuban]

```text
zuban found 1467 errors and 0 warnings in 63 files.
assert 1467 == 0
```

1467 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-9a026cfb77a2"></a>
## v1.29.0 stm32 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-stdlib-zuban]

```text
zuban found 1460 errors and 0 warnings in 66 files.
assert 1460 == 0
```

1460 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-be3d801ebf2e"></a>
## v1.29.0 stm32 stm32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-stm32-zuban]

```text
zuban found 1455 errors and 0 warnings in 62 files.
assert 1455 == 0
```

1455 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-2091dd5c316b"></a>
## v1.29.0 stm32-pybv11 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-pybv11-asyncio-zuban]

```text
zuban found 1455 errors and 0 warnings in 62 files.
assert 1455 == 0
```

1455 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-544d3b8912c7"></a>
## v1.29.0 stm32-pybv11 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-pybv11-machine-zuban]

```text
zuban found 1454 errors and 0 warnings in 61 files.
assert 1454 == 0
```

1454 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-767d3fd00aab"></a>
## v1.29.0 stm32-pybv11 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-pybv11-micropython-zuban]

```text
zuban found 1467 errors and 0 warnings in 63 files.
assert 1467 == 0
```

1467 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-e6270e8be47e"></a>
## v1.29.0 stm32-pybv11 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-pybv11-stdlib-zuban]

```text
zuban found 1460 errors and 0 warnings in 66 files.
assert 1460 == 0
```

1460 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-83b09e283e41"></a>
## v1.29.0 stm32-pybv11 stm32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-pybv11-stm32-zuban]

```text
zuban found 1455 errors and 0 warnings in 62 files.
assert 1455 == 0
```

1455 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-0bb6f6260271"></a>
## v1.29.0 unix asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-unix-asyncio-zuban]

```text
zuban found 1467 errors and 0 warnings in 61 files.
assert 1467 == 0
```

1467 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-42b76a1e6e4b"></a>
## v1.29.0 unix micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-unix-micropython-zuban]

```text
zuban found 1480 errors and 0 warnings in 63 files.
assert 1479 == 0
```

1479 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-7d27edb32ff1"></a>
## v1.29.0 unix stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-unix-stdlib-zuban]

```text
zuban found 1472 errors and 0 warnings in 65 files.
assert 1472 == 0
```

1472 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-49647079caa6"></a>
## v1.29.0 unix unix - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-unix-unix-zuban]

```text
zuban found 1466 errors and 0 warnings in 60 files.
assert 1466 == 0
```

1466 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-cbfbe39b379c"></a>
## v1.29.0 webassembly micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-webassembly-micropython-zuban]

```text
zuban found 1452 errors and 0 warnings in 71 files.
assert 1451 == 0
```

1451 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-330ec99c4357"></a>
## v1.29.0 webassembly stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-webassembly-stdlib-zuban]

```text
zuban found 1444 errors and 0 warnings in 73 files.
assert 1444 == 0
```

1444 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-4d6943f5b1c5"></a>
## v1.29.0 webassembly webassembly - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-webassembly-webassembly-zuban]

```text
zuban found 1438 errors and 0 warnings in 68 files.
assert 1438 == 0
```

1438 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-747f239f5b4a"></a>
## v1.29.0 windows asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-windows-asyncio-zuban]

```text
zuban found 1431 errors and 0 warnings in 59 files.
assert 1431 == 0
```

1431 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-2b4b7585d1e6"></a>
## v1.29.0 windows micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-windows-micropython-zuban]

```text
zuban found 1444 errors and 0 warnings in 61 files.
assert 1443 == 0
```

1443 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-33a8518a6455"></a>
## v1.29.0 windows stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-windows-stdlib-zuban]

```text
zuban found 1436 errors and 0 warnings in 63 files.
assert 1436 == 0
```

1436 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-edb8a6d62515"></a>
## v1.29.0 windows windows - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-windows-windows-zuban]

```text
zuban found 1430 errors and 0 warnings in 58 files.
assert 1430 == 0
```

1430 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-0caf6fa6b0e6"></a>
## v1.28.0 esp32 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-asyncio-zuban]

```text
zuban found 1478 errors and 0 warnings in 63 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-c7e9426a7675"></a>
## v1.28.0 esp32 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-bluetooth-zuban]

```text
zuban found 1477 errors and 0 warnings in 63 files.
assert 1477 == 0
```

1477 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-965af2ee1b4e"></a>
## v1.28.0 esp32 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32-zuban]

```text
zuban found 1479 errors and 0 warnings in 64 files.
assert 1479 == 0
```

1479 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-45b7f6e5dc4b"></a>
## v1.28.0 esp32 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-espnow-zuban]

```text
zuban found 1478 errors and 0 warnings in 63 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-da86386d6a3e"></a>
## v1.28.0 esp32 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-machine-zuban]

```text
zuban found 1477 errors and 0 warnings in 62 files.
assert 1477 == 0
```

1477 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-af275f32ee7f"></a>
## v1.28.0 esp32 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-micropython-zuban]

```text
zuban found 1497 errors and 0 warnings in 65 files.
assert 1497 == 0
```

1497 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-b95f639659ce"></a>
## v1.28.0 esp32 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-networking-zuban]

```text
zuban found 1477 errors and 0 warnings in 62 files.
assert 1477 == 0
```

1477 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-9d6d0571eeca"></a>
## v1.28.0 esp32 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-stdlib-zuban]

```text
zuban found 1483 errors and 0 warnings in 67 files.
assert 1483 == 0
```

1483 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-175c01b6e20f"></a>
## v1.28.0 esp32-esp32_generic_c6 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-asyncio-zuban]

```text
zuban found 1483 errors and 0 warnings in 64 files.
assert 1483 == 0
```

1483 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-dfe8eef902ad"></a>
## v1.28.0 esp32-esp32_generic_c6 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-bluetooth-zuban]

```text
zuban found 1482 errors and 0 warnings in 64 files.
assert 1482 == 0
```

1482 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-dbd46d263cbb"></a>
## v1.28.0 esp32-esp32_generic_c6 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-esp32-zuban]

```text
zuban found 1487 errors and 0 warnings in 67 files.
assert 1484 == 0
```

1484 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-56dfc6aea101"></a>
## v1.28.0 esp32-esp32_generic_c6 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-espnow-zuban]

```text
zuban found 1483 errors and 0 warnings in 64 files.
assert 1483 == 0
```

1483 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-0c07f61c23db"></a>
## v1.28.0 esp32-esp32_generic_c6 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-machine-zuban]

```text
zuban found 1482 errors and 0 warnings in 63 files.
assert 1482 == 0
```

1482 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-79b6df152c7d"></a>
## v1.28.0 esp32-esp32_generic_c6 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-micropython-zuban]

```text
zuban found 1502 errors and 0 warnings in 66 files.
assert 1502 == 0
```

1502 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-0ed07348da5d"></a>
## v1.28.0 esp32-esp32_generic_c6 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-networking-zuban]

```text
zuban found 1482 errors and 0 warnings in 63 files.
assert 1482 == 0
```

1482 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-12841faae250"></a>
## v1.28.0 esp32-esp32_generic_c6 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_c6-stdlib-zuban]

```text
zuban found 1488 errors and 0 warnings in 68 files.
assert 1488 == 0
```

1488 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-cdace47bbccf"></a>
## v1.28.0 esp32-esp32_generic_s3 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-asyncio-zuban]

```text
zuban found 1478 errors and 0 warnings in 63 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-8aaf3906e01a"></a>
## v1.28.0 esp32-esp32_generic_s3 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-bluetooth-zuban]

```text
zuban found 1477 errors and 0 warnings in 63 files.
assert 1477 == 0
```

1477 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-f909a0b593a4"></a>
## v1.28.0 esp32-esp32_generic_s3 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-esp32-zuban]

```text
zuban found 1480 errors and 0 warnings in 65 files.
assert 1479 == 0
```

1479 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-9b3b97465f5f"></a>
## v1.28.0 esp32-esp32_generic_s3 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-espnow-zuban]

```text
zuban found 1478 errors and 0 warnings in 63 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-cb74df8d845b"></a>
## v1.28.0 esp32-esp32_generic_s3 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-machine-zuban]

```text
zuban found 1477 errors and 0 warnings in 62 files.
assert 1477 == 0
```

1477 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-c75de046bd2a"></a>
## v1.28.0 esp32-esp32_generic_s3 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-micropython-zuban]

```text
zuban found 1497 errors and 0 warnings in 65 files.
assert 1497 == 0
```

1497 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-7cd39ff8bea3"></a>
## v1.28.0 esp32-esp32_generic_s3 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-networking-zuban]

```text
zuban found 1477 errors and 0 warnings in 62 files.
assert 1477 == 0
```

1477 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-07bd13d3cc39"></a>
## v1.28.0 esp32-esp32_generic_s3 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp32-esp32_generic_s3-stdlib-zuban]

```text
zuban found 1483 errors and 0 warnings in 67 files.
assert 1483 == 0
```

1483 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-1eef6e505816"></a>
## v1.28.0 esp8266 esp8266 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp8266-esp8266-zuban]

```text
zuban found 1455 errors and 0 warnings in 59 files.
assert 1455 == 0
```

1455 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-d2cf69ca4f27"></a>
## v1.28.0 esp8266 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp8266-machine-zuban]

```text
zuban found 1455 errors and 0 warnings in 59 files.
assert 1455 == 0
```

1455 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-74e7e63a8463"></a>
## v1.28.0 esp8266 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp8266-micropython-zuban]

```text
zuban found 1463 errors and 0 warnings in 62 files.
assert 1462 == 0
```

1462 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-9e8267583eeb"></a>
## v1.28.0 esp8266 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp8266-networking-zuban]

```text
zuban found 1455 errors and 0 warnings in 59 files.
assert 1455 == 0
```

1455 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-20c2790b227e"></a>
## v1.28.0 esp8266 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-esp8266-stdlib-zuban]

```text
zuban found 1461 errors and 0 warnings in 64 files.
assert 1461 == 0
```

1461 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3c5e24c37a8d"></a>
## v1.28.0 rp2 asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-asm_pio-zuban]

```text
zuban found 1497 errors and 0 warnings in 63 files.
assert 1497 == 0
```

1497 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-cfd181aa2811"></a>
## v1.28.0 rp2 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-asyncio-zuban]

```text
zuban found 1497 errors and 0 warnings in 63 files.
assert 1497 == 0
```

1497 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-a752d4d1e37e"></a>
## v1.28.0 rp2 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-machine-zuban]

```text
zuban found 1496 errors and 0 warnings in 62 files.
assert 1496 == 0
```

1496 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-694fc017856f"></a>
## v1.28.0 rp2 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-micropython-zuban]

```text
zuban found 1516 errors and 0 warnings in 65 files.
assert 1516 == 0
```

1516 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-0eda88cdd2dc"></a>
## v1.28.0 rp2 rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rp2-zuban]

```text
zuban found 1497 errors and 0 warnings in 63 files.
assert 1497 == 0
```

1497 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-0f476ff8a49d"></a>
## v1.28.0 rp2 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-stdlib-zuban]

```text
zuban found 1502 errors and 0 warnings in 67 files.
assert 1502 == 0
```

1502 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-b4d479ee1da4"></a>
## v1.28.0 rp2-rpi_pico asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico-asm_pio-zuban]

```text
zuban found 1463 errors and 0 warnings in 63 files.
assert 1463 == 0
```

1463 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-4586614ea230"></a>
## v1.28.0 rp2-rpi_pico asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico-asyncio-zuban]

```text
zuban found 1463 errors and 0 warnings in 63 files.
assert 1463 == 0
```

1463 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-4678531e0ed6"></a>
## v1.28.0 rp2-rpi_pico machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico-machine-zuban]

```text
zuban found 1462 errors and 0 warnings in 62 files.
assert 1462 == 0
```

1462 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-5d8329358d72"></a>
## v1.28.0 rp2-rpi_pico micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico-micropython-zuban]

```text
zuban found 1482 errors and 0 warnings in 65 files.
assert 1482 == 0
```

1482 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-c9d7fcfe6903"></a>
## v1.28.0 rp2-rpi_pico rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico-rp2-zuban]

```text
zuban found 1463 errors and 0 warnings in 63 files.
assert 1463 == 0
```

1463 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-b971504c0324"></a>
## v1.28.0 rp2-rpi_pico stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico-stdlib-zuban]

```text
zuban found 1468 errors and 0 warnings in 67 files.
assert 1468 == 0
```

1468 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-56c169ce0571"></a>
## v1.28.0 rp2-rpi_pico2 asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2-asm_pio-zuban]

```text
zuban found 1463 errors and 0 warnings in 63 files.
assert 1463 == 0
```

1463 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-156bf265926f"></a>
## v1.28.0 rp2-rpi_pico2 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2-asyncio-zuban]

```text
zuban found 1463 errors and 0 warnings in 63 files.
assert 1463 == 0
```

1463 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-429907ea5caf"></a>
## v1.28.0 rp2-rpi_pico2 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2-machine-zuban]

```text
zuban found 1462 errors and 0 warnings in 62 files.
assert 1462 == 0
```

1462 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-905f4f02a4c5"></a>
## v1.28.0 rp2-rpi_pico2 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2-micropython-zuban]

```text
zuban found 1482 errors and 0 warnings in 65 files.
assert 1482 == 0
```

1482 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-69e250fb8a4d"></a>
## v1.28.0 rp2-rpi_pico2 rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2-rp2-zuban]

```text
zuban found 1463 errors and 0 warnings in 63 files.
assert 1463 == 0
```

1463 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-02cd47f5ad2f"></a>
## v1.28.0 rp2-rpi_pico2 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2-stdlib-zuban]

```text
zuban found 1468 errors and 0 warnings in 67 files.
assert 1468 == 0
```

1468 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-e516f493f196"></a>
## v1.28.0 rp2-rpi_pico2_w asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-asm_pio-zuban]

```text
zuban found 1497 errors and 0 warnings in 63 files.
assert 1497 == 0
```

1497 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-f49031d2e2eb"></a>
## v1.28.0 rp2-rpi_pico2_w asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-asyncio-zuban]

```text
zuban found 1497 errors and 0 warnings in 63 files.
assert 1497 == 0
```

1497 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3b75cb09bd13"></a>
## v1.28.0 rp2-rpi_pico2_w machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-machine-zuban]

```text
zuban found 1496 errors and 0 warnings in 62 files.
assert 1496 == 0
```

1496 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-2eb5efcb234b"></a>
## v1.28.0 rp2-rpi_pico2_w micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-micropython-zuban]

```text
zuban found 1516 errors and 0 warnings in 65 files.
assert 1516 == 0
```

1516 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-c5d2900e085d"></a>
## v1.28.0 rp2-rpi_pico2_w networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-networking-zuban]

```text
zuban found 1496 errors and 0 warnings in 62 files.
assert 1496 == 0
```

1496 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-8078abf7f0d2"></a>
## v1.28.0 rp2-rpi_pico2_w rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-rp2-zuban]

```text
zuban found 1497 errors and 0 warnings in 63 files.
assert 1497 == 0
```

1497 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-266dfe70e235"></a>
## v1.28.0 rp2-rpi_pico2_w stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico2_w-stdlib-zuban]

```text
zuban found 1502 errors and 0 warnings in 67 files.
assert 1502 == 0
```

1502 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3cdd44194cba"></a>
## v1.28.0 rp2-rpi_pico_w aioble - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-aioble-zuban]

```text
zuban found 1499 errors and 0 warnings in 63 files.
assert 1499 == 0
```

1499 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-28210905e35d"></a>
## v1.28.0 rp2-rpi_pico_w asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-asm_pio-zuban]

```text
zuban found 1497 errors and 0 warnings in 63 files.
assert 1497 == 0
```

1497 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-85cfcf0be057"></a>
## v1.28.0 rp2-rpi_pico_w asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-asyncio-zuban]

```text
zuban found 1497 errors and 0 warnings in 63 files.
assert 1497 == 0
```

1497 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-a2c83b574a47"></a>
## v1.28.0 rp2-rpi_pico_w bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-bluetooth-zuban]

```text
zuban found 1496 errors and 0 warnings in 63 files.
assert 1496 == 0
```

1496 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-d1f0687d807a"></a>
## v1.28.0 rp2-rpi_pico_w machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-machine-zuban]

```text
zuban found 1496 errors and 0 warnings in 62 files.
assert 1496 == 0
```

1496 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-b2d86ad85bb3"></a>
## v1.28.0 rp2-rpi_pico_w micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-micropython-zuban]

```text
zuban found 1516 errors and 0 warnings in 65 files.
assert 1516 == 0
```

1516 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-4f9f5fdb31f8"></a>
## v1.28.0 rp2-rpi_pico_w networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-networking-zuban]

```text
zuban found 1496 errors and 0 warnings in 62 files.
assert 1496 == 0
```

1496 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-20ffbff3984f"></a>
## v1.28.0 rp2-rpi_pico_w rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-rp2-zuban]

```text
zuban found 1497 errors and 0 warnings in 63 files.
assert 1497 == 0
```

1497 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-cdc5c54c0bc0"></a>
## v1.28.0 rp2-rpi_pico_w stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-rp2-rpi_pico_w-stdlib-zuban]

```text
zuban found 1502 errors and 0 warnings in 67 files.
assert 1502 == 0
```

1502 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-cfb63899b881"></a>
## v1.28.0 samd asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-asyncio-zuban]

```text
zuban found 1434 errors and 0 warnings in 59 files.
assert 1434 == 0
```

1434 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-2ac2917ad05b"></a>
## v1.28.0 samd machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-machine-zuban]

```text
zuban found 1433 errors and 0 warnings in 58 files.
assert 1433 == 0
```

1433 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-a36436f98f49"></a>
## v1.28.0 samd micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-micropython-zuban]

```text
zuban found 1453 errors and 0 warnings in 61 files.
assert 1453 == 0
```

1453 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-bf3aea81d794"></a>
## v1.28.0 samd samd - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-samd-zuban]

```text
zuban found 1433 errors and 0 warnings in 58 files.
assert 1433 == 0
```

1433 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-ff1c7000bba4"></a>
## v1.28.0 samd stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-stdlib-zuban]

```text
zuban found 1439 errors and 0 warnings in 63 files.
assert 1439 == 0
```

1439 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-cab8154bddf3"></a>
## v1.28.0 samd-seeed_wio_terminal asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-seeed_wio_terminal-asyncio-zuban]

```text
zuban found 1434 errors and 0 warnings in 59 files.
assert 1434 == 0
```

1434 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-e8dce36279b9"></a>
## v1.28.0 samd-seeed_wio_terminal machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-seeed_wio_terminal-machine-zuban]

```text
zuban found 1433 errors and 0 warnings in 58 files.
assert 1433 == 0
```

1433 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3b5c72472ae4"></a>
## v1.28.0 samd-seeed_wio_terminal micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-seeed_wio_terminal-micropython-zuban]

```text
zuban found 1453 errors and 0 warnings in 61 files.
assert 1453 == 0
```

1453 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-bef68f641628"></a>
## v1.28.0 samd-seeed_wio_terminal samd - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-seeed_wio_terminal-samd-zuban]

```text
zuban found 1433 errors and 0 warnings in 58 files.
assert 1433 == 0
```

1433 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-fcd318188ca0"></a>
## v1.28.0 samd-seeed_wio_terminal stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-samd-seeed_wio_terminal-stdlib-zuban]

```text
zuban found 1439 errors and 0 warnings in 63 files.
assert 1439 == 0
```

1439 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-564f50bc8bca"></a>
## v1.28.0 stm32 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-asyncio-zuban]

```text
zuban found 1451 errors and 0 warnings in 62 files.
assert 1451 == 0
```

1451 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-1ee54e0636af"></a>
## v1.28.0 stm32 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-machine-zuban]

```text
zuban found 1450 errors and 0 warnings in 61 files.
assert 1450 == 0
```

1450 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-f9edeaa71caa"></a>
## v1.28.0 stm32 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-micropython-zuban]

```text
zuban found 1470 errors and 0 warnings in 64 files.
assert 1470 == 0
```

1470 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-98c999e81047"></a>
## v1.28.0 stm32 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-stdlib-zuban]

```text
zuban found 1456 errors and 0 warnings in 66 files.
assert 1456 == 0
```

1456 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-116d4759e197"></a>
## v1.28.0 stm32 stm32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-stm32-zuban]

```text
zuban found 1451 errors and 0 warnings in 62 files.
assert 1451 == 0
```

1451 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-85842af44713"></a>
## v1.28.0 stm32-pybv11 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-pybv11-asyncio-zuban]

```text
zuban found 1451 errors and 0 warnings in 62 files.
assert 1451 == 0
```

1451 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-ed94bfd07749"></a>
## v1.28.0 stm32-pybv11 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-pybv11-machine-zuban]

```text
zuban found 1450 errors and 0 warnings in 61 files.
assert 1450 == 0
```

1450 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-161ae65c328f"></a>
## v1.28.0 stm32-pybv11 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-pybv11-micropython-zuban]

```text
zuban found 1470 errors and 0 warnings in 64 files.
assert 1470 == 0
```

1470 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-17f89b327b71"></a>
## v1.28.0 stm32-pybv11 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-pybv11-stdlib-zuban]

```text
zuban found 1456 errors and 0 warnings in 66 files.
assert 1456 == 0
```

1456 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-6de9bd0372aa"></a>
## v1.28.0 stm32-pybv11 stm32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-stm32-pybv11-stm32-zuban]

```text
zuban found 1451 errors and 0 warnings in 62 files.
assert 1451 == 0
```

1451 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-bc6883c37b36"></a>
## v1.28.0 unix asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-unix-asyncio-zuban]

```text
zuban found 1466 errors and 0 warnings in 61 files.
assert 1466 == 0
```

1466 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-c236d85352c5"></a>
## v1.28.0 unix micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-unix-micropython-zuban]

```text
zuban found 1486 errors and 0 warnings in 64 files.
assert 1485 == 0
```

1485 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-6c39dbcfe35a"></a>
## v1.28.0 unix stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-unix-stdlib-zuban]

```text
zuban found 1471 errors and 0 warnings in 65 files.
assert 1471 == 0
```

1471 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-42c390f3f44f"></a>
## v1.28.0 unix unix - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-unix-unix-zuban]

```text
zuban found 1465 errors and 0 warnings in 60 files.
assert 1465 == 0
```

1465 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-cf7512c5dbc6"></a>
## v1.28.0 webassembly micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-webassembly-micropython-zuban]

```text
zuban found 1456 errors and 0 warnings in 72 files.
assert 1455 == 0
```

1455 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-2c1755af47b9"></a>
## v1.28.0 webassembly stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-webassembly-stdlib-zuban]

```text
zuban found 1441 errors and 0 warnings in 73 files.
assert 1441 == 0
```

1441 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-13564aa52ba1"></a>
## v1.28.0 webassembly webassembly - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-webassembly-webassembly-zuban]

```text
zuban found 1441 errors and 0 warnings in 72 files.
assert 1441 == 0

"check_pyscript/check_config.py"(3,14): Cannot find implementation or library stub for module named "pyscript.context"
"check_pyscript/check_ffi_storage.py"(22,60): Argument 2 to "storage" has incompatible type "type[Preferences]"; expected "type[Storage]"
"check_pyscript/check_ffi_storage.py"(23,4): Unsupported target for indexed assignment ("Preferences")
"check_pyscript/check_modules.py"(18,58): Unexpected keyword argument "indent" for "stringify"
"check_pyscript/check_web.py"(53,4): "Style" has no attribute "__delitem__"
"check_pyscript/check_web.py"(55,0): "Classes" has no attribute "discard"
```

1435 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-9ca5fb1e8716"></a>
## v1.28.0 windows asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-windows-asyncio-zuban]

```text
zuban found 1431 errors and 0 warnings in 59 files.
assert 1431 == 0
```

1431 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-9faeae233f43"></a>
## v1.28.0 windows micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-windows-micropython-zuban]

```text
zuban found 1451 errors and 0 warnings in 62 files.
assert 1450 == 0
```

1450 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-00cc71b7c3b5"></a>
## v1.28.0 windows stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-windows-stdlib-zuban]

```text
zuban found 1436 errors and 0 warnings in 63 files.
assert 1436 == 0
```

1436 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-b2db9bc2001d"></a>
## v1.28.0 windows windows - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-windows-windows-zuban]

```text
zuban found 1430 errors and 0 warnings in 58 files.
assert 1430 == 0
```

1430 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-2b24a164b76c"></a>
## v1.27.0 esp32 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-asyncio-zuban]

```text
zuban found 1477 errors and 0 warnings in 62 files.
assert 1477 == 0
```

1477 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-2981d56633e1"></a>
## v1.27.0 esp32 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-bluetooth-zuban]

```text
zuban found 1476 errors and 0 warnings in 62 files.
assert 1476 == 0
```

1476 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-482d1751ec8d"></a>
## v1.27.0 esp32 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32-zuban]

```text
zuban found 1478 errors and 0 warnings in 63 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-0b8dbfc7be30"></a>
## v1.27.0 esp32 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-espnow-zuban]

```text
zuban found 1477 errors and 0 warnings in 62 files.
assert 1477 == 0
```

1477 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3b3e27a39f56"></a>
## v1.27.0 esp32 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-machine-zuban]

```text
zuban found 1476 errors and 0 warnings in 61 files.
assert 1476 == 0
```

1476 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-e8e96bdc4bad"></a>
## v1.27.0 esp32 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-micropython-zuban]

```text
zuban found 1496 errors and 0 warnings in 64 files.
assert 1496 == 0
```

1496 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-84092ddc62e0"></a>
## v1.27.0 esp32 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-networking-zuban]

```text
zuban found 1476 errors and 0 warnings in 61 files.
assert 1476 == 0
```

1476 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-caf697ee8ae3"></a>
## v1.27.0 esp32 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-stdlib-zuban]

```text
zuban found 1482 errors and 0 warnings in 66 files.
assert 1482 == 0
```

1482 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-897deeded841"></a>
## v1.27.0 esp32-esp32_generic_c6 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-asyncio-zuban]

```text
zuban found 1477 errors and 0 warnings in 62 files.
assert 1477 == 0
```

1477 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-418f853d2c41"></a>
## v1.27.0 esp32-esp32_generic_c6 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-bluetooth-zuban]

```text
zuban found 1476 errors and 0 warnings in 62 files.
assert 1476 == 0
```

1476 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-72753720762c"></a>
## v1.27.0 esp32-esp32_generic_c6 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-esp32-zuban]

```text
zuban found 1481 errors and 0 warnings in 65 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-5cb50ef4f25a"></a>
## v1.27.0 esp32-esp32_generic_c6 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-espnow-zuban]

```text
zuban found 1477 errors and 0 warnings in 62 files.
assert 1477 == 0
```

1477 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-7cb4994d8d44"></a>
## v1.27.0 esp32-esp32_generic_c6 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-machine-zuban]

```text
zuban found 1476 errors and 0 warnings in 61 files.
assert 1476 == 0
```

1476 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-2e6722240759"></a>
## v1.27.0 esp32-esp32_generic_c6 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-micropython-zuban]

```text
zuban found 1496 errors and 0 warnings in 64 files.
assert 1496 == 0
```

1496 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-255320df2dbc"></a>
## v1.27.0 esp32-esp32_generic_c6 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-networking-zuban]

```text
zuban found 1476 errors and 0 warnings in 61 files.
assert 1476 == 0
```

1476 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-53335321ca72"></a>
## v1.27.0 esp32-esp32_generic_c6 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_c6-stdlib-zuban]

```text
zuban found 1482 errors and 0 warnings in 66 files.
assert 1482 == 0
```

1482 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-7b6ec087f0aa"></a>
## v1.27.0 esp32-esp32_generic_s3 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-asyncio-zuban]

```text
zuban found 1477 errors and 0 warnings in 62 files.
assert 1477 == 0
```

1477 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-c141ccf56e63"></a>
## v1.27.0 esp32-esp32_generic_s3 bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-bluetooth-zuban]

```text
zuban found 1476 errors and 0 warnings in 62 files.
assert 1476 == 0
```

1476 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-ef4ad26ffa36"></a>
## v1.27.0 esp32-esp32_generic_s3 esp32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-esp32-zuban]

```text
zuban found 1479 errors and 0 warnings in 64 files.
assert 1478 == 0
```

1478 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-93c15cee2810"></a>
## v1.27.0 esp32-esp32_generic_s3 espnow - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-espnow-zuban]

```text
zuban found 1477 errors and 0 warnings in 62 files.
assert 1477 == 0
```

1477 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-e63b0ea9eb2b"></a>
## v1.27.0 esp32-esp32_generic_s3 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-machine-zuban]

```text
zuban found 1476 errors and 0 warnings in 61 files.
assert 1476 == 0
```

1476 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-b21fd363dece"></a>
## v1.27.0 esp32-esp32_generic_s3 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-micropython-zuban]

```text
zuban found 1496 errors and 0 warnings in 64 files.
assert 1496 == 0
```

1496 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-37470adfce6c"></a>
## v1.27.0 esp32-esp32_generic_s3 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-networking-zuban]

```text
zuban found 1476 errors and 0 warnings in 61 files.
assert 1476 == 0
```

1476 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-df8a6de50ce0"></a>
## v1.27.0 esp32-esp32_generic_s3 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp32-esp32_generic_s3-stdlib-zuban]

```text
zuban found 1482 errors and 0 warnings in 66 files.
assert 1482 == 0
```

1482 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-656c6f18b98a"></a>
## v1.27.0 esp8266 esp8266 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp8266-esp8266-zuban]

```text
zuban found 1458 errors and 0 warnings in 60 files.
assert 1458 == 0
```

1458 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-01b73cf97bac"></a>
## v1.27.0 esp8266 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp8266-machine-zuban]

```text
zuban found 1458 errors and 0 warnings in 60 files.
assert 1458 == 0
```

1458 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-11847a01706d"></a>
## v1.27.0 esp8266 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp8266-micropython-zuban]

```text
zuban found 1466 errors and 0 warnings in 63 files.
assert 1465 == 0
```

1465 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-8576ca9f9732"></a>
## v1.27.0 esp8266 networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp8266-networking-zuban]

```text
zuban found 1458 errors and 0 warnings in 60 files.
assert 1458 == 0
```

1458 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-93fb0e5e3b15"></a>
## v1.27.0 esp8266 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-esp8266-stdlib-zuban]

```text
zuban found 1464 errors and 0 warnings in 65 files.
assert 1464 == 0
```

1464 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-0880dad7ddbb"></a>
## v1.27.0 rp2-rpi_pico2 asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2-asm_pio-zuban]

```text
zuban found 1453 errors and 0 warnings in 63 files.
assert 1453 == 0
```

1453 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-0ff18325a3bd"></a>
## v1.27.0 rp2-rpi_pico2 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2-asyncio-zuban]

```text
zuban found 1453 errors and 0 warnings in 63 files.
assert 1453 == 0
```

1453 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-54765a33d91a"></a>
## v1.27.0 rp2-rpi_pico2 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2-machine-zuban]

```text
zuban found 1452 errors and 0 warnings in 62 files.
assert 1452 == 0
```

1452 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-b6802158a238"></a>
## v1.27.0 rp2-rpi_pico2 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2-micropython-zuban]

```text
zuban found 1472 errors and 0 warnings in 65 files.
assert 1472 == 0
```

1472 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-1de6a32c5824"></a>
## v1.27.0 rp2-rpi_pico2 rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2-rp2-zuban]

```text
zuban found 1454 errors and 0 warnings in 64 files.
assert 1453 == 0
```

1453 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-d8f4e81b94d7"></a>
## v1.27.0 rp2-rpi_pico2 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2-stdlib-zuban]

```text
zuban found 1458 errors and 0 warnings in 67 files.
assert 1458 == 0
```

1458 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-521606fab1db"></a>
## v1.27.0 rp2-rpi_pico2_w asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-asm_pio-zuban]

```text
zuban found 1487 errors and 0 warnings in 63 files.
assert 1487 == 0
```

1487 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-d1f2152afaa5"></a>
## v1.27.0 rp2-rpi_pico2_w asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-asyncio-zuban]

```text
zuban found 1487 errors and 0 warnings in 63 files.
assert 1487 == 0
```

1487 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-f1ed93c2a710"></a>
## v1.27.0 rp2-rpi_pico2_w machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-machine-zuban]

```text
zuban found 1486 errors and 0 warnings in 62 files.
assert 1486 == 0
```

1486 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-e7df705b81f5"></a>
## v1.27.0 rp2-rpi_pico2_w micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-micropython-zuban]

```text
zuban found 1506 errors and 0 warnings in 65 files.
assert 1506 == 0
```

1506 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-32c10dc71c4b"></a>
## v1.27.0 rp2-rpi_pico2_w networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-networking-zuban]

```text
zuban found 1486 errors and 0 warnings in 62 files.
assert 1486 == 0
```

1486 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3e508cb9434f"></a>
## v1.27.0 rp2-rpi_pico2_w rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-rp2-zuban]

```text
zuban found 1487 errors and 0 warnings in 63 files.
assert 1487 == 0
```

1487 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-72d80eb95d0e"></a>
## v1.27.0 rp2-rpi_pico2_w stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico2_w-stdlib-zuban]

```text
zuban found 1492 errors and 0 warnings in 67 files.
assert 1492 == 0
```

1492 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-003f96bb9d82"></a>
## v1.27.0 rp2-rpi_pico_w aioble - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-aioble-zuban]

```text
zuban found 1489 errors and 0 warnings in 63 files.
assert 1489 == 0
```

1489 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-f39bd25f0954"></a>
## v1.27.0 rp2-rpi_pico_w asm_pio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-asm_pio-zuban]

```text
zuban found 1487 errors and 0 warnings in 63 files.
assert 1487 == 0
```

1487 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-e4dfa13308d3"></a>
## v1.27.0 rp2-rpi_pico_w asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-asyncio-zuban]

```text
zuban found 1487 errors and 0 warnings in 63 files.
assert 1487 == 0
```

1487 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-f2be9486ca21"></a>
## v1.27.0 rp2-rpi_pico_w bluetooth - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-bluetooth-zuban]

```text
zuban found 1486 errors and 0 warnings in 63 files.
assert 1486 == 0
```

1486 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-fdd8cf26550a"></a>
## v1.27.0 rp2-rpi_pico_w machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-machine-zuban]

```text
zuban found 1486 errors and 0 warnings in 62 files.
assert 1486 == 0
```

1486 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-63bc3e8b43d6"></a>
## v1.27.0 rp2-rpi_pico_w micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-micropython-zuban]

```text
zuban found 1506 errors and 0 warnings in 65 files.
assert 1506 == 0
```

1506 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-e09e9bb96e39"></a>
## v1.27.0 rp2-rpi_pico_w networking - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-networking-zuban]

```text
zuban found 1486 errors and 0 warnings in 62 files.
assert 1486 == 0
```

1486 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-e5c52ea46d81"></a>
## v1.27.0 rp2-rpi_pico_w rp2 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-rp2-zuban]

```text
zuban found 1487 errors and 0 warnings in 63 files.
assert 1487 == 0
```

1487 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3f2de5b776ff"></a>
## v1.27.0 rp2-rpi_pico_w stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-rp2-rpi_pico_w-stdlib-zuban]

```text
zuban found 1492 errors and 0 warnings in 67 files.
assert 1492 == 0
```

1492 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-bf7e19fdb313"></a>
## v1.27.0 samd asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-asyncio-zuban]

```text
zuban found 1432 errors and 0 warnings in 59 files.
assert 1432 == 0
```

1432 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-270b20692e18"></a>
## v1.27.0 samd machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-machine-zuban]

```text
zuban found 1431 errors and 0 warnings in 58 files.
assert 1431 == 0
```

1431 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-456f5ab9c43d"></a>
## v1.27.0 samd micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-micropython-zuban]

```text
zuban found 1451 errors and 0 warnings in 61 files.
assert 1451 == 0
```

1451 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-1e149b40f809"></a>
## v1.27.0 samd samd - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-samd-zuban]

```text
zuban found 1431 errors and 0 warnings in 58 files.
assert 1431 == 0
```

1431 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-4c414cb65e82"></a>
## v1.27.0 samd stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-stdlib-zuban]

```text
zuban found 1437 errors and 0 warnings in 63 files.
assert 1437 == 0
```

1437 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-5a64e1b5a309"></a>
## v1.27.0 samd-seeed_wio_terminal asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-seeed_wio_terminal-asyncio-zuban]

```text
zuban found 1432 errors and 0 warnings in 59 files.
assert 1432 == 0
```

1432 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-28eaa6495309"></a>
## v1.27.0 samd-seeed_wio_terminal machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-seeed_wio_terminal-machine-zuban]

```text
zuban found 1431 errors and 0 warnings in 58 files.
assert 1431 == 0
```

1431 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-a9a7941b268c"></a>
## v1.27.0 samd-seeed_wio_terminal micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-seeed_wio_terminal-micropython-zuban]

```text
zuban found 1451 errors and 0 warnings in 61 files.
assert 1451 == 0
```

1451 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-8c02a4e8a6bb"></a>
## v1.27.0 samd-seeed_wio_terminal samd - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-seeed_wio_terminal-samd-zuban]

```text
zuban found 1431 errors and 0 warnings in 58 files.
assert 1431 == 0
```

1431 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-a1960f3f4d98"></a>
## v1.27.0 samd-seeed_wio_terminal stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-samd-seeed_wio_terminal-stdlib-zuban]

```text
zuban found 1437 errors and 0 warnings in 63 files.
assert 1437 == 0
```

1437 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-c34f4e7bc4ed"></a>
## v1.27.0 stm32 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-asyncio-zuban]

```text
zuban found 1451 errors and 0 warnings in 62 files.
assert 1451 == 0
```

1451 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-a0150e2eac65"></a>
## v1.27.0 stm32 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-machine-zuban]

```text
zuban found 1450 errors and 0 warnings in 61 files.
assert 1450 == 0
```

1450 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-92bc4925f64d"></a>
## v1.27.0 stm32 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-micropython-zuban]

```text
zuban found 1470 errors and 0 warnings in 64 files.
assert 1470 == 0
```

1470 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-bf548b6fb736"></a>
## v1.27.0 stm32 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-stdlib-zuban]

```text
zuban found 1456 errors and 0 warnings in 66 files.
assert 1456 == 0
```

1456 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-def46d1d7634"></a>
## v1.27.0 stm32 stm32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-stm32-zuban]

```text
zuban found 1451 errors and 0 warnings in 62 files.
assert 1451 == 0
```

1451 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-3e1aeb6f9208"></a>
## v1.27.0 stm32-pybv11 asyncio - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-pybv11-asyncio-zuban]

```text
zuban found 1451 errors and 0 warnings in 62 files.
assert 1451 == 0
```

1451 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-4c82fca7bc6e"></a>
## v1.27.0 stm32-pybv11 machine - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-pybv11-machine-zuban]

```text
zuban found 1450 errors and 0 warnings in 61 files.
assert 1450 == 0
```

1450 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-559c0fcf1e3d"></a>
## v1.27.0 stm32-pybv11 micropython - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-pybv11-micropython-zuban]

```text
zuban found 1470 errors and 0 warnings in 64 files.
assert 1470 == 0
```

1470 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-5e271f47e7aa"></a>
## v1.27.0 stm32-pybv11 stdlib - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-pybv11-stdlib-zuban]

```text
zuban found 1456 errors and 0 warnings in 66 files.
assert 1456 == 0
```

1456 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

<a id="typecheck-detail-zuban-9d099f57b260"></a>
## v1.27.0 stm32-pybv11 stm32 - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.27.0-stm32-pybv11-stm32-zuban]

```text
zuban found 1451 errors and 0 warnings in 62 files.
assert 1451 == 0
```

1451 shared diagnostics omitted; see [Shared diagnostics](#shared-diagnostics).

## Shared diagnostics

```text
"_mpy_shed/IRQs.pyi"(39,18): Unsupported left operand type for | ("_SpecialForm") (Reported by 260 tests)
"_mpy_shed/IRQs.pyi"(39,6): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/__init__.pyi"(49,16): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/__init__.pyi"(49,28): Unsupported left operand type for | ("type[str]") (Reported by 260 tests)
"_mpy_shed/__init__.pyi"(53,10): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/__init__.pyi"(53,22): Unsupported left operand type for | ("type[str]") (Reported by 260 tests)
"_mpy_shed/__init__.pyi"(54,14): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/__init__.pyi"(58,11): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/_mp_available.pyi"(36,4): An implementation for an overloaded function is not allowed in a stub file (Reported by 260 tests)
"_mpy_shed/_mpy_builtins.pyi"(13,6): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/_mpy_builtins.pyi"(27,56): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/blockdevice.pyi"(28,30): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/blockdevice.pyi"(29,22): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/buffer_mp.pyi"(7,16): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/buffer_mp.pyi"(7,28): Unsupported left operand type for | ("type[bytearray]") (Reported by 260 tests)
"_mpy_shed/buffer_mp.pyi"(8,16): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/buffer_mp.pyi"(8,28): Unsupported left operand type for | ("type[bytearray]") (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(104,22): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(105,26): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(118,72): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(124,73): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(131,70): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(131,8): Signatures of "__ior__" and "__or__" are incompatible (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(133,63): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(133,8): Signatures of "__ior__" and "__or__" are incompatible (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(156,39): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(162,46): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(163,47): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(164,47): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(165,33): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(166,34): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(167,34): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(172,22): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(173,26): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(192,26): Name "UserString" is not defined (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(207,59): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(208,35): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(209,39): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(210,40): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(211,41): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(212,33): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(213,34): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(214,36): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(215,44): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(216,28): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(217,26): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(218,48): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(226,46): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(244,47): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(245,23): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(246,50): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(250,63): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(251,63): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(255,9): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(258,47): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(260,50): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(267,49): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(268,26): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(269,23): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(270,39): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(271,23): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(272,35): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(281,22): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(291,26): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(298,39): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(299,50): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(300,29): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(300,41): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(301,40): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(302,41): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(309,52): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(320,22): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(356,57): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(357,57): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(358,57): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(359,56): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(397,22): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(429,8): Signature of "__or__" incompatible with supertype "builtins.dict" (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(430,54): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(434,55): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(481,26): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(482,22): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(484,8): Signature of "__or__" incompatible with supertype "builtins.dict" (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(485,54): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(489,55): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(496,70): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(498,25): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(524,22): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(540,54): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(544,55): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(549,70): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(549,8): Signatures of "__ior__" and "__or__" are incompatible (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(551,63): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/collections/__init__.pyi"(551,8): Signatures of "__ior__" and "__or__" are incompatible (Reported by 260 tests)
"_mpy_shed/io_modes.pyi"(17,23): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/io_modes.pyi"(51,22): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/io_modes.pyi"(52,22): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/io_modes.pyi"(55,15): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/io_modes.pyi"(57,25): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/io_modes.pyi"(83,24): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/io_modes.pyi"(84,24): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/io_modes.pyi"(85,17): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/os_vfs.pyi"(23,18): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/os_vfs.pyi"(6,15): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/pathlike.pyi"(15,15): Name "ABC" is not defined (Reported by 260 tests)
"_mpy_shed/time_mp.pyi"(13,13): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/time_mp.pyi"(14,13): Invalid type comment or annotation (Reported by 260 tests)
"_mpy_shed/time_mp.pyi"(15,12): Invalid type comment or annotation (Reported by 260 tests)
"_pyscript.pyi"(16,7): Cannot find implementation or library stub for module named "storage" (Reported by 6 tests)
"_pyscript.pyi"(21,28): Name "JSModule" is not defined (Reported by 6 tests)
"_pyscript.pyi"(28,15): Name "XWorker" is not defined (Reported by 6 tests)
"_pyscript.pyi"(31,0): "classmethod" used with a non-method (Reported by 6 tests)
"aioespnow.pyi"(11,19): Module "typing" has no attribute "TypeAlias" (Reported by 24 tests)
"binascii.pyi"(25,10): Name "hexlify" is not defined (Reported by 3 tests)
"binascii.pyi"(26,10): Name "hexlify" is not defined (Reported by 3 tests)
"bluetooth.pyi"(38,7): Invalid type comment or annotation (Reported by 86 tests)
"bluetooth.pyi"(39,13): Invalid type comment or annotation (Reported by 86 tests)
"bluetooth.pyi"(40,17): Invalid type comment or annotation (Reported by 86 tests)
"bluetooth.pyi"(40,29): Unsupported left operand type for | ("type[tuple[UUID, Any]]") (Reported by 86 tests)
"bluetooth.pyi"(40,7): Invalid type comment or annotation (Reported by 46 tests)
"bluetooth.pyi"(41,10): Invalid type comment or annotation (Reported by 86 tests)
"bluetooth.pyi"(41,13): Invalid type comment or annotation (Reported by 46 tests)
"bluetooth.pyi"(42,17): Invalid type comment or annotation (Reported by 46 tests)
"bluetooth.pyi"(42,29): Unsupported left operand type for | ("type[tuple[UUID, Any]]") (Reported by 46 tests)
"bluetooth.pyi"(43,10): Invalid type comment or annotation (Reported by 46 tests)
"bluetooth.pyi"(610,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 38 tests)
"bluetooth.pyi"(611,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 22 tests)
"bluetooth.pyi"(628,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 48 tests)
"bluetooth.pyi"(629,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 24 tests)
"bluetooth.pyi"(674,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 38 tests)
"bluetooth.pyi"(675,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 22 tests)
"bluetooth.pyi"(692,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 48 tests)
"bluetooth.pyi"(693,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 24 tests)
"bluetooth.pyi"(756,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 38 tests)
"bluetooth.pyi"(757,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 22 tests)
"bluetooth.pyi"(765,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 38 tests)
"bluetooth.pyi"(766,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 22 tests)
"bluetooth.pyi"(774,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 48 tests)
"bluetooth.pyi"(775,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 24 tests)
"bluetooth.pyi"(783,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 48 tests)
"bluetooth.pyi"(784,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 24 tests)
"btree.pyi"(106,5): Name "btree" is not defined (Reported by 33 tests)
"btree.pyi"(108,5): Name "btree" is not defined (Reported by 33 tests)
"check_asm_pio_code_03.py"(13,20): Cannot assign to final name "TYPE_CHECKING" (Reported by 13 tests)
"check_collections/check_namedtuple.py"(7,6): "tuple[Any, ...]" has no attribute "name" (Reported by 44 tests)
"check_collections/check_namedtuple.py"(8,7): "tuple[Any, ...]" has no attribute "name" (Reported by 44 tests)
"check_collections/check_namedtuple_2.py"(9,32): Variable "check_collections.check_namedtuple_2.WifiConfig" is not valid as a type (Reported by 44 tests)
"check_demo/aiorepl.py"(198,37): Argument 1 to "write" of "IO" has incompatible type "bytes"; expected "str" (Reported by 38 tests)
"check_espnow.py"(53,6): "ESPNow" has no attribute "peers_table" (Reported by 6 tests)
"check_io.py"(11,24): Argument 1 to "BufferedWriter" has incompatible type "TextIOWrapper[_WrappedBuffer]"; expected "RawIOBase" (Reported by 43 tests)
"check_io.py"(6,23): Argument 1 to "StringIO" has incompatible type "int"; expected "str | None" (Reported by 43 tests)
"check_machine/check_devices.py"(28,11): "None" has no attribute "__iter__" (not iterable) (Reported by 9 tests)
"check_machine/check_ds18x20.py"(13,11): "None" has no attribute "__iter__" (not iterable) (Reported by 13 tests)
"check_machine/check_sleep.py"(18,4): Statement is unreachable (Reported by 9 tests)
"check_micropython/check_viper.py"(10,56): Name "ptr" is not defined (Reported by 27 tests)
"check_micropython/check_viper.py"(10,64): Name "uint" is not defined (Reported by 27 tests)
"check_micropython/check_viper.py"(11,19): Name "ptr8" is not defined (Reported by 27 tests)
"check_micropython/check_viper.py"(12,23): Name "ptr16" is not defined (Reported by 27 tests)
"check_micropython/check_viper.py"(13,19): Name "ptr32" is not defined (Reported by 27 tests)
"check_micropython/check_viper.py"(14,15): Name "uint" is not defined (Reported by 27 tests)
"check_micropython/check_viper.py"(5,23): Name "uint" is not defined (Reported by 27 tests)
"check_pyb.py"(18,4): Statement is unreachable (Reported by 6 tests)
"check_uctypes.py"(30,7): "__getattr__" of "struct" does not return a value (it only ever returns None) (Reported by 41 tests)
"check_uctypes.py"(31,7): "__getattr__" of "struct" does not return a value (it only ever returns None) (Reported by 41 tests)
"check_uctypes.py"(32,22): "__getattr__" of "struct" does not return a value (it only ever returns None) (Reported by 41 tests)
"check_uctypes.py"(32,22): Argument 1 to "hex" has incompatible type "None"; expected "SupportsIndex" (Reported by 41 tests)
"check_uctypes.py"(56,12): "__getattr__" of "struct" does not return a value (it only ever returns None) (Reported by 41 tests)
"check_uctypes.py"(56,12): Value of type "None" is not indexable (Reported by 41 tests)
"check_uctypes.py"(81,0): "None" has no attribute "WDGTB" (Reported by 41 tests)
"check_uctypes.py"(81,0): "__getattr__" of "struct" does not return a value (it only ever returns None) (Reported by 41 tests)
"check_uctypes.py"(82,0): "None" has no attribute "WDGA" (Reported by 41 tests)
"check_uctypes.py"(82,0): "__getattr__" of "struct" does not return a value (it only ever returns None) (Reported by 41 tests)
"check_uctypes.py"(83,26): "None" has no attribute "T" (Reported by 41 tests)
"check_uctypes.py"(83,26): "__getattr__" of "struct" does not return a value (it only ever returns None) (Reported by 41 tests)
"check_uio.py"(7,24): Argument 1 to "StringIO" has incompatible type "int"; expected "str | None" (Reported by 43 tests)
"cmath.pyi"(25,16): Unsupported left operand type for | ("type[SupportsFloat]") (Reported by 132 tests)
"cmath.pyi"(25,4): Invalid type comment or annotation (Reported by 132 tests)
"cmath.pyi"(27,16): Unsupported left operand type for | ("type[SupportsFloat]") (Reported by 82 tests)
"cmath.pyi"(27,4): Invalid type comment or annotation (Reported by 82 tests)
"community_code/sample_1.py"(71,19): "None" has no attribute "__aenter__" (Reported by 3 tests)
"community_code/sample_1.py"(71,19): "None" has no attribute "__aexit__" (Reported by 3 tests)
"community_code/sample_1.py"(71,19): Function does not return a value (it only ever returns None) (Reported by 3 tests)
"cryptolib.pyi"(126,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 51 tests)
"cryptolib.pyi"(147,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 51 tests)
"cryptolib.pyi"(39,55): Variable "cryptolib._WB" is not valid as a type (Reported by 67 tests)
"cryptolib.pyi"(39,66): Variable "cryptolib._WB" is not valid as a type (Reported by 67 tests)
"cryptolib.pyi"(41,55): Variable "cryptolib._WB" is not valid as a type (Reported by 67 tests)
"cryptolib.pyi"(41,66): Variable "cryptolib._WB" is not valid as a type (Reported by 67 tests)
"cryptolib.pyi"(42,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 51 tests)
"cryptolib.pyi"(51,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 51 tests)
"cryptolib.pyi"(56,55): Variable "cryptolib._WB" is not valid as a type (Reported by 67 tests)
"cryptolib.pyi"(56,66): Variable "cryptolib._WB" is not valid as a type (Reported by 67 tests)
"cryptolib.pyi"(58,55): Variable "cryptolib._WB" is not valid as a type (Reported by 67 tests)
"cryptolib.pyi"(58,66): Variable "cryptolib._WB" is not valid as a type (Reported by 67 tests)
"cryptolib.pyi"(72,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 51 tests)
"cryptolib.pyi"(78,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 51 tests)
"datetime.pyi"(113,14): Return type "None" of "__str__" incompatible with return type "str" in supertype "object" (Reported by 6 tests)
"esp32.pyi"(21,5): Cannot find implementation or library stub for module named "vfs" (Reported by 8 tests)
"esp32.pyi"(600,4): Cannot override writable attribute "RUNNING" with a final one (Reported by 8 tests)
"esp32.pyi"(606,4): Cannot override writable attribute "TYPE_APP" with a final one (Reported by 8 tests)
"esp32.pyi"(612,4): Cannot override writable attribute "TYPE_DATA" with a final one (Reported by 8 tests)
"esp32.pyi"(618,4): Cannot override writable attribute "BOOT" with a final one (Reported by 8 tests)
"espnow.pyi"(88,13): Invalid type comment or annotation (Reported by 48 tests)
"espnow.pyi"(89,11): Invalid type comment or annotation (Reported by 48 tests)
"espnow.pyi"(89,13): Invalid type comment or annotation (Reported by 10 tests)
"espnow.pyi"(90,11): Invalid type comment or annotation (Reported by 10 tests)
"espnow.pyi"(90,13): Invalid type comment or annotation (Reported by 24 tests)
"espnow.pyi"(91,11): Invalid type comment or annotation (Reported by 24 tests)
"espnow.pyi"(91,13): Invalid type comment or annotation (Reported by 5 tests)
"espnow.pyi"(92,11): Invalid type comment or annotation (Reported by 5 tests)
"hashlib.pyi"(60,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 71 tests)
"hashlib.pyi"(66,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 71 tests)
"hashlib.pyi"(85,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 20 tests)
"hashlib.pyi"(91,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 20 tests)
"hashlib.pyi"(93,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 51 tests)
"hashlib.pyi"(99,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 51 tests)
"heapq.pyi"(27,23): Variable "heapq._T" is not valid as a type (Reported by 162 tests)
"heapq.pyi"(27,34): Variable "heapq._T" is not valid as a type (Reported by 162 tests)
"heapq.pyi"(29,23): Variable "heapq._T" is not valid as a type (Reported by 97 tests)
"heapq.pyi"(29,34): Variable "heapq._T" is not valid as a type (Reported by 97 tests)
"heapq.pyi"(36,24): Variable "heapq._T" is not valid as a type (Reported by 162 tests)
"heapq.pyi"(36,35): Variable "heapq._T" is not valid as a type (Reported by 162 tests)
"heapq.pyi"(38,24): Variable "heapq._T" is not valid as a type (Reported by 97 tests)
"heapq.pyi"(38,35): Variable "heapq._T" is not valid as a type (Reported by 97 tests)
"inspect.pyi"(16,4): Method must have at least one argument. Did you forget the "self" argument? (Reported by 6 tests)
"machine.pyi"(105,0): Overloaded function signature 5 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 10 tests)
"machine.pyi"(1091,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 10 tests)
"machine.pyi"(1093,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 10 tests)
"machine.pyi"(1105,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 34 tests)
"machine.pyi"(1107,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 34 tests)
"machine.pyi"(1116,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 22 tests)
"machine.pyi"(1118,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 22 tests)
"machine.pyi"(113,0): Overloaded function signature 6 will never be matched: signature 3's parameter type(s) are the same or broader (Reported by 10 tests)
"machine.pyi"(1228,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 34 tests)
"machine.pyi"(1230,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 34 tests)
"machine.pyi"(1628,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 10 tests)
"machine.pyi"(1630,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 10 tests)
"machine.pyi"(1654,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 5 tests)
"machine.pyi"(1656,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 5 tests)
"machine.pyi"(1661,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 5 tests)
"machine.pyi"(1663,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 5 tests)
"machine.pyi"(1690,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 5 tests)
"machine.pyi"(1692,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 5 tests)
"machine.pyi"(1764,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 10 tests)
"machine.pyi"(1766,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 10 tests)
"machine.pyi"(2272,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(2274,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(2307,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 10 tests)
"machine.pyi"(2309,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 10 tests)
"machine.pyi"(24,5): Cannot find implementation or library stub for module named "vfs" (Reported by 18 tests)
"machine.pyi"(2574,47): Name "adcchannel" is not defined (Reported by 5 tests)
"machine.pyi"(2576,33): Name "adcchannel" is not defined (Reported by 5 tests)
"machine.pyi"(2578,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 5 tests)
"machine.pyi"(2578,42): Name "adcchannel" is not defined (Reported by 5 tests)
"machine.pyi"(2604,47): Name "adcchannel" is not defined (Reported by 5 tests)
"machine.pyi"(2606,33): Name "adcchannel" is not defined (Reported by 5 tests)
"machine.pyi"(2608,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 5 tests)
"machine.pyi"(2608,42): Name "adcchannel" is not defined (Reported by 5 tests)
"machine.pyi"(2756,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(2758,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(28,13): Invalid type comment or annotation (Reported by 4 tests)
"machine.pyi"(28,25): Unsupported left operand type for | ("type[tuple[int, int, int]]") (Reported by 4 tests)
"machine.pyi"(2805,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(2807,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(281,18): Unsupported left operand type for | ("type[int]") (Reported by 4 tests)
"machine.pyi"(281,6): Invalid type comment or annotation (Reported by 4 tests)
"machine.pyi"(282,10): Invalid type comment or annotation (Reported by 4 tests)
"machine.pyi"(282,22): Unsupported left operand type for | ("type[Pin]") (Reported by 4 tests)
"machine.pyi"(283,13): Invalid type comment or annotation (Reported by 4 tests)
"machine.pyi"(283,25): Unsupported left operand type for | ("type[tuple[int, int, int]]") (Reported by 4 tests)
"machine.pyi"(284,17): Invalid type comment or annotation (Reported by 4 tests)
"machine.pyi"(285,15): Invalid type comment or annotation (Reported by 4 tests)
"machine.pyi"(286,14): Invalid type comment or annotation (Reported by 4 tests)
"machine.pyi"(29,17): Invalid type comment or annotation (Reported by 4 tests)
"machine.pyi"(291,47): Name "adcchannel" is not defined (Reported by 4 tests)
"machine.pyi"(2921,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(2923,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(293,33): Name "adcchannel" is not defined (Reported by 4 tests)
"machine.pyi"(295,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 4 tests)
"machine.pyi"(295,42): Name "adcchannel" is not defined (Reported by 4 tests)
"machine.pyi"(2970,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(2972,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(30,15): Invalid type comment or annotation (Reported by 4 tests)
"machine.pyi"(3087,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(3089,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(31,14): Invalid type comment or annotation (Reported by 4 tests)
"machine.pyi"(31,18): Unsupported left operand type for | ("type[int]") (Reported by 22 tests)
"machine.pyi"(31,6): Invalid type comment or annotation (Reported by 22 tests)
"machine.pyi"(3155,47): Name "adcchannel" is not defined (Reported by 10 tests)
"machine.pyi"(3157,33): Name "adcchannel" is not defined (Reported by 10 tests)
"machine.pyi"(3159,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 10 tests)
"machine.pyi"(3159,42): Name "adcchannel" is not defined (Reported by 10 tests)
"machine.pyi"(32,13): Invalid type comment or annotation (Reported by 34 tests)
"machine.pyi"(32,18): Unsupported left operand type for | ("type[int]") (Reported by 4 tests)
"machine.pyi"(32,21): Unsupported left operand type for | ("type[Pin]") (Reported by 22 tests)
"machine.pyi"(32,25): Unsupported left operand type for | ("type[tuple[int, int, int]]") (Reported by 34 tests)
"machine.pyi"(32,6): Invalid type comment or annotation (Reported by 4 tests)
"machine.pyi"(32,9): Invalid type comment or annotation (Reported by 22 tests)
"machine.pyi"(3214,47): Name "adcchannel" is not defined (Reported by 6 tests)
"machine.pyi"(3216,33): Name "adcchannel" is not defined (Reported by 6 tests)
"machine.pyi"(3218,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 6 tests)
"machine.pyi"(3218,42): Name "adcchannel" is not defined (Reported by 6 tests)
"machine.pyi"(3219,47): Name "adcchannel" is not defined (Reported by 21 tests)
"machine.pyi"(3221,33): Name "adcchannel" is not defined (Reported by 21 tests)
"machine.pyi"(3223,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 21 tests)
"machine.pyi"(3223,42): Name "adcchannel" is not defined (Reported by 21 tests)
"machine.pyi"(3224,47): Name "adcchannel" is not defined (Reported by 7 tests)
"machine.pyi"(3226,33): Name "adcchannel" is not defined (Reported by 7 tests)
"machine.pyi"(3228,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 7 tests)
"machine.pyi"(3228,42): Name "adcchannel" is not defined (Reported by 7 tests)
"machine.pyi"(33,10): Invalid type comment or annotation (Reported by 4 tests)
"machine.pyi"(33,17): Invalid type comment or annotation (Reported by 34 tests)
"machine.pyi"(33,22): Unsupported left operand type for | ("type[Pin]") (Reported by 4 tests)
"machine.pyi"(3346,47): Name "adcchannel" is not defined (Reported by 10 tests)
"machine.pyi"(3348,33): Name "adcchannel" is not defined (Reported by 10 tests)
"machine.pyi"(3350,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 10 tests)
"machine.pyi"(3350,42): Name "adcchannel" is not defined (Reported by 10 tests)
"machine.pyi"(3373,47): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3375,33): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3377,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 8 tests)
"machine.pyi"(3377,42): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3384,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(3386,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(3389,47): Name "adcchannel" is not defined (Reported by 6 tests)
"machine.pyi"(3391,33): Name "adcchannel" is not defined (Reported by 6 tests)
"machine.pyi"(3393,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 6 tests)
"machine.pyi"(3393,42): Name "adcchannel" is not defined (Reported by 6 tests)
"machine.pyi"(3394,47): Name "adcchannel" is not defined (Reported by 21 tests)
"machine.pyi"(3396,33): Name "adcchannel" is not defined (Reported by 21 tests)
"machine.pyi"(3398,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 21 tests)
"machine.pyi"(3398,42): Name "adcchannel" is not defined (Reported by 21 tests)
"machine.pyi"(3399,47): Name "adcchannel" is not defined (Reported by 7 tests)
"machine.pyi"(34,15): Invalid type comment or annotation (Reported by 34 tests)
"machine.pyi"(3401,33): Name "adcchannel" is not defined (Reported by 7 tests)
"machine.pyi"(3403,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 7 tests)
"machine.pyi"(3403,42): Name "adcchannel" is not defined (Reported by 7 tests)
"machine.pyi"(3422,47): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3424,33): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3426,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 8 tests)
"machine.pyi"(3426,42): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3463,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(3465,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(35,14): Invalid type comment or annotation (Reported by 34 tests)
"machine.pyi"(3540,47): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3542,33): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3544,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 8 tests)
"machine.pyi"(3544,42): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3561,47): Name "adcchannel" is not defined (Reported by 10 tests)
"machine.pyi"(3563,33): Name "adcchannel" is not defined (Reported by 10 tests)
"machine.pyi"(3565,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 10 tests)
"machine.pyi"(3565,42): Name "adcchannel" is not defined (Reported by 10 tests)
"machine.pyi"(3589,47): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3591,33): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3593,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 8 tests)
"machine.pyi"(3593,42): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(36,18): Unsupported left operand type for | ("type[int]") (Reported by 34 tests)
"machine.pyi"(36,6): Invalid type comment or annotation (Reported by 34 tests)
"machine.pyi"(3628,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(3630,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 8 tests)
"machine.pyi"(3653,47): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3655,33): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3657,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 8 tests)
"machine.pyi"(3657,42): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(369,47): Name "adcchannel" is not defined (Reported by 4 tests)
"machine.pyi"(37,10): Invalid type comment or annotation (Reported by 34 tests)
"machine.pyi"(37,18): Unsupported left operand type for | ("type[int]") (Reported by 20 tests)
"machine.pyi"(37,22): Unsupported left operand type for | ("type[Pin]") (Reported by 34 tests)
"machine.pyi"(37,6): Invalid type comment or annotation (Reported by 20 tests)
"machine.pyi"(371,33): Name "adcchannel" is not defined (Reported by 4 tests)
"machine.pyi"(373,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 4 tests)
"machine.pyi"(373,42): Name "adcchannel" is not defined (Reported by 4 tests)
"machine.pyi"(38,13): Invalid type comment or annotation (Reported by 20 tests)
"machine.pyi"(38,21): Unsupported left operand type for | ("type[Pin]") (Reported by 20 tests)
"machine.pyi"(38,25): Unsupported left operand type for | ("type[tuple[int, int, int]]") (Reported by 20 tests)
"machine.pyi"(38,9): Invalid type comment or annotation (Reported by 20 tests)
"machine.pyi"(3837,47): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3839,33): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(3841,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 8 tests)
"machine.pyi"(3841,42): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(39,17): Invalid type comment or annotation (Reported by 20 tests)
"machine.pyi"(39,18): Unsupported left operand type for | ("type[int]") (Reported by 5 tests)
"machine.pyi"(39,6): Invalid type comment or annotation (Reported by 5 tests)
"machine.pyi"(3917,47): Name "adcchannel" is not defined (Reported by 10 tests)
"machine.pyi"(3919,33): Name "adcchannel" is not defined (Reported by 10 tests)
"machine.pyi"(3921,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 10 tests)
"machine.pyi"(3921,42): Name "adcchannel" is not defined (Reported by 10 tests)
"machine.pyi"(40,13): Invalid type comment or annotation (Reported by 5 tests)
"machine.pyi"(40,15): Invalid type comment or annotation (Reported by 20 tests)
"machine.pyi"(40,21): Unsupported left operand type for | ("type[Pin]") (Reported by 5 tests)
"machine.pyi"(40,25): Unsupported left operand type for | ("type[tuple[int, int, int]]") (Reported by 5 tests)
"machine.pyi"(40,9): Invalid type comment or annotation (Reported by 5 tests)
"machine.pyi"(41,14): Invalid type comment or annotation (Reported by 20 tests)
"machine.pyi"(41,17): Invalid type comment or annotation (Reported by 5 tests)
"machine.pyi"(42,15): Invalid type comment or annotation (Reported by 5 tests)
"machine.pyi"(42,18): Unsupported left operand type for | ("type[int]") (Reported by 20 tests)
"machine.pyi"(42,6): Invalid type comment or annotation (Reported by 20 tests)
"machine.pyi"(43,10): Invalid type comment or annotation (Reported by 20 tests)
"machine.pyi"(43,14): Invalid type comment or annotation (Reported by 5 tests)
"machine.pyi"(43,22): Unsupported left operand type for | ("type[Pin]") (Reported by 20 tests)
"machine.pyi"(44,18): Unsupported left operand type for | ("type[int]") (Reported by 5 tests)
"machine.pyi"(44,6): Invalid type comment or annotation (Reported by 5 tests)
"machine.pyi"(45,10): Invalid type comment or annotation (Reported by 5 tests)
"machine.pyi"(45,22): Unsupported left operand type for | ("type[Pin]") (Reported by 5 tests)
"machine.pyi"(462,47): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(464,33): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(466,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 8 tests)
"machine.pyi"(466,42): Name "adcchannel" is not defined (Reported by 8 tests)
"machine.pyi"(48,18): Unsupported left operand type for | ("type[int]") (Reported by 24 tests)
"machine.pyi"(48,6): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(49,12): Invalid type comment or annotation (Reported by 4 tests)
"machine.pyi"(49,13): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(49,21): Unsupported left operand type for | ("type[Pin]") (Reported by 24 tests)
"machine.pyi"(49,25): Unsupported left operand type for | ("type[tuple[int, int, int]]") (Reported by 24 tests)
"machine.pyi"(49,9): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(50,17): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(51,12): Invalid type comment or annotation (Reported by 114 tests)
"machine.pyi"(51,15): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(52,14): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(53,13): Invalid type comment or annotation (Reported by 67 tests)
"machine.pyi"(53,18): Unsupported left operand type for | ("type[int]") (Reported by 24 tests)
"machine.pyi"(53,25): Unsupported left operand type for | ("type[tuple[int, int, int]]") (Reported by 67 tests)
"machine.pyi"(53,6): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(54,10): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(54,17): Invalid type comment or annotation (Reported by 67 tests)
"machine.pyi"(54,22): Unsupported left operand type for | ("type[Pin]") (Reported by 24 tests)
"machine.pyi"(55,15): Invalid type comment or annotation (Reported by 67 tests)
"machine.pyi"(56,12): Invalid type comment or annotation (Reported by 111 tests)
"machine.pyi"(56,14): Invalid type comment or annotation (Reported by 67 tests)
"machine.pyi"(57,18): Unsupported left operand type for | ("type[int]") (Reported by 67 tests)
"machine.pyi"(57,6): Invalid type comment or annotation (Reported by 67 tests)
"machine.pyi"(58,10): Invalid type comment or annotation (Reported by 67 tests)
"machine.pyi"(58,13): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(58,22): Unsupported left operand type for | ("type[Pin]") (Reported by 67 tests)
"machine.pyi"(58,25): Unsupported left operand type for | ("type[tuple[int, int, int]]") (Reported by 24 tests)
"machine.pyi"(59,17): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(60,15): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(61,12): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(61,14): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(62,18): Unsupported left operand type for | ("type[int]") (Reported by 24 tests)
"machine.pyi"(62,6): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(63,10): Invalid type comment or annotation (Reported by 24 tests)
"machine.pyi"(63,22): Unsupported left operand type for | ("type[Pin]") (Reported by 24 tests)
"machine.pyi"(952,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 10 tests)
"machine.pyi"(954,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 10 tests)
"machine.pyi"(965,4): Cannot override final attribute "LSB" (previously declared in base class "SPI") (Reported by 10 tests)
"machine.pyi"(967,4): Cannot override final attribute "MSB" (previously declared in base class "SPI") (Reported by 10 tests)
"machine.pyi"(97,0): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 10 tests)
"micropython.pyi"(111,29): Variable "micropython._T" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(111,46): Variable "micropython._T" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(121,29): Variable "micropython._T" is not valid as a type (Reported by 154 tests)
"micropython.pyi"(121,46): Variable "micropython._T" is not valid as a type (Reported by 154 tests)
"micropython.pyi"(159,29): Variable "micropython._T" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(159,46): Variable "micropython._T" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(171,29): Variable "micropython._T" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(171,46): Variable "micropython._T" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(182,16): Variable "micropython.Const_T" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(182,31): Variable "micropython.Const_T" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(190,16): Variable "micropython.Const_T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(190,31): Variable "micropython.Const_T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(191,16): Variable "micropython.Const_T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(191,31): Variable "micropython.Const_T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(196,16): Variable "micropython.Const_T" is not valid as a type (Reported by 71 tests)
"micropython.pyi"(196,31): Variable "micropython.Const_T" is not valid as a type (Reported by 71 tests)
"micropython.pyi"(201,16): Variable "micropython.Const_T" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(201,31): Variable "micropython.Const_T" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(234,16): Variable "micropython.Const_T" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(234,31): Variable "micropython.Const_T" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(244,16): Variable "micropython.Const_T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(244,31): Variable "micropython.Const_T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(245,16): Variable "micropython.Const_T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(245,31): Variable "micropython.Const_T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(251,26): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(251,34): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(251,56): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(251,64): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(254,16): Variable "micropython.Const_T" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(254,31): Variable "micropython.Const_T" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(262,27): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(262,35): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(262,57): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(262,65): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(271,30): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(271,38): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(271,60): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(271,68): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(282,31): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(282,39): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(282,61): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(282,69): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(305,26): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 71 tests)
"micropython.pyi"(305,34): Variable "micropython._Ret" is not valid as a type (Reported by 71 tests)
"micropython.pyi"(305,56): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 71 tests)
"micropython.pyi"(305,64): Variable "micropython._Ret" is not valid as a type (Reported by 71 tests)
"micropython.pyi"(306,26): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 7 tests)
"micropython.pyi"(306,34): Variable "micropython._Ret" is not valid as a type (Reported by 7 tests)
"micropython.pyi"(306,56): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 7 tests)
"micropython.pyi"(306,64): Variable "micropython._Ret" is not valid as a type (Reported by 7 tests)
"micropython.pyi"(310,26): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(310,34): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(310,56): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(310,64): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(316,27): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 71 tests)
"micropython.pyi"(316,35): Variable "micropython._Ret" is not valid as a type (Reported by 71 tests)
"micropython.pyi"(316,57): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 71 tests)
"micropython.pyi"(316,65): Variable "micropython._Ret" is not valid as a type (Reported by 71 tests)
"micropython.pyi"(317,27): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 7 tests)
"micropython.pyi"(317,35): Variable "micropython._Ret" is not valid as a type (Reported by 7 tests)
"micropython.pyi"(317,57): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 7 tests)
"micropython.pyi"(317,65): Variable "micropython._Ret" is not valid as a type (Reported by 7 tests)
"micropython.pyi"(321,27): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(321,35): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(321,57): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(321,65): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(325,30): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 71 tests)
"micropython.pyi"(325,38): Variable "micropython._Ret" is not valid as a type (Reported by 71 tests)
"micropython.pyi"(325,60): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 71 tests)
"micropython.pyi"(325,68): Variable "micropython._Ret" is not valid as a type (Reported by 71 tests)
"micropython.pyi"(326,30): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 7 tests)
"micropython.pyi"(326,38): Variable "micropython._Ret" is not valid as a type (Reported by 7 tests)
"micropython.pyi"(326,60): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 7 tests)
"micropython.pyi"(326,68): Variable "micropython._Ret" is not valid as a type (Reported by 7 tests)
"micropython.pyi"(330,30): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(330,38): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(330,60): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(330,68): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(336,31): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 71 tests)
"micropython.pyi"(336,39): Variable "micropython._Ret" is not valid as a type (Reported by 71 tests)
"micropython.pyi"(336,61): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 71 tests)
"micropython.pyi"(336,69): Variable "micropython._Ret" is not valid as a type (Reported by 71 tests)
"micropython.pyi"(337,31): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 7 tests)
"micropython.pyi"(337,39): Variable "micropython._Ret" is not valid as a type (Reported by 7 tests)
"micropython.pyi"(337,61): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 7 tests)
"micropython.pyi"(337,69): Variable "micropython._Ret" is not valid as a type (Reported by 7 tests)
"micropython.pyi"(341,31): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(341,39): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(341,61): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(341,69): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(349,26): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(349,34): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(349,56): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(349,64): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(360,27): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(360,35): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(360,57): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(360,65): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(369,30): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(369,38): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(369,60): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(369,68): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(380,31): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(380,39): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(380,61): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(380,69): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(402,26): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 3 tests)
"micropython.pyi"(402,34): Variable "micropython._Ret" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(402,56): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 3 tests)
"micropython.pyi"(402,64): Variable "micropython._Ret" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(404,26): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(404,34): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(404,56): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(404,64): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(406,26): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(406,34): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(406,56): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(406,64): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(413,27): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 3 tests)
"micropython.pyi"(413,35): Variable "micropython._Ret" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(413,57): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 3 tests)
"micropython.pyi"(413,65): Variable "micropython._Ret" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(415,27): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(415,35): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(415,57): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(415,65): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(417,27): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(417,35): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(417,57): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(417,65): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(422,30): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 3 tests)
"micropython.pyi"(422,38): Variable "micropython._Ret" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(422,60): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 3 tests)
"micropython.pyi"(422,68): Variable "micropython._Ret" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(424,30): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(424,38): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(424,60): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(424,68): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(426,30): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(426,38): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(426,60): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(426,68): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(433,31): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 3 tests)
"micropython.pyi"(433,39): Variable "micropython._Ret" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(433,61): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 3 tests)
"micropython.pyi"(433,69): Variable "micropython._Ret" is not valid as a type (Reported by 3 tests)
"micropython.pyi"(435,31): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(435,39): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(435,61): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 4 tests)
"micropython.pyi"(435,69): Variable "micropython._Ret" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(437,31): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(437,39): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(437,61): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 83 tests)
"micropython.pyi"(437,69): Variable "micropython._Ret" is not valid as a type (Reported by 83 tests)
"micropython.pyi"(48,29): Variable "micropython._T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(48,46): Variable "micropython._T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(66,29): Variable "micropython._T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(66,46): Variable "micropython._T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(68,29): Variable "micropython._T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(68,46): Variable "micropython._T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(98,29): Variable "micropython._T" is not valid as a type (Reported by 4 tests)
"micropython.pyi"(98,46): Variable "micropython._T" is not valid as a type (Reported by 4 tests)
"neopixel.pyi"(21,20): Unsupported left operand type for | ("type[tuple[int, int, int]]") (Reported by 51 tests)
"neopixel.pyi"(21,8): Invalid type comment or annotation (Reported by 51 tests)
"neopixel.pyi"(22,20): Unsupported left operand type for | ("type[tuple[int, int, int]]") (Reported by 63 tests)
"neopixel.pyi"(22,8): Invalid type comment or annotation (Reported by 63 tests)
"neopixel.pyi"(24,20): Unsupported left operand type for | ("type[tuple[int, int, int]]") (Reported by 63 tests)
"neopixel.pyi"(24,8): Invalid type comment or annotation (Reported by 63 tests)
"polyscript.pyi"(22,7): Cannot find implementation or library stub for module named "storage" (Reported by 6 tests)
"pyb.pyi"(1038,4): Signature of "ioctl" incompatible with supertype "vfs.AbstractBlockDev" (Reported by 10 tests)
"pyb.pyi"(3192,4): Single overload definition, multiple required (Reported by 10 tests)
"pyb.pyi"(3206,4): Single overload definition, multiple required (Reported by 10 tests)
"pyb.pyi"(3259,4): Single overload definition, multiple required (Reported by 10 tests)
"pyb.pyi"(3318,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 10 tests)
"pyb.pyi"(3330,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 10 tests)
"pyb.pyi"(4047,30): Name "pinaf" is not defined (Reported by 10 tests)
"pyb.pyi"(4061,30): Name "pinaf" is not defined (Reported by 10 tests)
"pyb.pyi"(4341,14): Variable "pyb._WB" is not valid as a type (Reported by 10 tests)
"pyb.pyi"(4345,9): Variable "pyb._WB" is not valid as a type (Reported by 10 tests)
"pyb.pyi"(4374,25): Variable "pyb._WB" is not valid as a type (Reported by 10 tests)
"pyb.pyi"(4374,60): Variable "pyb._WB" is not valid as a type (Reported by 10 tests)
"pyb.pyi"(543,0): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 10 tests)
"pyb.pyi"(545,0): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 10 tests)
"pyb.pyi"(635,0): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 10 tests)
"pyb.pyi"(913,4): Signature of "readblocks" incompatible with supertype "vfs.AbstractBlockDev" (Reported by 10 tests)
"pyb.pyi"(915,4): Signature of "readblocks" incompatible with supertype "vfs.AbstractBlockDev" (Reported by 10 tests)
"pyb.pyi"(933,4): Signature of "writeblocks" incompatible with supertype "vfs.AbstractBlockDev" (Reported by 10 tests)
"pyb.pyi"(935,4): Signature of "writeblocks" incompatible with supertype "vfs.AbstractBlockDev" (Reported by 10 tests)
"pyb.pyi"(958,4): Signature of "ioctl" incompatible with supertype "vfs.AbstractBlockDev" (Reported by 10 tests)
"pyb.pyi"(960,4): Signature of "ioctl" incompatible with supertype "vfs.AbstractBlockDev" (Reported by 10 tests)
"pyscript/__init__.pyi"(32,0): Cannot redefine an existing name as final (Reported by 3 tests)
"pyscript/__init__.pyi"(40,0): Cannot redefine an existing name as final (Reported by 3 tests)
"pyscript/__init__.pyi"(73,0): "classmethod" used with a non-method (Reported by 3 tests)
"pyscript/__init__.pyi"(84,0): "classmethod" used with a non-method (Reported by 3 tests)
"pyscript/__init__.pyi"(89,0): "classmethod" used with a non-method (Reported by 3 tests)
"pyscript/fetch.pyi"(119,33): Function "pyscript.fetch._FetchPromise.bytearray" is not valid as a type (Reported by 3 tests)
"pyscript/fetch.pyi"(122,33): Function "pyscript.fetch._FetchPromise.bytearray" is not valid as a type (Reported by 3 tests)
"pyscript/fetch.pyi"(43,33): Function "pyscript.fetch._FetchResponse.bytearray" is not valid as a type (Reported by 3 tests)
"pyscript/fetch.pyi"(46,33): Function "pyscript.fetch._FetchResponse.bytearray" is not valid as a type (Reported by 3 tests)
"pyscript/web.pyi"(158,22): Argument 1 of "discard" is incompatible with supertype "builtins.set"; supertype defines the argument type as "object" (Reported by 3 tests)
"pyscript/web.pyi"(300,48): Invalid type comment or annotation (Reported by 3 tests)
"random.pyi"(100,35): Variable "random._T" is not valid as a type (Reported by 88 tests)
"random.pyi"(100,46): Variable "random._T" is not valid as a type (Reported by 88 tests)
"random.pyi"(98,35): Variable "random._T" is not valid as a type (Reported by 82 tests)
"random.pyi"(98,46): Variable "random._T" is not valid as a type (Reported by 82 tests)
"rp2/__init__.pyi"(155,15): Invalid type comment or annotation (Reported by 34 tests)
"rp2/__init__.pyi"(187,19): Name "_PIO_ASM_Program" is not defined (Reported by 22 tests)
"rp2/__init__.pyi"(197,19): Name "_PIO_ASM_Program" is not defined (Reported by 12 tests)
"rp2/__init__.pyi"(24,15): Invalid type comment or annotation (Reported by 34 tests)
"rp2/__init__.pyi"(262,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 12 tests)
"rp2/__init__.pyi"(272,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 12 tests)
"rp2/__init__.pyi"(308,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 12 tests)
"rp2/__init__.pyi"(319,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 12 tests)
"rp2/__init__.pyi"(345,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 12 tests)
"rp2/__init__.pyi"(348,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 12 tests)
"rp2/__init__.pyi"(451,46): Name "_PIO_ASM_Program" is not defined (Reported by 22 tests)
"rp2/__init__.pyi"(462,47): Name "_PIO_ASM_Program" is not defined (Reported by 22 tests)
"rp2/__init__.pyi"(485,35): Name "_PIO_ASM_Program" is not defined (Reported by 22 tests)
"rp2/__init__.pyi"(537,4): Signature of "readblocks" incompatible with supertype "vfs.AbstractBlockDev" (Reported by 12 tests)
"rp2/__init__.pyi"(557,4): Signature of "readblocks" incompatible with supertype "vfs.AbstractBlockDev" (Reported by 22 tests)
"rp2/__init__.pyi"(561,17): Name "_PIO_ASM_Program" is not defined (Reported by 22 tests)
"rp2/__init__.pyi"(562,17): Name "_PIO_ASM_Program" is not defined (Reported by 12 tests)
"rp2/__init__.pyi"(62,18): Invalid type comment or annotation (Reported by 22 tests)
"rp2/__init__.pyi"(63,15): Invalid type comment or annotation (Reported by 22 tests)
"rp2/__init__.pyi"(633,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 22 tests)
"rp2/__init__.pyi"(634,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 12 tests)
"rp2/__init__.pyi"(635,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 22 tests)
"rp2/__init__.pyi"(636,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 12 tests)
"rp2/__init__.pyi"(650,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 22 tests)
"rp2/__init__.pyi"(651,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 12 tests)
"rp2/__init__.pyi"(652,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 22 tests)
"rp2/__init__.pyi"(653,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 12 tests)
"rp2/__init__.pyi"(665,17): Name "_PIO_ASM_Program" is not defined (Reported by 22 tests)
"rp2/__init__.pyi"(666,17): Name "_PIO_ASM_Program" is not defined (Reported by 12 tests)
"rp2/__init__.pyi"(729,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 22 tests)
"rp2/__init__.pyi"(733,46): Name "_PIO_ASM_Program" is not defined (Reported by 12 tests)
"rp2/__init__.pyi"(739,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 22 tests)
"rp2/__init__.pyi"(744,47): Name "_PIO_ASM_Program" is not defined (Reported by 12 tests)
"rp2/__init__.pyi"(767,35): Name "_PIO_ASM_Program" is not defined (Reported by 12 tests)
"rp2/__init__.pyi"(775,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 22 tests)
"rp2/__init__.pyi"(786,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 22 tests)
"rp2/__init__.pyi"(812,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 22 tests)
"rp2/__init__.pyi"(815,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 22 tests)
"rp2/__init__.pyi"(875,32): Name "block" is not defined (Reported by 7 tests)
"rp2/__init__.pyi"(876,32): Name "block" is not defined (Reported by 9 tests)
"rp2/__init__.pyi"(924,4): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 7 tests)
"rp2/__init__.pyi"(925,4): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 9 tests)
"rp2/__init__.pyi"(926,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 7 tests)
"rp2/__init__.pyi"(927,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 9 tests)
"rp2/__init__.pyi"(928,4): Overloaded function signature 4 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 7 tests)
"rp2/__init__.pyi"(928,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 7 tests)
"rp2/__init__.pyi"(928,4): Overloaded function signature 4 will never be matched: signature 3's parameter type(s) are the same or broader (Reported by 7 tests)
"rp2/__init__.pyi"(929,4): Overloaded function signature 4 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 9 tests)
"rp2/__init__.pyi"(929,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 9 tests)
"rp2/__init__.pyi"(929,4): Overloaded function signature 4 will never be matched: signature 3's parameter type(s) are the same or broader (Reported by 9 tests)
"rp2/__init__.pyi"(938,32): Name "block" is not defined (Reported by 6 tests)
"rp2/__init__.pyi"(987,4): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 6 tests)
"rp2/__init__.pyi"(989,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 6 tests)
"rp2/__init__.pyi"(991,4): Overloaded function signature 4 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 6 tests)
"rp2/__init__.pyi"(991,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 6 tests)
"rp2/__init__.pyi"(991,4): Overloaded function signature 4 will never be matched: signature 3's parameter type(s) are the same or broader (Reported by 6 tests)
"rp2/asm_pio_rp2040.pyi"(72,16): Invalid base class "Protocol" (Reported by 90 tests)
"rp2/asm_pio_rp2040.pyi"(75,37): Invalid type comment or annotation (Reported by 90 tests)
"rp2/asm_pio_rp2040.pyi"(76,38): Invalid type comment or annotation (Reported by 90 tests)
"rp2/asm_pio_rp2040.pyi"(77,44): Invalid type comment or annotation (Reported by 90 tests)
"rp2/asm_pio_rp2040.pyi"(82,32): Module "rp2" has no attribute "_PIO_ASM_Program" (Reported by 34 tests)
"socket.pyi"(109,10): Invalid type comment or annotation (Reported by 20 tests)
"socket.pyi"(109,22): Unsupported left operand type for | ("type[tuple[str, int]]") (Reported by 20 tests)
"socket.pyi"(110,8): Invalid type comment or annotation (Reported by 20 tests)
"socket.pyi"(111,10): Invalid type comment or annotation (Reported by 10 tests)
"socket.pyi"(111,22): Unsupported left operand type for | ("type[tuple[str, int]]") (Reported by 10 tests)
"socket.pyi"(112,10): Invalid type comment or annotation (Reported by 96 tests)
"socket.pyi"(112,22): Unsupported left operand type for | ("type[tuple[str, int]]") (Reported by 96 tests)
"socket.pyi"(112,8): Invalid type comment or annotation (Reported by 10 tests)
"socket.pyi"(113,8): Invalid type comment or annotation (Reported by 96 tests)
"socket.pyi"(114,10): Invalid type comment or annotation (Reported by 51 tests)
"socket.pyi"(114,22): Unsupported left operand type for | ("type[tuple[str, int]]") (Reported by 51 tests)
"socket.pyi"(115,10): Invalid type comment or annotation (Reported by 4 tests)
"socket.pyi"(115,22): Unsupported left operand type for | ("type[tuple[str, int]]") (Reported by 4 tests)
"socket.pyi"(115,8): Invalid type comment or annotation (Reported by 51 tests)
"socket.pyi"(116,8): Invalid type comment or annotation (Reported by 4 tests)
"socket.pyi"(117,10): Invalid type comment or annotation (Reported by 4 tests)
"socket.pyi"(117,22): Unsupported left operand type for | ("type[tuple[str, int]]") (Reported by 4 tests)
"socket.pyi"(118,8): Invalid type comment or annotation (Reported by 4 tests)
"stdlib/__future__.pyi"(3,14): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_asyncio.pyi"(27,45): Can only assign concrete classes to a variable of type "type[Generator]" (Reported by 260 tests)
"stdlib/_codecs.pyi"(13,10): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_codecs.pyi"(13,22): Unsupported left operand type for | ("type[dict[int, int]]") (Reported by 260 tests)
"stdlib/_codecs.pyi"(14,10): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_codecs.pyi"(15,17): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_codecs.pyi"(27,23): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_codecs.pyi"(46,19): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_codecs.pyi"(51,0): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/_codecs.pyi"(57,0): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/_codecs.pyi"(61,0): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/_codecs.pyi"(61,0): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/_codecs.pyi"(69,0): Overloaded function signature 4 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/_codecs.pyi"(69,0): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/_decimal.pyi"(58,11): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(101,24): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(101,36): Unsupported left operand type for | ("type[SupportsDunderLT[Any]]") (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(171,21): Unsupported left operand type for | ("type[str]") (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(171,9): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(172,11): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(172,23): Unsupported left operand type for | ("type[bytes]") (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(173,13): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(173,25): Unsupported left operand type for | ("TypeVar") (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(173,43): Type variable "typing.AnyStr" is unbound (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(174,16): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(174,28): Unsupported left operand type for | ("type[str]") (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(176,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(210,21): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(211,21): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(212,14): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(213,24): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(239,23): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(240,23): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(241,16): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(247,16): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(248,20): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(248,32): Unsupported left operand type for | ("type[int]") (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(249,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(275,16): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(277,17): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(279,16): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(281,21): All bases of a protocol must be protocols (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(284,21): All bases of a protocol must be protocols (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(294,17): All bases of a protocol must be protocols (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(297,16): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(299,9): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(300,12): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(331,57): Type expected (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(335,45): Type expected (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(338,17): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(341,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(351,18): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(352,20): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(50,12): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(53,8): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/__init__.pyi"(58,11): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/dbapi.pyi"(12,24): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/dbapi.pyi"(9,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/_typeshed/dbapi.pyi"(9,27): Unsupported left operand type for | ("object") (Reported by 260 tests)
"stdlib/abc.pyi"(33,26): "classmethod" expects 2 type arguments, but 3 given (Reported by 260 tests)
"stdlib/abc.pyi"(33,42): Variable "abc._P" is not valid as a type (Reported by 260 tests)
"stdlib/abc.pyi"(35,42): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 260 tests)
"stdlib/abc.pyi"(38,27): "staticmethod" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/abc.pyi"(38,40): Variable "abc._P" is not valid as a type (Reported by 260 tests)
"stdlib/abc.pyi"(40,42): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 260 tests)
"stdlib/array.pyi"(193,23): Argument 1 of "__iadd__" is incompatible with supertype "typing.MutableSequence"; supertype defines the argument type as "Iterable[_T]" (Reported by 260 tests)
"stdlib/array.pyi"(193,44): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/array.pyi"(202,41): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/array.pyi"(27,14): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/array.pyi"(28,16): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/array.pyi"(29,18): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/array.pyi"(30,11): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/array.pyi"(94,21): Argument 1 of "extend" is incompatible with supertype "typing.MutableSequence"; supertype defines the argument type as "Iterable[_T]" (Reported by 260 tests)
"stdlib/asyncio/__init__.pyi"(11,6): Cannot find implementation or library stub for module named "asyncio.futures" (Reported by 260 tests)
"stdlib/asyncio/__init__.pyi"(37,10): Cannot find implementation or library stub for module named "asyncio.unix_events" (Reported by 260 tests)
"stdlib/asyncio/__init__.pyi"(46,20): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/__init__.pyi"(46,32): Unsupported left operand type for | ("type[Generator[Any, None, Any]]") (Reported by 260 tests)
"stdlib/asyncio/__init__.pyi"(46,53): Type variable "asyncio._T_co" is unbound (Reported by 260 tests)
"stdlib/asyncio/__init__.pyi"(46,72): Type variable "asyncio._T_co" is unbound (Reported by 260 tests)
"stdlib/asyncio/__init__.pyi"(47,20): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/__init__.pyi"(47,32): Unsupported left operand type for | ("type[Generator[Any, None, Any]]") (Reported by 260 tests)
"stdlib/asyncio/__init__.pyi"(47,53): Type variable "asyncio._T_co" is unbound (Reported by 260 tests)
"stdlib/asyncio/__init__.pyi"(47,82): Type variable "asyncio._T_co" is unbound (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(104,28): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(105,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(108,61): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(108,87): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(11,19): Module "socket" has no attribute "AddressFamily" (Reported by 185 tests)
"stdlib/asyncio/base_events.pyi"(11,34): Module "socket" has no attribute "SocketKind" (Reported by 185 tests)
"stdlib/asyncio/base_events.pyi"(11,56): Module "socket" has no attribute "_RetAddress" (Reported by 185 tests)
"stdlib/asyncio/base_events.pyi"(25,10): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(26,19): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(27,18): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(28,13): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(28,25): Unsupported left operand type for | ("type[bool]") (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(463,69): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(463,96): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(465,69): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(465,96): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(479,63): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(479,90): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(5,13): Cannot find implementation or library stub for module named "asyncio.futures" (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(68,64): A function returning TypeVar should receive at least one argument containing the same Typevar (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(79,28): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(80,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(86,28): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_events.pyi"(87,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/base_futures.pyi"(12,6): Cannot find implementation or library stub for module named "asyncio.futures" (Reported by 260 tests)
"stdlib/asyncio/coroutines.pyi"(22,39): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 260 tests)
"stdlib/asyncio/coroutines.pyi"(22,62): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/coroutines.pyi"(24,39): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 260 tests)
"stdlib/asyncio/coroutines.pyi"(24,55): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/coroutines.pyi"(26,41): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/coroutines.pyi"(27,32): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(102,34): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(120,64): A function returning TypeVar should receive at least one argument containing the same Typevar (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(139,32): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(14,6): Cannot find implementation or library stub for module named "asyncio.futures" (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(140,19): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(147,32): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(148,19): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(18,6): Cannot find implementation or library stub for module named "asyncio.unix_events" (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(181,32): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(182,19): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(190,61): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(190,87): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(52,10): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(53,19): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(54,18): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(55,13): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(55,25): Unsupported left operand type for | ("type[bool]") (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(561,69): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(561,96): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(565,69): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(565,96): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(587,63): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(587,93): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/events.pyi"(6,19): Module "socket" has no attribute "AddressFamily" (Reported by 185 tests)
"stdlib/asyncio/events.pyi"(6,34): Module "socket" has no attribute "SocketKind" (Reported by 185 tests)
"stdlib/asyncio/events.pyi"(6,56): Module "socket" has no attribute "_RetAddress" (Reported by 185 tests)
"stdlib/asyncio/events.pyi"(630,0): Class asyncio.events.BaseDefaultEventLoopPolicy has abstract attributes "get_child_watcher", "set_child_watcher" (Reported by 260 tests)
"stdlib/asyncio/format_helpers.pyi"(13,11): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/format_helpers.pyi"(13,23): Unsupported left operand type for | ("type[FunctionType]") (Reported by 260 tests)
"stdlib/asyncio/format_helpers.pyi"(13,52): Type application is only supported for generic classes (Reported by 6 tests)
"stdlib/asyncio/format_helpers.pyi"(13,77): Module has no attribute "partialmethod" (Reported by 6 tests)
"stdlib/asyncio/format_helpers.pyi"(18,0): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/asyncio/locks.pyi"(12,6): Cannot find implementation or library stub for module named "asyncio.futures" (Reported by 260 tests)
"stdlib/asyncio/micropython.pyi"(30,28): Name "Generator" is not defined (Reported by 260 tests)
"stdlib/asyncio/mixins.pyi"(10,36): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/sslproto.pyi"(93,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/streams.pyi"(199,27): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/streams.pyi"(32,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/tasks.pyi"(11,6): Cannot find implementation or library stub for module named "asyncio.futures" (Reported by 260 tests)
"stdlib/asyncio/tasks.pyi"(397,10): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/asyncio/tasks.pyi"(432,10): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/asyncio/tasks.pyi"(443,25): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/tasks.pyi"(443,37): Unsupported left operand type for | ("type[Generator[Any, None, Any]]") (Reported by 260 tests)
"stdlib/asyncio/tasks.pyi"(443,69): Type variable "asyncio.tasks._T_co" is unbound (Reported by 260 tests)
"stdlib/asyncio/tasks.pyi"(443,98): Type variable "asyncio.tasks._T_co" is unbound (Reported by 260 tests)
"stdlib/asyncio/tasks.pyi"(71,17): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/tasks.pyi"(71,63): Type variable "asyncio.tasks._T" is unbound (Reported by 260 tests)
"stdlib/asyncio/tasks.pyi"(71,79): Type variable "asyncio.tasks._T" is unbound (Reported by 260 tests)
"stdlib/asyncio/tasks.pyi"(72,16): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/tasks.pyi"(97,0): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/asyncio/threads.pyi"(10,35): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 260 tests)
"stdlib/asyncio/threads.pyi"(10,54): Variable "asyncio.threads._P" is not valid as a type (Reported by 260 tests)
"stdlib/asyncio/threads.pyi"(10,73): Variable "asyncio.threads._P" is not valid as a type (Reported by 260 tests)
"stdlib/asyncio/timeouts.pyi"(14,34): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/trsock.pyi"(12,10): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/trsock.pyi"(13,13): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/trsock.pyi"(14,14): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/trsock.pyi"(14,26): Unsupported left operand type for | ("type[bytearray]") (Reported by 260 tests)
"stdlib/asyncio/trsock.pyi"(15,7): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/asyncio/trsock.pyi"(93,37): "type" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1002,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1002,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1008,48): "tuple" expects 1 type argument, but 3 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1011,60): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1012,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection" (Reported by 260 tests)
"stdlib/builtins.pyi"(1013,27): Argument 1 of "__contains__" is incompatible with supertype "typing.Sequence"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1013,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Container" (Reported by 260 tests)
"stdlib/builtins.pyi"(1013,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1014,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1017,44): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1017,57): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1019,28): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1019,41): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1020,28): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1020,41): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1021,28): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1021,41): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1022,28): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1022,41): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1023,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1023,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1024,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1026,29): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1026,42): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1026,54): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1026,67): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1028,29): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1028,39): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1028,4): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1028,51): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1028,69): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1029,50): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1029,63): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1030,51): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1030,64): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1031,4): Return type "int" of "count" incompatible with return type "int" in supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1032,4): Return type "int" of "index" incompatible with return type "int" in supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1044,29): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1044,45): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1046,18): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1046,29): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1075,4): Return type "int" of "index" incompatible with return type "int" in supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1076,4): Return type "int" of "count" incompatible with return type "int" in supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1088,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection" (Reported by 260 tests)
"stdlib/builtins.pyi"(109,6): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1091,4): Signature of "__getitem__" incompatible with supertype "typing.MutableSequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1091,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1095,4): Signature of "__setitem__" incompatible with supertype "typing.MutableSequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1099,4): Signature of "__delitem__" incompatible with supertype "typing.MutableSequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1105,50): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1108,51): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1109,27): Argument 1 of "__contains__" is incompatible with supertype "typing.Sequence"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1109,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Container" (Reported by 260 tests)
"stdlib/builtins.pyi"(1109,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1115,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1115,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1136,42): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1140,27): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1150,51): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1159,4): "classmethod[Any, dict[Any, Any | None]]" not callable (Reported by 260 tests)
"stdlib/builtins.pyi"(1162,4): "classmethod[Any, dict[Any, Any]]" not callable (Reported by 260 tests)
"stdlib/builtins.pyi"(1178,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection" (Reported by 260 tests)
"stdlib/builtins.pyi"(1183,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1183,21): Argument 1 of "__eq__" is incompatible with supertype "typing.Mapping"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1183,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1183,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "typing.Mapping" (Reported by 260 tests)
"stdlib/builtins.pyi"(1198,73): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1198,8): Signatures of "__ior__" and "__or__" are incompatible (Reported by 260 tests)
"stdlib/builtins.pyi"(1200,42): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1200,66): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1200,8): Signatures of "__ior__" and "__or__" are incompatible (Reported by 260 tests)
"stdlib/builtins.pyi"(1214,4): Return type "bool" of "isdisjoint" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1222,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection" (Reported by 260 tests)
"stdlib/builtins.pyi"(1223,27): Argument 1 of "__contains__" is incompatible with supertype "typing.AbstractSet"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1223,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1223,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Container" (Reported by 260 tests)
"stdlib/builtins.pyi"(1226,57): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1228,52): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(123,56): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1230,4): Signatures of "__isub__" and "__sub__" are incompatible (Reported by 260 tests)
"stdlib/builtins.pyi"(1230,57): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1232,53): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1233,4): Return type "bool" of "__le__" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1233,4): Signatures of "__le__" of "set[_T]" and "__ge__" of "AbstractSet[object]" are unsafely overlapping (Reported by 260 tests)
"stdlib/builtins.pyi"(1234,4): Return type "bool" of "__lt__" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1234,4): Signatures of "__lt__" of "set[_T]" and "__gt__" of "AbstractSet[object]" are unsafely overlapping (Reported by 260 tests)
"stdlib/builtins.pyi"(1235,4): Return type "bool" of "__ge__" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1235,4): Signatures of "__ge__" of "set[_T]" and "__le__" of "AbstractSet[object]" are unsafely overlapping (Reported by 260 tests)
"stdlib/builtins.pyi"(1236,4): Return type "bool" of "__gt__" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1236,4): Signatures of "__gt__" of "set[_T]" and "__lt__" of "AbstractSet[object]" are unsafely overlapping (Reported by 260 tests)
"stdlib/builtins.pyi"(1237,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1237,21): Argument 1 of "__eq__" is incompatible with supertype "typing.AbstractSet"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1237,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1237,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1244,24): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1246,54): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1250,4): Return type "bool" of "isdisjoint" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1255,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection" (Reported by 260 tests)
"stdlib/builtins.pyi"(1256,27): Argument 1 of "__contains__" is incompatible with supertype "typing.AbstractSet"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1256,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1256,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Container" (Reported by 260 tests)
"stdlib/builtins.pyi"(1262,4): Return type "bool" of "__le__" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1262,4): Signatures of "__le__" of "frozenset[_T_co]" and "__ge__" of "AbstractSet[object]" are unsafely overlapping (Reported by 260 tests)
"stdlib/builtins.pyi"(1263,4): Return type "bool" of "__lt__" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1263,4): Signatures of "__lt__" of "frozenset[_T_co]" and "__gt__" of "AbstractSet[object]" are unsafely overlapping (Reported by 260 tests)
"stdlib/builtins.pyi"(1264,4): Return type "bool" of "__ge__" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1264,4): Signatures of "__ge__" of "frozenset[_T_co]" and "__le__" of "AbstractSet[object]" are unsafely overlapping (Reported by 260 tests)
"stdlib/builtins.pyi"(1265,4): Return type "bool" of "__gt__" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1265,4): Signatures of "__gt__" of "frozenset[_T_co]" and "__lt__" of "AbstractSet[object]" are unsafely overlapping (Reported by 260 tests)
"stdlib/builtins.pyi"(1266,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1266,21): Argument 1 of "__eq__" is incompatible with supertype "typing.AbstractSet"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1266,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1266,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "typing.AbstractSet" (Reported by 260 tests)
"stdlib/builtins.pyi"(1267,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1273,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1274,26): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1287,48): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1289,97): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1290,4): Return type "int" of "count" incompatible with return type "int" in supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1292,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection" (Reported by 260 tests)
"stdlib/builtins.pyi"(1293,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1293,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1294,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1295,27): Argument 1 of "__contains__" is incompatible with supertype "typing.Sequence"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1295,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Container" (Reported by 260 tests)
"stdlib/builtins.pyi"(1295,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1297,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(1339,32): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1369,11): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1390,11): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1467,74): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1469,46): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1469,92): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1471,4): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1471,46): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1471,89): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1473,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1473,4): Overloaded function signature 4 will never be matched: signature 3's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1473,82): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1474,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1518,16): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1518,28): Unsupported left operand type for | ("type[type]") (Reported by 260 tests)
"stdlib/builtins.pyi"(1518,35): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1518,53): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1528,76): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1530,103): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1532,130): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1542,9): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1553,9): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1566,9): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1567,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1604,9): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1624,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1637,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1648,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1659,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1702,11): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1726,4): Unsupported left operand type for | ("type[_SupportsPow2[Any, Any]]") (Reported by 260 tests)
"stdlib/builtins.pyi"(1734,24): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1734,57): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1736,0): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1738,0): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1738,0): Overloaded function signature 4 will never be matched: signature 3's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1743,0): Overloaded function signature 5 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1743,0): Overloaded function signature 5 will never be matched: signature 3's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1743,0): Overloaded function signature 5 will never be matched: signature 4's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1747,0): Overloaded function signature 7 will never be matched: signature 6's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(176,27): "type" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/builtins.pyi"(176,32): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1761,0): Overloaded function signature 12 will never be matched: signature 11's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1765,0): Overloaded function signature 14 will never be matched: signature 6's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1765,0): Overloaded function signature 14 will never be matched: signature 7's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1775,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(178,30): "type" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/builtins.pyi"(180,24): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1818,0): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(1818,83): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(183,26): Argument 1 of "__setattr__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "str" (Reported by 260 tests)
"stdlib/builtins.pyi"(184,26): Argument 1 of "__delattr__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "str" (Reported by 260 tests)
"stdlib/builtins.pyi"(185,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(185,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(186,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(186,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(187,4): Return type "str" of "__str__" incompatible with return type "str" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1876,79): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1878,101): "tuple" expects 1 type argument, but 3 given (Reported by 260 tests)
"stdlib/builtins.pyi"(188,4): Return type "str" of "__repr__" incompatible with return type "str" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1882,17): "tuple" expects 1 type argument, but 4 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1886,17): "tuple" expects 1 type argument, but 5 given (Reported by 260 tests)
"stdlib/builtins.pyi"(189,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1898,17): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1898,28): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(190,25): Argument 1 of "__format__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "str" (Reported by 260 tests)
"stdlib/builtins.pyi"(190,4): Return type "str" of "__format__" incompatible with return type "str" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1900,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(191,31): Argument 1 of "__getattribute__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "str" (Reported by 260 tests)
"stdlib/builtins.pyi"(192,4): Return type "int" of "__sizeof__" incompatible with return type "int" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(1933,10): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(1933,21): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(1939,49): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(1941,61): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(195,34): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(195,4): Return type "str | tuple[Any]" of "__reduce__" incompatible with return type "str | tuple[Any, ...]" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(195,45): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(196,4): Return type "str | tuple[Any]" of "__reduce_ex__" incompatible with return type "str | tuple[Any, ...]" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(196,65): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(196,76): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(200,4): Return type "Iterable[str]" of "__dir__" incompatible with return type "Iterable[str]" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(205,27): Free type variable expected in Generic[...] (Reported by 260 tests)
"stdlib/builtins.pyi"(205,31): Duplicate type variables in Generic[...] or Protocol[...] (Reported by 260 tests)
"stdlib/builtins.pyi"(207,35): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(210,35): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(212,66): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(222,30): Free type variable expected in Generic[...] (Reported by 260 tests)
"stdlib/builtins.pyi"(222,34): Duplicate type variables in Generic[...] or Protocol[...] (Reported by 260 tests)
"stdlib/builtins.pyi"(224,35): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(227,35): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(231,45): "type" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/builtins.pyi"(231,70): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(242,15): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(242,27): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(255,25): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(255,37): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(265,41): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(265,53): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(270,11): The erased type of self "builtins.type" is not a supertype of its class "type[builtins.type]" (Reported by 260 tests)
"stdlib/builtins.pyi"(270,13): "type" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/builtins.pyi"(270,53): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(270,65): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(280,47): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(280,59): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(295,18): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(296,18): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(301,54): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(303,76): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(304,34): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(304,45): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(308,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(312,29): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(334,23): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(337,13): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(348,43): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(355,44): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(357,25): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(357,43): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(359,29): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(359,58): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(363,4): Overloaded function signature 4 will never be matched: signature 3's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(367,4): Overloaded function signature 5 will never be matched: signature 3's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(367,4): Overloaded function signature 5 will never be matched: signature 4's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(389,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(389,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(390,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(390,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(398,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(403,56): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(404,34): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(408,40): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(420,45): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(433,46): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(437,4): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(440,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(440,4): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(451,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(451,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(452,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(452,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(462,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(472,9): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(474,95): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(490,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(490,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(491,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(491,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(495,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(508,46): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(510,88): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(512,25): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(512,43): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(516,23): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(516,41): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(520,21): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(520,68): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(520,95): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(523,4): Signature of "count" incompatible with supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(525,37): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(525,48): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(527,25): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(527,71): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(532,21): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(532,43): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(532,68): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(532,86): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(534,4): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(536,4): Return type "int" of "index" incompatible with return type "int" in supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(550,19): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(550,53): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(550,75): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(554,20): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(554,67): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(554,94): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(558,20): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(558,38): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(566,101): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(566,24): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(566,44): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(566,65): "tuple" expects 1 type argument, but 3 given (Reported by 260 tests)
"stdlib/builtins.pyi"(566,71): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(566,86): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(568,40): "tuple" expects 1 type argument, but 3 given (Reported by 260 tests)
"stdlib/builtins.pyi"(576,114): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(576,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(576,46): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(576,66): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(581,31): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(581,54): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(581,75): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(585,31): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(585,54): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(585,75): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(592,20): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(592,67): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(592,94): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(596,102): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(596,25): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(596,45): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(596,66): "tuple" expects 1 type argument, but 3 given (Reported by 260 tests)
"stdlib/builtins.pyi"(596,72): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(596,87): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(598,41): "tuple" expects 1 type argument, but 3 given (Reported by 260 tests)
"stdlib/builtins.pyi"(615,39): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(615,50): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(621,23): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(621,41): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(625,20): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(625,38): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(630,20): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(630,38): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(634,20): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(634,63): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(637,4): "staticmethod[dict[int, Any]]" not callable (Reported by 260 tests)
"stdlib/builtins.pyi"(639,19): "self" parameter missing for a non-static method (or an invalid type for self) (Reported by 260 tests)
"stdlib/builtins.pyi"(640,4): "staticmethod[dict[int, int]]" not callable (Reported by 260 tests)
"stdlib/builtins.pyi"(643,4): "staticmethod[dict[int, int | None]]" not callable (Reported by 260 tests)
"stdlib/builtins.pyi"(647,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(647,44): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(647,65): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(652,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(652,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(654,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(655,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(655,75): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(659,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(661,23): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(661,50): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(665,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection" (Reported by 260 tests)
"stdlib/builtins.pyi"(668,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(668,44): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(668,60): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(668,66): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(668,81): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(668,93): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(672,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(672,65): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(675,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(675,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(677,23): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(677,66): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(684,104): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(686,74): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(688,24): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(691,4): Signature of "count" incompatible with supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(695,33): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(695,55): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(703,4): Return type "int" of "index" incompatible with return type "int" in supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(716,51): "tuple" expects 1 type argument, but 3 given (Reported by 260 tests)
"stdlib/builtins.pyi"(725,52): "tuple" expects 1 type argument, but 3 given (Reported by 260 tests)
"stdlib/builtins.pyi"(732,33): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(732,55): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(744,40): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(747,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection" (Reported by 260 tests)
"stdlib/builtins.pyi"(749,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(750,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(760,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(760,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(761,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(761,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(779,21): Argument 1 of "append" is incompatible with supertype "typing.MutableSequence"; supertype defines the argument type as "int" (Reported by 260 tests)
"stdlib/builtins.pyi"(782,4): Signature of "count" incompatible with supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(787,33): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(787,55): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(793,21): Argument 1 of "extend" is incompatible with supertype "typing.MutableSequence"; supertype defines the argument type as "Iterable[int]" (Reported by 260 tests)
"stdlib/builtins.pyi"(796,4): Return type "int" of "index" incompatible with return type "int" in supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(797,43): Argument 2 of "insert" is incompatible with supertype "typing.MutableSequence"; supertype defines the argument type as "int" (Reported by 260 tests)
"stdlib/builtins.pyi"(810,51): "tuple" expects 1 type argument, but 3 given (Reported by 260 tests)
"stdlib/builtins.pyi"(821,52): "tuple" expects 1 type argument, but 3 given (Reported by 260 tests)
"stdlib/builtins.pyi"(828,33): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(828,55): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(840,40): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(843,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection" (Reported by 260 tests)
"stdlib/builtins.pyi"(846,4): Signature of "__getitem__" incompatible with supertype "typing.MutableSequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(846,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(850,4): Signature of "__setitem__" incompatible with supertype "typing.MutableSequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(854,4): Signature of "__delitem__" incompatible with supertype "typing.MutableSequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(857,52): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(860,51): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(864,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(864,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(865,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(865,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(874,17): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(885,23): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(885,34): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(887,25): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(887,36): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(889,28): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(889,39): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(904,45): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(905,27): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(906,33): "type" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/builtins.pyi"(908,27): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(908,66): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(908,77): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(910,27): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(910,4): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(910,77): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(910,88): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(912,27): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/builtins.pyi"(912,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(912,4): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(912,60): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(912,71): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(914,4): Overloaded function signature 4 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(914,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(914,4): Overloaded function signature 4 will never be matched: signature 3's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/builtins.pyi"(914,63): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(914,74): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(915,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(916,47): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(916,68): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(919,27): Argument 1 of "__contains__" is incompatible with supertype "typing.Sequence"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(919,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Container" (Reported by 260 tests)
"stdlib/builtins.pyi"(919,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Sequence" (Reported by 260 tests)
"stdlib/builtins.pyi"(921,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection" (Reported by 260 tests)
"stdlib/builtins.pyi"(922,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object" (Reported by 260 tests)
"stdlib/builtins.pyi"(922,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(923,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object" (Reported by 260 tests)
"stdlib/builtins.pyi"(927,47): "tuple" expects 1 type argument, but 2 given (Reported by 260 tests)
"stdlib/builtins.pyi"(927,68): Unexpected "..." (Reported by 260 tests)
"stdlib/builtins.pyi"(947,44): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(111,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(112,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(159,39): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(165,46): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(166,47): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(167,47): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(168,33): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(169,34): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(170,34): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(175,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(176,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(189,26): Name "UserString" is not defined (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(204,59): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(205,35): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(206,39): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(207,40): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(208,41): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(209,33): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(210,34): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(211,36): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(212,44): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(213,28): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(214,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(215,48): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(219,46): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(237,47): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(238,23): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(239,50): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(243,63): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(244,63): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(246,91): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(249,47): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(251,50): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(256,49): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(257,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(258,23): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(259,39): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(260,23): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(261,35): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(287,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(314,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(322,50): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(323,29): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(323,41): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(324,40): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(325,41): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(343,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(379,57): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(380,57): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(381,57): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(382,56): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(459,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(532,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(533,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(549,25): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/collections/__init__.pyi"(573,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(211,39): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(235,36): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(248,34): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(250,28): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(250,37): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(251,29): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(251,38): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(252,29): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(252,38): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(253,28): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(312,40): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(313,40): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(314,41): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(315,41): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(324,24): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(331,34): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(331,43): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(332,35): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(332,44): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(333,35): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(333,44): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(56,12): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/enum.pyi"(56,24): Unsupported left operand type for | ("type[str]") (Reported by 260 tests)
"stdlib/io.pyi"(174,15): Cannot override writeable attribute "read" in base "IOBase" with read-only property in base "_RawIOBase" (Reported by 260 tests)
"stdlib/io.pyi"(174,15): Cannot override writeable attribute "write" in base "IOBase" with read-only property in base "_RawIOBase" (Reported by 260 tests)
"stdlib/io.pyi"(175,20): Cannot override writeable attribute "read" in base "IOBase" with read-only property in base "_BufferedIOBase" (Reported by 260 tests)
"stdlib/io.pyi"(175,20): Cannot override writeable attribute "write" in base "IOBase" with read-only property in base "_BufferedIOBase" (Reported by 260 tests)
"stdlib/io.pyi"(176,16): Cannot override writeable attribute "read" in base "IOBase" with read-only property in base "_TextIOBase" (Reported by 260 tests)
"stdlib/io.pyi"(176,16): Cannot override writeable attribute "write" in base "IOBase" with read-only property in base "_TextIOBase" (Reported by 260 tests)
"stdlib/io.pyi"(176,16): Definition of "__iter__" in base class "_TextIOBase" is incompatible with definition in base class "IOBase" (Reported by 260 tests)
"stdlib/io.pyi"(176,16): Definition of "__next__" in base class "_TextIOBase" is incompatible with definition in base class "IOBase" (Reported by 260 tests)
"stdlib/io.pyi"(176,16): Definition of "readline" in base class "_TextIOBase" is incompatible with definition in base class "IOBase" (Reported by 260 tests)
"stdlib/io.pyi"(176,16): Definition of "readlines" in base class "_TextIOBase" is incompatible with definition in base class "IOBase" (Reported by 260 tests)
"stdlib/io.pyi"(277,15): Variable "io._OpenFile" is not valid as a type (Reported by 260 tests)
"stdlib/io.pyi"(285,15): Variable "io._OpenFile" is not valid as a type (Reported by 260 tests)
"stdlib/io.pyi"(293,0): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/io.pyi"(293,15): Variable "io._OpenFile" is not valid as a type (Reported by 260 tests)
"stdlib/json/__init__.pyi"(16,6): Cannot find implementation or library stub for module named "json.decoder" (Reported by 260 tests)
"stdlib/json/__init__.pyi"(17,6): Cannot find implementation or library stub for module named "json.encoder" (Reported by 260 tests)
"stdlib/os/__init__.pyi"(1019,27): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/os/__init__.pyi"(1154,49): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/os/__init__.pyi"(256,18): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/os/__init__.pyi"(300,61): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/os/__init__.pyi"(300,8): Signatures of "__ior__" and "__or__" are incompatible (Reported by 260 tests)
"stdlib/os/__init__.pyi"(302,69): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/os/__init__.pyi"(302,8): Signatures of "__ior__" and "__or__" are incompatible (Reported by 260 tests)
"stdlib/os/__init__.pyi"(44,4): Can only assign concrete classes to a variable of type "type[Iterator]" (Reported by 260 tests)
"stdlib/os/__init__.pyi"(446,0): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/os/__init__.pyi"(446,0): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/os/__init__.pyi"(447,0): Overloaded function implementation does not accept all possible parameters of signature 1 (Reported by 260 tests)
"stdlib/os/__init__.pyi"(447,0): Overloaded function implementation does not accept all possible parameters of signature 2 (Reported by 260 tests)
"stdlib/os/__init__.pyi"(447,0): Overloaded function implementation does not accept all possible parameters of signature 3 (Reported by 260 tests)
"stdlib/os/__init__.pyi"(448,4): An implementation for an overloaded function is not allowed in a stub file (Reported by 260 tests)
"stdlib/os/__init__.pyi"(608,9): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/os/__init__.pyi"(840,73): A function returning TypeVar should receive at least one argument containing the same Typevar (Reported by 260 tests)
"stdlib/os/__init__.pyi"(930,10): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/os/__init__.pyi"(971,39): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/os/__init__.pyi"(972,40): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/os/__init__.pyi"(975,40): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/os/__init__.pyi"(976,41): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/os/__init__.pyi"(983,12): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/os/__init__.pyi"(984,4): Unsupported left operand type for | ("type[tuple[Any, ...]]") (Reported by 260 tests)
"stdlib/os/__init__.pyi"(997,10): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/os/__init__.pyi"(997,22): Unsupported left operand type for | ("type[Mapping[bytes, bytes | str]]") (Reported by 260 tests)
"stdlib/re.pyi"(203,8): Module has no attribute "SRE_FLAG_ASCII" (Reported by 260 tests)
"stdlib/re.pyi"(205,12): Module has no attribute "SRE_FLAG_DEBUG" (Reported by 260 tests)
"stdlib/re.pyi"(206,8): Module has no attribute "SRE_FLAG_IGNORECASE" (Reported by 260 tests)
"stdlib/re.pyi"(208,8): Module has no attribute "SRE_FLAG_LOCALE" (Reported by 260 tests)
"stdlib/re.pyi"(210,8): Module has no attribute "SRE_FLAG_MULTILINE" (Reported by 260 tests)
"stdlib/re.pyi"(212,8): Module has no attribute "SRE_FLAG_DOTALL" (Reported by 260 tests)
"stdlib/re.pyi"(214,8): Module has no attribute "SRE_FLAG_VERBOSE" (Reported by 260 tests)
"stdlib/re.pyi"(216,8): Module has no attribute "SRE_FLAG_UNICODE" (Reported by 260 tests)
"stdlib/re.pyi"(219,12): Module has no attribute "SRE_FLAG_TEMPLATE" (Reported by 260 tests)
"stdlib/re.pyi"(244,12): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/re.pyi"(244,24): Unsupported left operand type for | ("type[int]") (Reported by 260 tests)
"stdlib/sre_constants.pyi"(12,47): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sre_parse.pyi"(30,19): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sre_parse.pyi"(31,23): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sre_parse.pyi"(32,11): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sre_parse.pyi"(33,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sre_parse.pyi"(34,9): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sre_parse.pyi"(35,11): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sre_parse.pyi"(6,26): Module "sre_constants" has no attribute "error" (Reported by 260 tests)
"stdlib/sre_parse.pyi"(88,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sre_parse.pyi"(89,19): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(105,9): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(106,10): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(107,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(108,18): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(109,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(109,37): Name "SSLSocket" is not defined (Reported by 155 tests)
"stdlib/ssl.pyi"(109,49): Name "SSLObject" is not defined (Reported by 155 tests)
"stdlib/ssl.pyi"(109,72): Name "SSLSocket" is not defined (Reported by 155 tests)
"stdlib/ssl.pyi"(242,16): Cannot assign to final name "CERT_NONE" (Reported by 155 tests)
"stdlib/ssl.pyi"(243,20): Cannot assign to final name "CERT_OPTIONAL" (Reported by 140 tests)
"stdlib/ssl.pyi"(244,20): Cannot assign to final name "CERT_REQUIRED" (Reported by 140 tests)
"stdlib/ssl.pyi"(246,0): Cannot assign to final name "CERT_NONE" (Reported by 155 tests)
"stdlib/ssl.pyi"(251,0): Cannot assign to final name "CERT_OPTIONAL" (Reported by 140 tests)
"stdlib/ssl.pyi"(256,0): Cannot assign to final name "CERT_REQUIRED" (Reported by 140 tests)
"stdlib/ssl.pyi"(290,26): Cannot assign to final name "PROTOCOL_TLS_CLIENT" (Reported by 155 tests)
"stdlib/ssl.pyi"(291,26): Cannot assign to final name "PROTOCOL_TLS_SERVER" (Reported by 155 tests)
"stdlib/ssl.pyi"(300,0): Cannot assign to final name "PROTOCOL_TLS_CLIENT" (Reported by 155 tests)
"stdlib/ssl.pyi"(302,0): Cannot assign to final name "PROTOCOL_TLS_SERVER" (Reported by 155 tests)
"stdlib/ssl.pyi"(414,34): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(416,34): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(418,36): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(439,75): Name "socket._RetAddress" is not defined (Reported by 155 tests)
"stdlib/ssl.pyi"(440,110): Name "socket._RetAddress" is not defined (Reported by 155 tests)
"stdlib/ssl.pyi"(467,8): An implementation for an overloaded function is not allowed in a stub file (Reported by 260 tests)
"stdlib/ssl.pyi"(476,41): Name "socket._RetAddress" is not defined (Reported by 155 tests)
"stdlib/ssl.pyi"(482,29): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(482,46): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(482,56): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(483,34): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(483,51): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(483,61): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(484,29): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(484,46): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(484,56): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(541,76): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/ssl.pyi"(694,0): Cannot assign to final name "PROTOCOL_DTLS_CLIENT" (Reported by 140 tests)
"stdlib/ssl.pyi"(696,0): Cannot assign to final name "PROTOCOL_DTLS_SERVER" (Reported by 140 tests)
"stdlib/ssl.pyi"(698,0): Cannot assign to final name "MBEDTLS_VERSION" (Reported by 140 tests)
"stdlib/ssl.pyi"(89,5): Cannot find implementation or library stub for module named "tls" (Reported by 105 tests)
"stdlib/sys/__init__.pyi"(161,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sys/__init__.pyi"(168,16): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sys/__init__.pyi"(24,11): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sys/__init__.pyi"(24,23): Unsupported left operand type for | ("type[str]") (Reported by 260 tests)
"stdlib/sys/__init__.pyi"(25,13): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sys/__init__.pyi"(332,17): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sys/__init__.pyi"(333,17): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sys/__init__.pyi"(333,29): Unsupported left operand type for | ("_SpecialForm") (Reported by 260 tests)
"stdlib/sys/__init__.pyi"(345,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sys/__init__.pyi"(484,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/sys/__init__.pyi"(484,27): Unsupported left operand type for | ("object") (Reported by 260 tests)
"stdlib/types.pyi"(100,9): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/types.pyi"(226,13): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/types.pyi"(291,13): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/types.pyi"(299,70): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/types.pyi"(356,51): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/types.pyi"(373,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/types.pyi"(393,27): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/types.pyi"(442,66): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/types.pyi"(511,107): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/types.pyi"(592,29): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 260 tests)
"stdlib/types.pyi"(592,71): The first argument to Callable must be a list of types, parameter specification, or "..." (Reported by 260 tests)
"stdlib/types.pyi"(604,53): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(1,0): Module shadows the typeshed module "typing" (Reported by 260 tests)
"stdlib/typing.pyi"(1026,38): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(1026,60): "Mapping" expects no type arguments, but 2 given (Reported by 260 tests)
"stdlib/typing.pyi"(1026,73): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(1027,13): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(140,13): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(140,20): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(146,27): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(148,39): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(182,43): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(182,55): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(199,38): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(331,31): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(331,39): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(346,19): Variable "typing._F" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(346,26): Variable "typing._F" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(347,23): Variable "typing._F" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(347,30): Variable "typing._F" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(348,39): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(348,60): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(351,33): Variable "typing._F" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(351,40): Variable "typing._F" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(357,36): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(357,44): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(382,27): Variable "typing._TC" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(382,35): Variable "typing._TC" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(384,18): Invalid base class "Protocol" (Reported by 260 tests)
"stdlib/typing.pyi"(389,20): Invalid base class "Protocol" (Reported by 260 tests)
"stdlib/typing.pyi"(394,22): Invalid base class "Protocol" (Reported by 260 tests)
"stdlib/typing.pyi"(399,20): Invalid base class "Protocol" (Reported by 260 tests)
"stdlib/typing.pyi"(404,20): Invalid base class "Protocol" (Reported by 260 tests)
"stdlib/typing.pyi"(409,18): Invalid base class "Protocol[_T_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(411,25): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(414,20): Invalid base class "Protocol[_T_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(420,44): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(423,12): Invalid base class "Protocol" (Reported by 260 tests)
"stdlib/typing.pyi"(428,15): Invalid base class "Protocol" (Reported by 260 tests)
"stdlib/typing.pyi"(436,15): Invalid base class "Protocol[_T_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(438,26): "Iterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(438,35): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(441,15): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(441,24): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(441,32): Invalid base class "Protocol[_T_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(443,26): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(444,26): "Iterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(444,35): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(447,17): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(447,26): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(447,34): Invalid base class "Protocol[_T_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(449,30): "Iterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(449,39): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(452,61): Unexpected keyword argument "default" for "TypeVar" (Reported by 260 tests)
"stdlib/typing.pyi"(453,53): Unexpected keyword argument "default" for "TypeVar" (Reported by 260 tests)
"stdlib/typing.pyi"(455,16): "Iterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(455,25): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(455,38): Invalid base class "Generic[_YieldT_co, _SendT_contra, _ReturnT_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(456,26): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(458,26): Variable "typing._SendT_contra" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(458,47): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(461,121): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(464,97): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(466,26): "Generator" expects no type arguments, but 3 given (Reported by 260 tests)
"stdlib/typing.pyi"(466,36): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(466,48): Variable "typing._SendT_contra" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(466,63): Variable "typing._ReturnT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(474,30): "Generator" expects no type arguments, but 3 given (Reported by 260 tests)
"stdlib/typing.pyi"(474,40): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(474,45): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(474,50): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(484,48): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(484,69): Invalid base class "Protocol[_T_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(487,58): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(487,79): Invalid base class "Protocol[_T_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(490,16): Invalid base class "Protocol[_T_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(492,27): "Generator" expects no type arguments, but 3 given (Reported by 260 tests)
"stdlib/typing.pyi"(492,37): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(492,42): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(492,47): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(498,16): "Awaitable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(498,26): Variable "typing._ReturnT_co_nd" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(498,43): Invalid base class "Generic[_YieldT_co, _SendT_contra_nd, _ReturnT_co_nd]" (Reported by 260 tests)
"stdlib/typing.pyi"(502,26): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(510,26): Variable "typing._SendT_contra_nd" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(510,50): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(513,121): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(516,97): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(523,0): Class typing.AwaitableGenerator has abstract attributes "__await__", "send", "throw" (Reported by 260 tests)
"stdlib/typing.pyi"(524,14): Variable "typing._ReturnT_co_nd" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(524,4): "Awaitable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(525,14): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(525,26): Variable "typing._SendT_contra_nd" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(525,4): "Generator" expects no type arguments, but 3 given (Reported by 260 tests)
"stdlib/typing.pyi"(525,44): Variable "typing._ReturnT_co_nd" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(526,4): Invalid base class "Generic[_YieldT_co, _SendT_contra_nd, _ReturnT_co_nd, _S]" (Reported by 260 tests)
"stdlib/typing.pyi"(531,20): Invalid base class "Protocol[_T_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(533,27): "AsyncIterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(533,41): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(536,20): "AsyncIterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(536,34): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(536,42): Invalid base class "Protocol[_T_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(538,27): "Awaitable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(538,37): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(539,27): "AsyncIterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(539,41): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(541,21): "AsyncIterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(541,35): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(541,48): Invalid base class "Generic[_YieldT_co, _SendT_contra]" (Reported by 260 tests)
"stdlib/typing.pyi"(542,27): "Coroutine" expects no type arguments, but 3 given (Reported by 260 tests)
"stdlib/typing.pyi"(542,37): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(542,42): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(542,47): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(544,27): Variable "typing._SendT_contra" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(544,48): "Coroutine" expects no type arguments, but 3 given (Reported by 260 tests)
"stdlib/typing.pyi"(544,58): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(544,63): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(544,68): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(549,19): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(549,24): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(549,29): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(549,9): "Coroutine" expects no type arguments, but 3 given (Reported by 260 tests)
"stdlib/typing.pyi"(552,108): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(552,113): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(552,118): Variable "typing._YieldT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(552,98): "Coroutine" expects no type arguments, but 3 given (Reported by 260 tests)
"stdlib/typing.pyi"(553,24): "Coroutine" expects no type arguments, but 3 given (Reported by 260 tests)
"stdlib/typing.pyi"(553,34): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(553,39): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(555,26): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(564,16): Invalid base class "Protocol[_T_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(570,17): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(570,26): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(570,34): "Container" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(570,44): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(570,52): Invalid base class "Protocol[_T_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(575,15): "Reversible" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(575,26): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(575,34): "Collection" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(575,45): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(578,41): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(581,43): "Sequence" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(581,52): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(583,27): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(584,27): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(586,26): "Iterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(586,35): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(587,30): "Iterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(587,39): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(589,22): "Sequence" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(589,31): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(591,40): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(594,41): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(597,43): "MutableSequence" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(597,59): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(600,45): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(603,47): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(603,56): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(611,28): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(613,29): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(613,38): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(615,38): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(616,28): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(617,31): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(617,40): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(617,48): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(619,18): "Collection" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(619,29): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(624,28): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(624,40): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(625,28): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(625,40): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(626,28): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(626,40): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(627,28): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(627,40): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(628,29): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(628,41): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(628,50): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(628,62): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(629,28): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(629,40): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(629,48): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(629,60): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(629,68): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(630,29): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(630,41): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(630,50): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(630,62): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(631,29): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(631,41): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(631,49): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(631,61): Variable "typing._T_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(631,69): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(633,32): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(633,41): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(635,17): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(635,29): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(637,25): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(639,29): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(642,21): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(643,28): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(644,26): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(644,38): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(644,46): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(645,27): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(645,39): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(645,4): Signatures of "__iand__" and "__and__" are incompatible (Reported by 260 tests)
"stdlib/typing.pyi"(645,48): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(646,27): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(646,39): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(646,47): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(647,27): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(647,39): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(647,4): Signatures of "__isub__" and "__sub__" are incompatible (Reported by 260 tests)
"stdlib/typing.pyi"(647,48): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(650,32): "Mapping" expects no type arguments, but 2 given (Reported by 260 tests)
"stdlib/typing.pyi"(650,40): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(650,45): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(653,29): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(653,47): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(653,55): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(653,65): Invalid base class "Generic[_KT_co, _VT_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(654,32): "Mapping" expects no type arguments, but 2 given (Reported by 260 tests)
"stdlib/typing.pyi"(654,40): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(654,48): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(655,29): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(655,38): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(655,4): Return type "set[tuple[Any, Any]]" of "__and__" incompatible with return type "AbstractSet" in supertype "AbstractSet" (Reported by 260 tests)
"stdlib/typing.pyi"(655,57): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(655,65): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(656,30): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(656,39): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(656,51): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(658,26): "Iterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(658,41): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(658,49): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(659,30): "Iterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(659,45): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(659,53): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(660,28): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(660,37): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(660,4): Return type "set[tuple[Any, Any] | Any]" of "__or__" incompatible with return type "AbstractSet" in supertype "AbstractSet" (Reported by 260 tests)
"stdlib/typing.pyi"(660,55): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(660,63): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(660,73): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(661,29): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(661,38): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(661,56): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(661,64): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(661,74): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(662,29): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(662,38): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(662,4): Return type "set[tuple[Any, Any]]" of "__sub__" incompatible with return type "AbstractSet" in supertype "AbstractSet" (Reported by 260 tests)
"stdlib/typing.pyi"(662,57): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(662,65): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(663,30): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(663,39): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(663,51): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(664,29): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(664,38): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(664,4): Return type "set[tuple[Any, Any] | Any]" of "__xor__" incompatible with return type "AbstractSet" in supertype "AbstractSet" (Reported by 260 tests)
"stdlib/typing.pyi"(664,56): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(664,64): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(664,74): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(665,30): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(665,39): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(665,57): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(665,65): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(665,75): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(667,28): "AbstractSet" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(667,40): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(668,32): "Mapping" expects no type arguments, but 2 given (Reported by 260 tests)
"stdlib/typing.pyi"(668,40): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(668,48): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(669,29): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(669,38): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(669,4): Return type "set[Any]" of "__and__" incompatible with return type "AbstractSet" in supertype "AbstractSet" (Reported by 260 tests)
"stdlib/typing.pyi"(669,51): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(670,30): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(670,39): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(670,51): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(672,26): "Iterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(672,35): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(673,30): "Iterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(673,39): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(674,28): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(674,37): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(674,4): Return type "set[Any]" of "__or__" incompatible with return type "AbstractSet" in supertype "AbstractSet" (Reported by 260 tests)
"stdlib/typing.pyi"(674,49): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(674,58): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(675,29): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(675,38): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(675,50): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(675,59): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(676,29): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(676,38): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(676,4): Return type "set[Any]" of "__sub__" incompatible with return type "AbstractSet" in supertype "AbstractSet" (Reported by 260 tests)
"stdlib/typing.pyi"(676,51): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(677,30): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(677,39): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(677,51): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(678,29): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(678,38): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(678,4): Return type "set[Any]" of "__xor__" incompatible with return type "AbstractSet" in supertype "AbstractSet" (Reported by 260 tests)
"stdlib/typing.pyi"(678,50): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(678,59): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(679,30): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(679,39): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(679,51): Variable "typing._KT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(679,60): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(681,30): "Collection" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(681,41): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(682,32): "Mapping" expects no type arguments, but 2 given (Reported by 260 tests)
"stdlib/typing.pyi"(682,40): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(682,45): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(684,26): "Iterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(684,35): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(685,30): "Iterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(685,39): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(687,14): "Collection" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(687,25): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(687,31): Invalid base class "Generic[_KT, _VT_co]" (Reported by 260 tests)
"stdlib/typing.pyi"(691,31): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(691,42): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(694,23): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(694,34): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(696,23): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(696,40): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(696,49): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(696,56): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(696,65): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(697,23): "ItemsView" expects no type arguments, but 2 given (Reported by 260 tests)
"stdlib/typing.pyi"(697,33): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(697,38): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(698,22): "KeysView" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(698,31): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(699,24): "ValuesView" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(699,35): Variable "typing._VT_co" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(703,21): "Mapping" expects no type arguments, but 2 given (Reported by 260 tests)
"stdlib/typing.pyi"(703,29): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(703,34): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(705,31): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(705,43): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(707,31): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(710,23): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(710,34): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(712,23): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(712,40): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(712,48): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(714,23): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(714,40): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(714,47): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(714,53): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(715,31): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(715,36): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(723,25): "MutableMapping" expects no type arguments, but 2 given (Reported by 260 tests)
"stdlib/typing.pyi"(723,40): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(723,45): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(723,62): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(723,95): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(725,30): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(725,44): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(725,55): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(747,47): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(747,52): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(747,71): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(749,24): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(749,39): Variable "typing._KT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(749,44): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(749,64): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(751,31): Variable "typing._VT" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(760,9): Invalid base class "Generic[AnyStr]" (Reported by 260 tests)
"stdlib/typing.pyi"(769,28): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(781,38): Variable "typing.AnyStr" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(783,23): "IO" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(787,46): Variable "typing.AnyStr" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(789,51): Variable "typing.AnyStr" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(802,20): "IO" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(805,23): Variable "typing.AnyStr" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(811,20): "IO" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(814,20): "IO" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(817,25): "IO" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(817,43): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(820,32): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(820,41): Variable "typing.AnyStr" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(822,26): Variable "typing.AnyStr" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(824,26): "Iterator" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(824,35): Variable "typing.AnyStr" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(826,27): "IO" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(826,30): Variable "typing.AnyStr" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(830,15): "IO" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(834,13): "IO" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(845,26): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(850,16): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(850,46): Unsupported left operand type for | ("type[bytes]") (Reported by 260 tests)
"stdlib/typing.pyi"(854,35): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(855,4): Unsupported left operand type for | ("type[object]") (Reported by 260 tests)
"stdlib/typing.pyi"(869,28): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(870,17): "Mapping" expects no type arguments, but 2 given (Reported by 260 tests)
"stdlib/typing.pyi"(870,30): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(872,19): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(879,17): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(879,31): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(891,23): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(891,31): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(897,19): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(897,29): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(897,37): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(899,24): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(899,32): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(901,27): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(901,35): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(921,23): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(924,21): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(925,13): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(932,46): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(932,66): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(937,72): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(939,29): "Iterable" expects no type arguments, but 1 given (Reported by 260 tests)
"stdlib/typing.pyi"(939,38): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(939,47): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(940,35): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(941,33): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(941,41): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(948,17): "Mapping" expects no type arguments, but 2 given (Reported by 260 tests)
"stdlib/typing.pyi"(949,15): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(951,27): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(952,27): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(958,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(961,28): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(963,21): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(963,38): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(964,21): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(964,28): Variable "typing._T" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(965,29): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(966,4): Return type "dict_items[str, object]" of "items" incompatible with return type "ItemsView" in supertype "Mapping" (Reported by 260 tests)
"stdlib/typing.pyi"(967,4): Return type "dict_keys[str, object]" of "keys" incompatible with return type "KeysView" in supertype "Mapping" (Reported by 260 tests)
"stdlib/typing.pyi"(968,4): Return type "dict_values[str, object]" of "values" incompatible with return type "ValuesView" in supertype "Mapping" (Reported by 260 tests)
"stdlib/typing.pyi"(971,32): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(971,62): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(973,42): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(975,33): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(975,63): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(977,43): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(977,8): Signatures of "__ror__" of "_TypedDict" and "__or__" of "dict[str, Any]" are unsafely overlapping (Reported by 260 tests)
"stdlib/typing.pyi"(979,33): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(979,63): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing.pyi"(986,23): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(989,24): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing.pyi"(992,71): Variable "typing.Any" is not valid as a type (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(342,17): Metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(353,22): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(356,28): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(358,21): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(363,29): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(366,32): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(366,44): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(368,8): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(370,33): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(370,45): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(372,8): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(374,33): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(374,45): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(406,20): Invalid base class "Protocol" (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(496,26): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(496,39): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(527,51): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(529,45): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(568,17): Invalid base class "Protocol" (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(611,17): Invalid type comment or annotation (Reported by 260 tests)
"stdlib/typing_extensions.pyi"(614,36): Invalid type comment or annotation (Reported by 260 tests)
"string/templatelib.pyi"(2,5): Cannot find implementation or library stub for module named "ustring" (Reported by 6 tests)
"stubs/mypy-extensions/mypy_extensions.pyi"(19,0): Class stubs.mypy-extensions.mypy_extensions._TypedDict has abstract attributes "__getitem__" (Reported by 260 tests)
"stubs/mypy-extensions/mypy_extensions.pyi"(19,17): Metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases (Reported by 260 tests)
"stubs/mypy-extensions/mypy_extensions.pyi"(26,28): Invalid type comment or annotation (Reported by 260 tests)
"stubs/mypy-extensions/mypy_extensions.pyi"(28,21): Invalid type comment or annotation (Reported by 260 tests)
"stubs/mypy-extensions/mypy_extensions.pyi"(33,29): Invalid type comment or annotation (Reported by 260 tests)
"time.pyi"(119,21): Variable "time._Ticks" is not valid as a type (Reported by 71 tests)
"time.pyi"(119,47): Variable "time._Ticks" is not valid as a type (Reported by 71 tests)
"time.pyi"(48,10): Invalid type comment or annotation (Reported by 71 tests)
"time.pyi"(49,10): Invalid type comment or annotation (Reported by 71 tests)
"time.pyi"(50,11): Invalid type comment or annotation (Reported by 71 tests)
"time.pyi"(53,23): Variable "time._Ticks" is not valid as a type (Reported by 71 tests)
"time.pyi"(53,39): Variable "time._Ticks" is not valid as a type (Reported by 71 tests)
"ubluetooth.pyi"(2,5): Cannot find implementation or library stub for module named "bluetooth" (Reported by 127 tests)
"ucryptolib.pyi"(2,5): Cannot find implementation or library stub for module named "cryptolib" (Reported by 74 tests)
"uctypes.pyi"(115,11): Invalid type comment or annotation (Reported by 152 tests)
"uctypes.pyi"(116,13): Invalid type comment or annotation (Reported by 152 tests)
"uctypes.pyi"(116,25): Unsupported left operand type for | ("type[tuple[Any, ...]]") (Reported by 152 tests)
"uctypes.pyi"(117,11): Invalid type comment or annotation (Reported by 97 tests)
"uctypes.pyi"(118,13): Invalid type comment or annotation (Reported by 97 tests)
"uctypes.pyi"(118,25): Unsupported left operand type for | ("type[tuple[Any, ...]]") (Reported by 97 tests)
"umachine.pyi"(2,5): Cannot find implementation or library stub for module named "machine" (Reported by 6 tests)
"uwebsocket.pyi"(2,5): Cannot find implementation or library stub for module named "websocket" (Reported by 122 tests)
"vfs.pyi"(104,0): Class vfs.VfsRom has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 10 tests)
"vfs.pyi"(105,0): Class vfs.VfsFat has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 4 tests)
"vfs.pyi"(105,0): Class vfs.VfsLfs1 has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 4 tests)
"vfs.pyi"(107,0): Class vfs.VfsFat has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 60 tests)
"vfs.pyi"(109,0): Class vfs.VfsFat has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 73 tests)
"vfs.pyi"(113,0): Class vfs.VfsLfs2 has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 10 tests)
"vfs.pyi"(132,0): Class vfs.VfsLfs1 has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 4 tests)
"vfs.pyi"(137,0): Class vfs.VfsLfs2 has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 10 tests)
"vfs.pyi"(138,0): Class vfs.VfsPosix has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 4 tests)
"vfs.pyi"(159,0): Class vfs.VfsLfs2 has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 4 tests)
"vfs.pyi"(165,0): Class vfs.VfsPosix has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 4 tests)
"vfs.pyi"(186,0): Class vfs.VfsLfs2 has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 4 tests)
"vfs.pyi"(67,0): Class vfs.VfsLfs2 has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 60 tests)
"vfs.pyi"(67,0): Class vfs.VfsPosix has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 4 tests)
"vfs.pyi"(69,0): Class vfs.VfsLfs2 has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 73 tests)
"vfs.pyi"(69,0): Class vfs.VfsPosix has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 7 tests)
"vfs.pyi"(69,0): Class vfs.VfsRom has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 4 tests)
"vfs.pyi"(76,0): Class vfs.VfsFat has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 10 tests)
"vfs.pyi"(78,0): Class vfs.VfsFat has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 14 tests)
"vfs.pyi"(88,0): Class vfs.VfsPosix has abstract attributes "ioctl", "readblocks", "writeblocks" (Reported by 3 tests)
```
