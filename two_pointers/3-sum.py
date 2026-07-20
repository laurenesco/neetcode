# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        # Empty list case
        if len(nums) == 0:
            return result

        for i in range(len(nums) - 2):
            value = nums[i]

            # Once we hit positives, zero sum not possible
            if value > 0:
                break;

            # Skip duplicates
            if i > 0 and nums[i-1] == value:
                continue;

            # Set pointer at smallest and largest remaining digits
            l = i + 1
            r = len(nums) - 1

            # Check the sums!
            while l < r:
                threeSum = nums[l] + nums[r] + value

                # If the sum works
                if (threeSum == 0):
                    result.append([nums[l], nums[r], value])

                    # Increment 
                    if r > l:
                        r -= 1

                    if l < r:
                        l += 1

                    # Skip duplicates
                    if nums[r] == nums[r-1]:
                        print("DUPLICATE R")
                        while r > l and nums[r] == nums[r-1]:
                            r -= 1

                    # Skip duplicates
                    if nums[l] == nums[l+1]:
                        print("DUPLICATE L")
                        while l < r and nums[l] == nums[l+1]:
                            l += 1

                # If sum too large
                if threeSum > 0:
                    r -= 1

                # If sum too small
                if threeSum < 0:
                    l += 1

        return result
