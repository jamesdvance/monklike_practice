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