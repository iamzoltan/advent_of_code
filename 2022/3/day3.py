import string


priority_sum = 0
priority_list = list(string.ascii_letters)


def priority_calc(item, priority_list):
    return priority_list.index(item) + 1


with open('day3.txt', 'r') as file:
    rucksacks = file.readlines()

# part one
#for sack in rucksacks:
#    sack = sack.strip('\n')
#    num_items = len(sack)
#    compartment1 = sack[:num_items//2]
#    compartment2 = sack[num_items//2:]
#    for item in compartment1:
#        if item in compartment2:
#            priority_sum += priority_calc(item, priority_list)
#            break

# part two
for i in range(0, len(rucksacks), 3):
    sacks = [x.strip('\n') for x in rucksacks[i:i+3]]
    for item in sacks[0]:
        if item in sacks[1] and item in sacks[2]:
            priority_sum += priority_calc(item, priority_list)
            break

print(priority_sum)
