# IN PROGRESS

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        # Empty list case
        if len(nums) == 0:
            return result

        # 1 triplet, != 0 case
        if len(nums) == 3 and sum(nums) != 0:
            return result

        # Loop with 2 pointers
        for i, value in enumerate(nums):
            # Once we hit positives, zero sum not possible
            if value >= 0:
                break;

            # Skip duplicates
            if i > 0 and nums[i-1] == value:
                continue;

            # Evaluate 2 sum against nums[i]
            for j in range(i + 1, len(nums) - 1):
                k = j + 1
                while k < len(nums):
                    if nums[j] + nums[k] == -(nums[i]):
                        result.append([nums[i], nums[j], nums[k]])
                    k += 1


        return result
