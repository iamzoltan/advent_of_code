import re
import numpy as np


with open("day7.txt") as f:
    rules = f.readlines()


label = 'shiny gold'
bag_dict = {}
bag_color_set = set()
for rule in rules:
    rule_bags = rule.strip('\n').split('contain') 
    parent_bag = rule_bags[0].replace(' bags', '').strip()
    child_dict = {}
    bag_nums = re.findall(r'\d+', rule_bags[1])
    children_bags = [x.strip(' 0123456789.').replace(' bag', '').rstrip('s') for x in rule_bags[1].split(',')]
    if children_bags == ['no other']:
        bag_dict[parent_bag] = {}
    else:
        for i, child_bag in enumerate(children_bags):
            child_dict[child_bag] = int(bag_nums[i])
        bag_dict[parent_bag] = child_dict  
    bag_color_set.add(parent_bag)


# Assert only one rule per color
assert len(bag_dict) == len(bag_color_set)


# Ex 1
color_set = set()
def check_num_bags(bag_dict, label, color_set=None):
    if color_set == None:
        color_set = set()
    keys = []
    vals = []
    for key, val in bag_dict.items():
        if label in val:
            keys.append(key)
            vals.append(val) 
    # Add all bags that can eventually contain a shiny gold bag
    for key in keys:
        color_set.add(key)
    if keys == []:
        # check if no bag contains color
        return 1
    return 1 + np.max([check_num_bags(bag_dict, key, color_set) for key in keys])


print("\nExercise 1:")
print("===========\n")
print(f"Longest chain of bags containing a {label} bag: {check_num_bags(bag_dict, label, color_set)}")
print(f"Number of outter bag colors that can contain a {label} bag: {len(color_set)}")


# Ex 2
def check_num_bags2(bag_dict, label):
    if label not in bag_dict.keys() or bag_dict[label] == {}:
        return 0
    else:
        return np.sum([val + val*check_num_bags2(bag_dict, key) for key, val in bag_dict[label].items()])


print("\nExercise 2:")
print("=============\n")
print(f"Number of bag a {label} must contain: {check_num_bags2(bag_dict, label)}")
