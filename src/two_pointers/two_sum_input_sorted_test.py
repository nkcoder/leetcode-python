from two_sum_input_sorted import two_sum_input_sorted


def test_two_sum_array_sorted():
    assert two_sum_input_sorted([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_input_sorted([2, 3, 4], 6) == [1, 3]
    assert two_sum_input_sorted([-1, 0], -1) == [1, 2]
    assert two_sum_input_sorted([0, 0, 3, 4], 0) == [1, 2]
    assert two_sum_input_sorted([0, 0, 3, 4], 3) == [1, 3]
    assert two_sum_input_sorted([0, 0, 3, 4], 4) == [1, 4]
    assert two_sum_input_sorted([0, 0, 3, 4], 7) == [3, 4]
