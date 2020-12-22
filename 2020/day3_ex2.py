import numpy as np


with open("day3.txt") as f:
    tree_map = f.readlines()


runs = [1, 3, 5, 7, 1]
rises = [1, 1, 1, 1, 2]
num_trees = np.zeros(len(runs))
for j, run in enumerate(runs):
    for i, line in enumerate(tree_map):
        if rises[j] > 1:
            if i*rises[j] > len(tree_map):
                break
        line = line.strip('\n')
        if tree_map[i*rises[j]][(i*run)%len(line)] == "#":
            num_trees[j] += 1


print(num_trees)
print(np.prod(num_trees))

