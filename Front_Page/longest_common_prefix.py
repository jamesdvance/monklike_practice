"""
14. Longest Common Prefix
Easy

Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

# 1. Obvious Solution
# Yet beats 92.37% runtime, 72.37% memory

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # O(N)
        shortest= 201
        for i in range(len(strs)):
            shortest= min(shortest, len(strs[i]))

        # O(M)
        prefix = ""
        for i in range(shortest):
            # O(N) 
            val = strs[0][i]
            match = True
            for str_ in strs[1:]:
                if val != str_[i]:
                    match = False
                    break
            if not match:
                break
            else:
                prefix+=val
        
        return prefix