from remove_element import remove_element

def test_remove_element():
    nums = [3, 2, 2, 3]
    val = 3
    expected_nums = [2, 2]
    assert remove_element(nums, val) == 2
    assert sorted(expected_nums) == sorted(nums[0:2])

    nums2 = [0, 1, 2, 2 ,3, 0, 4, 2]
    val2 = 2
    expected_nums2 = [0, 0, 1, 3, 4]
    assert remove_element(nums2, val2) == 5
    assert sorted(expected_nums2) == sorted(nums2[0:5])
