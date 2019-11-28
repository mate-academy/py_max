"""
docstring
"""
from functools import reduce

def max_(lst) -> int:
    """

    :param lst:
    :return:
    """
    return reduce(lambda x, y: x if x > y else y, lst)
