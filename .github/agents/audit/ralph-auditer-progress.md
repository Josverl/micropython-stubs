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
| reference\micropython\machine\I2C.pyi |pending |  |  |
| reference\micropython\machine\I2S.pyi |pending |  |  |
| reference\micropython\machine\Pin.pyi |pending |  |  |
| reference\micropython\machine\PWM.pyi |pending |  |  |
| reference\micropython\machine\RTC.pyi |pending |  |  |
| reference\micropython\machine\SD.pyi |pending |  |  |
| reference\micropython\machine\SDCard.pyi |pending |  |  |
| reference\micropython\machine\Signal.pyi |pending |  |  |
| reference\micropython\machine\SPI.pyi |pending |  |  |
| reference\micropython\machine\Timer.pyi |pending |  |  |
| reference\micropython\machine\TimerWiPy.pyi |pending |  |  |
| reference\micropython\machine\UART.pyi |pending |  |  |
| reference\micropython\machine\USBDevice.pyi |pending |  |  |
| reference\micropython\machine\WDT.pyi |pending |  |  |
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
| reference\micropython\pyb\CAN.pyi | pending |  |  |
| reference\micropython\pyb\DAC.pyi | pending |  |  |
| reference\micropython\pyb\ExtInt.pyi | pending |  |  |
| reference\micropython\pyb\Flash.pyi | pending |  |  |
| reference\micropython\pyb\I2C.pyi | pending |  |  |
| reference\micropython\pyb\LCD.pyi | pending |  |  |
| reference\micropython\pyb\LED.pyi | pending |  |  |
| reference\micropython\pyb\Pin.pyi | pending |  |  |
| reference\micropython\pyb\RTC.pyi | pending |  |  |
| reference\micropython\pyb\Servo.pyi | pending |  |  |
| reference\micropython\pyb\SPI.pyi | pending |  |  |
| reference\micropython\pyb\Switch.pyi | pending |  |  |
| reference\micropython\pyb\Timer.pyi | pending |  |  |
| reference\micropython\pyb\UART.pyi | pending |  |  |
| reference\micropython\pyb\USB_HID.pyi | pending |  |  |
| reference\micropython\pyb\USB_VCP.pyi | pending |  |  |
| reference\micropython\random\__init__.pyi | done |  | Corrected random/uniform return types and generic choice return |
| reference\micropython\rp2\__init__.pyi | pending |  |  |
| reference\micropython\rp2\asm_pio.pyi | pending |  |  |
| reference\micropython\rp2\DMA.pyi | pending |  |  |
| reference\micropython\rp2\Flash.pyi | pending |  |  |
| reference\micropython\rp2\PIO.pyi | pending |  |  |
| reference\micropython\rp2\PIOASMEmit.pyi | pending |  |  |
| reference\micropython\rp2\StateMachine.pyi | pending |  |  |
| reference\micropython\select\__init__.pyi | pending |  |  |
| reference\micropython\socket\__init__.pyi | pending |  |  |
| reference\micropython\ssl\__init__.pyi | pending |  |  |
| reference\micropython\stm\__init__.pyi | pending |  |  |
| reference\micropython\struct\__init__.pyi | done |  | No API changes needed after review against py/modstruct.c |
| reference\micropython\sys\__init__.pyi | pending |  |  |
| reference\micropython\time\__init__.pyi | pending |  |  |
| reference\micropython\tls\__init__.pyi | pending |  |  |
| reference\micropython\uctypes\__init__.pyi | pending |  |  |
| reference\micropython\vfs\__init__.pyi | pending |  |  |
| reference\micropython\wipy\__init__.pyi | pending |  |  |
| reference\micropython\wm8960\__init__.pyi | pending |  |  |
| reference\micropython\zephyr\__init__.pyi | pending |  |  |
| reference\micropython\zephyr\DiskAccess.pyi | pending |  |  |
| reference\micropython\zephyr\FlashArea.pyi | pending |  |  |
| reference\micropython\zephyr\zsensor.pyi | pending |  |  |
| reference\micropython\zlib\__init__.pyi | done |  | Corrected compress/decompress signatures to micropython-lib zlib.py |
