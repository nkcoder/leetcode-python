from add_binary import add_binary

def test_add_binary():
    assert add_binary("11", "1") == "100"
    assert add_binary("1010", "1011") == "10101"
    assert add_binary("111111", "11") == "1000010"
