# Memory: 8 MB•Time: 48ms•Submitted at: 07/15/2026 13:25
# Beats 100% in runtime, 97.2% in memory

# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

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
