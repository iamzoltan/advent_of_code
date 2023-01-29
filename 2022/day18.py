import numpy as np


with open('day18.txt', 'r') as file:
    cubes = file.read()


cubes = cubes.split('\n')[:-1]
points = [[int(x) for x in y.split(',')] for y in cubes]


shared_sides = {}
max_x, min_x = 0, 100
max_y, min_y = 0, 100
max_z, min_z = 0, 100
for i, point in enumerate(points):
    shared_sides[cubes[i]] = 0
    for j in range(len(points)):
        if j != i:
            max_x = max(max_x, point[0])
            max_y = max(max_y, point[1])
            max_z = max(max_z, point[2])
            min_x = min(min_x, point[0])
            min_y = min(min_y, point[1])
            min_z = min(min_z, point[2])
            a = np.array(point)
            b = np.array(points[j])
            if np.sum(abs(a - b)) == 1:
                shared_sides[cubes[i]] += 1


# part 1
num_sides = len(points)*6 - sum(shared_sides.values())
print(num_sides)


# part 2
print(min_x, min_y, min_z)
print(max_x, max_y, max_z)
area = np.zeros((max_x, max_y, max_z))
for point in points:
    x, y, z = point
    area[x-1, y-1, z-1] = 1


num_internal_cubes = 0
for x in range(1, max_x-1):
    for y in range(1, max_y-1):
        for z in range(1, max_z-1):
            if area[x, y, z] == 0:
                if area[x, y, z+1] == 1 and area[x, y, z-1] == 1:
                    if area[x, y-1, z] == 1 and area[x, y+1, z] == 1:
                        if area[x-1, y, z] == 1 and area[x+1, y, z] == 1:
                            num_internal_cubes += 1
                        elif area[x-1, y, z] == 0 and area[x+1, y, z] == 1:
                            num_internal_cubes += 1
                        elif area[x-1, y, z] == 1 and area[x+1, y, z] == 0:
                            num_internal_cubes += 1
                    elif area[x, y-1, z] == 0 and area[x, y+1, z] == 1:
                        if area[x-1, y, z] == 1 and area[x+1, y, z] == 1:
                            num_internal_cubes += 1
                    elif area[x, y-1, z] == 1 and area[x, y+1, z] == 0:
                        if area[x-1, y, z] == 1 and area[x+1, y, z] == 1:
                            num_internal_cubes += 1
                    

                    
                elif area[x, y, z-1] == 0 and area[x, y, z+1] == 1:
                    if area[x, y-1, z] == 1 and area[x, y+1, z] == 1:
                        if area[x-1, y, z] == 1 and area[x+1, y, z] == 1:
                            num_internal_cubes+=1
                elif area[x, y, z-1] == 1 and area[x, y, z+1] == 0:
                    if area[x, y-1, z] == 1 and area[x, y+1, z] == 1:
                        if area[x-1, y, z] == 1 and area[x+1, y, z] == 1:
                            num_internal_cubes+=1

                     


print(area)
print(num_internal_cubes)
print(num_sides - num_internal_cubes*6)
