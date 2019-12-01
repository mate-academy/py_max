import max


def test_list():
    assert max.max_item([2, 1, 5, 4, 7]) == 7


def test_equal():
    assert max.max_item([1, 1, 1, 1]) == 1


def test_empty():
    assert max.max_item([1]) == 1