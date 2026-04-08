# Memory: 8.2 MB•Time: 45ms•Submitted at: 04/08/2026 13:27
# Beats 7.01% in runtime, 2.26% in memory

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numbers = []

        for i in range(len(nums)):
            if nums[i] in numbers:
                return True
            else:
                numbers.append(nums[i])
        
        return False
