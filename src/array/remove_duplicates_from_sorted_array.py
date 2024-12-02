def remove_duplicates_from_sorted_array(nums: list[int]):
    i, j = 0, 1

    while i < len(nums) and j < len(nums):
        if nums[i] == nums[j]:
            j = j + 1
        else:
            nums[i + 1] = nums[j]
            i = i + 1
            j = j + 1

    return i + 1
