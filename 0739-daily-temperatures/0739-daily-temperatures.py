class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        days = [0]*len(temperatures)
        stack = []
        
        for i,x in enumerate(temperatures):
            while stack and (x>temperatures[stack[-1]]):
                past_index = stack.pop()
                days[past_index] = i - past_index
            stack.append(i)  
        return days      

        