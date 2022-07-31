"""

You are given an integer array nums. The range of a 
subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

Data structures: 
hash map

Brute Force
"""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

    	i,j =0,1
    	cur_sum = []
    	for i in range(len(nums)):
    		j = i+1 
    		while j < len(nums):
    			if nums[j]