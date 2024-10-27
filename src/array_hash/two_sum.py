# Easy: https:// leetcode.com/problems/two-sum/

def two_sum(nums: list[int], target: int) -> list[int]:
    # the value is a set, because we might the same element twice in the input, for example: [3, 3]
    index_map: dict[int, set[int]] = {}

    for i in range(len(nums)):
        if nums[i] in index_map:
            index_map.get(nums[i]).add(i)
        else:
            index_map[nums[i]] = {i}

    nums.sort()
    i, j = 0, len(nums) - 1

    while i <= j:
        tmp_sum = nums[i] + nums[j]
        if tmp_sum == target:
            if index_map[nums[i]] == index_map[nums[j]]:
                return list(index_map[nums[i]])
            return list([index_map[nums[i]].pop(), index_map[nums[j]].pop()])
        elif tmp_sum > target:
            j -= 1
        else:
            i += 1
