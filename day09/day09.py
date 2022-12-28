#!/usr/bin/env python

def tail_is_adjacent(head, tail):
    headx = head[0]
    heady = head[1]
    tailx = tail[0]
    taily = tail[1]
    if (headx - tailx) in (-1, 0, 1) and (heady - taily) in (-1, 0, 1):
        return True
    return False


if __name__ == "__main__":
    visited = [tuple([0,0])]
    with open("input09.txt", encoding='us-ascii') as file:
        headx = 0
        heady = 0
        tailx = 0
        taily = 0

        for line in file:
            data = line.strip().split(" ")
            direction = data[0]
            steps = int(data[1])

            for i in range(steps):
                if direction == "L":
                    headx -= 1
                    if not tail_is_adjacent((headx, heady), (tailx, taily)):
                        tailx = headx + 1
                        taily = heady
                        visited.append((tailx, taily))
                elif direction == "R":
                    headx += 1
                    if not tail_is_adjacent((headx, heady), (tailx, taily)):
                        tailx = headx - 1
                        taily = heady
                        visited.append((tailx, taily))
                elif direction == "U":
                    heady += 1
                    if not tail_is_adjacent((headx, heady), (tailx, taily)):
                        tailx = headx
                        taily = heady - 1
                        visited.append((tailx, taily))
                elif direction == "D":
                    heady -= 1
                    if not tail_is_adjacent((headx, heady), (tailx, taily)):
                        tailx = headx
                        taily = heady + 1
                        visited.append((tailx, taily))

    print(len(set(visited)))
