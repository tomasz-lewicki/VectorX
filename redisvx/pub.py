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
