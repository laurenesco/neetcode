# Memory: 8 MB•Time: 28ms•Submitted at: 07/19/2026 17:54

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        result = []

        for idx in range(len(cost)):
            if idx < 2:
                result.append(cost[idx])
            else:
                result.append(min(result[idx-1], result[idx-2]) + cost[idx])

        return min(result[-2], result[-1])
