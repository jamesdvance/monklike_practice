"""
472. Concatenated Words

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

Rephrase: Find and return words in a given list that are comprised of two or more other words in an array

1. Sort array by length of words
2. For each word, check each word from range len(checkword) - len(word) work together to become work 
3. Use a cache to automatically get a check if a word already existed in the word

This would work fine if we were capped at two words. Instead in a brute force solution, will have to iteratively check each word 
with a size big enough

datastructure: A queue of words of partially unmatched words or something

And words can repeat 
"""

"""
Discussion Solution 1: DFS
"""
from collections import lru_cache
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    	d = set(words)

    	@lru_cache
    	def dfs(word):
    		for i in range(1, len(word)):
    			prefix = word[:i]
    			suffix=word[i:]

    			if prefix in d and suffix in d:
    				return True 

    			if prefix in d and dfs(suffix):
    				return True 

    			if suffix in d and dfs(prefix):
    				return True 

    		return False

    	res = []
    	for word in words:
    		if dfs(word):
    			res.append(word)

    	return res

"""

"""