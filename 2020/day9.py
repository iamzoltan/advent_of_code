import numpy as np


with open("day9.txt") as f:
    data = f.readlines()


def list_sum(array, target_sum):
    for i, item in enumerate(array):
        counter = i + 1
        while counter < len(array):
            pair_sum = array[counter] + item
            if pair_sum == target_sum:
                return True
            counter += 1
    return False


buffer_size = 25
xmas_buffer = []
for i, line in enumerate(data):
    if i < buffer_size:
        xmas_buffer.append(int(line))
    elif list_sum(xmas_buffer, int(line)):
        xmas_buffer.pop(0)
        xmas_buffer.append(int(line))
    else:
        # Ex 1
        print(f"\nFirst line that doesn't fit the xmas cypher: {int(line)}")
        print(f"This occured at index: {i}")
        print(f"Total digits: {len(data)}\n")
        # Ex 2
        print("Looking for cypher weakness score...")
        data_seen = np.array([int(x) for x in data[:i]])
        for j in range(1, len(data_seen)):
            pointer = j + 1
            while pointer < len(data_seen):
                if int(np.sum(data_seen[j:pointer])) == int(line):
                    data_min, data_max = np.min(data_seen[j:pointer]), np.max(data_seen[j:pointer])
                    print(f"The cypher weakness score is: {data_min + data_max}\n")
                    exit()
                    break
                pointer += 1
            

        break
