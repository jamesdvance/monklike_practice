"""
680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.


Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

1 <= s.length <= 105
s consists of lowercase English letters.

Rephrase: Return true if s is a palindrome or would be after deleting 1 character from it 

Examples:
"abca"
stopping point = r =3
l =0 , r =3; a==a
l=1, r = 2 b!=c but s[1] == s[1] s0 r-=1 
l=1 r=1
"abc" -> False on first pass
"abbaq"

"accddcc"

"ebcbb

ececabbacec

bbcbe"


This one modifies, the one below and makes it slightly faster
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:

    	# two pointers, will advance by one pointer once their different

    	l,r = 0, len(s)-1 
    	unmatched = False
    	while l<r and l<=len(s)//2:
    		if s[l] != s[r] and not unmatched:
    			if s[r-1] == s[l] and s[l+1] == s[r]:

    				return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]

    			elif s[r-1] == s[l]:
    				r-=1 
    				unmatched=True 
    			elif s[l+1] == s[r]:
    				l+=1
    				unmatched=True 
    			else:
    				return False 

    		elif s[l] != s[r] and unmatched:
    			return False 
    		else:
    			l+=1
    			r-=1 

    	return True


"""
My solution below. It actually worked lol
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:

    	# two pointers, will advance by one pointer once their different

    	l,r = 0, len(s)-1 
    	unmatched = False
    	while l<r and l<=len(s)//2:
    		if s[l] != s[r]:
    			return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]
    		else:
    			l+=1
    			r-=1
    	return True

