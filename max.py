"""docstring"""
from typing import Iterable
from functools import reduce


def max_item(list_item: Iterable[int]) -> int:
    """"return max element of list using reduce function"""
    return reduce(lambda x, y: x if x > y else y, list_item)
