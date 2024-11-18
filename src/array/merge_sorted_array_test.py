from merge_sorted_array import merge_sorted_array

def test_merge_sorted_array():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge_sorted_array(nums1, 3, nums2, 3)
    assert(nums1 == [1, 2, 2, 3, 5, 6])

def test_merge_sorted_array_2nd_empty():
    nums1 = [1]
    nums2 = []
    merge_sorted_array(nums1, 1, nums2, 0)
    assert(nums1 == [1])

def test_merge_sorted_array_1st_empty():
    nums1 = [0]
    nums2 = [1]
    merge_sorted_array(nums1, 0, nums2, 1)
    assert(nums1 == [1])
