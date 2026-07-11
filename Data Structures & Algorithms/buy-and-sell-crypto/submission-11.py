class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        currP = 0
        minBuy = prices[0]
        for i in range(len(prices)):
            minBuy = min(prices[i],minBuy)
            currP = prices[i]- minBuy
            maxP = max(currP, maxP)
        return maxP
            