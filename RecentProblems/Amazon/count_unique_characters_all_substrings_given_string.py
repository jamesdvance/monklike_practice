"""
828. Count Unique Characters of All Substrings of a Given String

Let's define a function countUniqueChars(s) that returns the number of unique characters on s.

For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the 
unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
Given a string s, return the sum of countUniqueChars(t) where t is a substring of s.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.

Input: s = "LEETCODE"
Output: 92

Rephrase: returns the sum of the lengths of all unique substrings that appear exactly once in a string

Data structures: 

hash map for unique counts of strings
i j counters for dual iteration through string

Below 'brute force' just gets a time limit exceeded

AA

i =0, j=1
countUnq(A) -> 
"""
from collections import defaultdict, Counter
from functools import lru_cache
class Solution:
	def uniqueLetterString(self, s: str) -> int:
		ret =0 
		seen = set()

		@lru_cache
		def countUniqueChars(t):
			unq_lens = [len(c) for c,ct in Counter(t).items() if ct==1]
			return sum(unq_lens) if len(unq_lens) >0 else 0

		for i in range(len(s)):
			for j in range(i+1,len(s)+1):
				# since we're counting repeated substrings, 
				ret+=countUniqueChars(s[i:j])

		return ret 


"""
Correct Brute Force

"""



"""
Optimized
"""
class Solution:
	def uniqueLetterString(self, s):

		index = {c:[-1,-1] for c in ascii_uppercase}
		res = 0
		for i, c in enumerate(s):
			k,j=index[c] # -1 
			ret += (i-j) * (j-k) 

		for c in index:
			k, j = index[c]
			res += (len(s) - j) * (j-k) 

		return res % (10**9 + 7) 


"""
"""
# ord - returns an integer (Unicode code) representing a given character
class Solution:
	def uniqueLetterString(self, s):
		res = [0]*(len(s)+1) # 
		idxs = [[-1,-1]]*26
		for i,c in enumerate(s):
			code=ord(c)-ord('A')
			first,second=idxs[code]
			res[i+1]=1+res[i]+(i-1-second)-(second-first)
			idxs[code]=[second,i]

		return sum(res)%(10**9+7)

"""
Another solution that maybe doesn't rely on unicode vars 
"""

def uniqueLetterString(self, s):
	map1 = collections.defaultdict(lambda:-1) # last index for this letter
	map2 = collections.defaultdict(lambda:-1) # second to last index for this letter
	cur =0
	res =0
	for i,ch in enumerate(s):
		cur += (i-map1[ch]) - (map1[ch] - map2[ch])
		map2[ch] = map1[ch]
		map1[ch] =1 
		res += cur 

	return res