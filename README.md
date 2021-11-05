# VectorX

_(Vector eXchange)_ - IPC library to exchange vectors.

## 

| method |     | atomic R/W? | topic identifier |
| ------ | --- | ----------- | ---------------- |
| shm    |     | no          |                  |
| redis  |     | yes         | `/shm` file name |
| ZMQ    |     | yes         |                  |


## Benchmarks 
The goal is to exchange `100 000` count of `1080x1920` `uint8` arrays (i.e. 1080p grayscale frame) in the shortest time possible.
Atomicity is nice to have, but not required.
Subscriber must be able to perform meaningful operation on the image (here `np.sum()`).
Dirty or "unsafe" tricks are permitted (and welcome).



| method | Intel Xeon | Apple M1 | Jetson Nano | atomic R/W? | topic identifier |
| ------ | ---------- | -------- | ----------- | ----------- | ---------------- |
| shm    | 12075 FPS  |          |             | no          | `/shm` file name |
| redis  |            |          |             | yes         | port number      |
| ZMQ    |            |          |             | yes         | port number      |

## Test SHM

```shell
python3 shm/sub.py
python3 shm/pub.py # In a different window 
```




