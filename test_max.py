from max import max_


def test_list():
    assert max_([2, 1, 5, 4, 7]) == 7


def test_equal():
    assert max_([1, 1, 1, 1]) == 1


def test_empty():
    assert max_([1]) == 1
