"""
Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Rephrase: Return list of all combinations of the given DISTINCT integers in all possible orders

Input: Integer list. Output: List of Integer Lists

Edge cases and examples: [1,2,3], [1],

Data structures:
Recursive stack 

Pseudo:

start left to right 
reach a base case at a list of size 1
iterate so that they all occupy a given position

@cache_decorator
function permute 
    if len(nums) = 1 return nums

    perms_list = []
    for i in nums.length:
        nums[0], nums[i]  = nums[i],nums[0]

        perms_list.append([nums[0]]+permute(nums)

    
    return perms_list

return permute(nums)

Trials:

[1,2,3]

i = 0, loop_nums = [1,2,3], inner stack 1 permute([2,3]), inner stack 2: permute([3])  -> [[1,2,3]]
i = 0, loop_nums = [1,2,3], inner stack 1 permute([3,2]), inner stack 2: permute([2])  -> [[1,3,2]]
i = 1 loop_nums [ 2,1,3], inner
"""
from typing import List
from functools import lru_cache
class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms_list = []
        if len(nums) == 1:
            return [nums]

        for i in range(len(nums)):
            loop_nums = list(nums) # deep copy
            loop_nums[i], loop_nums[0] = loop_nums[0], loop_nums[i]
            loop_perms = self.permute(loop_nums[1:])
            for j in range(len(loop_perms)):
                perms_list.append([nums[i]]+loop_perms[j])

        return perms_list

"""
Leetcode solution

Uses backtracking

"""

class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first =0):
            if first == n:
                output.append(nums[:])
            for i in range(first,n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                # swap back to position
                nums[first], nums[i] = nums[i], nums[first] 

        n = len(nums)
        output = []
        backtrack()
        return output


            