"""Own implementation of built-in max() function using reduce()"""

from typing import Iterable
from functools import reduce


def max_(arr: Iterable[int]) -> int:
    """Return the highest value"""
    return reduce(lambda x, y: x if x > y else y, arr)
