import numpy as np


with open("day10.txt", "r") as file:
    instructions = file.readlines()


registerX = 1
signal_strength = 0
cycle = 0
value_buffer = np.array([])

# TODO: Functionize?
for instruction in instructions:
    if instruction.strip('\n') == 'noop':
        value_buffer = np.append(value_buffer, 0)
        continue
    else:
        value = int(instruction.strip('\n').split(' ')[-1])
        value_buffer = np.concatenate((value_buffer, np.array([0, value])))

# Part 1
for value in value_buffer:
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strength += registerX * cycle
        print(registerX, cycle)
    registerX += value_buffer[cycle-1]


print(signal_strength)


# Part 2
# Sprite position is the registerX
CRT_line = ""
cycle = 0
registerX = 1
pos = 0
for value in value_buffer:
    cycle += 1
    if abs(registerX - pos) < 2:
        CRT_line += "#"
    else:
        CRT_line += "."
    if cycle in [40, 80, 120, 160, 200, 240]:
        print(CRT_line)
        CRT_line = ""
        pos = 0
        registerX += value_buffer[cycle-1]
        continue
    registerX += value_buffer[cycle-1]
    pos += 1
    
