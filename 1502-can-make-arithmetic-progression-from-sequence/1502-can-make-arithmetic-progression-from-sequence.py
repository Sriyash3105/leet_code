class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        n = len(arr)
        if n <= 2:
            return True

        small = min(arr)
        big = max(arr)

        if (big - small) % (n - 1) != 0:
            return False

        diff = (big - small) // (n - 1)
        arr_set = set(arr)

        curr = small
        for i in range(n):
            if curr not in arr_set:
                return False
            curr += diff

        return True