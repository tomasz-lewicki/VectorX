
ZMQ: 10000/6.124=1633 buf/s
```shell
time (python3 zmq/pub.py & python3 zmq/sub.py)
5.11s user 5.48s system 172% cpu 6.124 total
```


SHM: 10000/1.018= 10k buf/s (!)
```shell
time (python3 shm/pub.py python3 shm/sub.py)
( python3 shm/pub.py python3 shm/sub.py; )  2.11s user 1.28s system 333% cpu 1.018 total
```