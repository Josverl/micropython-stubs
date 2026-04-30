# Micropython v1.28.0
from esp32 import Partition

# esp32: bdev is discovered via Partition.find(...).
# Note: esp8266 uses a different FlashBdev implementation.
bdev: Partition | None
