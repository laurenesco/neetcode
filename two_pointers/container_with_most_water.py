# Memory: 7.7 MB•Time: 28ms•Submitted at: 05/08/2026 13:18
# Beats 100% in runtime, 100% in memory

# You are given an integer array heights where heights[i] represents the height of the ith bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        area = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            new_area = min(heights[l], heights[r]) * (r - l)

            area = area if new_area < area else new_area

            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1

        return area
