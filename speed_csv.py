import csv
import sys
import time

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
    
    for vehicle_speed in reduced_data:   
        sys.stdout.write("Speed:%s   \r" % (vehicle_speed[1]) )
        sys.stdout.flush()
        time.sleep(45 / 1000.0)


