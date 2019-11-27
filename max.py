"""docstring"""
from typing import Iterable
from functools import reduce


def max_(iterable: Iterable[int]) -> int:
    """
    Returns maximal element from iterable
    :param iterable: Iterable[int]
    :return: int
    """

    return reduce(lambda a, b: a if a > b else b, iterable)
