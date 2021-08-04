from vectorx import recv_array
import zmq


PORT = "5556"

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect(f"tcp://localhost:{PORT}")

cnt = 0

for i in range(int(1e3)):
    cnt += 1
    print(cnt)
    arr = recv_array(socket)
