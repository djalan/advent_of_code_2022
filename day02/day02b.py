#!/usr/bin/env python

LOSS = 0
DRAW = 3
WIN = 6

# X lose
# Y draw
# Z win

total_points = 0

with open('input02.txt') as file:
    for line in file:
        round_points = 0
        weapon = None
        game = line.split()
        opponent = game[0]
        me = game[1]

        
        # rock
        if opponent == 'A':
            if me == 'X':
                weapon = 'scissors'
            elif me == 'Y':
                weapon = 'rock'
            elif me == 'Z':
                weapon = 'paper'

        # paper
        elif opponent == 'B':
            if me == 'X':
                weapon = 'rock'
            elif me == 'Y':
                weapon = 'paper'
            elif me == 'Z':
                weapon = 'scissors'

        # scissor
        elif opponent == 'C':
            if me == 'X':
                weapon = 'paper'
            elif me == 'Y':
                weapon = 'scissors'
            elif me == 'Z':
                weapon = 'rock'

        if me == 'Y':
            round_points += DRAW
        elif me == 'Z':
            round_points += WIN
               
        # points for my choice
        if weapon == 'rock':
            round_points += 1  # rock
        elif weapon == 'paper':
            round_points += 2  # paper
        elif weapon == 'scissors':
            round_points += 3  # scissors

        total_points += round_points

print(f"Score is:", total_points)
