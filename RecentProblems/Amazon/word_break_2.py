
"""
Word Break II
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a 
sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
"""

"""
We shouldn't memo at the start level 
Start adn end is ok, we can always check from there

"catsanddog"
(95%)
"""
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    	ret_list = [] 
    	word_dict = set(wordDict)
    	@lru_cache
    	def backtrack(start, cur_str):

    		if start == len(s):
    			ret_list.append(cur_str)
    			return True 

    		for end in range(start+1, len(s)+1):
    			if s[start:end] in word_dict:
    				new_str= cur_str+" "+s[start:end] if start >0 else s[start:end]
    				backtrack(end, new_str)

    	backtrack(0, "")
    	return ret_list	


        	