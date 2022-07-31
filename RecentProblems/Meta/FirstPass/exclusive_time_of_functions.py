"""
 n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

stackdict = {}

"""
from collections import defaultdict
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = [] 
        res= [0]*n
        prev_time=0
        for log in logs:
            pid, pos, t = log.split(":")
            pid, t = int(pid),int(t)
            if pos=="start":
                if stack:
                    res[stack[-1]] += t-prev_time # end of previous function
                stack.append(pid)
                pid=t
            else: # End 
                res[stack.pop()] += t - prev_time +1 
                prev_time = time+1 

        return res