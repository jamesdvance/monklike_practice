"""
Solution 1: 
Modified Binary Search
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
    	left = 0
    	right = len(nums)-1
    	while left <= right:
    		pivot = left+(right-left)//2
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
    			if target > pivot_val and target <= nums[left]:
    				# target is after pivot, after rotation
    				right= pivot-1
    			else:
    				# target is less than pivot or target is > pivot val and before rotation
    				left = pivot+1

    	if pivot_val != target:
    		return -1
    	else:
    		return pivot

"""
Solution 2: 
Find pivot point, then binary search
"""

"""
Attempt # 2:

33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot 
index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Rephrase: Return location of a given item, in an array that was sorted, and then re-arranged once. 

Data strcutures: 
indexes of left and right

approach: 
iterate through nums looking for the rotation spot (where nums[i] < nums[i-1])
from there, choose where to search for the item


[4,5,6,1,2,3], tgt =2 -> 4
[1], tgt =0 -> -1 
[3,4,5,1,2], tgt = 6 -> -1

0,5 mid = 2 
3,5 mid=4
3,4 mid = 3 

4, 5 mid = 4
-> 4 

[4,5,6,7,0,1,2]
0
0, 6, mid = 3 
4,6, mid =5
6, 6 mid=5

[1,3],3

[3,1], 1
0,1 mid =1 

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # find inflection point
        l, r =0,len(nums)-1

        while l <=r: 
            mid = (l+r)//2 
            if mid ==0 and nums[mid] > nums[r]:
                l = mid+1
            elif mid >0 and nums[mid] < nums[mid-1]:
                break
            elif nums[mid] > nums[0]:
                l = mid +1
            else:
                r = mid -1

        if target == nums[mid]:
            return mid 
        elif mid ==0:
            l = 0 
            r = len(nums)-1
        elif target >= nums[0]:
            r=mid-1
            l = 0 
        else:
            l=mid+1  
            r = len(nums)-1 

        while l < r:
            mid = (l+r)//2 
            if nums[mid]==target:
                return mid 
            elif nums[mid] >target:
                r = mid-1
            else:
                l = mid+1 

        return -1




