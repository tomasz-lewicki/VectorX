SHAPE = (1080, 1920, 1)
N_BUF = int(1e5)

import time
import numpy as np
from multiprocessing import shared_memory

img_sha = np.ones(SHAPE, dtype=np.uint8)
shm = shared_memory.SharedMemory(name="image_buffer", create=True, size=img_sha.nbytes)
img_sha = np.ndarray(SHAPE, dtype=np.uint8, buffer=shm.buf)

start = time.perf_counter()

for _ in range(N_BUF):
    img_sha = np.ones(SHAPE, dtype=np.uint8)

howlong = time.perf_counter() - start
print(f"{N_BUF/howlong:0.2f} buffers/s")

shm.close()
shm.unlink()
