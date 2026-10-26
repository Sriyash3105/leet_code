class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            name, domain = s.lower().split('@')
            return name[0] + "*****" + name[-1] + '@' + domain

        digits = ""
        for char in s:
            if char.isdigit():
                digits += char

        local = "***-***-" + digits[-4:]
        extra = len(digits) - 10

        if extra == 0:
            return local
        return "+" + "*" * extra + "-" + local