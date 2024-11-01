def test_no_zero_input():
    from product_of_array_except_self import product_of_array_except_self 

    assert product_of_array_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_of_array_except_self([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert product_of_array_except_self([1, 2, 3, 4, 5, 6]) == [720, 360, 240, 180, 144, 120]

def test_zero_input():
    from product_of_array_except_self import product_of_array_except_self

    assert product_of_array_except_self([0, 2, 3, 4]) == [24, 0, 0, 0]
    assert product_of_array_except_self([1, 2, 3, 4, 5, 0]) == [0, 0, 0, 0, 0, 120]
    assert product_of_array_except_self([0, 0, 3, 4, 5, 6]) == [720, 720, 0, 0, 0, 0]