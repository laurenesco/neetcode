# Memory: 7.7 MB•Time: 27ms•Submitted at: 04/08/2026 13:44
# Beats 92.62% in runtime, 99.6% in memory

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Utilize set length to compare with list

        return len(nums) != len(set(nums))
