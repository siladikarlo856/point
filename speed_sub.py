#
#   Weather update client
#   Connects SUB socket to tcp://localhost:5556
#   Collects weather updates and finds avg temp in zipcode
#

import sys
import zmq


#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from vehicle speed server...")
socket.connect("tcp://localhost:5560")

# Subscribe to all
socket.setsockopt_string(zmq.SUBSCRIBE, "speed:")

while True:
    string = socket.recv_string()
    #print(string)
    sys.stdout.write("%s   \r" % (string) )
    sys.stdout.flush()