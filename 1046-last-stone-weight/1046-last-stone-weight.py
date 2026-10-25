class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        copy = [x*(-1) for x in stones]
        heapq.heapify(copy)
        while len(copy) != 1:
            a = heapq.heappop(copy)
            b = heapq.heappop(copy)
            if a != b:
                heapq.heappush(copy,a-b)
            elif not copy and (a==b):
                return 0    
            else:
                pass    
           
        return -1*copy[0]                            


