"""imports"""
from functools import reduce


def max_(lst) -> int:
    """max"""
    maximal = lst[0]

    def change_local(_, ele):
        nonlocal maximal
        if ele > maximal:
            maximal = ele
    reduce(change_local, lst)
    return maximal
