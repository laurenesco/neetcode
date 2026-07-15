# Memory: 8 MB•Time: 48ms•Submitted at: 07/15/2026 13:25
# Beats 100% in runtime, 97.2% in memory

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                tmp = prices[r] - prices[l]
                profit = max(profit, tmp)
            else:
                l = r
            r += 1

        return profit
