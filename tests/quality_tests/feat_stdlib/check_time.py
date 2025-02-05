import time

# ref : https://github.com/Josverl/micropython-stubs/issues/771

local_time = (2024, 12, 29, 17, 33, 32, 6, 364)
seconds = time.mktime(local_time)  # stubs-ignore:  version < 1.24.0
