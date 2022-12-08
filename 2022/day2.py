score = 0


with open('day2.txt', 'r') as file:
    strategy_guide = file.readlines()


# part one
def decrypt(move):
    if move == 'A' or move == 'X':
        return 'rock'
    elif move == 'B' or move == 'Y':
        return 'paper'
    else:
        return 'scissors'


# part two
# A = rock, B = paper, C = scissors
# X = you lose, Y = draw, Z = you win
def decrypt2(your_move, opp_move):
    if your_move == 'X':
        if opp_move == 'A':
            return 'scissors'
        elif opp_move == 'B':
            return 'rock'
        else:
            return 'paper'
    elif your_move == 'Y':
        return decrypt(opp_move)
    else:
        if opp_move == 'A':
            return 'paper'
        elif opp_move == 'B':
            return 'scissors'
        else:
            return 'rock'


for game in strategy_guide:
    opp_move, your_move = game.strip('\n').split(' ')
    # First decrypt moves
    # your_move = decrypt(your_move) # part one
    your_move = decrypt2(your_move, opp_move) # part two
    opp_move = decrypt(opp_move)
    # Check for draw
    if your_move == opp_move:
        score += 3
    if your_move == 'rock':
        score += 1
        if opp_move == 'scissors':
            score += 6
    elif your_move == 'paper':
        score += 2
        if opp_move == 'rock':
            score += 6
    elif your_move == 'scissors': 
        score += 3
        if opp_move == 'paper':
            score += 6

print(score)


