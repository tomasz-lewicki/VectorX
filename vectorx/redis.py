"""
This file read the camera and save images into Redis
"""
import redis, struct
import numpy as np


def imToRedis(r, a, n):
    """Store given Numpy array 'a' in Redis under key 'n'"""
    h, w = a.shape[:2]
    shape = struct.pack(">II", h, w)
    encoded = shape + a.tobytes()

    # Store encoded data in Redis
    r.set(n, encoded)


RedisPool = redis.Redis(host="localhost", port=6379, db=0)

while True:
    img = np.zeros((1920, 1080), dtype=np.uint8)
    imToRedis(RedisPool, img, "img")
    print(img.shape)
    flagProcessed = RedisPool.set("flagProcessed", 0)



## sub

import cv2
import redis, struct
import numpy as np


def imFromRedis(r, n):
    """Read image from redis"""
    encoded = r.get(n)
    h, w = struct.unpack(">II", encoded[:8])
    data = np.frombuffer(encoded, dtype=np.uint8, offset=8).reshape(h, w)

    return data


RedisPool = redis.Redis(host="localhost", port=6379, db=0)

cnt = 0
while cnt < 1e3:
    flagProcessed = int(RedisPool.get("flagProcessed"))
    if not flagProcessed:
        cnt += 1
        print(cnt)
        img = imFromRedis(RedisPool, "img")
        RedisPool.set("flagProcessed", 1)
