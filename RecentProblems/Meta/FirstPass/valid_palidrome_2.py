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
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.

Algorithm: 
1. Iterate over s from both sides simultaneously 
2. If the two aren't equal, check if either the final remaining equal each other by incrementing either left pointer or right pointer
3. 
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r  = 0 , len(s)-1 
        while l < r:
            if s[l]==s[r]:
                l+=1
                r-=1 
            else:
                return s[l:r]==s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]

        return True