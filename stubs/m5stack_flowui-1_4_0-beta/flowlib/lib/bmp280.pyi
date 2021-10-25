from typing import Any

class BMP280:
    def compute_delay_time() -> None: ...
    def read_compensated_data() -> None: ...
    def read_raw_data() -> None: ...
    values: Any

BMP280_I2CADDR: int
BMP280_OSAMPLE_1: int
BMP280_OSAMPLE_16: int
BMP280_OSAMPLE_2: int
BMP280_OSAMPLE_4: int
BMP280_OSAMPLE_8: int
BMP280_POWER_MODE_FORCED: int
BMP280_POWER_MODE_NORMAL: int
BMP280_POWER_MODE_SLEEP: int
BMP280_REGISTER_CONFIG: int
BMP280_REGISTER_CONTROL: int
BMP280_REGISTER_ID: int
BMP280_REGISTER_RESET: int
BMP280_REGISTER_STATUS: int
T_INIT_MAX: int
T_MEASURE_PER_OSRS_MAX: int
T_SETUP_PRESSURE_MAX: int

class array:
    def append() -> None: ...
    def decode() -> None: ...
    def extend() -> None: ...

time: Any

def unpack() -> None: ...
def unpack_from() -> None: ...
