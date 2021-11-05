import time 
import multiprocessing as mp 
import numpy as np
from vectorx.shm import SharedArrayPub, SharedArraySub

class MockCamera:
    def read(self):
        return np.ones((224,224,3), dtype=np.uint8)

def publish(n_iter):

    cam = MockCamera()
    
    pub_arr = SharedArrayPub(
        shape=(224,224,3),
        dtype=np.uint8,
        topic_name='test_rgb_camera'
        )

    for i in range(n_iter):
        print(f"write {i}")
        pub_arr = cam.read()

def subscribe(n_iter, should_run):

    cam = MockCamera()
    
    sub_arr = SharedArraySub(
        shape=(224,224,3),
        dtype=np.uint8,
        topic_name='test_rgb_camera'
        )

    i = 0
    while should_run.is_set():
        i+=1
        print(f"read {i}")
        s = np.sum(sub_arr)

N_ITER = int(1e5)

if __name__ == '__main__':

    pub_process = mp.Process(target=publish, args=[N_ITER])
    
    sub_should_run = mp.Event()
    sub_should_run.set()
    sub_process = mp.Process(target=subscribe, args=[N_ITER, sub_should_run])
    
    start = time.perf_counter()
    
    # start processes
    pub_process.start()
    sub_process.start()

    pub_process.join() # pub exits first
    sub_should_run.clear() # tell sub to exit
    sub_process.join() # wait for sub
    elapsed_t = time.perf_counter() - start

    print(f"{N_ITER/elapsed_t} FPS")

    




