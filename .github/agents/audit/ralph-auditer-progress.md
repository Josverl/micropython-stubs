# Ralph Auditer Progress Ledger

Status values: pending | in_progress | done | skipped | blocked

| Module | Status | Commit | Notes |
|---|---|---|---|
| reference\micropython\_espnow\__init__.pyi | done | 9df18a103 | Added send() overloads and RATE_* constants from modespnow.c v1.28.0 |
| reference\micropython\_rp2\__init__.pyi | done | efbaf26fc | Removed PIOASMEmit export; not present in _rp2 C module globals |
| reference\micropython\_thread\__init__.pyi | done | 632ad0ea5 | Aligned start_new_thread return/kwargs, stack_size overloads, and LockType/context manager API |
| reference\micropython\aioespnow\__init__.pyi | done |  | No stub changes needed; signatures match lib/micropython-lib/micropython/aioespnow/aioespnow.py |
| reference\micropython\array\__init__.pyi | done | 7669cd57c | Fixed __iadd__ to return array (objarray.c returns lhs_in) |
| reference\micropython\asyncio\__init__.pyi | done | 30800821b | Added exported __version__ constant from extmod/asyncio/__init__.py |
| reference\micropython\asyncio\core.pyi | done |  | No API changes needed after source review against extmod/asyncio/core.py |
| reference\micropython\asyncio\event.pyi | done |  | Corrected wait return annotations to match extmod/asyncio/event.py |
| reference\micropython\asyncio\funcs.pyi | done |  | Corrected wait_for and gather return types to match extmod/asyncio/funcs.py |
| reference\micropython\asyncio\lock.pyi | done |  | Corrected acquire and async context manager return annotations |
| reference\micropython\asyncio\stream.pyi | done |  | Corrected stream/server function return annotations from extmod/asyncio/stream.py |
| reference\micropython\asyncio\task.pyi | done |  | No API changes needed after review against extmod/asyncio/task.py and extmod/modasyncio.c |
| reference\micropython\binascii\__init__.pyi | done |  | Added b2a_base64 newline kwarg from extmod/modbinascii.c |
| reference\micropython\bluetooth\__init__.pyi | done | 362977422 | Added FLAG_* module constants from extmod/modbluetooth.c globals table |
| reference\micropython\btree\__init__.pyi | done | e5b18c7e9 | Aligned close/flush returns and added put/seq legacy methods from extmod/modbtree.c |
| reference\micropython\cmath\__init__.pyi | done |  | Corrected complex-returning function signatures and polar/rect typing |
| reference\micropython\collections\__init__.pyi | done |  | No API changes needed after review against py/modcollections.c |
| reference\micropython\cryptolib\__init__.pyi | done |  | Added MODE_ECB/MODE_CBC/MODE_CTR constants from extmod/modcryptolib.c |
| reference\micropython\deflate\__init__.pyi | done |  | No stub changes needed; API and constants align with extmod/moddeflate.c |
| reference\micropython\errno\__init__.pyi | done |  | No API changes needed after review against py/moderrno.c |
| reference\micropython\esp\__init__.pyi | done |  | Corrected deepsleep signature to support optional second arg from ports/esp8266/modesp.c |
| reference\micropython\esp32\__init__.pyi | done |  | Corrected wake_on_ext0/ext1/gpio overloads (allow no-arg forms) and boolean level type from ports/esp32/modesp32.c |
| reference\micropython\espnow\__init__.pyi | done |  | No API changes needed after review against ports/esp32/modules/espnow.py |
| reference\micropython\framebuf\__init__.pyi | done |  | Corrected color-format constant types, poly() return type, and blit palette type from extmod/modframebuf.c |
| reference\micropython\gc\__init__.pyi | done |  | collect() return typed as int|None to match MICROPY_PY_GC_COLLECT_RETVAL builds |
| reference\micropython\gzip\__init__.pyi | done |  | Corrected function-based API and return types from micropython-lib gzip.py |
| reference\micropython\hashlib\__init__.pyi | done |  | Removed duplicate overload blocks; API verified against extmod/modhashlib.c |
| reference\micropython\heapq\__init__.pyi | done |  | Removed duplicate TypeVar declaration; API verified against extmod/modheapq.c |
| reference\micropython\io\__init__.pyi | done |  | Added missing IOBase and BufferedWriter exports; removed conflicting AnyReadableBuf/AnyWritableBuf redefinitions |
| reference\micropython\jsffi\__init__.pyi | done |  | Removed non-exported __version__ and relaxed JsException/JsProxy construction to match ports/webassembly implementation |
| reference\micropython\json\__init__.pyi | done |  | No API changes needed after review against extmod/modjson.c |
| reference\micropython\lcd160cr\__init__.pyi | done |  | Corrected constants/member types and orient/startup-deco signatures to match micropython-lib lcd160cr.py |
| reference\micropython\machine\__init__.pyi | done |  | Added optional PinBase/DAC/I2CTarget/dht_readinto exports from extmod/modmachine.c globals |
| reference\micropython\machine\ADC.pyi | done |  | Aligned constructor/init/block typing and added WIDTH_13BIT constant from extmod machine_adc + esp32 constants |
| reference\micropython\machine\ADCBlock.pyi | done |  | Made bits keyword optional for constructor/init per extmod/machine_adc_block.c parse helper and docs |
| reference\micropython\machine\ADCWiPy.pyi | done |  | Corrected channel return/callable channel object typing and removed misplaced ADCWiPy.adcchannel method per cc3200 pybadc.c |
| reference\micropython\machine\CAN.pyi | done |  | Tightened enum/flag constant types to int to match extmod/machine_can.c ROM_INT exports |
| reference\micropython\machine\I2C.pyi | done |  | Added constructor timeout kwarg, tightened scan() to list[int], and typed SoftI2C constructor pins/kwargs per machine.I2C docs |
| reference\micropython\machine\I2S.pyi | done |  | Added optional mck kwarg, typed constants as int, and made shift signature keyword-only per machine.I2S docs |
| reference\micropython\machine\Pin.pyi | done |  | Typed Pin mode/pull/IRQ constants as int, irq() return as _IRQ, and toggle() as None |
| reference\micropython\machine\PWM.pyi | done |  | Added invert kwarg to constructor/init per machine.PWM docs; cleaned stale imports |
| reference\micropython\machine\RTC.pyi | done |  | Typed ALARM0 as int, fixed RTC.memory read/write overloads, and relaxed irq return to _IRQ|None |
| reference\micropython\machine\SD.pyi | done |  | Removed positional-only marker so documented keyword args (e.g. pins=...) type-check |
| reference\micropython\machine\SDCard.pyi | done |  | Added documented cmd/data kwargs; removed unused imports |
| reference\micropython\machine\Signal.pyi | done |  | Added explicit __init__ return typing; removed unused import |
| reference\micropython\machine\SPI.pyi | done |  | Set constants to int; adjusted read/write return types for cross-port None|int behavior |
| reference\micropython\machine\Timer.pyi | done |  | ONE_SHOT/PERIODIC constants typed as int |
| reference\micropython\machine\TimerWiPy.pyi | done |  | Added mode/trigger constants and tightened channel/irq/freq typing |
| reference\micropython\machine\UART.pyi | done |  | Added INV_TX/INV_RX and flow-control kwargs (flow/rts/cts); flush->None |
| reference\micropython\machine\USBDevice.pyi | done |  | Normalized BUILTIN_CDC_MSC as descriptor object type |
| reference\micropython\machine\WDT.pyi | done |  | No change; signature already matches docs (id/timeout constructor + feed) |
| reference\micropython\math\__init__.pyi | done |  | Added log(x, base) overload and precise modf tuple typing |
| reference\micropython\micropython\__init__.pyi | done |  | Removed duplicate TypeVar import; API review against py/modmicropython.c |
| reference\micropython\neopixel\__init__.pyi | done |  | No API changes needed after review against neopixel driver/docs |
| reference\micropython\network\__init__.pyi | done |  | Added module-level country/hostname/ipconfig/route and STA/AP/status constants from extmod/modnetwork.c |
| reference\micropython\network\LAN.pyi | done |  | No API changes needed after network-family review against v1.28 sources/docs |
| reference\micropython\network\PPP.pyi | done |  | No API changes needed after network-family review against v1.28 sources/docs |
| reference\micropython\network\WIZNET5K.pyi | done |  | No API changes needed after network-family review against v1.28 sources/docs |
| reference\micropython\network\WLAN.pyi | done |  | No API changes needed after network-family review against v1.28 sources/docs |
| reference\micropython\network\WLANWiPy.pyi | done |  | No API changes needed after network-family review against v1.28 sources/docs |
| reference\micropython\onewire\__init__.pyi | done |  | Tightened scan/reset/read/write/CRC typings to match micropython-lib onewire driver |
| reference\micropython\openamp\__init__.pyi | done |  | Added ENDPOINT_ADDR_ANY and corrected Endpoint.send/RemoteProc/new_service_callback signatures from extmod openamp sources |
| reference\micropython\os\__init__.pyi | done |  | No API changes needed after review against extmod/modos.c and docs |
| reference\micropython\platform\__init__.pyi | done |  | No API changes needed after review against extmod/modplatform.c |
| reference\micropython\pyb\__init__.pyi | done |  | Fixed top-level signature drift: removed leaked Timer/CAN overloads, added deprecated country alias, corrected unique_id bytes and setter arg types |
| reference\micropython\pyb\Accel.pyi | done |  | Added source-exposed read/write methods and tightened filtered_xyz tuple typing from stm32 accel.c |
| reference\micropython\pyb\ADC.pyi | done |  | Corrected read_timed return type to int (bytes written) per ports/stm32/adc.c |
| reference\micropython\pyb\CAN.pyi | done |  | Added CAN-FD init/send/clearfilter kwargs; corrected recv return shape and callback/send buffer typing |
| reference\micropython\pyb\DAC.pyi | done |  | Typed DAC mode constants as int and corrected write_timed input buffer to readable |
| reference\micropython\pyb\ExtInt.pyi | done | 71724f2ea | Added EVT_* constants and typed IRQ/EVT constants as int; callback allows None per extint.c constructor parsing |
| reference\micropython\pyb\Flash.pyi | done | 30d4fd8b6 | Aligned readblocks/writeblocks to int status returns and generalized buffer mutability per storage.c |
| reference\micropython\pyb\I2C.pyi | done | 008455d7d | Fixed constructor/init signatures, send parameter, mem_write buffer direction, and scan typing per pyb_i2c.c |
| reference\micropython\pyb\LCD.pyi | done |  | No stub changes needed after review against ports/stm32/lcd.c locals dict and method signatures |
| reference\micropython\pyb\LED.pyi | done |  | No stub changes needed after review against ports/stm32/led.c API (on/off/toggle/intensity) |
| reference\micropython\pyb\Pin.pyi | done |  | Added missing Pin IRQ/on-off helpers and IRQ/OUT/OPEN_DRAIN constants; corrected names() to list[str] per ports/stm32/pin.c. |
| reference\micropython\pyb\RTC.pyi | done |  | Restored missing method bodies, added init(), precise datetime tuple typing, and wakeup overloads for (None|ms|wucksel,wut) per ports/stm32/rtc.c. |
| reference\micropython\pyb\Servo.pyi | done |  | Replaced duplicate/incomplete overload set; aligned angle/speed/pulse_width/calibration signatures to ports/stm32/servo.c argument counts and returns. |
| reference\micropython\pyb\SPI.pyi | done |  | Added MASTER/SLAVE constants, dir/nss kwargs, and buffer-aware recv/send_recv overload returns; corrected send parameter to readable buffer per ports/stm32/pyb_spi.c. |
| reference\micropython\pyb\Switch.pyi | done |  | Completed constructor stub body; API otherwise already matched ports/stm32/usrsw.c (call/value/callback). |
| reference\micropython\pyb\Timer.pyi | done |  | Typed BRK_OFF/BRK_LOW/BRK_HIGH constants as int per ports/stm32/timer.c ROM_INT exports |
| reference\micropython\pyb\UART.pyi | done |  | Aligned RTS/CTS constant types and stream signatures (readline/write, write buffer direction) with extmod/machine_uart.c + ports/stm32/machine_uart.c |
| reference\micropython\pyb\USB_HID.pyi | done |  | Corrected USB_HID.send return type to int bytes-sent per ports/stm32/usb.c |
| reference\micropython\pyb\USB_VCP.pyi | done |  | Typed RTS/CTS/IRQ_RX as int and aligned readline/recv/send signatures to ports/stm32/usb.c stream + VCP APIs |
| reference\micropython\random\__init__.pyi | done |  | Corrected random/uniform return types and generic choice return |
| reference\micropython\rp2\__init__.pyi | done |  | Added optional deprecated country() alias overloads from ports/rp2/modrp2.c (exports mod_network_country_obj when CYW43 enabled) |
| reference\micropython\rp2\asm_pio.pyi | done | a1e543cf4 | Aligned pull/mov helper signatures to ports/rp2/modules/rp2.py (`pull(value,value2)`, `mov(dest,src)`) |
| reference\micropython\rp2\DMA.pyi | done | 4d801f0fb | Added register attrs, made unpack_ctrl static, and aligned constructor/config kwargs to ports/rp2/rp2_dma.c |
| reference\micropython\rp2\Flash.pyi | done | 12edf5eec | Aligned constructor kwargs and block API buffer/return typing to ports/rp2/rp2_flash.c |
| reference\micropython\rp2\PIO.pyi | done | 2fe8e9cf6 | Added gpio_base API, made state_machine program optional, and set irq trigger default to 0xF00 per rp2_pio.c |
| reference\micropython\rp2\PIOASMEmit.pyi | done | 3d1b9e308 | Added side_pindir kwarg and aligned pull/mov signatures to ports/rp2/modules/rp2.py PIOASMEmit methods |
| reference\micropython\rp2\StateMachine.pyi | done | e2f2104a8 | Corrected constructor/init defaults, active() return typing, and get/put buffer signatures per ports/rp2/rp2_pio.c |
| reference\micropython\select\__init__.pyi | done | bd35e1cd4 | Corrected select() tuple return type and poll.unregister() return to None per extmod/modselect.c |
| reference\micropython\socket\__init__.pyi | done | 2cc9c252d | Corrected socket.sendto() return type to int per extmod/modsocket.c |
| reference\micropython\ssl\__init__.pyi | done |  | No stub changes needed after review across extmod/modtls_mbedtls.c, extmod/modtls_axtls.c, and ports/cc3200/modssl.c exports |
| reference\micropython\stm\__init__.pyi | done |  | No API changes needed after review against ports/stm32/modstm.c (mem objects + conditional rfcore/subghz APIs) |
| reference\micropython\struct\__init__.pyi | done |  | No API changes needed after review against py/modstruct.c |
| reference\micropython\sys\__init__.pyi | done |  | No stub changes needed after review against py/modsys.c exports and signatures |
| reference\micropython\time\__init__.pyi | done |  | No stub changes needed after review against extmod/modtime.c exports and signatures |
| reference\micropython\tls\__init__.pyi | done | 7f5ac49b2 | Normalized backend-dependent TLS constants from extmod/modtls_mbedtls.c and modtls_axtls.c |
| reference\micropython\uctypes\__init__.pyi | done | f36c03082 | Corrected integer constant types and added exported BF* constants per extmod/moductypes.c |
| reference\micropython\vfs\__init__.pyi | done |  | Added optional VfsRom/rom_ioctl exports and set umount() return to None from extmod/modvfs.c + extmod/vfs.c |
| reference\micropython\wipy\__init__.pyi | done |  | No stub changes needed; heartbeat([enable]) overload matches ports/cc3200/modwipy.c behavior (bool getter, None setter). |
| reference\micropython\wm8960\__init__.pyi | done |  | Aligned __init__ default sample_rate, volume getter/setter returns, mute(enable,...) signature, and helper method None returns to wm8960.py. |
| reference\micropython\zephyr\__init__.pyi | done |  | Typed API from ports/zephyr/modzephyr.c: is_preempt_thread->bool, current_tid->int, thread_analyze(cpu)->None, shell_exec(str)->None. |
| reference\micropython\zephyr\DiskAccess.pyi | pending |  |  |
| reference\micropython\zephyr\FlashArea.pyi | pending |  |  |
| reference\micropython\zephyr\zsensor.pyi | pending |  |  |
| reference\micropython\zlib\__init__.pyi | done |  | Corrected compress/decompress signatures to micropython-lib zlib.py |
