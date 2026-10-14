from collections import deque

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        
        queue = deque(students)
        sandwich = deque(sandwiches)
        count = 0
        while queue :
            if queue[0] == sandwich[0]:
                queue.popleft()
                sandwich.popleft()
                count = 0
            else:
                temp = queue.popleft()
                queue.append(temp)
                
                if count == len(queue):
                    return count
                count+=1     
        return count        