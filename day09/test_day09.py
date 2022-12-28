#!/usr/bin/env pytest

import pytest

from day09 import tail_is_adjacent

HEAD = (0, 0)


def test_is_adjacent_overlap():
    assert True == tail_is_adjacent(HEAD, (0, 0))


def test_is_adjacent_same_x():
    assert True == tail_is_adjacent(HEAD, (0, 1))
    assert True == tail_is_adjacent(HEAD, (0, -1))


def test_is_adjacent_same_y():
    assert True == tail_is_adjacent(HEAD, (-1, 0))
    assert True == tail_is_adjacent(HEAD, (1, 0))


def test_not_adjacent_same_x():
    assert False == tail_is_adjacent(HEAD, (0, 2))
    assert False == tail_is_adjacent(HEAD, (0, -2))


@pytest.mark.parametrize(
    "tail",
    [
        (0, 3),
        (0, 4),
    ],
)
def test_not_adjacent_same_x_bigger_gap(tail):
    assert False == tail_is_adjacent(HEAD, tail)


def test_not_adjacent_same_y():
    assert False == tail_is_adjacent(HEAD, (2, 0))
    assert False == tail_is_adjacent(HEAD, (-2, 0))


@pytest.mark.parametrize(
    "tail",
    [
        (3, 0),
        (4, 0),
    ],
)
def test_not_adjacent_same_y_bigger_gap(tail):
    assert False == tail_is_adjacent(HEAD, tail)
