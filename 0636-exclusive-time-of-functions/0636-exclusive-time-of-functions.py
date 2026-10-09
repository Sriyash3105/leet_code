class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        ans = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            func_id_str, func, time_str = log.split(":")
            func_id = int(func_id_str)
            time = int(time_str)

            if func == "start":
                if stack:
                    current = stack[-1]
                    ans[current] += time - prev_time
                    
                stack.append(func_id)
                prev_time = time
                
            else:
                current = stack.pop()
                ans[current] += time - prev_time + 1
                prev_time = time + 1    
                
        return ans