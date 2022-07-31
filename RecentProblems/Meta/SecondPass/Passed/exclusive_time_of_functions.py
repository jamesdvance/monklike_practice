"""

"""
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        stack = []
        prev_time =0
        ret_arr=[0]*n
        for log in logs:
            task, pos, time = log.split(":")
            task, time = int(task), int(time)
            if pos == "start":
                if stack:
                    ret_arr[stack[-1]] += time-prev_time
                stack.append(task)
                prev_time = time 
            else:
                ret_arr[stack.pop()] += time - prev_time +1 
                prev_time = time +1 

        return ret_arr