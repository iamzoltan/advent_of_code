import numpy as np


num_valid_passwords = 0
with open("day2.txt") as f:
    lines = f.readlines()
    for line in lines:
        terms = line.split(sep=" ")
        policy_limits = terms[0].split(sep="-")
        policy_char = terms[1][0]
        password = terms[2].strip("\n")
        if password[int(policy_limits[0])-1] == policy_char == password[int(policy_limits[1])-1]:
            continue
        elif password[int(policy_limits[0])-1] != policy_char != password[int(policy_limits[1])-1]:
            continue
        else:
            num_valid_passwords += 1

print(f"# of valid passwords: {num_valid_passwords}")
