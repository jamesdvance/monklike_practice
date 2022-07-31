"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Uses Kadane's Algorithm

intialize with first -0 

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    	maxSub = nums[0]
    	curSum = 0

    	for n in nums:
    		if curSum < 0:
    			curSum = 0
    		curSum +=n
    		maxSub = max(maxSub, curSum)

    	return maxSum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = arr_max = nums[0]
        for num in nums[1:]:
            if curr_max + num > num:
                curr_max += num
            else:
                curr_max = num
            
            arr_max = max(curr_max, arr_max)
                
        return cur_max