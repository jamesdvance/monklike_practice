"""
Word Break
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Naive Brute Force iterates over every start, end combo and checks if they are in the wordDict. This is 2^N

Two Optimized Versions - Recursion with Memoization and BFS

The Recursion takes the original version and adds memoization

With memoization, its n^^3 
"""
from typing import Set,List 
from collections import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        @lru_cache
        def word_break_memo(s, start):
            if start == len(s):
                return True 
            
            for end in range(start+1, len(s)+1):
                if s[start:end] in word_set and word_break_memo(s, end):
                    return True 
            
            return False 
        
        return word_break_memo(s, 0)



"""
BFS
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    	word_set = set(wordDict)
    	q= deque()
    	visited = set()

    	q.append(0)
    	while q:
    		start = q.popleft() 
    		if start in visited:
    			continue 

    		for end in range(start+1, len(s)+1):
    			if s[start:end] in word_set:
    				# Only add another start if we already have the word break
    				q.append(end)
    				if end == len(s):
    					return True 

    		visited.add(start)
    	return False 