from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without repeating characters.

        Approach:
        1. If s in substr
        2. Will need to keep left and right pointers
        3. If starting at both ends, may be way to count until they meet
        4. Can iterate through existing pointers and use an ordered dictionary or list
        5. Start with left and right diff of 1, to the left. 
        6. If find a duplicate, record length before find, then set left to prev find
        7. replace existing with current index
        """
        if not s:
            return
        if len(s) ==1:
            return s 

        left =0 
        curr_max =0 

        seen = {}
        for i in range(len(s)):
            if s[i] in seen:
                prev_idx = seen[s[i]]
                streak = i -1-left # len of prev streak
                if streak > curr_max:
                    curr_max = streak
                
                for j in range(left, prev_idx+1):
                    del seen[s[j]]
                left = prev_idx+1

            seen[s[i]] = i

        streak = i - left # len of final streak
        if streak > curr_max:
            curr_max = streak

        return curr_max


