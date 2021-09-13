#
#   Vehicle speed
#   Binds PUB socket to tcp://*:5560
#   Publishes Nevera vehicle speed 
#

import zmq
import csv
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5560")

# open file for reading
with open('vehicle_speed.csv') as csvDataFile:
    # read file as csv file 
    csvReader = csv.reader(csvDataFile)
    # for every row, print the row
    
    reduce_factor = 10 # 5ms between reading
    reduced_data = []
    i = 0
    for row in csvReader:
        if i % reduce_factor == 0:
            reduced_data.append(row)    
        i = i + 1 


while True:
    for vehicle_speed in reduced_data:   
        socket.send_string(f"speed:{vehicle_speed[1]}")
        time.sleep(45 / 1000.0)
        



    
    


