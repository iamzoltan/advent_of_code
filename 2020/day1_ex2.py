import numpy as np

# Two pointer method
# Sort input data and then use two pointers to travers the list for target sum
data = np.sort(np.loadtxt("day1.txt"))
target_sum = 2020


for i, x in enumerate(data):
    pointer1 = i + 1
    pointer2 = len(data) - 1
    while pointer1 < pointer2:
        triplet_sum = x + data[pointer1] + data[pointer2]
        if triplet_sum < target_sum:
            pointer1 += 1
        elif triplet_sum > target_sum:
            pointer2 -= 1
        elif triplet_sum == target_sum:
            print(x, data[pointer1], data[pointer2])
            print(x * data[pointer1] * data[pointer2])
            break
