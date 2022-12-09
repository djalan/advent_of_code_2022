#!/usr/bin/env python

import string
from itertools import islice

lower = list(string.ascii_lowercase)
lower_index = list(range(1,27))

upper = list(string.ascii_uppercase)
upper_index = list(range(27,53))

priorities = dict(zip(lower, lower_index))
priorities.update(
        dict(zip(upper, upper_index))
)

total_priorities = 0
with open('input03.txt') as file:
    for rucksack in file:
        half = len(rucksack) // 2
        first_half = rucksack[:half]
        second_half = rucksack[half:]

        intersection = set(first_half) & set(second_half)
        total_priorities += priorities[intersection.pop()]

print(total_priorities)


##########
# part b
##########
total_priorities = 0
with open('input03.txt') as file:
    while True:
        group_lines = list(islice(file, 3))
        if not group_lines:
            break

        one = group_lines[0].strip()
        two = group_lines[1].strip()
        three = group_lines[2].strip()

        intersection = set(one).intersection(two, three)
        total_priorities += priorities[intersection.pop()]

print(total_priorities)
