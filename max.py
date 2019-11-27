"""
Create own implementation of built-in max() function using reduce().
"""


from typing import Iterable
import functools


def max_(lst: Iterable[int]) -> int:
    """My build-in max() function"""
    return functools.reduce(lambda x, y: x if x > y else y, lst)
