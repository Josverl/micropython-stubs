from _typeshed import Incomplete

_MIN_ADDRESS: int
_TMP_ADDRESS: int
_MAX_ADDRESS: Incomplete
_CMD_HDR_LEN: int
_CMD_CRC_LEN: int
_CMD_DIR_SET: int
_CMD_DIR_GET: int
_CMD_CHIP_RESET: Incomplete
_CMD_SET_ADDRESS: Incomplete
_CMD_GET_ADDRESS: Incomplete
_CMD_GET_PRODUCT_ID: Incomplete
_CMD_GET_FW_VERSION: Incomplete
_CMD_SET_BOOTLOADER: Incomplete
_CMD_SET_FLASH_WRITE: Incomplete
_CMD_GET_FLASH_READ: Incomplete
_CMD_SET_DIGITAL_PIN: Incomplete
_CMD_GET_DIGITAL_BUS: Incomplete
_CMD_SET_DIGITAL_DEF: Incomplete
_CMD_SET_DIGITAL_BUS_OA: Incomplete
_CMD_CFG_ANALOG_ADC: Incomplete
_CMD_CFG_ANALOG_DIN: Incomplete
_CMD_CFG_ANALOG_PWM: Incomplete
_CMD_CFG_ANALOG_DAC: Incomplete
_CMD_CFG_ANALOG_RTD: Incomplete
_CMD_CFG_ANALOG_HIZ: Incomplete
_CMD_SET_ANALOG_DAC: Incomplete
_CMD_SET_ANALOG_RTD_TIM: Incomplete
_CMD_GET_ANALOG_PIN: Incomplete
_CMD_GET_ANALOG_PIN_ALL: Incomplete
_CMD_GET_ANALOG_ADC: Incomplete
_CMD_GET_ANALOG_ADC_ALL: Incomplete
_CMD_GET_ANALOG_RTD: Incomplete
_CMD_GET_ANALOG_DIN: Incomplete
_CMD_SET_ANALOG_PWM_DEF: Incomplete
_CMD_SET_ANALOG_DAC_DEF: Incomplete
_CMD_SET_ANALOG_TIMEOUT: Incomplete
_CHANNEL_MODES: Incomplete
_CHANNEL_TYPES: Incomplete

class Expansion:
    opta: Incomplete
    type: Incomplete
    addr: Incomplete
    name: Incomplete
    channels: Incomplete
    def __init__(self, opta, type, addr, name) -> None: ...
    def product_id(self):
        """
        Returns the product ID bytes of the expansion.
        """

    def firmware_version(self):
        """
        Returns the firmware version of the expansion.
        """

    def _flash(self, address, size: int = 0, data: Incomplete | None = None):
        """
        Reads from or writes to the flash memory at the specified address.

        NOTE: This should be used for production purposes only!

        Parameters:
            - address : The memory address to read from or write to.
            - size : Number of bytes to read from the flash memory.
            - data : Bytes to write to the flash memory.

        Returns:
            Data read from the flash memory as bytes, if reading. Returns None if writing.
        """

    def digital(self, pins: Incomplete | None = None, timeout: Incomplete | None = None, default: int = 0):
        """
        Reads or writes digital pins.

        Parameters:
            - pins : Digital pins mask to set. If None, returns the state of all pins.
            - timeout : The timeout in milliseconds, after which pins revert to the default state.
            - default : The default state to which the pins will revert to after the timeout expires.

        Note:
            - For Opta Analog, this functions supports writing digital LEDs only.

        Returns: The current state of the digital pins if reading, or None if setting the pins.
        """

    def analog(
        self,
        channel: Incomplete | None = None,
        channel_type: Incomplete | None = None,
        channel_mode: Incomplete | None = None,
        timeout: Incomplete | None = None,
        **kwargs,
    ):
        """
        Configures or reads analog channels.

        Parameters:
            - timeout : Set timeout in milliseconds after which analog channels revert to their default
                        states set previously with analog(). Note if this is set, all other args are ignored.
            - channel : The channel number to configure, read, or write. If None, reads all ADC channels.
            - channel_type : Channel type can be "adc", "dac", "pwm", "rtd", "hiz", "din".
            - channel_mode : "voltage" or "current" (default="voltage" for ADC channels).

        kwargs :
            hiz configuration:
            - no args.

            adc configuration:
            - average : Number of points for moving average (0-255, default=0).
            - rejection : Enable rejection (default=False).
            - diagnostic : Enable diagnostic (default=False).
            - pulldown : Enable pulldown (default=True for voltage, False for current).
            - secondary : This ADC channel is shared with another function (default=False).

            dac configuration:
            - use_slew : Enable slew rate control (default=False).
            - slew_rate : Slew rate if `use_slew` is True (default=0).
            - limit_current : Limit current (default=False).
            - value : Value to write to a DAC channel.
            - default_value: The default value to revert to, after the timeout set with timeout() expires.

            pwm configuration:
            - period: PWM period in uS (for example 1000uS).
            - duty:  high duty cycle in % (for example 50%).
            - default_period: The default value to revert to, after the timeout set with timeout() expires.
            - default_duty: The default value to revert to, after the timeout set with timeout() expires.

            rtd configuration:
            - use_3_wire: 3-Wire RTD (default = False).
            - current_ma: RTD current in mA (default = 1.2mA).
            - update_time: The update time of all RDT channels.

            din (digital input) configuration:
            - comparator : Enable comparator (default=True).
            - filtered : Select the filtered input to the comparator (default=True).
            - inverted : Invert the output from the digital input comparator (default=False).
            - scale : Comparator voltage scale (default=False).
            - threshold : Comparator voltage threshold (default 9).
            - sink : Sets the sink current in digital input logic mode (0-31, default 1)
            - debounce_mode : Debounce mode ("simple", "integrator" or None to disable debounce, default="simple")
            - debounce_time : Debounce time (0-31, default 24)

        Returns: ADC value(s) if reading, or None if configuring a channel or setting the analog timeout.
        """

class Opta:
    bus: Incomplete
    cmd_buf: Incomplete
    det: Incomplete
    exp_types: Incomplete
    def __init__(self, bus_id, freq: int = 400000, det: Incomplete | None = None) -> None:
        """
        Initializes an Opta controller.

        Parameters:
            - bus_id : The I2C bus identifier.
            - freq : I2C bus frequency (default=400_000).
            - det : GPIO pin used for bus detection (default is a PULL_UP input pin named "BUS_DETECT").
        """

    def _log_debug(self, msg) -> None: ...
    def _log_enabled(self, level): ...
    def _bus_read(self, addr, buf) -> None: ...
    def _bus_write(self, addr, buf) -> None: ...
    def _crc8(self, buf, poly: int = 7, crc: int = 0): ...
    def _cmd(self, addr, cmd, fmt: Incomplete | None = None, *args): ...
    def _reset_bus(self, addr) -> None: ...
    def _set_address(self, addr, addr_new: Incomplete | None = None): ...
    def enum_devices(self):
        """
        Initializes the bus, resets all expansions, and returns a list of detected expansions.
        Returns: A list of detected expansions on the bus.
        """
