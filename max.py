"""module docstring"""
#from typing import Iterable
import functools


def n_max(initial_list):
    """func docstring"""
    return functools.reduce(lambda x, y: x if x > y else y, initial_list)
