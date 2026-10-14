class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0 and n%2 == 0:
            temp = self.myPow(x,int(n/2))
            return temp*temp
        elif n > 0 and n%2 == 1:
            temp = self.myPow(x,int(n/2))
            return x*temp*temp
        else:
            temp = 1/self.myPow(x,-n)
            return temp  

        