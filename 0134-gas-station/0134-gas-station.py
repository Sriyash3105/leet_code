class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        if self.sum(gas)<self.sum(cost):
            return -1
        current = 0
        start = 0

        for i in range(n):
            current += gas[i]-cost[i]
            if current<0:
                start = i+1
                current = 0
        return start        


    def sum(self,arr):
        res = 0
        for i in arr:
            res+=i
        return res    
