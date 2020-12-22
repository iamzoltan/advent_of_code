import numpy as np


num_valid_passwords = 0
with open("day2.txt") as f:
    lines = f.readlines()
    for line in lines:
        terms = line.split(sep=" ")
        policy_limits = terms[0].split(sep="-")
        policy_char = terms[1][0]
        password = terms[2].strip("\n")
        num_char = 0
        for char in password:
            if char == policy_char:
                num_char += 1
        if int(policy_limits[1]) < num_char:
            continue
        elif int(policy_limits[0]) > num_char:
            continue
        else:
            num_valid_passwords += 1

print(f"# of valid passwords: {num_valid_passwords}")
