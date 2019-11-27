"""
docstring
"""
import max


def test_list():
    """

    :return:
    """
    assert max.max_([2, 1, 5, 4, 7]) == 7


def test_equal():
    """

    :return:
    """
    assert max.max_([1, 1, 1, 1]) == 1


def test_empty():
    """

    :return:
    """
    assert max.max_([1]) == 1
