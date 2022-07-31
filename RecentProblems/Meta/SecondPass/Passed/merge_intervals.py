"""
1. Sort by first number in interval
2. iterate through, and append if starting number greater than last number
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        ret_arr = [] 
        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if not ret_arr or ret_arr[-1][1] < interval[0]:
                ret_arr.append(interval)
            else:
                ret_arr[-1][1] = max(ret_arr[-1][1], interval[1])

        return ret_arr