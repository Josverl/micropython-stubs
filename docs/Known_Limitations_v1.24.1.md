# Known Limitations in v1.24.1 of the micropython-stubs

This is a list of known limitations in the v1.24.1 the micropython-stubs.
This list was collated on Feb 1, 2025. 


## stdlib
The micropython-stdlib-stubs have a customised version of the typeshed  stdlib stubs.
while this does provide a lot of functionality, it there are a few remaining issues that need to be resolved.
As currently only pyright can work with 

QA test | code fragment| type check error 
--------|--------------| ----------------
feat_bluetooth\check_examples\ble_uart_repl.py:46: | `os.dupterm_notify(None) # stubs-ignore: linter=="pyright"`| -
feat_stdlib\check_collections\check_ordereddict.py:14: | `[("z", 1), ("a", 2)]  # stubs-ignore:  linter in ["pyright"]`| error: Argument of type "list[tuple[str, int]]" cannot be assigned to parameter "map" of type "Mapping[_KT@OrderedDict, _VT@OrderedDict]" in function "__init__"
feat_stdlib_only\check_ssl.py:48: | `return (ssl.wrap_socket(client, cert=cert, key=key, **self.kwargs), #type: ignore # stubs-ignore: port == "stdlib"`| -
feat_stdlib_only\check_collections\check_ordereddict.py:5: | `d = OrderedDict([("z", 1), ("a", 2)])  # stubs-ignore: linter == "pyright"`| -
feat_stdlib_only\check_sys\check_sys.py:31: | `previous = sys.atexit(byebye) # stubs-ignore: linter == "mypy"`| error: Module has no attribute "atexit"; maybe "exit"?  [attr-defined]
feat_asyncio\check_demo\aiorepl.py:67: |`return await exec_task  `| # type: ignore # pyright/mypy doesn't like the await here
feat_asyncio\check_demo\aiorepl.py:197: |`sys.stdout.write(b)  # type: ignore `| # TODO write(bytes) not supported by stubs
feat_asyncio\check_demo\auart_hd.py:17: |`from primitives.delay_ms import Delay_ms  # type: ignore`|

## MYPY  micropython stdlib stubs

Currently mypy cannot (yet) use the micropython stdlib stubs. as a result of this the differences between MicroPython and CPython are not taken into account. 
This means that mypy will report errors for things that actually work  MicroPython. 
There is work planned to further reduce the number of errors reported by mypy.
See: https://github.com/Josverl/micropython-stubs/issues/781


QA test | code fragment| type check error 
--------|--------------| ----------------
feat_aioble\community_code\sample_1.py:53: | `await asyncio.sleep_ms(4)  # stubs-ignore: linter == "mypy"`| 
feat_aioble\examples_bluetooth\ble_bonding_peripheral.py:140: | `key = sec_type, bytes(key)  # stubs-ignore: linter == "mypy"`| 
feat_asyncio\check_basics_01.py:31: | `tasks[x] = asyncio.create_task(bar2(x))  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_basics_03.py:9: | `await asyncio.sleep_ms(200 * n)  # Pause by varying amounts # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\aiorepl.py:103: | `s = asyncio.StreamReader(sys.stdin)  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\aiorepl.py:106: | `hist = [] * _HISTORY_LIMIT  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\aiorepl.py:173: | `cmd  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\aiorepl.py:180: | `sys.stdout.write(b)  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\aiorepl.py:183: | `sys.stdout.write(b)  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\aiorepl.py:191: | `sys.stdout.write(cmd)  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\auart_hd.py:25: | `self.swriter = asyncio.StreamWriter(self.uart, {})  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\auart_hd.py:26: | `self.sreader = asyncio.StreamReader(self.uart)  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\auart_hd.py:34: | `await self.swriter.awrite(  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\auart_hd.py:38: | `await asyncio.sleep_ms(300)  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\auart_hd.py:51: | `self.swriter = asyncio.StreamWriter(self.uart, {})  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\auart_hd.py:52: | `self.sreader = asyncio.StreamReader(self.uart)  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\auart_hd.py:68: | `await self.swriter.awrite("{}\r\n".format(command))  # stubs-ignore: linter=="mypy"`| 
feat_asyncio\check_demo\roundrobin.py:21: | `await asyncio.sleep_ms(0)  # stubs-ignore: linter=="mypy"`| 
feat_networking\check_examples\http_client.py:18: | `s.write(b"GET / HTTP/1.0\r\n\r\n")  # stubs-ignore: linter == "mypy"`| 
feat_networking\check_examples\http_client.py:19: | `print(s.read())  # stubs-ignore: linter == "mypy"`| 
feat_stdlib\check_array.py:5: | `ar = array.array("I", [0 for _ in range(NUM_LEDS)])  # stubs-ignore:  linter == "mypy"`| 
feat_stdlib\check_io.py:7: | `buffer_1 = io.StringIO(alloc_size)  # stubs-ignore: version<=1.18.0 or linter == "mypy"`| 
feat_stdlib\check_io.py:8: | `buffer_2 = io.BytesIO(alloc_size)  # stubs-ignore: version<=1.18.0 or linter == "mypy"`| 
feat_stdlib\check_io.py:12: | `buf = io.BufferedWriter(stream, 8) # stubs-ignore:  linter == "mypy"`| Argument 1 to "BufferedWriter" has incompatible type "TextIOWrapper[_WrappedBuffer]"; expected "RawIOBase"  [arg-type]
feat_stdlib\check_uio.py:7: | `buffer_1 = uio.StringIO(alloc_size)  # stubs-ignore:  linter == "mypy"`| 
feat_stdlib\check_uio.py:8: | `buffer_2 = uio.BytesIO(alloc_size)  # stubs-ignore:  linter == "mypy"`| 
feat_stdlib\check_sys\check_print_exception.py:3: | `from sys import print_exception  # stubs-ignore: linter == "mypy"`| 
feat_stdlib\check_sys\check_sys.py:24: | `sys.print_exception(exc)  # stubs-ignore:  linter == "mypy"`| 
feat_stdlib\check_sys\check_sys.py:32: | `previous = sys.atexit(byebye)  # stubs-ignore:  linter == "mypy"`| 


## Differences between functionality in ports
Different ports (and boards) implement a different subset of the MicroPython functionality.
Sometimes this is due to hardware differences, sometimes it is due to the fact that the port is not yet fully implemented.
In testing a number of these differences have been encounteres, and silenced to reduce the test-noise caused by these differences.

QA test | code fragment| type check error 
--------|--------------| ----------------
feat_machine\check_machine\check_deepsleep.py:9: | `if machine.reset_cause() == machine.DEEPSLEEP_RESET:  # stubs-ignore: port in ['samd','rp2']`| 
feat_machine\check_machine\check_deepsleep.py:15: | `machine.deepsleep(10000)  # stubs-ignore: port=='samd'`| 
feat_micropython\check_gc.py:21: | `gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())  # stubs-ignore: port=='samd'`| 
feat_networking\check_ssl_1.py:11: | `protocol=ssl.PROTOCOL_TLS_SERVER  # stubs-ignore: board in ['rpi_pico_w'] or port == 'esp32'`| 
feat_networking\check_network\check_country.py:6: | `network.country("NL")  # stubs-ignore: version <= 1.19.1 or port in ["esp8266"]`| 
feat_stdlib\check_os\check_uname.py:9: | `os.uname().release == "1.13.0"  # stubs-ignore: port in ["samd"]`| 
feat_stdlib\check_os\check_uname.py:10: | `and os.uname().version < "v1.13-103"  # stubs-ignore: port in ["samd"]`| 
feat_stdlib\check_os\check_uname.py:15: | `os_uname = os.uname()  # stubs-ignore: port in ["samd"]`| 
feat_stdlib\check_os\check_uname.py:22: | `assert_type(os_uname.sysname, str)  # stubs-ignore: port in ["samd"]`| 
feat_stdlib\check_os\check_uname.py:23: | `assert_type(os_uname.nodename, str)  # stubs-ignore: port in ["samd"]`| 
feat_stdlib\check_os\check_uname.py:24: | `assert_type(os_uname.release, str)  # stubs-ignore: port in ["samd"]`| 
feat_stdlib\check_os\check_uname.py:25: | `assert_type(os_uname.machine, str)  # stubs-ignore: port in ["samd"]`| 
feat_stdlib\check_os\check_uname.py:26: | `assert_type(os_uname.version, str)  # stubs-ignore: port in ["samd"]`| 

## Miscellaneous

QA test | code fragment| type check error 
--------|--------------| ----------------

feat_espnow\check_espnow.py:22: |`e.send(peer, str(i) * 20, True)  # type: ignore `| # TODO: https://github.com/orgs/micropython/discussions/16654
feat_espnow\check_espnow.py:52: |`print(e.peers_table)  # type: ignore `|# TODO: espnow ESPNow.peers_table - deal with undetectable attributes
feat_espnow\check_utils\timer.py:114: |`i, dt = next(self.timer)  # type: ignore`|
feat_micropython\check_uctypes.py:29: |`assert header.EI_MAG == b"\x7fELF" # type: ignore `| #  uctypes - known member does not work
feat_micropython\check_uctypes.py:30: |`assert header.EI_DATA == 1, "Oops, wrong endianness. Could retry with uctypes.BIG_ENDIAN." # type: ignore `| uctypes - known member does not work
feat_micropython\check_uctypes.py:31: |`print("machine:", hex(header.e_machine))# type: ignore`| uctypes - known member does not work
feat_micropython\check_uctypes.py:58: |`print("x:", struct1.ptr[0].x) # type: ignore `|uctypes - known member does not work
feat_micropython\check_uctypes.py:83: |`WWDG.WWDG_CFR.WDGTB = 0b10  # type: ignore `|uctypes - known member does not work
feat_micropython\check_uctypes.py:84: |`WWDG.WWDG_CR.WDGA = 1  # type: ignore #  `|uctypes - known member does not work
feat_micropython\check_uctypes.py:85: |`print("Current counter:", WWDG.WWDG_CR.T) # type: ignore `|uctypes - known member does not work
feat_micropython\check_micropython\check_asm_thumb.py:1: |`# type: ignore`| micropython.asm_thumb - document that the opcodes are not recognized
feat_micropython\check_micropython\check_viper.py:10: |`buf = ptr8(self.linebuf)  # type: ignore`| micropython.viper - document that the opcodes are not recognized
feat_stdlib\check_uio.py:11: |`buf = io.BufferedWriter(stream, 8)  # type: ignore "`| # TODO stdlib.io "TextIOWrapper" is incompatible with "RawIOBase
feat_stdlib\check_json\check_json.py:56: |`json.dump(data, file, indent=4)  # type: ignore`|
feat_stdlib\check_json\check_json.py:59: |`data = json.load(file, cls=None)  # type: ignore`|
feat_stdlib\check_json\check_json.py:60: |`data = json.load(file, object_hook=None)  # type: ignore`|
feat_stdlib\check_json\check_json.py:61: |`data = json.load(file, object_pairs_hook=None)  # type: ignore`|
feat_stdlib\check_json\check_json.py:62: |`data = json.load(file, parse_float=None)  # type: ignore`|
feat_stdlib\check_json\check_json.py:63: |`data = json.load(file, parse_int=None)  # type: ignore`|
feat_stdlib\check_json\check_json.py:64: |`data = json.load(file, parse_constant=None)  # type: ignore`|
feat_stdlib\check_json\check_json.py:67: |`data = json.loads(JSON_DATA, cls=None)  # type: ignore`|
feat_stdlib\check_json\check_json.py:68: |`data = json.loads(JSON_DATA, object_hook=None)  # type: ignore`|
feat_stdlib\check_json\check_json.py:69: |`data = json.loads(JSON_DATA, object_pairs_hook=None)  # type: ignore`|
feat_stdlib\check_json\check_json.py:70: |`data = json.loads(JSON_DATA, parse_float=None)  # type: ignore`|
feat_stdlib\check_json\check_json.py:71: |`data = json.loads(JSON_DATA, parse_int=None)  # type: ignore`|
feat_stdlib\check_json\check_json.py:72: |`data = json.loads(JSON_DATA, parse_constant=None)  # type: ignore`|
feat_stdlib\check_sys\check_implementation.py:12: |`assert_type(impl, NamedTuple)  # type: ignore | # TODO sys.implementation is not a tuple`
feat_stdlib_only\check_ssl.py:31: |`ctx.load_cert_chain(cert, key) # type: ignore`| 