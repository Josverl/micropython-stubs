# ty failures and expected failures

[Back to type checker test report](typecheck_report.md)

<a id="typecheck-detail-ty-ca5f102067e3"></a>
## - stdlib stdlib_only - XFAIL

**Full test specification**

```text
tests/quality_tests/test_stdlib_only.py::test_typecheck_stdlib_only[ty-local-stdlib_only---stdlib]
```

```text
ty found 10 errors and 1 warnings in 3 files.
assert 10 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_stdlib_only_ty_0/check_io.py"(12,29): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_stdlib_only_ty_0/check_ssl.py"(48,24): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_stdlib_only_ty_0/check_ssl.py"(48,44): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_stdlib_only_ty_0/check_ssl.py"(48,55): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_stdlib_only_ty_0/check_sys/check_stdio.py"(6,0): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_stdlib_only_ty_0/check_sys/check_stdio.py"(11,0): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_stdlib_only_ty_0/check_sys/check_stdio.py"(28,15): unresolved-attribute: Attribute `readinto` is not defined on `BinaryIO` in union `BinaryIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_stdlib_only_ty_0/check_sys/check_stdio.py"(33,20): unresolved-attribute: Attribute `readinto` is not defined on `BinaryIO` in union `BinaryIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_stdlib_only_ty_0/check_sys/check_stdio.py"(41,8): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_stdlib_only_ty_0/check_sys/check_stdio.py"(42,8): unresolved-attribute: Attribute `readinto` is not defined on `BinaryIO` in union `BinaryIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_stdlib_only_ty_0/check_sys/check_stdio.py"(43,8): unresolved-attribute: Attribute `readinto` is not defined on `BinaryIO` in union `BinaryIO | Any`
```

<a id="typecheck-detail-ty-3cceaf1f077c"></a>
## v1.29.0 esp32 asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e3/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-348035a3ce4d"></a>
## v1.29.0 esp32 bluetooth - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-bluetooth-ty]
```

```text
ty found 10 errors and 1 warnings in 8 files.
assert 10 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e2/check_examples/ble_advertising.py"(85,39): invalid-argument-type: Argument to `UUID.__init__` is incorrect: Expected `int | str`, found `float*`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e2/check_examples/ble_bonding_peripheral.py"(130,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e2/check_examples/ble_bonding_peripheral.py"(196,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e2/check_examples/ble_simple_central.py"(222,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e2/check_examples/ble_simple_central.py"(244,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e2/check_examples/ble_simple_peripheral.py"(102,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e2/check_examples/ble_temperature.py"(99,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e2/check_examples/ble_temperature_central.py"(242,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e2/check_examples/ble_temperature_central.py"(251,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e2/check_examples/ble_uart_peripheral.py"(114,12): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e2/check_examples/ble_uart_repl.py"(84,4): unresolved-attribute: Module `os` has no member `dupterm`
```

<a id="typecheck-detail-ty-f145429371c4"></a>
## v1.29.0 esp32 esp32 - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32-ty]
```

```text
ty found 3 errors and 4 warnings in 2 files.
assert 3 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e5/check_machine/check_Pin.py"(56,4): deprecated: The function `read` is deprecated: Use read_u16() instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e5/check_machine/check_Pin.py"(59,4): deprecated: The function `atten` is deprecated: Use ADC.init(atten=atten) instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e5/check_machine/check_Pin.py"(61,4): deprecated: The function `width` is deprecated: Use ADC.block().init(bits=bits) instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e5/check_machine/check_Pin.py"(64,4): deprecated: The function `read` is deprecated: Use read_u16() instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e5/check_machine/check_devices.py"(12,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e5/check_machine/check_devices.py"(14,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e5/check_machine/check_devices.py"(27,0): unresolved-attribute: Module `time` has no member `sleep_ms`
```

<a id="typecheck-detail-ty-53c8d4773419"></a>
## v1.29.0 esp32 espnow - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-espnow-ty]
```

```text
ty found 3 errors and 1 warnings in 2 files.
assert 3 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e8/check_espnow.py"(14,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e8/check_utils/timer.py"(5,25): unresolved-import: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e8/check_utils/timer.py"(5,35): unresolved-import: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e8/check_utils/timer.py"(5,47): unresolved-import: Module `utime` has no member `ticks_ms`
```

<a id="typecheck-detail-ty-8df47c05d5f8"></a>
## v1.29.0 esp32 micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-micropython-ty]
```

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e11/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-4d03a823d9c3"></a>
## v1.29.0 esp32 networking - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-networking-ty]
```

```text
ty found 4 errors and 7 warnings in 4 files.
assert 4 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e15/check_examples/http_client_ssl.py"(15,12): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e15/check_examples/http_client_ssl.py"(21,10): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e15/check_examples/http_client_ssl.py"(22,16): deprecated: The function `read` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.recv` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e15/check_examples/http_server_ssl.py"(66,23): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e15/check_examples/http_server_ssl.py"(69,12): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e15/check_examples/http_server_ssl.py"(70,12): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e15/check_examples/http_server_ssl.py"(90,29): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e15/check_ssl_1.py"(16,42): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e15/check_ssl_2.py"(50,20): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e15/check_ssl_2.py"(52,20): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e15/check_ssl_2.py"(53,20): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
```

<a id="typecheck-detail-ty-c91e7751c088"></a>
## v1.29.0 esp32 stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e17/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-135acccd1e2e"></a>
## v1.29.0 esp32-esp32_generic_c6 asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e34/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-2f69e3102b4a"></a>
## v1.29.0 esp32-esp32_generic_c6 bluetooth - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-bluetooth-ty]
```

```text
ty found 10 errors and 1 warnings in 8 files.
assert 10 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e15/check_examples/ble_advertising.py"(85,39): invalid-argument-type: Argument to `UUID.__init__` is incorrect: Expected `int | str`, found `float*`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e15/check_examples/ble_bonding_peripheral.py"(130,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e15/check_examples/ble_bonding_peripheral.py"(196,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e15/check_examples/ble_simple_central.py"(222,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e15/check_examples/ble_simple_central.py"(244,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e15/check_examples/ble_simple_peripheral.py"(102,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e15/check_examples/ble_temperature.py"(99,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e15/check_examples/ble_temperature_central.py"(242,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e15/check_examples/ble_temperature_central.py"(251,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e15/check_examples/ble_uart_peripheral.py"(114,12): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e15/check_examples/ble_uart_repl.py"(84,4): unresolved-attribute: Module `os` has no member `dupterm`
```

<a id="typecheck-detail-ty-3636e15d0f51"></a>
## v1.29.0 esp32-esp32_generic_c6 esp32 - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-esp32-ty]
```

```text
ty found 6 errors and 4 warnings in 4 files.
assert 3 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e14/check_machine/check_Pin.py"(56,4): deprecated: The function `read` is deprecated: Use read_u16() instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e14/check_machine/check_Pin.py"(59,4): deprecated: The function `atten` is deprecated: Use ADC.init(atten=atten) instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e14/check_machine/check_Pin.py"(64,4): deprecated: The function `read` is deprecated: Use read_u16() instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e14/check_machine/check_devices.py"(12,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e14/check_machine/check_devices.py"(14,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e14/check_machine/check_devices.py"(27,0): unresolved-attribute: Module `time` has no member `sleep_ms`
```

<a id="typecheck-detail-ty-572896766017"></a>
## v1.29.0 esp32-esp32_generic_c6 espnow - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-espnow-ty]
```

```text
ty found 3 errors and 1 warnings in 2 files.
assert 3 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e21/check_espnow.py"(14,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e21/check_utils/timer.py"(5,25): unresolved-import: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e21/check_utils/timer.py"(5,35): unresolved-import: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e21/check_utils/timer.py"(5,47): unresolved-import: Module `utime` has no member `ticks_ms`
```

<a id="typecheck-detail-ty-bc3654cc236a"></a>
## v1.29.0 esp32-esp32_generic_c6 micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-micropython-ty]
```

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e22/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-98d9afc44aa5"></a>
## v1.29.0 esp32-esp32_generic_c6 networking - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-networking-ty]
```

```text
ty found 4 errors and 7 warnings in 4 files.
assert 4 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e9/check_examples/http_client_ssl.py"(15,12): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e9/check_examples/http_client_ssl.py"(21,10): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e9/check_examples/http_client_ssl.py"(22,16): deprecated: The function `read` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.recv` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e9/check_examples/http_server_ssl.py"(66,23): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e9/check_examples/http_server_ssl.py"(69,12): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e9/check_examples/http_server_ssl.py"(70,12): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e9/check_examples/http_server_ssl.py"(90,29): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e9/check_ssl_1.py"(16,42): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e9/check_ssl_2.py"(50,20): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e9/check_ssl_2.py"(52,20): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e9/check_ssl_2.py"(53,20): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
```

<a id="typecheck-detail-ty-6909a76f92f9"></a>
## v1.29.0 esp32-esp32_generic_c6 stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_c6-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e28/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-5fa7a8ff91c2"></a>
## v1.29.0 esp32-esp32_generic_s3 asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e43/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-c0eb20268d4e"></a>
## v1.29.0 esp32-esp32_generic_s3 bluetooth - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-bluetooth-ty]
```

```text
ty found 10 errors and 1 warnings in 8 files.
assert 10 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e61/check_examples/ble_advertising.py"(85,39): invalid-argument-type: Argument to `UUID.__init__` is incorrect: Expected `int | str`, found `float*`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e61/check_examples/ble_bonding_peripheral.py"(130,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e61/check_examples/ble_bonding_peripheral.py"(196,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e61/check_examples/ble_simple_central.py"(222,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e61/check_examples/ble_simple_central.py"(244,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e61/check_examples/ble_simple_peripheral.py"(102,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e61/check_examples/ble_temperature.py"(99,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e61/check_examples/ble_temperature_central.py"(242,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e61/check_examples/ble_temperature_central.py"(251,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e61/check_examples/ble_uart_peripheral.py"(114,12): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e61/check_examples/ble_uart_repl.py"(84,4): unresolved-attribute: Module `os` has no member `dupterm`
```

<a id="typecheck-detail-ty-30f9263e0d0e"></a>
## v1.29.0 esp32-esp32_generic_s3 esp32 - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-esp32-ty]
```

```text
ty found 4 errors and 4 warnings in 3 files.
assert 3 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e27/check_machine/check_Pin.py"(56,4): deprecated: The function `read` is deprecated: Use read_u16() instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e27/check_machine/check_Pin.py"(59,4): deprecated: The function `atten` is deprecated: Use ADC.init(atten=atten) instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e27/check_machine/check_Pin.py"(64,4): deprecated: The function `read` is deprecated: Use read_u16() instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e27/check_machine/check_devices.py"(12,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e27/check_machine/check_devices.py"(14,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e27/check_machine/check_devices.py"(27,0): unresolved-attribute: Module `time` has no member `sleep_ms`
```

<a id="typecheck-detail-ty-3d29f56d4e66"></a>
## v1.29.0 esp32-esp32_generic_s3 espnow - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-espnow-ty]
```

```text
ty found 3 errors and 1 warnings in 2 files.
assert 3 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e20/check_espnow.py"(14,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e20/check_utils/timer.py"(5,25): unresolved-import: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e20/check_utils/timer.py"(5,35): unresolved-import: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e20/check_utils/timer.py"(5,47): unresolved-import: Module `utime` has no member `ticks_ms`
```

<a id="typecheck-detail-ty-1647080b5459"></a>
## v1.29.0 esp32-esp32_generic_s3 micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-micropython-ty]
```

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_e33/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-594e82be2737"></a>
## v1.29.0 esp32-esp32_generic_s3 networking - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-networking-ty]
```

```text
ty found 4 errors and 7 warnings in 4 files.
assert 4 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e55/check_examples/http_client_ssl.py"(15,12): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e55/check_examples/http_client_ssl.py"(21,10): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e55/check_examples/http_client_ssl.py"(22,16): deprecated: The function `read` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.recv` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e55/check_examples/http_server_ssl.py"(66,23): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e55/check_examples/http_server_ssl.py"(69,12): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e55/check_examples/http_server_ssl.py"(70,12): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e55/check_examples/http_server_ssl.py"(90,29): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e55/check_ssl_1.py"(16,42): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e55/check_ssl_2.py"(50,20): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e55/check_ssl_2.py"(52,20): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e55/check_ssl_2.py"(53,20): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
```

<a id="typecheck-detail-ty-7122d929796c"></a>
## v1.29.0 esp32-esp32_generic_s3 stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp32-esp32_generic_s3-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_e37/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-271cd8b86577"></a>
## v1.29.0 esp8266 micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp8266-micropython-ty]
```

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e32/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-3a2fcf5232ef"></a>
## v1.29.0 esp8266 networking - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp8266-networking-ty]
```

```text
ty found 4 errors and 7 warnings in 4 files.
assert 4 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e25/check_examples/http_client_ssl.py"(15,12): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e25/check_examples/http_client_ssl.py"(21,10): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e25/check_examples/http_client_ssl.py"(22,16): deprecated: The function `read` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.recv` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e25/check_examples/http_server_ssl.py"(66,23): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e25/check_examples/http_server_ssl.py"(69,12): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e25/check_examples/http_server_ssl.py"(70,12): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e25/check_examples/http_server_ssl.py"(90,29): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e25/check_ssl_1.py"(16,42): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e25/check_ssl_2.py"(50,20): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e25/check_ssl_2.py"(52,20): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_e25/check_ssl_2.py"(53,20): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
```

<a id="typecheck-detail-ty-11176c683854"></a>
## v1.29.0 esp8266 stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-esp8266-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_e38/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-e5371b325318"></a>
## v1.29.0 rp2 asm_pio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-asm_pio-ty]
```

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r8/check_asm_pio_code.py"(50,23): unresolved-attribute: Module `time` has no member `ticks_ms`
```

<a id="typecheck-detail-ty-62075a18b4ec"></a>
## v1.29.0 rp2 asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r19/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-09f6f0e2a242"></a>
## v1.29.0 rp2 micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-micropython-ty]
```

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r7/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-08b1d7c3d3cf"></a>
## v1.29.0 rp2 rp2 - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rp2-ty]
```

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r1/check_machine/check_Pin.py"(20,4): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r1/check_machine/check_Pin.py"(22,4): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r1/check_machine/check_ds18x20.py"(12,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r1/check_time.py"(6,0): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r1/check_time.py"(7,0): unresolved-attribute: Module `utime` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r1/check_time.py"(8,8): unresolved-attribute: Module `utime` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r1/check_time.py"(9,8): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r1/check_time.py"(9,24): unresolved-attribute: Module `utime` has no member `ticks_ms`
```

<a id="typecheck-detail-ty-5a13d8e658d7"></a>
## v1.29.0 rp2 stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r13/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-dd7ee0f13b16"></a>
## v1.29.0 rp2-rpi_pico asm_pio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-asm_pio-ty]
```

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r27/check_asm_pio_code.py"(50,23): unresolved-attribute: Module `time` has no member `ticks_ms`
```

<a id="typecheck-detail-ty-84bac47a77de"></a>
## v1.29.0 rp2-rpi_pico asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r13/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-f7ad84e3fb3d"></a>
## v1.29.0 rp2-rpi_pico micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-micropython-ty]
```

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r1/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-80615def3cb4"></a>
## v1.29.0 rp2-rpi_pico rp2 - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-rp2-ty]
```

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r14/check_machine/check_Pin.py"(20,4): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r14/check_machine/check_Pin.py"(22,4): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r14/check_machine/check_ds18x20.py"(12,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r14/check_time.py"(6,0): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r14/check_time.py"(7,0): unresolved-attribute: Module `utime` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r14/check_time.py"(8,8): unresolved-attribute: Module `utime` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r14/check_time.py"(9,8): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r14/check_time.py"(9,24): unresolved-attribute: Module `utime` has no member `ticks_ms`
```

<a id="typecheck-detail-ty-a9cafbf6429d"></a>
## v1.29.0 rp2-rpi_pico stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r7/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-d1c433596264"></a>
## v1.29.0 rp2-rpi_pico2 asm_pio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-asm_pio-ty]
```

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r53/check_asm_pio_code.py"(50,23): unresolved-attribute: Module `time` has no member `ticks_ms`
```

<a id="typecheck-detail-ty-2728d14a98ae"></a>
## v1.29.0 rp2-rpi_pico2 asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r41/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-ae72db2b19ed"></a>
## v1.29.0 rp2-rpi_pico2 micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-micropython-ty]
```

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r25/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-c37faaf2402e"></a>
## v1.29.0 rp2-rpi_pico2 rp2 - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-rp2-ty]
```

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r19/check_machine/check_Pin.py"(20,4): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r19/check_machine/check_Pin.py"(22,4): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r19/check_machine/check_ds18x20.py"(12,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r19/check_time.py"(6,0): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r19/check_time.py"(7,0): unresolved-attribute: Module `utime` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r19/check_time.py"(8,8): unresolved-attribute: Module `utime` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r19/check_time.py"(9,8): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r19/check_time.py"(9,24): unresolved-attribute: Module `utime` has no member `ticks_ms`
```

<a id="typecheck-detail-ty-61300be3ac3f"></a>
## v1.29.0 rp2-rpi_pico2 stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r31/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-70aa8e4f3b7a"></a>
## v1.29.0 rp2-rpi_pico2_w asm_pio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-asm_pio-ty]
```

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_r41/check_asm_pio_code.py"(50,23): unresolved-attribute: Module `time` has no member `ticks_ms`
```

<a id="typecheck-detail-ty-4113fb6d5a36"></a>
## v1.29.0 rp2-rpi_pico2_w asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r59/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-2ec44712092c"></a>
## v1.29.0 rp2-rpi_pico2_w micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-micropython-ty]
```

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r33/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-1d2daa7938a7"></a>
## v1.29.0 rp2-rpi_pico2_w networking - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-networking-ty]
```

```text
ty found 4 errors and 7 warnings in 4 files.
assert 4 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r59/check_examples/http_client_ssl.py"(15,12): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r59/check_examples/http_client_ssl.py"(21,10): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r59/check_examples/http_client_ssl.py"(22,16): deprecated: The function `read` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.recv` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r59/check_examples/http_server_ssl.py"(66,23): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r59/check_examples/http_server_ssl.py"(69,12): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r59/check_examples/http_server_ssl.py"(70,12): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r59/check_examples/http_server_ssl.py"(90,29): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r59/check_ssl_1.py"(16,42): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r59/check_ssl_2.py"(50,20): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r59/check_ssl_2.py"(52,20): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r59/check_ssl_2.py"(53,20): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
```

<a id="typecheck-detail-ty-a8cd1e706df5"></a>
## v1.29.0 rp2-rpi_pico2_w rp2 - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-rp2-ty]
```

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r27/check_machine/check_Pin.py"(20,4): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r27/check_machine/check_Pin.py"(22,4): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r27/check_machine/check_ds18x20.py"(12,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r27/check_time.py"(6,0): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r27/check_time.py"(7,0): unresolved-attribute: Module `utime` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r27/check_time.py"(8,8): unresolved-attribute: Module `utime` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r27/check_time.py"(9,8): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r27/check_time.py"(9,24): unresolved-attribute: Module `utime` has no member `ticks_ms`
```

<a id="typecheck-detail-ty-e0de2afa46ce"></a>
## v1.29.0 rp2-rpi_pico2_w stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico2_w-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r53/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-ca428241d499"></a>
## v1.29.0 rp2-rpi_pico_w aioble - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-aioble-ty]
```

```text
ty found 12 errors and 0 warnings in 9 files.
assert 11 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r49/community_code/sample_1.py"(11,17): unresolved-import: Module `time` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r49/community_code/sample_1.py"(53,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r49/examples_bluetooth/ble_advertising.py"(85,39): invalid-argument-type: Argument to `UUID.__init__` is incorrect: Expected `int | str`, found `float*`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r49/examples_bluetooth/ble_bonding_peripheral.py"(196,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r49/examples_bluetooth/ble_simple_central.py"(222,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r49/examples_bluetooth/ble_simple_central.py"(244,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r49/examples_bluetooth/ble_simple_peripheral.py"(102,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r49/examples_bluetooth/ble_temperature.py"(99,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r49/examples_bluetooth/ble_temperature_central.py"(242,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r49/examples_bluetooth/ble_temperature_central.py"(251,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r49/examples_bluetooth/ble_uart_peripheral.py"(114,12): unresolved-attribute: Module `time` has no member `sleep_ms`
```

<a id="typecheck-detail-ty-6decd13a4df1"></a>
## v1.29.0 rp2-rpi_pico_w asm_pio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-asm_pio-ty]
```

```text
ty found 1 errors and 0 warnings in 1 files.
assert 1 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r15/check_asm_pio_code.py"(50,23): unresolved-attribute: Module `time` has no member `ticks_ms`
```

<a id="typecheck-detail-ty-2ea9f3a6c423"></a>
## v1.29.0 rp2-rpi_pico_w asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r38/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-328672f30765"></a>
## v1.29.0 rp2-rpi_pico_w bluetooth - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-bluetooth-ty]
```

```text
ty found 10 errors and 1 warnings in 8 files.
assert 9 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r43/check_examples/ble_advertising.py"(85,39): invalid-argument-type: Argument to `UUID.__init__` is incorrect: Expected `int | str`, found `float*`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r43/check_examples/ble_bonding_peripheral.py"(130,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r43/check_examples/ble_bonding_peripheral.py"(196,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r43/check_examples/ble_simple_central.py"(222,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r43/check_examples/ble_simple_central.py"(244,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r43/check_examples/ble_simple_peripheral.py"(102,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r43/check_examples/ble_temperature.py"(99,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r43/check_examples/ble_temperature_central.py"(242,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r43/check_examples/ble_temperature_central.py"(251,8): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r43/check_examples/ble_uart_peripheral.py"(114,12): unresolved-attribute: Module `time` has no member `sleep_ms`
```

<a id="typecheck-detail-ty-4028b26ebea6"></a>
## v1.29.0 rp2-rpi_pico_w micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-micropython-ty]
```

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r26/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-1b7bd7a8b45d"></a>
## v1.29.0 rp2-rpi_pico_w networking - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-networking-ty]
```

```text
ty found 4 errors and 7 warnings in 4 files.
assert 4 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r21/check_examples/http_client_ssl.py"(15,12): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r21/check_examples/http_client_ssl.py"(21,10): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r21/check_examples/http_client_ssl.py"(22,16): deprecated: The function `read` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.recv` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r21/check_examples/http_server_ssl.py"(66,23): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r21/check_examples/http_server_ssl.py"(69,12): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r21/check_examples/http_server_ssl.py"(70,12): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r21/check_examples/http_server_ssl.py"(90,29): deprecated: The function `write` is deprecated: Deprecated since Python 3.6. Use `SSLSocket.send` method instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r21/check_ssl_1.py"(16,42): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r21/check_ssl_2.py"(50,20): deprecated: The function `wrap_socket` is deprecated: Deprecated since Python 3.7; removed in Python 3.12. Use `SSLContext.wrap_socket()` instead.
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r21/check_ssl_2.py"(52,20): unknown-argument: Argument `cert` does not match any known parameter of function `wrap_socket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_r21/check_ssl_2.py"(53,20): unknown-argument: Argument `key` does not match any known parameter of function `wrap_socket`
```

<a id="typecheck-detail-ty-6eb3effd45a5"></a>
## v1.29.0 rp2-rpi_pico_w rp2 - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-rp2-ty]
```

```text
ty found 8 errors and 0 warnings in 3 files.
assert 8 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r33/check_machine/check_Pin.py"(20,4): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r33/check_machine/check_Pin.py"(22,4): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r33/check_machine/check_ds18x20.py"(12,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r33/check_time.py"(6,0): unresolved-attribute: Module `utime` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r33/check_time.py"(7,0): unresolved-attribute: Module `utime` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r33/check_time.py"(8,8): unresolved-attribute: Module `utime` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r33/check_time.py"(9,8): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_r33/check_time.py"(9,24): unresolved-attribute: Module `utime` has no member `ticks_ms`
```

<a id="typecheck-detail-ty-d89d363a4003"></a>
## v1.29.0 rp2-rpi_pico_w stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-rp2-rpi_pico_w-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_r32/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-073ff6324364"></a>
## v1.29.0 samd asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s30/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-6bc262ee1cd2"></a>
## v1.29.0 samd micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-micropython-ty]
```

```text
ty found 21 errors and 2 warnings in 4 files.
assert 18 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s17/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-7bd9c87d6249"></a>
## v1.29.0 samd stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_s23/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-1c0e835245b6"></a>
## v1.29.0 samd-seeed_wio_terminal asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-seeed_wio_terminal-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s16/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-918d20107591"></a>
## v1.29.0 samd-seeed_wio_terminal micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-seeed_wio_terminal-micropython-ty]
```

```text
ty found 21 errors and 2 warnings in 4 files.
assert 18 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s48/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-36ef4ca58f5e"></a>
## v1.29.0 samd-seeed_wio_terminal stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-samd-seeed_wio_terminal-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_s10/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-75763f53fe6f"></a>
## v1.29.0 stm32 asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s17/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-fb90518fe573"></a>
## v1.29.0 stm32 micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-micropython-ty]
```

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s5/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-9905cf0ff099"></a>
## v1.29.0 stm32 stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_s11/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-42739240d0a8"></a>
## v1.29.0 stm32-pybv11 asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-pybv11-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s22/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-3db3889bc258"></a>
## v1.29.0 stm32-pybv11 micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-pybv11-micropython-ty]
```

```text
ty found 21 errors and 2 warnings in 4 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s10/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-2acaae7c81e4"></a>
## v1.29.0 stm32-pybv11 stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-stm32-pybv11-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_s16/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-40ba38b843d6"></a>
## v1.29.0 unix asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-unix-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_u6/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-7145b8712d99"></a>
## v1.29.0 unix micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-unix-micropython-ty]
```

```text
ty found 22 errors and 2 warnings in 5 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_u2/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-c145fe273b4b"></a>
## v1.29.0 unix stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-unix-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_u3/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-3267e5b12640"></a>
## v1.29.0 webassembly micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-webassembly-micropython-ty]
```

```text
ty found 22 errors and 2 warnings in 5 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w7/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-2d22baf13466"></a>
## v1.29.0 webassembly stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-webassembly-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw3/test_typecheck_local_v1_29_0_w5/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```

<a id="typecheck-detail-ty-4379a2376c42"></a>
## v1.29.0 webassembly webassembly - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-webassembly-webassembly-ty]
```

```text
ty found 15 errors and 0 warnings in 7 files.
assert 15 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_config.py"(8,20): unknown-argument: Argument `target` does not match any known parameter of function `display`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_config.py"(8,36): unknown-argument: Argument `append` does not match any known parameter of function `display`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_ffi_storage.py"(23,4): invalid-assignment: Cannot assign to a subscript on an object of type `Preferences`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_html.py"(11,37): unknown-argument: Argument `target` does not match any known parameter of function `display`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_html.py"(29,0): unresolved-attribute: Unresolved attribute `onopen` on type `WebSocket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_html.py"(30,0): unresolved-attribute: Unresolved attribute `onmessage` on type `WebSocket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_html.py"(31,0): unresolved-attribute: Unresolved attribute `onclose` on type `WebSocket`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_modules.py"(16,22): too-many-positional-arguments: Too many positional arguments to bound method `Event.remove_listener`: expected 1, got 2
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_pyworker.py"(5,23): unknown-argument: Argument `target` does not match any known parameter of function `display`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_pyworker.py"(5,40): unknown-argument: Argument `append` does not match any known parameter of function `display`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_when.py"(10,15): too-many-positional-arguments: Too many positional arguments to function `when`: expected 1, got 2
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_when.py"(18,15): too-many-positional-arguments: Too many positional arguments to function `when`: expected 1, got 2
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_when.py"(28,14): too-many-positional-arguments: Too many positional arguments to function `when`: expected 1, got 2
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_workers.py"(6,19): missing-argument: No arguments provided for required parameters `x2`, `x3` of function `create_named_worker`
"/tmp/pytest-of-vscode/pytest-15/popen-gw1/test_typecheck_local_v1_29_0_w1/check_pyscript/check_workers.py"(6,68): unknown-argument: Argument `type` does not match any known parameter of function `create_named_worker`
```

<a id="typecheck-detail-ty-16ea3ca16cef"></a>
## v1.29.0 windows asyncio - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-windows-asyncio-ty]
```

```text
ty found 22 errors and 2 warnings in 6 files.
assert 22 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_basics_03.py"(9,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/aiorepl.py"(64,12): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/aiorepl.py"(103,33): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `TextIO | Any`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/aiorepl.py"(110,12): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/aiorepl.py"(120,20): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/aiorepl.py"(127,24): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/aiorepl.py"(128,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/aiorepl.py"(154,42): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/aiorepl.py"(198,20): no-matching-overload: No overload of bound method `IO.write` matches arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/auart_hd.py"(25,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/auart_hd.py"(25,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/auart_hd.py"(25,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/auart_hd.py"(26,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/auart_hd.py"(34,22): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/auart_hd.py"(38,22): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/auart_hd.py"(51,23): missing-argument: No arguments provided for required parameters `reader`, `loop` of `StreamWriter.__init__`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/auart_hd.py"(51,44): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `WriteTransport`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/auart_hd.py"(51,55): invalid-argument-type: Argument to `StreamWriter.__init__` is incorrect: Expected `BaseProtocol`, found `dict[Unknown, Unknown]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/auart_hd.py"(52,44): invalid-argument-type: Argument to `StreamReader.__init__` is incorrect: Expected `int`, found `UART`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/auart_hd.py"(68,18): unresolved-attribute: Object of type `StreamWriter` has no attribute `awrite`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_demo/roundrobin.py"(21,14): unresolved-attribute: Module `uasyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_tasks.py"(11,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_tasks.py"(13,14): unresolved-attribute: Module `asyncio` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw2/test_typecheck_local_v1_29_0_w8/check_wait_for_ms.py"(11,23): unresolved-attribute: Module `asyncio` has no member `wait_for_ms`
```

<a id="typecheck-detail-ty-18163d6a0ffe"></a>
## v1.29.0 windows micropython - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-windows-micropython-ty]
```

```text
ty found 22 errors and 2 warnings in 5 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_gc.py"(8,12): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_gc.py"(14,10): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_gc.py"(21,0): unresolved-attribute: Module `gc` has no member `threshold`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_gc.py"(21,13): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_gc.py"(21,34): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_gc.py"(33,46): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_gc.py"(33,61): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_gc.py"(41,49): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_gc.py"(41,64): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_gc.py"(43,47): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_gc.py"(43,62): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_gc.py"(45,54): unresolved-attribute: Module `gc` has no member `mem_free`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_gc.py"(45,69): unresolved-attribute: Module `gc` has no member `mem_alloc`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_micropython/check_native.py"(16,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_micropython/check_native.py"(17,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_time.py"(6,0): unresolved-attribute: Module `time` has no member `sleep_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_time.py"(7,0): unresolved-attribute: Module `time` has no member `sleep_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_time.py"(8,8): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_time.py"(9,8): unresolved-attribute: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_time.py"(9,24): unresolved-attribute: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_timedfunction.py"(17,12): unresolved-attribute: Module `utime` has no member `ticks_us`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_timedfunction.py"(19,16): unresolved-attribute: Module `utime` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w4/check_timedfunction.py"(19,33): unresolved-attribute: Module `utime` has no member `ticks_us`
```

<a id="typecheck-detail-ty-ce3f92c06743"></a>
## v1.29.0 windows stdlib - XFAIL

**Full test specification**

```text
tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-windows-stdlib-ty]
```

```text
ty found 21 errors and 20 warnings in 12 files.
assert 21 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_collections/check_namedtuple_2.py"(7,0): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_io.py"(6,23): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_io.py"(7,22): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_io.py"(11,24): invalid-argument-type: Argument to `BufferedWriter.__init__` is incorrect: Argument type `TextIOWrapper[_WrappedBuffer]` does not satisfy upper bound `_BufferedWriterStream` of type variable `_BufferedWriterStreamT`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(37,4): undefined-reveal: `reveal_type` used without importing it
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(42,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(43,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(44,26): too-many-positional-arguments: Too many positional arguments to function `dump`: expected 2, got 3
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(54,37): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(57,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(58,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(59,52): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(60,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(61,44): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(62,49): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(65,40): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(66,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(67,54): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(68,48): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(69,46): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_json/check_json.py"(70,51): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_os/check_files.py"(26,15): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_os/check_mount.py"(9,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_os/check_mount.py"(13,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_os/check_mount.py"(17,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_os/check_os_mount.py"(8,0): unresolved-attribute: Module `os` has no member `mount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_os/check_os_mount.py"(10,0): unresolved-attribute: Module `os` has no member `umount`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_sys/check_executable.py"(4,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_sys/check_print_exception.py"(3,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_sys/check_sys.py"(24,0): unresolved-attribute: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_time.py"(6,22): invalid-argument-type: Argument to function `mktime` is incorrect: Expected `tuple[int, int, int, int, int, int, int, int, int]`, found `tuple[Literal[2024], Literal[12], Literal[29], Literal[17], Literal[33], Literal[32], Literal[6], Literal[364]]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_time.py"(11,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_time.py"(11,27): unresolved-import: Module `time` has no member `ticks_diff`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_time.py"(11,39): unresolved-import: Module `time` has no member `ticks_add`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_time.py"(12,16): unresolved-import: Module `sys` has no member `print_exception`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_time.py"(30,17): unresolved-import: Module `time` has no member `ticks_ms`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_time.py"(34,33): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_time.py"(38,38): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_time.py"(48,19): unused-type-ignore-comment: Unused blanket `type: ignore` directive
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_uio.py"(7,24): invalid-argument-type: Argument to `StringIO.__init__` is incorrect: Expected `str | None`, found `Literal[512]`
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w10/check_uio.py"(8,23): invalid-argument-type: Argument to `BytesIO.__init__` is incorrect: Expected `Buffer`, found `Literal[512]`
```
