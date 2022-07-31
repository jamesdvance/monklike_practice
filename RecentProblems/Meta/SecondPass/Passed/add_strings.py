
"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers
 (such as BigInteger). You must also not convert the inputs to integers directly.
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
    	l1 = len(num1)-1
    	l2 = len(num2)-1
    	if l2 > l1:
    		num1,num2 = num2,num1
    		l1,l2 = l2,l1
    	# l1 always greater than l2

    	rem =0
    	ret_sum = ""
    	while l1 >=0:
    		dig1 = num1[l1]
    		dig2 = 0 if l2 <0 else num2[l2]
    		cur_sum = int(dig1)+int(dig2)+rem 
    		ret_sum=str(cur_sum%10)+ret_sum
    		rem = cur_sum//10
    		l1-=1
    		l2-=1

    	if rem > 0:
    		ret_sum = str(rem)+ret_sum

    	return ret_sum



