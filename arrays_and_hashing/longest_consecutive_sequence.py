# Memory: 8 MB•Time: 27ms•Submitted at: 04/20/2026 12:57
# Beats 100% in runtime, 56.34% in nmemory

# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        tmp_result = 0

        # Empty list case
        if (len(nums) == 0):
            return 0

        values = set(nums)

        for num in values:
            if num - 1 not in values: 
                # Start of sequence
                curr_num = num
                tmp_result = 0

                # Check sequence length
                while curr_num + 1 in values:
                    tmp_result += 1
                    curr_num += 1
                    result = max(tmp_result, result)

        return result + 1
