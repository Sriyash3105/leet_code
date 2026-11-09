class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        maxReach = 0
        for i,x in enumerate(nums):
            if i > maxReach:
                return False
            maxReach = max(maxReach,i+nums[i])
            if maxReach>n-1:
                return True
        return True      