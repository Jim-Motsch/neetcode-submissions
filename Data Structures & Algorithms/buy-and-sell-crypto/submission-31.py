class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = prices[0]
        l = 0
        for r in range(len(prices)):
            minP = min(prices[r],minP)
            profit = prices[r]-minP
            maxP = max(profit, maxP)
        return maxP

