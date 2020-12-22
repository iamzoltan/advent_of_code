import numpy as np


with open("day8.txt") as f:
    data = f.readlines()


def execute_inst(accumulator, pointer, data_cp):
    inst_set = data_cp[pointer].split(' ')
    action, value = inst_set[0], int(inst_set[1])
    if action == 'acc':
        accumulator += value
        pointer += 1
    elif action == 'jmp':
        jmp_ind.append(pointer)
        pointer += value
    elif action == 'nop':
        nop_ind.append(pointer)
        pointer += 1
    return accumulator, pointer


jmp_ind = []
nop_ind = []
accumulator = 0
loop_detected = False
pointer = 0
pointer_location_set = set()
data_copy = data.copy()
while not loop_detected:
    if pointer == len(data):
        print("Done")
        break
    pointer_cache = pointer
    pointer_location_set.add(pointer)
    accumulator, pointer = execute_inst(accumulator, pointer, data_copy)
    if pointer in pointer_location_set:
        loop_detected = True
        print("\nLoop Dectected!! - Check accumulator and look to fix loop:")
        print("==========================================================\n")
        # Ex1
        print(f"Accumulator at: {accumulator}")
        print(f"Loop Start Index: {pointer}")
        print(f"Loop End Index: {pointer_cache}\n")
        print("Checking jmp flips... ")
        
        for j_ind in jmp_ind:
            data_copy = data.copy()
            pointer_location_set = set()
            pointer = 0
            accumulator = 0
            data_copy[j_ind] = data_copy[j_ind].replace('jmp', 'nop')
            while pointer not in pointer_location_set:
                pointer_location_set.add(pointer)
                accumulator, pointer = execute_inst(accumulator, pointer, data_copy)
                if pointer == len(data):
                    print("Done - Program executes after flipping a jmp to a nop:")
                    print("======================================================\n")
                    print(f"Index of corrupted inst: {j_ind}\n")
                    print(f"Corrupted data: {data[j_ind]}")
                    print(f"Fixed data: {data_copy[j_ind]}")
                    # Ex2
                    print(f"Accumlator after a sequence terminates: {accumulator}")
                    exit()


        
