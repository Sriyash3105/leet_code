class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
       
        for ch in b:
            if ch not in a:
                return -1
        r = (len(b)//len(a))
        count = 1       
        while count <= r +2:
            
            if b in a*count:
                return count
            else:
                count+=1    
        return -1    
        