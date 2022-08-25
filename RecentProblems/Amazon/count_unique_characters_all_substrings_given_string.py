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


Solutions
https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/2365561/Python%3A-O(26*N)

https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/2334046/O(N)-DP-Python-simple-method
"""

"""
Brute Force
1. Iterate through s s**2 times with a double-loop
2. Each time, return the total unique chars found in the substring. 
3. Cache results for a given substring
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
Optimized # 1
This solution keeps a cur value that both keeps getting incremented and keeps getting added to the final result.
In that way, its similar to the Meta problem "Subarray Sum Equals K", where the number of subarrays keeps getting both incremented and added to the result at each pass.
That's because we are counting *unique characters* so essentially the length of all unique strings needs to be constantly incremented
The key part of the solution is that Each additional character added, adds itself as a subarray, and a unique subarray going back to its last occurence 
The idea of an O(N) solution is we can iterate from 0 to n and there's enough information to calculate the total subarrays ending at each i 

"ABA" -> 8
"LEETCODE" -> 92

ABA
ans=0, curr=0, prev = {}
i =0, ch = A
prev = {A:[-1]}
curr = 1 
prev = {A: [-1, 0]}
ans = 1 
** A ** = 1 unique subarray
i =1 ch = B
prev = {A:[-1,0],B:[-1]}
curr = 1 + 1-(-1) = 3 
prev = {A:[-1,0],B:[-1:1]}
ans = 1 + 3 = 4 
** AB ** = A, B, AB unique subarrays with 4 unique characters total 
i = 2, ch =A
curr = 3 + (2-0) = 5
curr = 5 - (0-(-1)) = 4  Here, we've subtracted out the occurance of A before B because in all subarrays its not unique 
ans = 4 +4 = 8 
Finished



"""
class Solution:
	def uniqueLetterString(self,s:str)->int:
		ans,curr,prev = 0,0,defaultdict(list)
		for i, ch in enumerate(s):
			if len(prev[ch]) ==0: # this is the first occurance
				prev[ch].append(-1) # the second to last occurance was at -1. Everything between 0 and this string is a unique subarray for this char
			curr+= (1 if i==0 else i - prev[ch][-1]) # Current total unique strings in all subarrays at this index i needs to have all positions between now and last occurance of ch
			if len(prev[ch]) >1:
				curr -= (prev[ch][-1] - prev[ch][-2]) # We need to subtract the recent position before this from this position. So that all 
				# of those subarrays that we are counting now, do not get a count for this character between those positions
				# note, we *alread* subtracted out the counts from this position to the current position

			prev[ch].append(i)
			ans+=curr 
		return ans

"""
Optimized # 2 

"""
class Solution:
	def uniqueLetterString(self,s:str)->int:
		dp = [0] * (len(s)+1)
		m = defaultdict(lambda: [-1]) # default is -1 

		for i, c in enumerate(s):
			l = m[c] # total occurances of string so far. Defaults to [-1] 
			dp[i] = dp[i-1] # At least as many unique substrings in the current string as in the previous (we'll fix the case where cur string is a dupe below)
			dp[i]+=i-l[-1] # Adding length of chars between this one and its last occurance
			if len(l) >=2:
				dp[i] -= l[-1] - l[-2] # subtract distance between prev occurance and prev before that

			m[c].append(i) # update that list

		return sum(dp) # this holds the sum of all unique substrings at each i


