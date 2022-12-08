import numpy as np


with open('day1.txt', 'r') as file:
    calories = file.readlines()

elves = []
max_cals = 0
curr_cals = 0

for item in calories:
    if item != '\n':
        curr_cals += int(item.strip('\n'))
    else:
        if curr_cals > max_cals:
            max_cals = curr_cals
        elves.append(curr_cals)
        curr_cals = 0

print(max_cals)

print(sum(np.sort(elves)[-3:]))


