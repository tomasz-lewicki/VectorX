import numpy as np
from multiprocessing import shared_memory

class SharedArrayPub:

    def __init__(self, shape, dtype, topic_name):

        # Figure out the size of shm to allocate
        el_cnt = np.prod(shape)
        el_size = dtype().itemsize
        nbytes = el_cnt * el_size

        # Allocate shared memory
        self._shm = shared_memory.SharedMemory(
            name=topic_name,
            create=True, 
            size=nbytes
            )

        self._arr = np.ndarray(shape, dtype, buffer=self._shm.buf)

    def __getitem__(self, key):
        return self._arr[key]

    def __setitem__(self, key, value):
        self._arr[key] = value

    def __del__(self):
        self._shm.close()
        self._shm.unlink()


class SharedArraySub:

    def __init__(self, shape, dtype, topic_name):

        self._shm = self.get_shm_by_name(topic_name)

        self._arr = np.ndarray(
            shape,
            dtype=np.uint8,
            buffer=self._shm.buf)

    def __getitem__(self, key):
        return self._arr[key]

    @staticmethod
    def get_shm_by_name(topic_name):
        try:
            shm = shared_memory.SharedMemory(
                name=topic_name,
                create=False
                )
        except FileNotFoundError:
            raise("Topic Name not Found")
        
        return shm
    
    def __del__(self):
        self._shm.close()