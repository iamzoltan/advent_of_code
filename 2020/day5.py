with open("day5.txt") as f:
    seats = f.readlines()


seat_ids = []
max_seat_ID = 0
for seat in seats:
    row_range = list(range(128))
    col_range = list(range(8))
    for char in seat:
        if char == 'F':
            row_range = row_range[:len(row_range)//2]
        elif char == 'B':
            row_range = row_range[len(row_range)//2:]
        elif char == 'L':
            col_range = col_range[:len(col_range)//2]
        elif char == 'R':
            col_range = col_range[len(col_range)//2:]

    row = row_range[0]
    col = col_range[0]
    seat_ID =  row * 8 + col
    seat_ids.append(seat_ID)
    if seat_ID > max_seat_ID:
        max_seat_ID = seat_ID


print(f"Ex1: Max seat ID = {max_seat_ID}")
all_ids = list(range(46, 916))
for i, seat_id in enumerate(sorted(seat_ids)):
    if seat_id != all_ids[i]:
        print(seat_id, all_ids[i])
        print(f"Your missing seat id is: {all_ids[i]}")
        break
