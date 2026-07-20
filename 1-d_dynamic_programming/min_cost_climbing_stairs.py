# Memory: 8 MB•Time: 28ms•Submitted at: 07/19/2026 17:54

# You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

# You may choose to start at the index 0 or the index 1 floor.

# Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        result = []

        for idx in range(len(cost)):
            if idx < 2:
                result.append(cost[idx])
            else:
                result.append(min(result[idx-1], result[idx-2]) + cost[idx])

        return min(result[-2], result[-1])
