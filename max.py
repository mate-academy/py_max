"""Create your own implementation of built-in max() function using reduce()."""
from typing import Iterable
from functools import reduce


def max_(array: Iterable[int]) -> int:
    """Return the largest item in an iterable or the largest of two or more arguments."""
    return reduce(lambda x, y: x if x > y else y, array)
