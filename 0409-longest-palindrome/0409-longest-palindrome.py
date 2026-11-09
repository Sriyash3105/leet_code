class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        even = 0
        odd = 0
        cnt = 0
        for i in s:
            count[i]+=1
        for k,v in count.items():
            if v % 2 == 0:
                even += v
            else:
                odd += v
                cnt+=1
        if odd == 0:
            return even
        else:
            return even+odd-cnt+1              

        