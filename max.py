"""module docstring"""
#from typing import Iterable
import functools

def finding_max(initial_list):
    """func docstring"""
    maxxx = functools.reduce(lambda x, y: x if x > y else y, initial_list)
    return maxxx
