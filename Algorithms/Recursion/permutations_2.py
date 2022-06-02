"""
Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Input: nums = [1,1,2]
Output:
[[1,1,2],
[1,2,1],
[2,1,1]]

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Rephrase: Given an integer list of numbers, which might include duplicates, return all possible unique permutations 

Input: List of integers. Output: List of lists of integers. Each inner list is a unique permutation

Data structures:
Recursive stack 
set for to determine if this number was used in the existing permutation or not 
or memoization of a function that takes the value, not the index . 

Pseudo: 

when does a duplicate happen? When the same recursion is implemented with the same value of pivot point
but instead of skipping the list entirely, should just add the current nums to the appended list and not do recursion

Example
[1,1,2]
permute[[],[1,1,2]] -> backgrack([1],[1,2]) -> backtrack([1,2],[1])
ret_list = [[1,2,1]]
permute([1],[1,2]) -> Returns None because its already seen this
permute([2],[1,1]) -> permute([2,1],[1]) 
ret_list = [[1,2,1],[2,1,1]] + nums... 


Example
[1,1,2]

[1] + permute([1,2]) -> [1] + permute([2]) returns [2] -> [1,1,2]
[1] + permute([1,2]) -> [2] + permute([1]) returns [1]  -> [1,2,1]
[2] + permute([1,1]) -> [1] + permute[1] returns [1] -> [2,1,1]

"""
#from functools import lru_cache
class Solution:
	def permuteUnique(self, nums: List[int]) -> List[List[int]]:
		perms_list = []
		if len(nums) == 1:
			return [nums]

		nums_orig = set()
		for i in range(len(nums)):
			if nums[i] not in nums_orig:
				loop_nums = list(nums) # deep copy

				loop_nums[i], loop_nums[0] = loop_nums[0], loop_nums[i]
				loop_perms = self.permuteUnique(loop_nums[1:])
				for j in range(len(loop_perms)):
					perms_list.append([nums[i]]+loop_perms[j])
			
			nums_orig.add(nums[i])

		return perms_list

