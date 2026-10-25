class Solution:
    def isPossible(self, target: list[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        total = sum(target)
        max_heap = [-1*x for x in target]
        heapq.heapify(max_heap)
        while max_heap[0] != -1:
            max_element = -1*heapq.heappop(max_heap)
            rest =  total - max_element
            if rest == 1:
                return True
            if rest == 0 or max_element <= rest:
                return False
            new =  max_element % rest  
            if new == 0:
                return False  
            heapq.heappush(max_heap,-1*new)
            total = total -max_element + new  
        return True      

        