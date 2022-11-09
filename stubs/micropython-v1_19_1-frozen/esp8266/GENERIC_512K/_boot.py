# Micropython 1.19.1 frozen stubs
import gc

gc.threshold((gc.mem_free() + gc.mem_alloc()) // 4)
