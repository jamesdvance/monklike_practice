class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <2:
            return len(s)

        left =0 
        curr_max =0 

        seen = {}
        for i in range(len(s)):
            if s[i] in seen:
                prev_idx = seen[s[i]]
                streak = i -left # len of prev streak
                if streak > curr_max:
                    curr_max = streak
                
                for j in range(left, prev_idx+1):
                    del seen[s[j]]
                left = prev_idx+1

            seen[s[i]] = i

        streak = i - left+1 # len of final streak
        if streak > curr_max:
            curr_max = streak

        return curr_max

"""
Leetcode solution
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0]*128

        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] # returns unicode code for a given character

            # Move left pointer forward until getting past the previous right index
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -=1
                left +=1

            res = max(res, right-left+1)
