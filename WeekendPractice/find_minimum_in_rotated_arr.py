"""
153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array 
[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

Start: 2:24
Finish: Probably after break

Rephrase: A sorted array has been rotated.We don't know how many times. 
We need a modified binary search that finds the min element in O(LogN) time

Data structures: 
keep track of ranges

Algos: The fact that its rotated means that for any two indeces i,j where nums[i] < nums[j] nums[i] is the min of 
that subset of #'s 

Need to find the widest subarray that holds true of that property, and the first elem will be the min element


[3,4,5,1,2]
l=0,r = 4 mid = 2 (val = 5)
l=3, 4=5, mid = 3
return nums[mid]

[4,5,6,7,0,1,2]
l=0,r=6, mid =3 (val=7)
l=4, r=6, mid=5
return nums[mid]

[11,13,15,17]
l=0,r=3 mid=1 (val=13)

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, len(nums)-1
        # Find rotation point 
        while l <= r:
            mid = r+l//2
            if mid ==0 and nums[mid] < nums[n-1]:
                return nums[0]
            elif mid ==0:
                l+=1
                # keep looking for the edge
            elif nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[0] \
                and nums[mid] > nums[r]: # rotation after mid and before r 
                l = mid+1
            elif nums[mid] < nums[0] \
                and nums[mid] < nums[l]: # totation after l and before mid
                r = mid-1
            else: # This is an always increasing array 
                return nums[0]

        return nums[mid] # in case length 1

