from roman_to_integer import roman_to_integer, roman_to_integer2


def test_roman_to_integer():
    assert roman_to_integer("III") == 3
    assert roman_to_integer("LVIII") == 58
    assert roman_to_integer("MCMXCIV") == 1994


def test_roman_to_integer2():
    assert roman_to_integer2("III") == 3
    assert roman_to_integer2("LVIII") == 58
    assert roman_to_integer2("MCMXCIV") == 1994
