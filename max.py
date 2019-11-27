"""
max
"""
from typing import Iterable
import functools


def max_(items: Iterable[int]) -> int:
    """

    :param items: list
    :return: return max number
    """
    def find_max(value1, value2):
        if value1 > value2:
            return value1
        return value2

    return functools.reduce(find_max, items)
