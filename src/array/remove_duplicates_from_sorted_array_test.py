from remove_duplicates_from_sorted_array import remove_duplicates_from_sorted_array


def test_remove_duplicates_from_sorted_array():
    nums = [1, 1, 2]
    expected = [1, 2]
    k = remove_duplicates_from_sorted_array(nums)
    assert k == 2
    assert expected == sorted(nums[:2])


def test_remove_duplicates_from_sorted_array_2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected = [0, 1, 2, 3, 4]

    k = remove_duplicates_from_sorted_array(nums)
    assert k == 5
    assert expected == sorted(nums[:5])


def test_remove_duplicate_from_sorted_array_3():
    nums = [0, 0]
    expected = [0]

    k = remove_duplicates_from_sorted_array(nums)
    assert k == 1
    assert expected == sorted(nums[:1])
