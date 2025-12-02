# Part A
password = 0
cur = 50
with open('input.txt', 'r') as f:
    for line in f:
        dir = 1 if line[0] == 'R' else -1
        step = int(line[1:]) % 100

        cur += (dir * step)
        cur %= 100

        if cur == 0:
            password += 1
print(f"Part A: {password}")

# Part B
password = 0
cur = 50
with open('input.txt', 'r') as f:
    for line in f:
        dir = 1 if line[0] == 'R' else -1
        step = int(line[1:])

        password += step // 100
        step %= 100

        next = cur + (dir * step)

        if (next < 0 or next > 100) and cur != 0:
            password += 1

        cur = next % 100

        if cur == 0:
            password += 1

print(f"Part B: {password}")
