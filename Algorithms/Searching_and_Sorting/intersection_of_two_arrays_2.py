"""
Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Rephrase: Return the intersection of two arrays, where elements in the intersection appear as many times as they appear in both arrays

Inputs: two integer lists. Output: one integer list

Examples: [4,9,5], nums2 = [9,4,9,8,4]; [1,2,2,1], nums2 = [2,2]

Data structures:
dictionary to keep counter of number of times elem appeared

Pseudo:

iterate_through_longer_list
populate_list1_counts
iterate_through_shorter_list
    if in list1_counts, add to output array and decrement list1_counts
    if list1_counts ==0: do not add 

Examples: [4,9,5], nums2 = [9,4,9,8,4];
list1_counts = {4:1,9:1,5:1}
ret_list = [9,4]
"""
from typing import List
from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        list1_counts = defaultdict(lambda: 0)
        ret_list = []

        for num in nums1: 
            list1_counts[num]+=1

        for num in nums2:
            if list1_counts[num] >0:
                ret_list.append(num)
                list1_counts[num]-=1 

        return ret_list

"""
Leetcode Solution 2: Sorting

Sort nums1 and nums2
Initialize i,j,k to 0 
Move indices i thru nums1, j thru nums2
    increment i if nums1[i] is smaller
    increment j if nums2[j] is smaller
    if numbers, are same, copy number into nums[k] and increment all 3
return first k elements of nums1 (mega space saver)
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i = j = k =0
        while i <len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                nums1[k]= nums1[i]
                k+=1
                j+=1
                i+=1

        return nums1[:k]