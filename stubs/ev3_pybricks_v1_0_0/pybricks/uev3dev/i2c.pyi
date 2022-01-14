from typing import Any

class SMBus:
    def _access(self, *argv) -> Any: ...
    _slave: int
    def block_process_call(self, *argv) -> Any: ...
    def process_call(self, *argv) -> Any: ...
    def read_block_data(self, *argv) -> Any: ...
    def read_byte(self, *argv) -> Any: ...
    def read_byte_data(self, *argv) -> Any: ...
    def read_i2c_block_data(self, *argv) -> Any: ...
    def read_word_data(self, *argv) -> Any: ...
    def set_address(self, *argv) -> Any: ...
    def write_block_data(self, *argv) -> Any: ...
    def write_byte(self, *argv) -> Any: ...
    def write_byte_data(self, *argv) -> Any: ...
    def write_i2c_block_data(self, *argv) -> Any: ...
    def write_quick(self, *argv) -> Any: ...
    def write_word_data(self, *argv) -> Any: ...

_I2C_FUNCS: int
_I2C_FUNC_10BIT_ADDR: int
_I2C_FUNC_I2C: int
_I2C_FUNC_NOSTART: int
_I2C_FUNC_PROTOCOL_MANGLING: int
_I2C_FUNC_SLAVE: int
_I2C_FUNC_SMBUS_BLOCK_PROC_CALL: int
_I2C_FUNC_SMBUS_PEC: int
_I2C_FUNC_SMBUS_PROC_CALL: int
_I2C_FUNC_SMBUS_QUICK: int
_I2C_FUNC_SMBUS_READ_BLOCK_DATA: int
_I2C_FUNC_SMBUS_READ_BYTE: int
_I2C_FUNC_SMBUS_READ_BYTE_DATA: int
_I2C_FUNC_SMBUS_READ_I2C_BLOCK: int
_I2C_FUNC_SMBUS_READ_WORD_DATA: int
_I2C_FUNC_SMBUS_WRITE_BLOCK_DATA: int
_I2C_FUNC_SMBUS_WRITE_BYTE: int
_I2C_FUNC_SMBUS_WRITE_BYTE_DATA: int
_I2C_FUNC_SMBUS_WRITE_I2C_BLOCK: int
_I2C_FUNC_SMBUS_WRITE_WORD_DATA: int
_I2C_M_IGNORE_NAK: int
_I2C_M_NOSTART: int
_I2C_M_NO_RD_ACK: int
_I2C_M_RD: int
_I2C_M_RECV_LEN: int
_I2C_M_REV_DIR_ADDR: int
_I2C_M_STOP: int
_I2C_M_TEN: int
_I2C_PEC: int
_I2C_RDWR: int
_I2C_RETRIES: int
_I2C_SLAVE: int
_I2C_SLAVE_FORCE: int
_I2C_SMBUS: int
_I2C_SMBUS_BLOCK_DATA: int
_I2C_SMBUS_BLOCK_MAX: int
_I2C_SMBUS_BLOCK_PROC_CALL: int
_I2C_SMBUS_BYTE: int
_I2C_SMBUS_BYTE_DATA: int
_I2C_SMBUS_I2C_BLOCK_BROKEN: int
_I2C_SMBUS_I2C_BLOCK_DATA: int
_I2C_SMBUS_PROC_CALL: int
_I2C_SMBUS_QUICK: int
_I2C_SMBUS_READ: int
_I2C_SMBUS_WORD_DATA: int
_I2C_SMBUS_WRITE: int
_I2C_TENBIT: int
_I2C_TIMEOUT: int
_i2c_smbus_data: Any
_i2c_smbus_ioctl_data: Any
_size_of_i2c_smbus_data: int
_size_of_i2c_smbus_ioctl_data: int

def ioctl() -> None: ...

uctypes: Any
