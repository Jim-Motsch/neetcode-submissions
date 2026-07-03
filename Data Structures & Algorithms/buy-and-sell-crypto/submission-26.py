class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = 999
        profit = 0
        l = 0
        for r in range(len(prices)):
            minP = min(prices[r],minP)
            
            if profit <= maxP:
                l = r
            profit = prices[l] - minP
            maxP = max(profit, maxP)
        return maxP

