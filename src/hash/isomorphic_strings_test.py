from isomophic_strings import isomophic_strings

def test_isomophic_strings():
    isomophic_strings("egg", "tdd") == True
    isomophic_strings("foo", "bar") == False
    isomophic_strings("paper", "title") == True
