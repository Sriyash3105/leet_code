class Solution:
    def pivotInteger(self, n: int) -> int:
        disc = (n*(n+1))//2
        x = sqrt(disc)
        if isinstance(x,float) and x.is_integer():
            return int(x)
        else:
            return -1    