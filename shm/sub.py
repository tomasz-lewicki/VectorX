import numpy as np
from multiprocessing import shared_memory

existing_shm = shared_memory.SharedMemory(name="image_buffer")

SHAPE = (1080, 1920)

c = np.ndarray(SHAPE, dtype=np.uint8, buffer=existing_shm.buf)

cnt = 0
while True:
    cnt += 1
    print(f"{cnt} {np.sum(c[:,0])}")

existing_shm.close()
