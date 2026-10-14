class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        l = 0
        var = tickets[k]
        time=0
        count = 0
        for idx,i in enumerate(tickets):
            if i>=var:
                time+=var
            else:
                time+=i
            if (idx > k) and (i>=var):   
                count += 1
        return time - count           


        