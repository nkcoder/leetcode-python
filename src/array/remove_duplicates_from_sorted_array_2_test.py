from remove_duplicates_from_sorted_array_2 import remove_duplicates_from_sorted_array_2


def test_remove_duplicates_from_sorted_array_2():
    nums = [1, 1, 2]
    expected = [1, 1, 2]
    k = remove_duplicates_from_sorted_array_2(nums)
    assert k == 3
    assert expected == sorted(nums[:3])


def test_remove_duplicates_from_sorted_array_2_2():
    nums = [1, 1, 1, 2, 2, 3]
    expected = [1, 1, 2, 2, 3]
    k = remove_duplicates_from_sorted_array_2(nums)
    assert k == 5
    assert expected == sorted(nums[:5])


def test_remove_duplicates_from_sorted_array_2_3():
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    expected = [0, 0, 1, 1, 2, 3, 3]
    k = remove_duplicates_from_sorted_array_2(nums)
    assert k == 7
    assert expected == sorted(nums[:7])
