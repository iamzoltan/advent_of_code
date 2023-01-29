import numpy as np


with open ('day14.txt', 'r') as file:
    rock_points = file.read()


# rock = 1
# sand = 2
# empty = 0
# start = 4
rock_points = rock_points.split('\n')[:-1]
grid = np.empty((200, 1000))


all_ys = []
for line in rock_points:
    line = line.split(' -> ')
    last_x, last_y = None, None
    for point in line:
        x, y = point.split(',')
        x, y = int(x), int(y)
        all_ys.append(y)
        if last_x == None:
            last_x, last_y = x, y
            continue
        if x == last_x:
            if last_y < y:
                grid[last_y:y+1, x] = 1
            else:
                grid[y:last_y+1, x] = 1
        else:
            if last_x < x:
                grid[y, last_x:x+1] = 1
            else:
                grid[y, x:last_x+1] = 1
        last_x, last_y = x, y


max_y = max(all_ys)
#print(max_y)
is_filled = False
sand_x, sand_y = 500, 0
grid[0, 500] = 4
# part 2 (add floor)
grid[max_y + 2, :] = 1
sand_units = 0
while not is_filled:
    # part 1
    #if sand_y > max_y:
    #    is_filled = True
    #    continue
    # part 2
    if grid[0, 500] == 2:
        is_filled = True
        continue
    if grid[sand_y+1, sand_x] == 0:
        sand_y +=1
    else:
        if grid[sand_y+1, sand_x-1] == 0:
            sand_y += 1
            sand_x -= 1
        elif grid[sand_y+1, sand_x+1] == 0:
            sand_y += 1
            sand_x += 1
        else:
            grid[sand_y, sand_x] = 2
            sand_units += 1
            sand_x, sand_y = 500, 0
            continue


#print(grid[0:50, 490:510])
print(sand_units)
