from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Return longest common subsequence of strings

        Thoughts: 
            * Need a pointer to beginning and ending of current string and comparison string
            * Recurrence relation: 
                * could work in opposite directions
                * Make one side smaller
                * Eliminate by checking if a string either matches 
            * Basecase:  l2 = len(text1) or l2 = len(text2) - longest
            * Makes sense to start with longest strings first then subset
        """
        
        @lru_cache(maxsize=None)
        def dp(i,j):
            if i ==0 and j==0:
                return 1 if text1[i] == text2[j] else 0
            elif i <0 or j <0:
                return 0
                
            return dp(i-1,j-1)+1 if text1[i] == text2[j] else max(dp(i-1,j), dp(i,j-1))
        
        return dp(len(text1)-1, len(text2)-1)