SHAPE = (1080, 1920)

import numpy as np
from multiprocessing import shared_memory

img_sha = np.ones(SHAPE, dtype=np.uint8)
shm = shared_memory.SharedMemory(name="image_buffer", create=True, size=img_sha.nbytes)
img_sha = np.ndarray(SHAPE, dtype=np.uint8, buffer=shm.buf)

for i in range(int(1e4)):
    img_sha = np.ones(SHAPE, dtype=np.uint8)

shm.close()
shm.unlink()
