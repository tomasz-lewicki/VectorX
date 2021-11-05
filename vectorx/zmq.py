import zmq
import numpy as np

class ZmqPub:
    def __init__():
        self._ctx = zmq.Context()
        self._socket = context.socket(zmq.PUSH)
        self._socket.bind(f"tcp://*:{port}")

    def _send_array(socket, A, flags=0, copy=True, track=False):
        """send a numpy array with metadata"""
        metadata = dict(
            dtype=str(A.dtype),
            shape=A.shape,
        )
        self._socket.send_json(metadata, flags | zmq.SNDMORE)
        self._socket.send(A, flags, copy=copy, track=track)

class ZmqSub:
    def __init__(port):
        context = zmq.Context()
        socket = context.socket(zmq.PULL)
        socket.connect(f"tcp://localhost:{port}")

    def _recv_array(socket, flags=0, copy=True, track=False):
        """recv a numpy array"""
        metadata = self._socket.recv_json(flags=flags)
        msg = self._socket.recv(flags=flags, copy=copy, track=track)
        buf = memoryview(msg)
        A = np.frombuffer(buf, dtype=metadata["dtype"])
        return A.reshape(metadata["shape"])


sub = ZmqSub("5556")

while True:
    arr = np.ones(SHAPE, dtype=np.uint8)
    send_array(socket, arr)

import zmq

# Socket to talk to server


cnt = 0

for i in range(int(1e4)):
    cnt += 1
    print(cnt)
    arr = recv_array(socket)
