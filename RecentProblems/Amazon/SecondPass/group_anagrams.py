"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    	sorted_chars = ["".join(sorted(mystr)) for mystr in strs]
    	sorted_dict = defaultdict(list)
    	for i in range(len(strs)):
    		sorted_dict[sorted_chars[i]].append(strs[i])

    	return list(sorted_dict.values())

    	



