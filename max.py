"""Search max digit module"""
from typing import Iterable
from functools import reduce


def max_(lst: Iterable[int]) -> int:
    """
    Search max digit with reduce method function
    :param lst: list
    :return: result
    """
    def maxfrom2(first, second):
        """
        func max analog for 2 arguments
        :param first:
        :param second:
        :return: maximum digit
        """
        if first > second:
            return first
        return second
    return reduce(maxfrom2, lst)
