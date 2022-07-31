"""
253. Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.


Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106

Start: 3:12
End: 3:40

Rephrase: Return number of conference rooms where that means: number of times the intervals overlap

inputs: List of integer lists
outputs: integer

[[0:5], [10,15]]-> 1

[[0,4],[4,10]] -> 1 ? 

[[2,8],[2,3], [3,4], [3,6],[5,12], [7,10]]-> 3

[1,5],[1,2],

Data structures:
Could be done as a DFS problem 
Could be done by shorting based on index and iterating

Key logic: meeting rooms overlap when their endtime is greater than or equal to another's start time 
Total overlapping = total rooms minus ones who don't overlap
In example one, tehre are three meetings, and two don't overlap with each other whereas one meeting overlaps with two rooms
so 3 -1 =2
One can't be labeled as 'overlapper' multiple times and can't contribute to another overlapping 

So we probably want a hashmap
Duplicates are a problem in this solve method

Example:

[[0:5], [10,15]]

[[2,8],[2,3], [3,4], [3,6],[5,12], [7,10],]-> 5
1 i=0
2 i=1
3 i=2
4 i =3
5 i = 4

[[7,10],[2,4]] -> 
[[2,4],[7,10]]
1



[[2,8], [3,4], [5,6], [7,10],]-> 


[[9,10],[4,9],[4,17]]

[4,9],[4,17],[9,10] ->2
"""

class Solution:

	def minMeetingRooms(self, intervals: List[List[int]]) -> int:

		intervals.sort(key=lambda x: x[0]) # ONLogN
		rooms = 1

		for i in range(len(intervals)):
			j = i +1
			if  j < len(intervals) and intervals[j][0] <= intervals[i][1]:
				rooms+=1

		return rooms

"""
Above was a big fat fail

Solution 1 from Leetcode: Uses Priority Queues / Min Heap

1. 
"""
import heapq
class Solution:

	def minMeetingRooms(self, intervals: List[List[int]]) -> int:

		if len(intervals) ==0:
			return 0 

		free_rooms = []
		intervals.sort(key=lambda x:x[0])
		heapq.heappush(free_rooms, intervals[0][1])

		for i in intervals[1:]:
			if free_rooms[0] <= i[0]:
				heapq.heappop(free_rooms)

			heapq.heappush(free_rooms, i[1])

		return len(heapq)


"""
Solution 2 From Leetcode: Chronological Ordering

"""

class Solution:

	def minMeetingRooms(self, intervals: List[List[int]]) -> int:
		


