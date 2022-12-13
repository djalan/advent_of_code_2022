#!/usr/bin/env python

with open('input05.txt') as file:
    content = file.readlines()
    crates = content[:8]
    moves = content[10:]

    # create ship 
    positions = list(range(1,34,4))  # 9 stacks
    ship = {}
    for i in range(1,10):
        ship[i] = []

    for line in crates:
        for i in range(9):
            crate_name = line[positions[i]]
            if crate_name != ' ':
                ship[i+1].append(crate_name)

    for stack in ship.values():
        stack.reverse()

    # moves
    for line in moves:
        info = line.split()
        how_much = int(info[1])
        from_where = int(info[3])
        to_where = int(info[5])

        for i in range(how_much):
            removed = ship[from_where].pop()
            ship[to_where].append(removed)

    # answer
    top = ''
    for stack in ship.values():
        if len(stack) > 0:
            top += stack[-1]

print(top)
