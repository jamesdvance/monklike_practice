"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.


Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
"""
from functools import lru_cache
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    	d = set(words)
    	ret_arr = []

    	@lru_cache
    	def dfs(word):
    		for i in range(1, len(word)+1):
    			pref = word[:i]
    			suff = word[i:]
    			if pref and suff in d:
    				return True
    			elif pref in d and dfs(suff):
    				return True
    			elif suff in d and dfs(pref):
    				return True 

    		return False

    	for word in words:
    		if dfs(word):
    			ret_arr.append(word)

    	return ret_arr
