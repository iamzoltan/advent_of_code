stacks = []
moves = []
switch = False


with open('day5.txt', 'r') as file:
    for line in file.readlines():
        if not switch:
            if line == '\n':
                switch = True
                continue
            else:
                stacks.append(line.strip('\n'))
        else:
            moves.append(line.strip('\n'))

def parse_stacks(stacks):
    num_spaces = len(stacks[0])
    num_stacks = int(stacks[-1][-2])
    stacks_dict = dict.fromkeys(list(range(1, num_stacks + 1))) 
    crates_ind = list(range(1, num_spaces, 4))
    assert len(crates_ind) == num_stacks
    stacks = stacks[:-1]
    for stack in stacks[::-1]:
        for i, ind in enumerate(crates_ind):
            if stack[ind] == " ":
                continue
            if stacks_dict[i+1] == None:
                stacks_dict[i+1] = ""
            stacks_dict[i+1] += stack[ind]
    return stacks_dict


cargo = parse_stacks(stacks)
print(cargo)
print(moves[0].split(" "))


def move_cargo(cargo, moves):
    amt, frm, to = 0, 0, 0
    for move in moves:
        move = move.split(" ")
        amt = int(move[1])
        frm = int(move[3])
        to = int(move[5])
        crates_moved = cargo[frm][-amt:]
        cargo[frm] = cargo[frm][:-amt]
        # part one
        #cargo[to] += crates_moved[::-1]
        # part two
        cargo[to] += crates_moved
    
# mutates passed in dict
move_cargo(cargo, moves)
print(cargo)
top_crates = ""

for value in cargo.values():
    top_crates += value[-1]

print(top_crates)


