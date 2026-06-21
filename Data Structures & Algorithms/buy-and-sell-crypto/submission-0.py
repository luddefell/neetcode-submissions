class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ### Intialize needed variables
        current_profit = 0
        current_buy = prices[0]
        current_sell = prices[0]
        global_profit = 0
        # if there is a new minimum we create a new subarray
        # if there is a new maximum we add to the profit of the current subarray
        for price in prices:
            if price >= current_sell:
                current_profit = current_profit + (price - current_sell)
                current_sell = price
            if price < current_buy:
                current_profit = 0
                current_sell = price
                current_buy = price
            if current_profit > global_profit:
                global_profit = current_profit
        return global_profit
