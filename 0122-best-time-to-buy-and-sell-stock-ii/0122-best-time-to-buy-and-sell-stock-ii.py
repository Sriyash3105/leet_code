class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        Profit = 0
        for i in range(n-1):
            if prices[i+1]>prices[i] :
                Profit += prices[i+1]-prices[i]
    
        return Profit                