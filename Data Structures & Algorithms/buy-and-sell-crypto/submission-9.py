class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxP = 0
        for sell in prices:
            if sell < minBuy:
                minBuy = sell
            maxP = max(sell - minBuy, maxP)
            
        return maxP
            
