from transitions import Machine

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
