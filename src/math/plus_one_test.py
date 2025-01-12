from plus_one import plus_one

def test_plus_one():
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plus_one([9]) == [1, 0]
    assert plus_one([9, 9]) == [1, 0, 0]
