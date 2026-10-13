class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        if n == 1:
            return heights[0]
        stack = []
        maxArea = 0
        for i,h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                past_index = stack.pop()
                height = heights[past_index]
                if not stack:
                    width = i
                else:
                    width = i-stack[-1]-1
                maxArea = max(maxArea,height*width)
            stack.append(i) 
        while stack:
            past_index = stack.pop()
            height = heights[past_index]
            if not stack:
                width = n
            else:
                width = n - stack[-1] - 1
                
            maxArea = max(maxArea, height * width)
            
        return maxArea    
        return maxArea       