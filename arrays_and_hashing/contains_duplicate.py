# Memory: 8.2 MB•Time: 45ms•Submitted at: 04/08/2026 13:27
# Beats 7.01% in runtime, 2.26% in memory

# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Map approach, if value exists return false

        numbers = []

        for i in range(len(nums)):
            if nums[i] in numbers:
                return True
            else:
                numbers.append(nums[i])
        
        return False
