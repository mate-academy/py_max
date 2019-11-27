"""
docstring
"""


def max_(lst) -> int:
    """

    :param lst:
    :return:
    """
    maximum = lst[0]
    for i in lst:
        if i > maximum:
            maximum = i
    return maximum
