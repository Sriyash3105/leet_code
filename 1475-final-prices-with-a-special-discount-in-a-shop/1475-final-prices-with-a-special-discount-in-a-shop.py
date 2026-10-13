class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        n = len(prices)
        discount = [0]*n
        stack = []
        for i,x in enumerate(prices):
            while stack and (x<=prices[stack[-1]]):
                past_index =  stack.pop()
                discount[past_index] = x

            stack.append(i) 
            res = []
        for i in range(len(prices)):
            res.append(prices[i]-discount[i])
        return res    

        