# Medium: https://leetcode.com/problems/top-k-frequent-elements/description/


# use hash for count => sort
# complexity: T-O(nlogn), S-O(n)
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    num_2_count: dict[int, int] = {}

    for n in nums:
        num_2_count[n] = num_2_count.get(n, 0) + 1

    count_2_num: dict[int, list] = {}
    for n, c in num_2_count.items():
        if c in count_2_num:
            count_2_num[c].append(n)
        else:
            count_2_num[c] = [n]

    count_sorted = sorted(list(count_2_num.keys()), reverse=True)

    result = []
    i = 0
    while len(result) < k and i < len(count_sorted):
        data = count_2_num[count_sorted[i]]
        result.extend(data)
        i += 1

    return result
