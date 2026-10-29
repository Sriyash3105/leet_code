class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        s= s.lstrip()
        if not s :
            return 0
        if not s[0].isdigit() and s[0] != '-' and s[0] != '+':
            return 0
        if s[0] == '+':
            ans = self.stringtonum(s[1:])
        elif s[0] == '-':
            ans = -1 * self.stringtonum(s[1:])
        else:
            ans = self.stringtonum(s)
        INT_MIN,INT_MAX = -2147483648,2147483647    
        if ans < INT_MIN: return INT_MIN
        if ans > INT_MAX: return INT_MAX
        return ans  

    def stringtonum(self,s : str):
        ans = 0 
        for ch in s:
            if not ch.isdigit():
                break
            else:
                ans = int(ch) + 10*ans

        return ans