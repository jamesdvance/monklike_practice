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
[1,3,3]
output 4


"""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
    	res =0
    	n = len(nums)
    	for r in range(n):
    		l,r = nums[i],nums[i]
    		for j in range(i,n):
    			l = min(l, nums[j]) # take the min of next available 
    			r = max(r,nums[j])
    			res += r-l 

    	return res 

"""
Explanation: 
Steps
1. Iterate over each number in nums
2. Iterate from that number to the end, taking the max and min of each number in the range
[1,4,5,3,2]/47
"""

"""
Optimized

Uses stack 
2. First, must understand that sum{ Max(subarray) - Min(subarray) } refactors into sum({Max(subarray)}) - sum(Min(subarray))
3. Now, we can get the min and max by passing over the list and building a monotonic stack in each case 
4. In order to do each of these loops efficiently in O(N) time, multiply a given minimum at some position i by the current smallest position - i 
and i - previous smallest position

"""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
    	min_sum =0 
    	max_sum =0 
    	stack = []
    	for j in range(n+1): # j is the range of 
    		while stack and (j==n or nums[stack[-1]] > nums[j]):
    			i = stack.pop() # index of the value which this is smaller than 
    			prev_smaller = stack[-1] if stack else -1
    			minsum+=nums[i] * (next_smaller - i) * (i-prev_smaller)
    		stack.append(next_smaller)

    	stack = [] 
    	while j 


    	return maxsum - minsum 










"""
Explanation
Intuition:
Data Structure

"""

