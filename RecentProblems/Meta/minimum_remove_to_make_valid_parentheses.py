"""
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"


Rephrase: Ensure each left parenthesis has a corresponding right paranethsis and vice versa

Input: Str
Output: str

Data structures:
stack to hold all rightward parentheses
Iterate once, filling the stack with rightward paranthesis once found. 

If there are still parens left, start iterating again, popping the leftmost parens fond, until the stack is empty


Examples
)ac(g)()(asdfd)) -> ac(g)()(asdfd)
[]



((())

))((

"())()((("

ret_str = ()()(((


O(2N) worse case
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
    	right_params = [] # stack 
    	rem_left = []

    	for i,s_i in enumerate(s):
    		if s_i=="(":
    			right_params.append(i)
    		elif s_i==")":
    			if right_params:
    				right_params.pop()
    			else:
    				rem_left.append(i)

    	ret_str = ""
    	for i in range(len(s)):
    		if i not in rem_left + right_params:
    			ret_str+=s[i]

    	return ret_str 

"""
Leetcode Solutions:

Stack + String Builder
Two Pass String Builder

Two Pass String Builder SOlution


"())()((("
first_pass_chars = []
0: balance = 1, open_seen = 1 
first_pass_chars = [(]
1: balance = 0, open_seen = 1 
first_pass_chars = [()]
2: balance = 0, open_seen =1 
first_pass_chars = [()]
3: balance = 1 open_seen = 2 
first_pass_chars = [()(]
4: balance = 0 open_seen = 2 
first_pass_chars = [()()]
5: balance = 1 open_seen = 3 
first_pass_chars = [()()(]
6: balance = 2 open_seen = 4
first_pass_chars = [()()((]
7: balance = 3 open_seen = 5
first_pass_chars = [()()(((]

open_to_keep = 5-3 =2 
first_pass_chars = [()()(((]

"""

class Solution:
	def minRemoveToMakeValid(self, s:str)->str:
		first_pass_chars = []
		balance = 0
		open_seen = 0
		for c in s:
			if c=="(":
				balance+=1
				open_seen+=1
			if c == ")":
				if balance == 0:
					continue 
				balance -=1 

			first_pass_chars.append(c)

		result = [] 
		open_to_keep = open_seen - balance 
		for c in first_pass_chars:
			if c == "(":
				open_to_keep -=1 
				if open_to_keep < 0:
					continue 

			result.append(c)

		return "".join(result)