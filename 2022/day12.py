# NOTE: This solution was inspired by github user blin00
import numpy as np
import string
from collections import deque


# use this to convert text map to int for comparison
alpha = list(string.ascii_lowercase)
nums = list(range(len(alpha)))
converter = dict(zip(alpha, nums))
converter['E'], converter['S'] = 101, 100


with open('day12.txt', 'r') as file:
    h_map = file.readlines()


height_map = np.empty((len(h_map), len(h_map[0])-1))
x_max, y_max = height_map.shape
for i, line in enumerate(h_map):
    for j, char in enumerate(list(line.strip('\n'))):
        height_map[i, j] = converter[char]


def node_check4(i, j, x_size=None, y_size=None):
    for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        ii = i + di
        jj = j + dj
        if x_size is not None:
            if ii < 0 or ii >= x_size:
                continue
        if y_size is not None:
            if jj < 0 or jj >= y_size:
                continue
        yield ii, jj


# find starting and ending positions, replace values in map with heights
start_pos = np.argwhere(height_map == 100)[0]
end_pos = np.argwhere(height_map == 101)[0]
height_map[start_pos[0], start_pos[1]] = 0
height_map[end_pos[0], end_pos[1]] = len(alpha) - 1


# create our move queue and visited node set
move_queue = deque()
move_queue.append((end_pos[0], end_pos[1], 0))
visited_nodes = set()


# start from the top and work down
num_steps = 1e18
while move_queue:
    i, j, d = move_queue.popleft()
    if (i, j) in visited_nodes:
        continue
    visited_nodes.add((i, j))
    for ii, jj in node_check4(i, j, x_max, y_max):
        if height_map[i, j] <= height_map[ii, jj] + 1:
            move_queue.append((ii, jj, d + 1))
    # part 1
    #if [i, j] == [start_pos[0], start_pos[1]]:
    # part 2
    if height_map[i, j] == 0:
        num_steps = min(num_steps, d)
print(num_steps)
