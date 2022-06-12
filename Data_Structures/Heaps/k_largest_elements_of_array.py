"""
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Under the hood this solution works by building a heap in linear time. As it builds the heap, 
it checks whether the heap is of size k. If so, it removes the smallest elements (since we want to return )
kth items. 

Is O(N) average  c ase 
"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

"""
Leetcode Solution
"""
# Same as my solution or use QuickSelect algorithm

"""
Neetcode Solution (QuickSelect)
QuickSelect - O(N) average time, worst time is O(N**2).
IS O(N) because its O(N) + O(N/2) + O(N/4)... which equals 2N aka O(N)

QuickSelect specifically can help find the nth largest value. Uses a pivot and sorts array so that 
every element to the left of it is less, every element to the right is greater

Calls itself recursively on the remaining array


"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k # is the kth-largest item if number is sorted ascended

        def quickSelect(l,r):
            pivot, p = nums[r], l 
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p +=1 # partition is in next position

            nums[p], nums[r] = pivot, nums[p]

            if p > k:   return quickSelect(l, p-1)
            elif p <k:  return quickSelect(p+1,r)
            else:       return nums[p]

        return quickSelect(0,len(nums)-1)







