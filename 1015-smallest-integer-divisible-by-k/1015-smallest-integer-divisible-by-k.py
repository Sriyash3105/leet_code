class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0:
            return -1
        if k%5 == 0:
            return -1
        remainder =  set()
        n=1
        res=1
        while True:
            r = n%k
            if r in remainder:
                return -1
            if not r:
                return res
            remainder.add(r)
            n = (10*r) + 1
            res+=1   
        return -1            
        