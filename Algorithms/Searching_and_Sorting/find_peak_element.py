"""
Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rephrased: Find the element which is bigger than its two neighbors. If its the last element in the array,
it only needs to be greater than the pnultimate element

Must run in Olog(n)

Will need stopping conditions and searching conditions

begin, end and mid

Pseudo:

def check_stopping

while start <= end:
    mid = start + (end-start)//2
    if check_stopping(nums[start]):
        return start
    else:
        start+=1
    check_stopping(nums[end])
    check_stopping(nums[mid])

[1,2,1,3,5,6,4]
s = 0, e = 6, mid=3, 3 <5
s = 4, e=6, mid = 5, 6>4
s = 4,e=5 mid = 4, 5 <6 
s = 5, e=5 , stopping criteria reached

"""
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end= n-1
        while start < end:
            mid = start + (end-start)//2
            if nums[mid]< nums[mid+1]:
                # rising slope
                start = mid+1
            else:
                # falling slope - peak is prior
                end = mid
        
        return start


# Explanation of theory https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=3
"""
Would have helped to have visualized the solution
[1,2,]
"""