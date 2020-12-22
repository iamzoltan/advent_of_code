import numpy as np



def validate_passport(passport):
    if not (len(passport['byr']) == 4 and 1920 <= int(passport['byr']) <= 2002 and passport['byr'].isnumeric()):
        return False
    if not (len(passport['iyr']) == 4 and 2010 <= int(passport['iyr']) <= 2020 and passport['iyr'].isnumeric()):
        return False
    if not (len(passport['eyr']) == 4 and 2020 <= int(passport['eyr']) <= 2030 and passport['eyr'].isnumeric()):
        return False
    if 'cm' in passport['hgt']:
        if not (150 <= int(passport['hgt'].strip('cm')) <= 193):
            return False
    elif 'in' in passport['hgt']:
        if not (59 <= int(passport['hgt'].strip('in')) <= 76):
            return False
    else:
        return False
    if not (passport['hcl'][0] == "#" and len(passport['hcl'].strip('#')) == 6):
        return False
    for char in str(passport['hcl'][1:]):
        if not (char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or char in ['a', 'b', 'c', 'd', 'e', 'f']):
            return False
    if not (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False
    if not (len(passport['pid']) == 9 and passport['pid'].isnumeric()):
        return False
    return True


with open("day4b.txt") as f: 
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
                if validate_passport(passport):
                    num_valid_passports += 1
        elif len(passport.keys()) == 7 and ('cid' not in passport.keys()):
            if validate_passport(passport):
                num_valid_passports += 1
        del passport
        passport = {}
        continue
    items = line.strip("\n").split(" ")
    for item in items:
        keyitem = item.strip("\n").split(":")
        passport[keyitem[0]] = keyitem[1]

print(f"Number of valid passports: {num_valid_passports}")
print(f"Total number of passports: {len(passport_dicts)}")
