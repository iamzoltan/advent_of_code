import numpy as np


with open("day11.txt") as f:
    seat_layout = f.readlines()
split_seats = np.array([list(seat_row.strip('\n')) for seat_row in seat_layout])
padded_seats = np.array([['0'] * (split_seats.shape[1]+2) for i in range(split_seats.shape[0]+2)])
padded_seats[1:-1, 1:-1] = split_seats
seat_layout2 = padded_seats.copy()


def apply_rules(seats, seats_copy):
    for i, seat_row in enumerate(seats):
        for j, seat in enumerate(seat_row):
            if seat == ".":
                continue
            # Rule 1
            elif seat == "L":
                if seats[i, j+1] != "#" and seats[i+1, j+1] != "#" and \
                    seats[i+1, j] != "#" and seats[i+1, j-1] != "#" and \
                    seats[i, j-1] != "#" and seats[i-1, j-1] != "#" and \
                    seats[i-1, j] != "#" and seats[i-1, j+1] != "#":
                        seats_copy[i, j] = "#"
            # Rule 2
            elif seat == "#":
                count = np.count_nonzero(seats[i-1, j-1:j+2] == "#") + \
                        np.count_nonzero(seats[i+1, j-1:j+2] == "#") + \
                        np.count_nonzero(seats[i, j-1:j+2] == "#") - 1
                if count >= 4:
                    seats_copy[i, j] = "L"
            # Rule 3
            else:
                continue
    return seats, seats_copy


def check_empty(array):
    empty_min = 10000 - 1
    occ_min = 10000
    if array.size == 0:
        return "empty"
    if "L" in array:
        empty_min = np.min(np.argwhere(array == "L"))
    if "#" in array:
        occ_min = np.min(np.argwhere(array == "#"))
    if empty_min < occ_min:
        return "empty"
    else:
        return "occupied"


def apply_rules2(seats, seats_copy):
    for i, seat_row in enumerate(seats):
        for j, seat in enumerate(seat_row):
            if seat == ".":
                continue

            # Rule 1
            elif seat == "L":
              # print(seats[1:i+7, 1:j+7])
                
                # Upper vertical line
                upp_vert = np.flip(seats[1:i, j])
                if check_empty(upp_vert) == "occupied":
                    continue

                # Upper right diagonal
                #upp_r_diag = np.flip(np.diag(np.flip(seats[1:i, j+1:len(seat_row)-(j+1)])))
                upp_r_diag = np.diag(np.flip(seats[1:i, j+1:j+i], 0))
                if check_empty(upp_r_diag) == "occupied":
                    continue

                # Right horizontal line
                #r_horiz = seats[i, j+1:len(seat_row)-(j+1)]
                r_horiz = seats[i, j+1:-1]
                if check_empty(r_horiz) == "occupied":
                    continue

                # Bottom right diagonal
                #bot_r_diag = np.diag(seats[i+1:len(seats)-(i+1), j+1:len(seat_row)-(j+1)])
                bot_r_diag = np.diag(seats[i+1:-1, j+1:-1])
                if check_empty(bot_r_diag) == "occupied":
                    continue

                # Bottom vertical line
                #bot_vert = seats[i+1:len(seats)-(i+1), j]
                bot_vert = seats[i+1:-1, j]
                if check_empty(bot_vert) == "occupied":
                    continue

                # Bottom left diagonal
                #bot_l_diag = np.diag(np.flip(seats[i+1:len(seats)-(i+1), 1:j]))
                bot_l_diag = np.diag(np.flip(seats[i+1:i+j, 1:j], 1))
                if check_empty(bot_l_diag) == "occupied":
                    continue

                # Left horizontal line
                #l_horiz = seats[i, 1:j]
                l_horiz = np.flip(seats[i, 1:j])
                if check_empty(l_horiz) == "occupied":
                    continue

                # Upper left diagonal
                #upp_l_diag = np.flip(np.diag(seats[1:i, 1:j]))
                if j > i:
                    upp_l_diag = np.flip(np.diag(seats[1:i, j-i+1:j]))
                elif j == 1:
                    upp_l_diag = np.array([])
                elif j == i:
                    upp_l_diag = np.flip(np.diag(seats[1:i, 1:j]))
                else:
                    upp_l_diag = np.flip(np.diag(seats[i-j+1:i+1, 1:j]))
                if check_empty(upp_l_diag) == "occupied":
                    continue

                seats_copy[i, j] = "#"

            # Rule 2
            elif seat == "#":
                count = 0
                # Upper vertical line
                upp_vert = np.flip(seats[1:i, j])
                if upp_vert.size != 0:
                    first_vis_ind = np.argwhere(upp_vert != ".")
                    if first_vis_ind.size != 0 and upp_vert[first_vis_ind[0]] == "#":
                        count += 1
                    elif upp_vert[0] == "#":
                        count += 1

                # Upper right diagonal
                upp_r_diag = np.diag(np.flip(seats[1:i, j+1:j+i], 0))
                if upp_r_diag.size != 0:
                    first_vis_ind = np.argwhere(upp_r_diag != ".")
                    if first_vis_ind.size != 0 and upp_r_diag[first_vis_ind[0]] == "#":
                        count += 1
                    elif upp_r_diag[0] == "#":
                        count += 1

                # Right horizontal line
                r_horiz = seats[i, j+1:-1]
                if r_horiz.size != 0:
                    first_vis_ind = np.argwhere(r_horiz != ".")
                    if first_vis_ind.size != 0 and r_horiz[first_vis_ind[0]] == "#":
                        count += 1
                    elif r_horiz[0] == "#":
                        count += 1

                # Bottom right diagonal
                bot_r_diag = np.diag(seats[i+1:-1, j+1:-1])
                if bot_r_diag.size != 0:
                    first_vis_ind = np.argwhere(bot_r_diag != ".")
                    if first_vis_ind.size != 0 and bot_r_diag[first_vis_ind[0]] == "#":
                        count += 1
                    elif bot_r_diag[0] == "#":
                        count += 1 

                # Bottom vertical line
                bot_vert = seats[i+1:-1, j]
                if bot_vert.size != 0:
                    first_vis_ind = np.argwhere(bot_vert != ".")
                    if first_vis_ind.size != 0 and bot_vert[first_vis_ind[0]] == "#":
                        count += 1
                    elif bot_vert[0] == "#":
                        count += 1

                # Bottom left diagonal
                bot_l_diag = np.diag(np.flip(seats[i+1:i+j, 1:j], 1))
                if bot_l_diag.size != 0:
                    first_vis_ind = np.argwhere(bot_l_diag != ".")
                    if first_vis_ind.size != 0 and bot_l_diag[first_vis_ind[0]] == "#":
                        count += 1
                    elif bot_l_diag[0] == "#":
                        count += 1

                # Left horizontal line
                l_horiz = np.flip(seats[i, 1:j])
                if l_horiz.size != 0:
                    first_vis_ind = np.argwhere(l_horiz != ".")
                    if first_vis_ind.size != 0 and l_horiz[first_vis_ind[0]] == "#":
                        count += 1
                    elif l_horiz[0] == "#":
                        count += 1

                # Upper left diagonal
                if j > i:
                    upp_l_diag = np.flip(np.diag(seats[1:i, j-i+1:j]))
                elif j == 1:
                    upp_l_diag = np.array([])
                elif j == i:
                    upp_l_diag = np.flip(np.diag(seats[1:i, 1:j]))
                else:
                    upp_l_diag = np.flip(np.diag(seats[i-j+1:i+1, 1:j]))
                if upp_l_diag.size != 0:
                    first_vis_ind = np.argwhere(upp_l_diag != ".")
                    if first_vis_ind.size != 0 and upp_l_diag[first_vis_ind[0]] == "#":
                        count += 1
                    elif upp_l_diag[0] == "#":
                        count += 1

                if count >= 5:
                    seats_copy[i, j] = "L"

            # Rule 3
            else:
                continue
    return seats, seats_copy




seats0, seats1 = padded_seats.copy(), seat_layout2.copy()
while True:
   seats0, seats1  = apply_rules(seats0, seats1)
   if (seats0 == seats1).all():
       break
   seats0 = seats1.copy()
   seats1 = seats0.copy()


print("\nExercise 1:")
print("===========\n")
print(f"Number of Occupied Seats: {np.count_nonzero(seats1 == '#')}\n")


seats0, seats1 = padded_seats.copy(), seat_layout2.copy()
counter = 0
while True:
   seats0, seats1  = apply_rules2(seats0, seats1)
   if (seats0 == seats1).all():
       break
   seats0 = seats1.copy()
   seats1 = seats0.copy()
   counter += 1


print("\nExercise 2:")
print("===========\n")
print(f"Number of Occupied Seats: {np.count_nonzero(seats1 == '#')}")
