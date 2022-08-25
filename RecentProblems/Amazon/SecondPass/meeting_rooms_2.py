"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

[[7,10],[2,4]]
My answer => 1, expected 2 

"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort by meeting start time
        intervals.sort(key=lambda x: x[0])
        # Create a min heap
        h = [intervals[0][1]]
        heapq.heapify(h)
        for interval in intervals[1:]:
        # If this meeting starts before the one ending the earliest ends:
            if interval[0] >= h[0]:
                heapq.heappop(h)
            heapq.heappush(h,interval[1])

        return len(h)

    		