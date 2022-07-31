"""


Algorithm:
1. 
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort By first number
        intervals.sort(key=lambda x: x[0])
        # 
        ret_arr = []
        for interval in intervals:
            if not ret_arr or interval[0] > ret_arr[-1][1]:
                ret_arr.append(interval)
            else:
                ret_arr[-1][1] = max(ret_arr[-1][1], interval[1])

        return ret_arr
