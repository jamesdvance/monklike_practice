"""
Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Approach: 

Need to merge intervals in a non-overlapping inclusive way

Will need to capture the existing endpoints of each intervals.
Can build an array data structure with endpoints, but need to be able to specify 
If the gap between is an interval or gap between intervals. Makes sense to just build the final data structure

The obvious pattern is to iterate through the output, and search for the latest endpoint.
Makes sense to sort by the right interval then sort by the left interval. 


 [[1,3],[2,6],[8,10],[15,18]]


[[1,4],[0,2],[3,5]]
"""

class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:

		def sort_arr():
			pass

		# Sort by second index first
		intervals.sort(key=lambda x:x[1])

		sorted_intervals = [None]*len(intervals)

		right_bound = intervals[0][1]
		total_endings = 0
		same_start =0 
		same_end = 1
		for a in range(1,len(intervals)):
			
			if right_bound == intervals[a][1]:
				#intervals_chunk.append(intervals[a])
				same_end +=1

			elif right_bound != intervals[a][1]:
				#if same_end - same_start > 1:
				intervals_chunk = intervals[same_start:same_end]
				intervals_chunk.sort(key=lambda x:x[0])
				sorted_intervals[same_start:same_end] = intervals_chunk
				#else:
				#	sorted_intervals[a] = intervals[a]

				same_start = a
				same_end = a+1
				right_bound=intervals[a][1]


		intervals_chunk = intervals[same_start:same_end]
		intervals_chunk.sort(key=lambda x:x[0])
		sorted_intervals[same_start:same_end] = intervals_chunk
		intervals_chunk[same_start:same_end] = intervals_chunk

		unique_intervals = []

		i = 0
		while i < len(sorted_intervals):
			right = sorted_intervals[i][1]
			left = sorted_intervals[i][0]
			j = 1
			while i+j < len(sorted_intervals) \
				and right >= sorted_intervals[i+j][0]-1:
				left = min(left, sorted_intervals[i+j][0])
				right= sorted_intervals[i+j][1]
				j+=1

			unique_intervals.append([left, right])

			i=i+j

		return unique_intervals

"""
My sorting solution above got tripped up on an example problem of non-overlapping but adjacent intervals.
Still not sure why the given solution is incorrect. 

Leetcode had two solutions - graph and sorting
"""

"""
Leetcode Sorting

Sort by insertion.
"""



class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:

		# They sort by LEFT interval
		intervals.sort(key=lambda x: x[0])

		merged = []

		for interval in intervals:
			if not merged or merged[-1][1] < interval[0]:
				merged.append(interval)
			else:
				# Merging. The upper bound becomes highest of the two upper bounds
				merged[-1][1] = max(merged[-1][1], interval[1])

		return merged
				