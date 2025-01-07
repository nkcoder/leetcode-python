from collections import defaultdict


def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    num_indices = defaultdict(list)
    for i, n in enumerate(nums):
        num_indices[n].append(i)

    for key, value in num_indices.items():
        if len(value) == 1:
            continue

        for i in range(len(value) - 1):
            if value[i + 1] - value[i] <= k:
                return True

    return False
