#!/usr/bin/env python


sums = [-1]
elf_total = 0

with open('input01.txt') as file:
    for line in file:
        try:
            calories = int(line)
            elf_total += calories
        except ValueError:
            sums.append(elf_total)
            elf_total = 0
        
max_calories = max(sums)
elf_number = sums.index(max_calories)

print(f"Elf #{elf_number} has #{max_calories} calories")


# part b

max_1 = max_calories

sums.remove(max_1)
max_2 = max(sums)
sums.remove(max_2)
max_3 = max(sums)

print("Total of top 3:", max_1 + max_2 + max_3)
