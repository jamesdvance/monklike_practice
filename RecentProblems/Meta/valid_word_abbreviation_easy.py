"""
408. Valid Word Abbreviation
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:
"apple", abbr = "a2e"
Input: word = 
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".

Start: 10:50
End: 11:05

Iterate through word and the abbrev. 
Once you get to a digit, find digit value
Then skip iterator for the word by the jump amount

Anytime there's a mistmach, return False

word = "internationalization", abbr = "i12iz4n""


Input
"internationalization"
"i5a11o1"

My solution: Fails on this lame edge case 
"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

    	i, j = 0,0 
    	nums_set = set(["1","2","3","4","5","6","7","8","9"])
    	zero_set = set(["0"])

    	while i < len(word) and j < len(abbr):
    		if abbr[j] in nums_set:
    			jump = abbr[j]
    			if j+1 < len(abbr):
    				j+=1
	    			while j < len(abbr) and abbr[j] in nums_set.union(zero_set):
	    				jump+=abbr[j]
	    				j+=1
    			jump = int(jump)
    			i+=jump 
    			if j == len(abbr) and i == len(word):
    				return True
    			elif i >= len(word) or j >= len(abbr):
    				return False
    		if word[i] != abbr[j]:
    			return False
    		else:
    			i+=1 
    			j+=1 

    	return True 


"""
Solution From Comments
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

    	i = j = 0 
    	m,n  = len(word), len(abbr)

    	while i < m and j < n:
    		if word[i] == abbr[j]:
    			i+=1
    			j+=1

    		elif abbr[j] == "0":
    			return False 
    		elif abbr[j].isnumeric():
    			k = j 
    			while k < n and abbr[k].isnumeric():
    				k+=1 # bring to one past last numeric 
    			i += int(abbr[j:k])
    			j = k
    		else:
    			return False  

    	return i == m and j == n