"""

Let's define a function countUniqueChars(s) that returns the number of unique characters on s.

For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since 
they appear only once in s, therefore countUniqueChars(s) = 5.
Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. The test cases are generated 
such that the answer fits in a 32-bit integer.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

 Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

CHARACTERS MUST APPEAR ONLY ONCE TO BE COUNTED
"""

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        ans = 0
        cur = 0 
        prev = defaultdict(list) # holding the previous location of the character
        for i, c in enumerate(s):
            if len(prev[c])==0:
                prev[c].append(-1)
            if i==0:
                cur=1 # 1 subarray to start out with 
            else:
                cur+= i-prev[c][-1] # Each new ith starts i+1 new subarrays. The single extra character gets added to each subarray beteween i and prev


            if len(prev[c]) > 1:
                # cur is constantly updated (never re-initialized). Subarrays that crossed the area above but also crossed the section below should be 
                # subtracted out. Because these are no longer 'unique'
                cur -= (prev[c][-1] - prev[c][-2])

            ans+=cur 
            prev[c].append(i)

        return ans 


