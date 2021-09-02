import time
import zmq

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting date and time from publisher...")
socket.connect("tcp://localhost:5561")
socket.setsockopt_string(zmq.SUBSCRIBE, "time")


while True:
    string = socket.recv_string()
    print("Current published %s" % string)
    time.sleep(0.5)