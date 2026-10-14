class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        indices = deque(range(len(tickets)))
        time = 0
        while indices:
            index = indices.popleft()
            tickets[index]-=1
            time+=1
            if tickets[index] == 0 and index == k:
                return time
            if tickets[index]>0:
                indices.append(index)
        return time            



        