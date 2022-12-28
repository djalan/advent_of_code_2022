#st!/usr/bin/env pytest

from day08 import create_ndarray

# 30373
# 25512
# 65332
# 33549
# 35390
FILE = 'sample08.txt'


def test_nda():
    nda = create_ndarray(FILE)

    assert nda[0, 0] == 3  # top left
    assert nda[0, 4] == 3  # top right

    assert nda[4, 0] == 3  # bottom left
    assert nda[4, 4] == 0  # bottom right
