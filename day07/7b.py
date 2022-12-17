#!/usr/bin/env python

from pathlib import PurePath

with open('input07.txt') as file:
    path = PurePath()
    files = {}
    folders = {}

    # every file size
    for line in file:
        data = line.strip().split(' ')

        if data[0] == '$':
            cmd = data[1]
            if cmd == 'cd':
                directory = data[2]
                if directory == '..':
                    # try:
                    #     folders[path.parent] += folders[path]
                    # except KeyError:
                    #     folders[path.parent] = folders[path]
                    path = path.parent
                elif directory == '/':
                    path = PurePath('/')
                    # folders[path] = 0
                else:
                    path = path / directory

            elif cmd == 'ls':
                next

        elif data[0] == 'dir':
            next

        elif data[0].isnumeric():
            size = int(data[0])
            name = data[1]
            fullpath = path / name
            files[fullpath] = size

            for parent in fullpath.parents:
                try:
                    folders[parent] += size
                except KeyError:
                    folders[parent] = size
            # try:
            #     folders[path] += size
            # except KeyError:
            #     folders[path] = size

# for k,v in files.items():
#     print(k, v)

# for k, v in folders.items():
#     print(k, v)

sum_sizes = 0
for k, v in folders.items():
    if k != PurePath('/') and v <= 100_000:
        sum_sizes += v

print(f"{sum_sizes=}")


# part B
TOTAL_SPACE = 70_000_000
REQUIRED_SPACE = 30_000_000
actual_unused_space = TOTAL_SPACE - folders[PurePath('/')]
target_space_to_free = REQUIRED_SPACE - actual_unused_space

list_big_enough_dir = []

for v in folders.values():
    if v >= target_space_to_free:
        list_big_enough_dir.append(v)

print(f"{sorted(list_big_enough_dir)[0]=}")

