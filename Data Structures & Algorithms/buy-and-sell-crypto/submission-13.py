class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currP = 0
        maxP = 0
        currBuy = prices[0]
        for i in range(len(prices)):
            if currBuy > prices[i]:
                currBuy = prices[i]
                currP = currP + (currBuy - prices[i])
            else:
                currP = max(currP, prices[i]-currBuy)
            maxP = max(currP, maxP)
        return maxP