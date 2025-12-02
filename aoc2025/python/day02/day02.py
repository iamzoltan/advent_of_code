# Part 1
sum = 0
with open('input.txt', 'r') as f:
    line = f.readline()

ranges = line.strip().split(',')
for r in ranges:
    first_id, last_id = r.split('-')
    for id in range(int(first_id), int(last_id)+1):
        # Check for non even string
        str_id = str(id)
        num_digs = len(str_id)
        if num_digs % 2 != 0:
            continue

        midpoint = num_digs // 2
        if str_id[midpoint:] == str_id[:midpoint]:
            sum += id

print(f"Part 1: {sum}")


# Part 2
sum = 0
with open('input.txt', 'r') as f:
    line = f.readline()

ranges = line.strip().split(',')
for r in ranges:
    first_id, last_id = r.split('-')
    for id in range(int(first_id), int(last_id)+1):
        str_id = str(id)
        num_digs = len(str_id)
        # Check if substring can make up string
        for i in range(1, num_digs // 2 + 1):
            if num_digs % i == 0:
                if str_id[:i] * (num_digs // i) == str_id:
                    sum += id
                    break
print(f"Part 2: {sum}")


