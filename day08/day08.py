#!/usr/bin/env python

import numpy as np
import logging

def create_ndarray(file='input08.txt'):
    with open(file, encoding = 'us-ascii') as f:
        table = []
        for line in f:
            row = [int(char) for char in line.strip()]
            table.append(row)
        return np.array(table)


if __name__ == "__main__":
    logging.basicConfig(filename='8.log', filemode='w', level=logging.DEBUG)

    # nda = create_ndarray('sample08.txt')
    nda = create_ndarray()
    visible = []
    number_rows = len(nda)
    number_cols = len(nda[0])

    # add coordinates for first and last ROW
    for m in [0, number_rows - 1]:
        for n in range(number_cols):
            visible.append((m,n))

    # add coordinates for first and last COLUMN
    for m in range(number_rows):
        for n in [0, number_cols - 1]:
            visible.append((m,n))

    # sample.txt
    # 30373
    # 25512
    # 65332
    # 33549
    # 35390
    for m in range(1, number_rows - 1):
        for n in range(1, number_cols - 1):
            whoami = nda[m, n]
            logging.debug(whoami)

            before = nda[m, :n]
            if max(before) < whoami:
                visible.append((m,n))
                logging.debug("left: %s,%s %s", m, n, before)

            before = nda[m, n+1:]
            if max(before) < whoami:
                visible.append((m,n))
                logging.debug("right: %s,%s %s", m, n, before)

            before = nda[:m, n]
            if max(before) < whoami:
                visible.append((m,n))
                logging.debug("top: %s,%s %s", m, n, before)

            before = nda[m+1:, n]
            if max(before) < whoami:
                visible.append((m,n))
                logging.debug("bottom: %s,%s %s", m, n, before)

    print(f"total: {len(set(visible))}")
    logging.debug("total: %s", len(set(visible)))
