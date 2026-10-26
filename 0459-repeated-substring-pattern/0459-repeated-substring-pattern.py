class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s) 
        for idx in range(n // 2):
            if n % (idx + 1) == 0:
                k = n // (idx + 1)
                sub = s[:idx + 1]
                comp = sub * k
                
                if comp == s:
                    return True
                    
        return False