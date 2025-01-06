from happy_number import is_happy


def test_is_happy():
    assert is_happy(19)
    assert not is_happy(2)
