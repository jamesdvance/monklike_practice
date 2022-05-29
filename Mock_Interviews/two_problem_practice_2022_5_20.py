"""
1. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that 
the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target 
if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
(0, 6)
7
(3, 6)
0

Input: nums = [9,0,1,2,6,7], target = 3
Output: -1
(0,5)
1
(3,5)
6
(3,4)
2
(3,3)
2


Input: nums = [2,3,4,6,0,1], target = 1
Output: 6


Thoughts:
1. Will use a binary search 
2. Rotation point = nums[i-1] > nums[i] < nums[i+1]

Last ditch effort: find the rotation point first, then the pivot will be easy-er
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
    	left = 0
    	right = len(nums)-1
    	while left <= right:
    		pivot = right+(right-left)//2
    		pivot_val = nums[pivot]
    		if pivot_val == target:
    			return pivot
    		if pivot_val >= nums[left]:
    			# rotation is after pivot
    			if target < pivot_val and target >= nums[left]:
    				# target is before pivot
    				left = pivot+1
    			else:
    				# target is after pivot. Target is > pivot val or is less but after rotation
    				right = pivot-1
    		else:
    			#elif pivot_val < nums[left]: 
    			# rotation is before pivot
    			if target < pivot_val and target < nums[right]:
    				# target is after pivot, after rotation
    				left = pivot+1
    			else:
    				# target is less than pivot or target is > pivot val and before rotation
    				right = pivot-1

    	if pivot_val != target:
    		return -1
    	else:
    		return pivot
"""
Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

"""