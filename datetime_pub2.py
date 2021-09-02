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
    date_string = now.strftime("%d/%m/%Y")
    time_string = now.strftime("%H:%M:%S")
    socket.send_string("datetime: %s" % (dt_string))
    socket.send_string("date:%s" % (date_string))
    socket.send_string("time:%s" % (time_string))
    time.sleep(1)
        
