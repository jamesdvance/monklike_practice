"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    	n = len(nums)
    	left_sum = [0] * n
    	right_sum = [0] * n 
    	ans = []

    	left_sum[0] = nums[0]
    	for i in range(1, n):
    		left_sum[i] = nums[i]*left_sum[i-1]

    	right_sum[n-1] = nums[n-1]
    	for i in range(n-2,-1,-1):
    		right_sum[i] = nums[i]*right_sum[i+1]

    	for i in range(n):
    		lprod = left_sum[i-1]  if i > 0 else 1
    		rprod = right_sum[i+1] if i <n-1 else 1
    		ans.append(lprod*rprod)

    	return ans


"""
Easier way to do the final iteration
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    	n = len(nums)
    	left_sum = [0] * n
    	right_sum = [0] * n 
    	ans = []

    	left_sum[0] = 1
    	for i in range(1, n):
    		left_sum[i] = nums[i-1]*left_sum[i-1]

    	right_sum[n-1] =1
    	for i in range(n-2,-1,-1):
    		right_sum[i] = nums[i+1]*right_sum[i+1]

    	for i in range(n):
    		ans.append(left_sum[i]*right_sum[i])

    	return ans