"""
2104. Sum of Subarray Ranges

You are given an integer array nums. The range of a subarray of nums is 
the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

Brute force - isolate each sub array, take the max and the min and add the difference to the result

Slightly better than brute force

Use two pointers, and keep looking for the min, max

Hints: 
1. Can you get the max/min of a certain subarray by using the max/min of a smaller subarray within it?
2. Notice the max of the subarray from index i to j is equal to max of (max of subarray from index i to j-1 and nums[j])


Brute Force

"""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
    	res =0
    	n = len(nums)
    	for r in range(n):
    		l,r = nums[i],nums[i]
    		for j in range(i,n):
    			l = min(l, nums[j]) # take the min of next available 
    			r = max(r,A[j])
    			res += r-l 

    	return res 

"""
Optimized

Uses stack 
"""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
    	res = 0 
    	inf = float('inf')
    	A = [-inf] + nums + [-inf]
    	s = [] 
    	for i,x in enumerate(A):
    		while s and A[s[-1]] > x:
    			j = s.pop()
    			k = s[-1]
    			res-=A[j] * ( i-j)*(j-k)
    		s.append(j)

    	A = [inf] + nums + [inf]
    	s= []
    	for i,x in enumerate(A):
    		while s and A[s[-1]] < x:
    			j = s.pop()
    			k = s[-1]
    			res += A[j] * (j-i) *(j-k)
    		s.append(i)
    	return res








class Solution:
	def subArrayRanges(self, arr:List[int])->int:

		n = len(arr)
		nge = [-1]*n 
		pge = [-1]*n 
		nse = [-1]*n
		pse = [-1]*n 

		st = [] 
		for i in range(n):
			while len(st) and arr[st[-1]] > arr[i]:
				