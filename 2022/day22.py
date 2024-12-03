with open('test22.txt', 'r') as file:
    map_steps = file.read().split('\n')


# Facing: R = 0, D = 1, L = 2, U = 3
# Spin: R for clockwise, L for counterclockwise
mapp, steps = map_steps[:-3], list(map_steps[-2])
max_y = len(mapp)
pos_x, pos_y, facing = 1, 1, 0
print(mapp)


num_steps = 0
turn = ''
cum_move = ''
while steps:
    temp = steps.pop(0)
    if temp == 'R' or temp == 'L':
        turn = temp
        num_steps = int(cum_move)
        print(num_steps)
        cum_move = ''
        print(mapp[pos_y-1])
        break
        continue
    cum_move += temp
    
