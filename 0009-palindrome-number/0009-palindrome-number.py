class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x<10:
            return True
        else:
            obj = str(x)
            l,r = 0,len(obj)-1
            while l<r:
                if obj[l] != obj[r]:
                    return False
                l+=1
                r-=1    
            return True
            
