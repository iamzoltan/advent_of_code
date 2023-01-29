"""
The Following are the falling rock formations

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##

"""

def looper(array):
    while True:
        yield array[0]
        array = array[1:] + array[:1]

def print_grid(grid, max_y, width):
    viz = [["."] * width for _ in range(max_y + 3)]
    for (x, y) in grid:
        viz[y][x] = "#"
    viz = "\n".join(["".join(line) for line in viz])
    print(viz[::-1])


rocks = looper([
    {(0, 0), (1, 0), (2, 0), (3, 0)},
    {(1, 0), (1, 1), (0, 1), (2, 1), (1, 2)},
    {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},
    {(0, 0), (0, 1), (0, 2), (0, 3)},
    {(0, 0), (0, 1), (1, 0), (1, 1)}
])


with open('day17.txt', 'r') as file:
    jets = looper(file.read().split('\n')[0])


max_y = 0
width = 7


grid = set()
count = 0

# TODO: solve part two
for count in range(2022):
#    if count % 1000000 == 0:
#        print('yoyoma')
    rock = next(rocks)
    rock = {(x + 2, y + max_y + 3) for (x, y) in rock}
    while True:
#        print_grid(grid ^ rock, max_y + 4, width)
#        print('')
#        print(rock)
        jet = next(jets)
        # Move Right
        if jet == ">":
            shift_rock = {(x + 1, y) for (x, y) in rock}
            if not any((x, y) in grid or x >= width for (x, y) in shift_rock):
                rock = shift_rock
        # Move Left
        else:
            shift_rock = {(x - 1, y) for (x, y) in rock}
            if not any((x, y) in grid or x < 0 for (x, y) in shift_rock):
                rock = shift_rock
        # Move Down
        shift_rock = {(x, y - 1) for (x, y) in rock}
        if not any((x, y) in grid or y < 0 for (x, y) in shift_rock):
            rock = shift_rock
        else:
            for (x, y) in rock:
                grid.add((x, y))
                # plus 1 because of floor (at -1)
                if y + 1 > max_y:
                    max_y = y + 1
#            print_grid(grid, max_y, width)
            break
        #print(jet)

print(max_y)


