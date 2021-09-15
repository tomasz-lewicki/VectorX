import time
import numpy as np
from multiprocessing import shared_memory

N_BUF = int(1e5)
existing_shm = None

while existing_shm is None:
    try:
        existing_shm = shared_memory.SharedMemory(name="image_buffer")
    except FileNotFoundError:
        time.sleep(0.1)
        print("Waiting for publisher to create shm|", end="\r")
        time.sleep(0.1)
        print("Waiting for publisher to create shm/", end="\r")
        time.sleep(0.1)
        print("Waiting for publisher to create shm-", end="\r", flush=True)

SHAPE = (1080, 1920, 1)

c = np.ndarray(SHAPE, dtype=np.uint8, buffer=existing_shm.buf)

cnt = 0
try:
    while True:
        cnt += 1
        print(f"{cnt} {np.sum(c[:,0])}")
finally:
    existing_shm.close()
