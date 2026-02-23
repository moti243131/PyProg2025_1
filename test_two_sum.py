import pytest

from two_sum import two_sum


def test_example1() -> None:
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_example2() -> None:
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_example3() -> None:
    assert two_sum([3, 3], 6) == [0, 1]


def test_no_solution() -> None:
    result = two_sum([1, 2, 3], 10)
    assert result == []


def test_single_pair() -> None:
    result = two_sum([1, 2, 3, 4], 7)
    assert result in ([2, 3], [3, 2])


def test_one_numder() -> None:
    result = two_sum([1, 9], 18)
    assert result == [1, 1]
