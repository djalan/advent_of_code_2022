#!/usr/bin/env python

LOSS = 0
DRAW = 3
WIN = 6

total_points = 0

with open('input02.txt') as file:
    for line in file:
        round_points = 0
        game = line.split()
        opponent = game[0]
        me = game[1]
        
        # rock
        if opponent == 'A':
            if me == 'X':
                round_points += DRAW
            elif me == 'Y':
                round_points += WIN
            elif me == 'Z':
                round_points += LOSS

        # paper
        elif opponent == 'B':
            if me == 'X':
                round_points += LOSS
            elif me == 'Y':
                round_points += DRAW
            elif me == 'Z':
                round_points += WIN

        # scissor
        elif opponent == 'C':
            if me == 'X':
                round_points += WIN
            elif me == 'Y':
                round_points += LOSS
            elif me == 'Z':
                round_points += DRAW
               
        # points for my choice
        if me == 'X':
            round_points += 1  # rock
        elif me == 'Y':
            round_points += 2  # paper
        elif me == 'Z':
            round_points += 3  # scissors

        total_points += round_points

print(f"Score is:", total_points)
