class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price_arr = [] 
        min_price = float("inf")
        max_price = 0 
        max_price_arr = []
        for i in range(len(prices)):
            if prices[i] > min_price:
                min_price=  prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price 

        return max_profit
