"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""

"""
DP Solution:
If we know a palindrome exists at positions i and j, then a bigger neighboring one exists only if i-1 == j +1 
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
    	res = [0,0] # longest palindrome at s 
    	len_s = len(s)
    	for l in range(len(s)):
    		r = l 
    		# Move right until right does not equal l 
    		while r < len_s-1 and s[r+1] == s[l]:
    			r +=1 
    		# Move left until left does not equal 
    		# even palindrome
    		while l > 0 and r < len_s+1 and s[l-1] == s[r+1]:
    			l -= 1
    			r +=1 
    		if r- l  > res[1] - res[0]:
    			res = [l, r]

    	return r - l + 1 

"""
Start from center, work outwards (Neetcode solution)
O(N^2) - works outward from each 
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
    	res = ""
    	res_len =0
    	for i in range(len(s)):
    		# Check for odd-length palindrome
    		l, r = i, i 
    		while l >= 0 and r < len(s) and s[l] == s[r]:
    			if (r-l+1) > res_len:
    				res = s[l:r+1] # inclusive of r 
    				res_len = r - l + 1
    			l-=1 
    			r+=1 
    		# Check For even-length palindrome
    		l,r = i, i+1 
    		while l >= 0 and r < len(s) and s[l] == s[r]:
    			if (r-l+1) > res_len:
    				res = s[l:r+1]
    				res_len = r-l+1 
    			l-=1 # we're moving away from the middle
    			r+=1

    	return res_len 





