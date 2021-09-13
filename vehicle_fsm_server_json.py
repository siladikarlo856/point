import zmq
from transitions import Machine
import json

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
    message = socket.recv_json()
    print("Received request: %s" % message)
    client_id = message['id']
    client_request = message['request']
    print("Request received from: %s" % (client_id) )
    if client_request != 'get_state':
        try:
            car.trigger(client_request)
        except:
            print("FSM can not handle trigger: %r. Sending current state." % (client_request))
    #  Send reply back to client
    print("Current car state: %r" % (car.state))
    socket.send_string(car.state)
