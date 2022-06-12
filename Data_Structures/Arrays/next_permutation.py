"""
Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater 
permutation of its integer. More formally, if all the permutations of the array are sorted in one container 
according to their lexicographical order, then the next permutation of that array is the permutation that 
follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Rephrase: Gven an array, return array in new order which is the lowest possible re-arrangement of the numbers
If it is already the highest possible re-arrangement,  return the sorted order, lowest to highest 

Input: An integer array, Output: an integer array

Examples: [2,5,4] -> [2,4,5];, [6,4,5] -> [6,5,4]; [1,2,3,4,5,6,5] -> [1,3,2,4,5,6,5];[1,5,3,3,5]-> [1,5,5,3,3]; [8,9,6,3,2,4] -> [9,8,6,3,2,4];
[10,9,4,3,5,4] ->[10,9,4,3,4,5]; [5,6,4,2] -> []

Datastructures: Can't use more than constant memory. So will need to use
An existing minimum, and its position. The n+1 minimum, and its position

Steps:
Iterate over array
track array's minimum so far 
If array is already sorted in descending order, return array sorted
Look for point where numbers start increasing. Hold a pointer to that point. Find the minimum which is larger than  among that list, and swap it to the first point of the list 
swap the smallest greater than the swap poin

"""
from typing import List
class Solution:
    def nextPermutation(self, nums:List[int])->List[int]:

        swap_point = -1
        incr_val = nums[0]
        cur_swap = []
        found_incr = False
        for i  in range(1,len(nums)):
            if nums[i] > nums[i-1] and not found_incr:
                found_incr=True
                swap_point = i
                incr_anch = nums[i-1]
                cur_swap = []
            elif nums[i] > nums[j]:
                if len(cur_swap)==0:
                    cur_swap[0]


        if swap_point == -1:
            nums.sort(reverse=True)
        
        return nums

"""
I failed 
LeetCode Answer

[8,9,6,3,2,4] -> [9,8,6,3,2,4];
[6,4,5] -> [6,5,4];
[1,2,3,4,5,6,5] -> [1,3,2,4,5,6,5];
[1,3,2] -> [2,1,3]; # requires more than one swap
i=1
j=2 : 2 <=3 -> j = 1
j=1 : 3 <=3 -> j = 0
j =0: 1 <= 3 0> j =-1
j =-1

Even this doesn't work in cases that require more than one swap
"""
from typing import List
class Solution:
    def nextPermutation(self, nums:List[int])->None:
        i = len(nums)-2
        while i >=0 and nums[i+1] <= nums[i]:
            i-=1
        
        if i>=0:
            j = len(nums)-1
            while nums[j] <= nums[i] and j>=0:
                j-=1
            
            nums[i], nums[j] = nums[j], nums[i]

        else:
            nums.sort()

    