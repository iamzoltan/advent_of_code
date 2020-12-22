import numpy as np


with open("day4.txt") as f:
    passports = f.readlines()


passport_entries = ['byr', 'eyr', 'hgt', 'pid', 'hcl', 'iyr', 'ecl', 'cid']
num_valid_passports = 0
passport_dicts = []
passport = {}
for i, line in enumerate(passports):
    if line == "\n":
        passport_dicts.append(passport)
        if len(passport_entries) == len(passport.keys()):
            if (np.sort(passport_entries) == np.sort(list(passport.keys()))).all():
                num_valid_passports += 1
        elif len(passport.keys()) == 7 and ('cid' not in passport.keys()):
            num_valid_passports += 1
        else:
            print(passport.keys())
        del passport
        passport = {}
        continue
    items = line.strip("\n").split(" ")
    for item in items:
        keyitem = item.strip("\n").split(":")
        passport[keyitem[0]] = keyitem[1]

print(f"Number of valid passports: {num_valid_passports}")
print(len(passport_dicts))
