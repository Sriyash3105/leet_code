class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        ans = []
        idx = 0
        k = len(target)
        for i in range(n):
            if idx == len(target):
                return ans
            if i+1 in target:
                ans.append("Push")
                idx += 1
            else:
                ans.append("Push")
                ans.append("Pop")  
                  
        return ans        

