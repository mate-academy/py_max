'''
Module
'''
from typing import Iterable
from functools import reduce


def max_(lst: Iterable[int]) -> int:
    '''

    :param lst:
    :return:
    '''
    return reduce(lambda x, y: x if x > y else y, lst)
