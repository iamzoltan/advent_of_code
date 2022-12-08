import numpy as np


with open('day8.txt', 'r') as file:
    tree_grid = file.readlines()


def populate_grid(tree_grid):
    hor_len = len(tree_grid[0]) - 1
    vert_len = len(tree_grid)
    grid = np.ndarray((vert_len, hor_len))
    for i in range(vert_len):
        row = tree_grid[i].strip('\n')
        for j in range(hor_len):
            grid[i, j] = int(row[j])
    return grid


def count_visible_trees(tree_grid):
    hid_tree_sum = 0
    hor_len = len(tree_grid[0])
    vert_len = len(tree_grid)
    for i in range(1, vert_len-1):
        row = tree_grid[i, :]
        for j in range(1, hor_len-1):
            height = tree_grid[i, j]
            col = tree_grid[:, j]
            col_bools = 1*(col >= height)
            row_bools = 1*(row >= height)
            if sum(col_bools[:i]) >= 1 and sum(col_bools[i+1:]) >= 1:
                if sum(row_bools[:j]) >= 1 and sum(row_bools[j+1:]) >= 1:
                    hid_tree_sum += 1
    return hor_len * vert_len - hid_tree_sum


def calc_distance(bin_array):
    count = 0
    if bin_array.size == 0:
        return 0
    for item in bin_array:
        if item < 1:
            count += 1
        else:
            return count + 1
    return count


def calc_highest_scenic_score(tree_grid):
    highest_score = 0
    hor_len = len(tree_grid[0])
    vert_len = len(tree_grid)
    for i in range(vert_len):
        row = tree_grid[i, :]
        for j in range(hor_len):
            height = tree_grid[i, j]
            col = tree_grid[:, j]
            col_bools = 1*(col >= height)
            row_bools = 1*(row >= height)
            up_col = col_bools[:i]
            down_col = col_bools[i+1:]
            left_row = row_bools[:j]
            right_row = row_bools[j+1:]
            score = calc_distance(up_col[::-1]) * \
                    calc_distance(down_col) * \
                    calc_distance(left_row[::-1]) * \
                    calc_distance(right_row)
            highest_score = max(score, highest_score)
    return highest_score


tree_grid = populate_grid(tree_grid)
print(count_visible_trees(tree_grid))
print(calc_highest_scenic_score(tree_grid))
