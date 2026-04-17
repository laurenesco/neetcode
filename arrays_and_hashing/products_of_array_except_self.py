# Memory: 7.7 MB•Time: 28ms•Submitted at: 04/17/2026 14:22
# Beats 100% in runtime, 100% in memory

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_sum = 1
        has_zeroes = 0

        # Get overall product
        for num in nums:
            total_sum *= num

            if num == 0:
                has_zeroes += 1

            if has_zeroes > 1:
                restultant = [0] * len(nums);
                return restultant

        resultant = [];

        # For each value in nums
        for i, num in enumerate(nums):
            
            if has_zeroes == 1 and num != 0:
                # Array with 0, this index not 0
                resultant.append(0)

            elif has_zeroes == 1 and num == 0:
                # Index = 0, recalculate result
                result = 1
                for num in nums:
                    if num != 0:
                        result *= num

                resultant.append(int(result))

            else:
                # Normal case
                resultant.append(int(total_sum / num))

        return resultant

