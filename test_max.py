import max


def test_list():
    assert max.n_max([2, 1, 5, 4, 7]) == 7


def test_equal():
    assert max.n_max([1, 1, 1, 1]) == 1


def test_empty():
    assert max.n_max([1]) == 1