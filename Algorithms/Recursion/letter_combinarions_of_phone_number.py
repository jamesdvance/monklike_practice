"""
Start: 5/13/2022 6:22
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Functional cases:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = "459"

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

-----------------------------------------------------

My thoughts: 
This is using the phonepad on the where each letter maps to 3 digits
Given each number, get their permutations

Obviously we're gonna need memoization

Going to need a dictionary of these

Base case: two lists of length 1

Functional cases: 
[]

"""
from functools import lru_cache

class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		if len(digits)<1:
			return []

		num_vals={"2":("a","b","c"),
			"3":("d","e","f"),
			"4":("g","h","i"),
			"5":("j","k","l"),
			"6":("g","h","i"),
			"7":("p","q","r"),
			"8":("t","u","v"),
			"9":("w","x","y","z")}

		if len(digits)<2:
			return num_vals[digits]

		# Recursive
		combined_list = []
		# O(N)
		@lru_cache
		def combine_strings(to_combine_list:tuple)->list:
			"to_combine_list is a list of lists"
			#nonlocal combined_list
			combos = len(to_combine_list)
			# base case
			if sum([len(inner_list) for inner_list \
				in to_combine_list]) == combos:
				return ["".join([inner_list[0] for \
					inner_list in listto_combine_list])]
			
			combined_list = []
			# Not base case
			for i in range(combos):
				inner_len = len(to_combine_list[i])
				if inner_len >1:
					for j in range(inner_len):
						combined_list += combine_strings(to_combine_list[0:i]\
							+[to_combine_list[i][j]]\
							+to_combine_list[i+1:combos])     
			return list(set(combined_list))

		return combine_strings(tuple([num_vals[s] for s in digits]))




"""
Leetcode solution
* Doesn't need cache, because tries every combo exactly once
* Rec f't returns nothing, just appends to global list
"""
class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		if len(digits)<1:
			return []

		num_vals={"2":"abc"
			"3":"def",
			"4":"ghi",
			"5":"jkl",
			"6":"ghi",
			"7":"pqrs",
			"8":"tuv",
			"9":"wxrz"}

		if len(digits)<2:
			return [n for n in num_vals[digits]]

		def backtrack(index, path):

			if len(path) == len(digits):
				combinations.append("".join(path))
				return 

			chars = num_vals[digits[index]]

			for char in chars:

				path.append(char)
				backtrack(index+1,path)
				path.pop() # remove last item, aka char


		combinations = []
		backtrack(0,[])
		return combinations