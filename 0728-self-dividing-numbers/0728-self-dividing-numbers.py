class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        res = []
        num = left
        while num <= right:
            if self.isSelfDividing(num):
                res.append(num)
            num+=1
        return res        
    def isSelfDividing(self,n):
        if n < 10:
            return True
        k = n
        while k:
            r = k%10
            if r == 0:
                return False
            if n%r != 0:
                return False  
            k = k//10
        return True              
        