"""
3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105


Rephrase: Return all unique triplet combinations in an array that add up to zero

Data structures:
two pointers

Input: nums = [0,0,0]
-1
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    	if len(nums) <3:
    		return []
    	
    	self.ret = set() 
    	nums.sort() # O(NLogN)

    	non_neg = False
    	i=0
    	for i in range(len(nums)):
    		if nums[i] > 0:
    			break 

    	if nums[i] < 0:
    		return []

    	tried = set()
    	for j in range(0,i):
    		if nums[j] not in tried:
    			tried.add(nums[j])
    			self.twoSum(nums[j]*-1, nums[j+1:])

    	return list(self.ret)

    def twoSum(self,tgt:int, nums:List[int]):
    	k, l = 0, len(nums)-1
    	while k <l:
    		if nums[k] + nums[l] == tgt: 
    			self.ret.add((tgt*-1, nums[k], nums[l]))
    			k+=1
    			l-=1
    		elif nums[k] + nums[l] < tgt:
    			k+=1
    		else:
    			l-=1
