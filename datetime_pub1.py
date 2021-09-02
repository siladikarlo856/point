#
#   Date time publisher
#   Binds PUB socket to tcp://*:5561
#   Publishes date and time
#

import zmq
import time
import datetime

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5561")


while True:
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    socket.send_string(dt_string)
    time.sleep(1)
        
