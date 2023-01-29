import numpy as np


with open('day15.txt', 'r') as file:
    sensors_beacons = file.read().split('\n')[:-1]


beacons = set()
sensors = {}


for i, sensor_beacon in enumerate(sensors_beacons):
    sensor, beacon = sensor_beacon.split(': ')
    sensor = sensor.split(', ')
    sensor_x, sensor_y = int(sensor[0].split('=')[-1]), int(sensor[1].split('=')[-1])
    beacon = beacon.split(', ')
    beacon_x, beacon_y = int(beacon[0].split('=')[-1]), int(beacon[1].split('=')[-1])
    # keep beacons in a set
    beacons.add((beacon_x, beacon_y))
    # Store sensors in dict with manhattan distances
    sensors[(sensor_x, sensor_y)] = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)


# Remove overlap and grab intervals
def interval_union(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    unions = [intervals.pop(0)]
    while intervals:
        # if next interval is in current union, extend union
        # otherwise close union and move on.
        if unions[-1][1] >= intervals[0][0]:
            if intervals[0][1] >= unions[-1][1]:
                unions[-1][1] = intervals[0][1]
            intervals.pop(0)
        else:
            unions.append(intervals.pop(0))
    return unions


# This for the searched intervals on the x-axis
def find_intervals(y_target, sensors):
    intervals = []
    for sensor in sensors.keys():
        # compare manhattan (scanned) distance and the distance between 
        # the sensor and target y value
        remainder = sensors[sensor] - abs(sensor[1] - y_target)
        if remainder >= 0:
            intervals.append([sensor[0]-remainder, sensor[0]+remainder])
    return intervals

# part 1
y_target = 2000000
unions = interval_union(find_intervals(y_target, sensors))
searched_spaces = sum([x[1]-x[0]+1 for x in unions])
# remove beacons and sensors from union
num_beacs_sens = sum([1 for x in sensors.keys() if x[1] == y_target] + \
                        [1 for x in beacons if x[1] == y_target])
searched_spaces -= num_beacs_sens
print(searched_spaces)


# part 2
# there can only be one spot, so check for gaps in unions
y_max = 4000000
for y in range(0, y_max+1):
    unions = interval_union(find_intervals(y, sensors))
    if len(unions) == 2 and (0 <= unions[0][1]+1 < y_max):
        print((unions[0][1]+1)*4000000 + y)
        break
