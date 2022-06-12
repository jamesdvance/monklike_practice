"""
One Edit Distance

Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.

Rephrase: Return a boolean indicating if two strings could be made equal by performing an operation on one digit

Inputs: Two strings of length 0 to 10**4. Output: boolean

Edge cases and examples: 
both null strings: s:"", t:"" -> True; s:"", t:"a" ->True; s:"", t:"ab" -> False; s:"adsfd", t:"adsfe" -> True
s:"adsfd", t:"adbfe" -> False; s:"adsfd", t:"adbfe" -> False; s:"adsfde", t:"adsfe" -> True;

Data structures
Dual pointer
Two pointer

Requirements: 
Look for a deletion if one string has length s+1
Look for a single replacement if strings have equal length 

Pseudocode: 

compare_length
if s.length > t.length:
	# make it so s is always shorter than t 
	# iterate through s and t simultaneously. Once you find character that is in t but not s, move t's pointer up one and continue. 
	If you find another mismatch, return false. 
	Otherwise, return true

if s.length == t.length:
	iterate through s and t. If you find a mismatch, incremment a counter. If you find another, return false. Otherwise return true

if the longest string has length 1, always return true
If the difference between string length > 1: return false

"cab"
"ad"
"""

class Solution:
	def isOneEditDistance(self, s: str, t: str) -> bool:
		len_s = len(s)
		len_t = len(t)

		if s==t:
			return False

		if len_s > len_t:
			s, t = t, s 
			len_t, len_s = len_s, len_t

		if max(len_s,len_t) <2:
			return True 
		if len_t-len_s>1:
			return False 
	
		for i in range(len_s):
			if s[i] != t[i]:
				if len_s ==len_t:
					return s[i+1:]==t[i+1:]

				else:
					return t[i+1:] == s[i:]

		return len_t == len_s+1

