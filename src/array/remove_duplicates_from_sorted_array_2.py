# Medium:https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
# two pointers


def remove_duplicates_from_sorted_array_2(nums: list[int]) -> int:
    i, j = 0, 1
    duplicated = False

    while i < len(nums) and j < len(nums):
        if nums[i] == nums[j]:
            if duplicated:
                j = j + 1
            else:
                nums[i + 1] = nums[j]

                i = i + 1
                j = j + 1
                duplicated = True
        else:
            nums[i + 1] = nums[j]

            i = i + 1
            j = j + 1
            duplicated = False

    return i + 1
