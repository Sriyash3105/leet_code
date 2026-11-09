class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        l,r = 0,n-1
        maxArea = 0
        while l<r:
            currentHeight = min(height[l],height[r])
            maxArea = max(maxArea,currentHeight*(r-l))
            if height[l]>height[r]:
                r-=1
            else:
                l+=1        
        return maxArea        