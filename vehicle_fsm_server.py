import zmq
from transitions import Machine
import signal

class Vehicle(object):
    pass

car = Vehicle()

states = ['off', 'ignition', 'on', 'P', 'R', 'N', 'D']
transitions = [
    {'trigger': 'key_inserted', 'source': 'off', 'dest': 'ignition'},
    {'trigger': 'key_removed', 'source': 'ignition', 'dest': 'off'},
    {'trigger': 'start', 'source': 'ignition', 'dest': 'P'},
    {'trigger': 'stop', 'source': 'P', 'dest': 'off'},
    {'trigger': 'reverse', 'source': 'P', 'dest': 'R'},
    {'trigger': 'park', 'source': 'R', 'dest': 'P'},
    {'trigger': 'neutral', 'source': 'R', 'dest': 'N'},
    {'trigger': 'reverse', 'source': 'N', 'dest': 'R'},
    {'trigger': 'drive', 'source': 'N', 'dest': 'D'},
    {'trigger': 'neutral', 'source': 'D', 'dest': 'N'}
]

state_machine = Machine(model=car, states=states, transitions=transitions, initial='off')


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5570")

while True:
    #  Wait for next request from client
    message = socket.recv_string()
    print("Received request: %s" % message)
    if message != 'get_state':
        try:
            car.trigger(message)
        except:
            print("FSM can not handle trigger: %r. Sending current state." % (message))
    #  Send reply back to client
    print("Current car state: %r" % (car.state))
    socket.send_string(car.state)
