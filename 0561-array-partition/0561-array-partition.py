class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        for i,x in enumerate(nums):
            if i % 2 ==0:
                s += x
        return s