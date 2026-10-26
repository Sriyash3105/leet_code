class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = ""
        count = 0
        for char in s:
            if char.isalnum():
                count += 1

        if count % k == 0:
            l = 0
            for char in s:
                if char.isalnum():
                    ans += char.upper()
                    l += 1
                    if l == k:
                        ans += '-'
                        l = 0
        else:
            r = count % k
            l = 0
            for char in s:
                if char.isalnum():
                    ans += char.upper()
                    if r:
                        r -= 1
                        if r == 0:
                            ans += '-'
                    else:
                        l += 1
                        if l == k:
                            ans += '-'
                            l = 0

        if ans and ans[-1] == '-':
            ans = ans[:-1]

        return ans