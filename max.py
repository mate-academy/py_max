"""
module max
"""
from typing import Iterable
from functools import reduce


def max_(lst: Iterable[int]) -> int:
    """
    Implementation of built-in max() function using reduce().
    :param lst: Iterable[int]
    :return: int
    """
    return reduce(lambda x, y: x if x > y else y, lst)
