# TODO: adapt part one to work with part two
import numpy as np
from collections import deque


with open('day9.txt', 'r') as file:
    motions = file.readlines()


def translate_head(head_pos, direction):
    if direction == 'L':
        trans_tup = (-1, 0)
    elif direction == 'R':
        trans_tup = (1, 0)
    elif direction == 'U':
        trans_tup = (0, 1)
    elif direction == 'D':
        trans_tup = (0, -1)
    return tuple(map(sum, zip(head_pos, trans_tup)))


def is_tail_follow(head_pos, tail_pos, dist):
    dx = abs(head_pos[0] - tail_pos[0])
    dy = abs(head_pos[1] - tail_pos[1])
    if dx > dist or dy > dist:
        return True
    else:
        return False


visited_nodes = set()
head_pos = (0, 0)
prev_head = head_pos
tail_pos = (0, 0)
# part 1
#dist = 1
# part 2 NOTE: part 2 mostly taken from blin00, works for p1 too
knots = [[0,0] for _ in range(10)]
visited_nodes.add(tail_pos)
for i, motion in enumerate(motions):
    direction, step_size = motion.strip('\n').split(' ')
    count = int(step_size)
    while count != 0:
        count -= 1
        # part 2
        head_delta = (0, 0)
        head_delta = translate_head(head_delta, direction)
        knots[0][0] += head_delta[0]
        knots[0][1] += head_delta[1]
        for j in range(1, len(knots)):
            headx = knots[j - 1][0]
            heady = knots[j - 1][1]           
            tailx = knots[j][0]
            taily = knots[j][1]
            if headx == tailx:
                if abs(heady - taily) >= 2:
                    if taily > heady:
                        taily -= 1
                    else:
                        taily += 1
            elif heady == taily:
                if abs(headx - tailx) >= 2:
                    if tailx > headx:
                        tailx -= 1
                    else:
                        tailx += 1
            else:
                if abs(headx -tailx) >= 2 or abs(heady - taily) >= 2:
                    dx = np.sign(headx - tailx)
                    dy = np.sign(heady - taily)
                    tailx += dx
                    taily += dy
            knots[j][0] = tailx
            knots[j][1] = taily
        visited_nodes.add((knots[-1][0], knots[-1][1]))
                
        # part 1
        #prev_head = head_pos
        #head_pos = translate_head(head_pos, direction)
        #if is_tail_follow(head_pos, tail_pos, dist):
        #    tail_pos = prev_head
        #if tail_pos in visited_nodes:
        #    continue
        #visited_nodes.add(tail_pos)


print(len(visited_nodes))
