# Medium: https://leetcode.com/problems/longest-consecutive-sequence/description/



# Check each num if it can start a sequence (no left num), use a separate set to check
# T-O(n), M-O(n)
def longest_consecutive_sequence(nums: list[int]) -> int:
    nums_set = set(nums)
    longest_sequence = 0
    
    for n in nums:
        if n - 1 not in nums_set:
            length = 0
            while n + length in nums_set:
                length += 1
            if length > longest_sequence:
                longest_sequence = length
    
    return longest_sequence
            

    
    