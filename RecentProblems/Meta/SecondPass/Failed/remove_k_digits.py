"""
Given string num representing a non-negative integer num, 
and an integer k, return the smallest possible integer after removing k digits from num.

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Plan: Iterate l to r. If a number is larger than the largest number in the stack, remove from stack. decrement k 


"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
    	mono_stack = [num[0]]

    	i =1
    	for n in num[1:]:
    		while k and mono_stack and n < mono_stack[-1]:
    			mono_stack.pop()
    			k-=1

    		mono_stack.append(n)

    	if k >0:
    		mono_stack = mono_stack[:-k]
    	
    	return str(int("".join(mono_stack))) if mono_stack else "0"



