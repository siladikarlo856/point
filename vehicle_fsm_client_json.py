import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to vehicle_fsm_server server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5570")

socket.send_json({"id":"karlo","request":"key_inserted"})
print(socket.recv())