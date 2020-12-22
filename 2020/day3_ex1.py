with open("day3.txt") as f:
    tree_map = f.readlines()


num_trees = 0
run = 3
for i, line in enumerate(tree_map):
    line = line.strip('\n')
    if i*run < len(line):
        if tree_map[i][i*run] == "#":
            num_trees += 1
    else:
        if tree_map[i][(i*run)%len(line)] == "#":
            num_trees += 1


print(num_trees)
