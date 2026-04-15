# Memory: 7.7 MB•Time: 27ms•Submitted at: 04/15/2026 14:14
# Beats 100% in runtime, 99.97% in memory

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i, first in enumerate(nums):
            j = i + 1
            while j < len(nums):
                if first + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result
                j += 1

        return result;
                    
