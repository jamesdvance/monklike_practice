"""
Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.


Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rephrase: Find the first and last index of item repeated (or not) in array, given an ascending array

Input type: list. Output type integer list of size 2

Edge cases: [], target = 4; [1111], target = 2; [111111], target =1;, [1], target=1

Data structures: can do in place. 
Algorithms: Recursive binary search or iterative binary search

Pseudocode:

1. start with basic binary search looking for the element
2. If element not found, return [-1,-1]
3. If element found, break binary search loop and 
    start new binary search until start = elemen and end = elem
4. New binary search looks first for i,j where j = elem and i != elem 
and then for k,l where k=elem and l!= elem

"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) ==1:
            return [-1,-1] if nums[0]!=target else [0,0]
        elif len(nums)==0:
            return [-1,-1]

        l, r = 0, len(nums)-1
        found_elem = False
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                found_elem = True
                break 
            elif nums[m]>target:
                r = m-1 
            else:
                l = m+1

        if not found_elem:
            return [-1,-1]
        
        # binary search for ends
        orig_m = m
        orig_r = r
        r = m # l is only target if initial l was always target in which case its 0 anyways\
        #l = l-1 if l > 0 else 0
        while l <= r:
            m = l+(r-l)//2
            # Edge case - final
            if nums[m] == target:
                if m ==0 or nums[m-1] != target:
                    break 
                else:
                    r = m-1
            else:
                if nums[m+1] == target:
                    m = m+1
                    break 
                else:
                    l = m+1

        start = m 
        l = orig_m
        r = orig_r
        while l <=r:
            m = l+(r-l)//2
            if nums[m] == target:
                if m ==len(nums)-1 or nums[m+1] !=target:
                    break
                else:
                    l = m+1
            else:
                if nums[m-1] ==target:
                    m = m-1
                    break
                else:
                    r = m-1

        end = m 
        return [start, end] 


"""
Leetcode solution

"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        lower_bound = self.findBound(nums,target,True)
        if lower_bound == -1:
            return [-1,-1]

        upper_bound = self.findBound(nums,target,False)
        return [lower_bound, upper_bound]

    def findBound(self, nums: List[int], target:int, isFirst:bool)->int:
        N=len(nums)
        begin, end = 0, N-1
        while begin <= end:
            mid = (begin+end)//2
            if nums[mid]==target:
                if isFirst:
                    if mid == begin or nums[mid-1] < target:
                        return mid 

                    else:
                        end = mid-1

                else:
                    if mid == end or nums[mid+1] > target:
                        return mid 
                    else:
                        begin = mid+1
            elif nums[mid]>target:
                end = mid-1
            else:
                begin = mid+1

        return -1

 
