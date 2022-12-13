#!/usr/bin/env python

contain_total = 0
with open('input04.txt') as file:
    for line in file:
        pairs = line.strip().split(',')
        first_min_section = int(pairs[0].split('-')[0])
        first_max_section = int(pairs[0].split('-')[1])
        second_min_section = int(pairs[1].split('-')[0])
        second_max_section = int(pairs[1].split('-')[1])

        if first_min_section <= second_min_section and first_max_section >= second_max_section:
            contain_total += 1
        elif second_min_section <= first_min_section and second_max_section >= first_max_section:
            contain_total += 1

print(f"{contain_total=}")
