with open("day6.txt") as f:
    data = f.readlines()


# problem 1 (any)
total_yes = 0
group_num_yes = []
alpha_set = set()
for line in data:
    if line == '\n':
        group_num_yes.append(len(alpha_set))
        total_yes += len(alpha_set)
        alpha_set = set()
        continue
    for char in line.strip('\n'):
        alpha_set.add(char)


print(sum(group_num_yes))
print(total_yes)


# problem 2 (all)
total_yes = 0
group_counter = 0
group_yes = 0
group_num_yes = []
alpha_dict = {}
for line in data:
    if line == '\n':
        for key, val in alpha_dict.items():
            if val == group_counter:
                group_yes += 1
        group_num_yes.append(group_yes)
        total_yes += group_yes
        group_yes = 0
        group_counter = 0
        alpha_dict = {}
        continue
    for char in line.strip('\n'):
        if char in alpha_dict.keys():
            alpha_dict[char] += 1
        else:
            alpha_dict[char] = 1
    group_counter += 1



print(sum(group_num_yes))
print(total_yes)
