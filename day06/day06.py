#!/usr/bin/env python

with open('input06.txt') as file:
    s = file.readline()

    UNIQ_CHAR = 14
    start_position = 0
    
    for i in range(len(s) - (UNIQ_CHAR - 1)):
        set_char = set()
        for j in range(UNIQ_CHAR):
            set_char.add(s[i+j])
        if len(set_char) == UNIQ_CHAR:
            start_position = i
            break

print(f"Number of processed char: {start_position + UNIQ_CHAR}")

