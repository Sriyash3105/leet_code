class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        actual = set()
        for i in range(n):
            actual.add(i+1)
        given = set(nums)
        return list(actual-given)    
        