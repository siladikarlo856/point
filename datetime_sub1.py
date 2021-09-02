import zmq

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting date and time from publisher...")
socket.connect("tcp://192.168.50.136:5561")
socket.setsockopt_string(zmq.SUBSCRIBE, "")


while True:
    string = socket.recv_string()
    print("Current published %s" % string)
