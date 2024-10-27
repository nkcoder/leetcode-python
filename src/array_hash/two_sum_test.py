from two_sum import two_sum, two_sum2, two_sum3


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]

def test_two_sum2():
    assert two_sum2([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum2([3, 2, 4], 6) == [1, 2]
    assert two_sum2([3, 3], 6) == [0, 1]

def test_two_sum3():
    assert two_sum3([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum3([3, 2, 4], 6) == [1, 2]
    assert two_sum3([3, 3], 6) == [0, 1]
    
