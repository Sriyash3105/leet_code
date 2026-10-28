class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen =  set()
        
        for i,e in enumerate(nums):
            if target - e in seen:
                return [nums.index(target-e),i]
            seen.add(e)    
        