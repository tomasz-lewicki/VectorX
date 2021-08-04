import zmq
import numpy as np
from vectorx import send_array

PORT = "5556"
SHAPE = (1080, 1920)

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind(f"tcp://*:{PORT}")

while True:
    arr = np.zeros(SHAPE, dtype=np.uint8)
    send_array(socket, arr)
