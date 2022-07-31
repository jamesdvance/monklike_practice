"""
Add Strings
"11"
"123"

Facebook interviewers like this question and propose it in four main variations. The choice of algorithm should be based on the input format:

Strings (the current problem). Use schoolbook digit-by-digit addition. Note, that to fit into constant space is not possible for languages with immutable strings, for example, for Java and Python. Here are two examples:

Add Binary: sum two binary strings.

Add Strings: sum two non-negative numbers in a string representation without converting them to integers directly.

Integers. Usually, the interviewer would ask you to implement a sum without using + and - operators. Use bit manipulation approach. Here is an example:

Sum of Two Integers: Sum two integers without using + and - operators.
Arrays. The same textbook addition. Here is an example:

Add to Array Form of Integer.
Linked Lists. Sentinel Head + Textbook Addition. Here are some examples:

Plus One.

Add Two Numbers.

Add Two Numbers II.
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
    	diff = len(num1) - len(num2)
    	if diff <0:
    		num2, num1 = num1, num2 
    		diff*=-1
    	ret_str = ""

    	carry =0 
    	for i in range(len(num1)-1,-1,-1):
    		j = i-diff
    		if j >=0:
    			sum1 = int(num2[j]) + int(num1[i]) +carry 
    		else:
    			sum1 = int(num1[i]) + carry
    		ret_str = str(sum1%10) + ret_str
    		carry = sum1//10

    	if carry:
    		ret_str = str(carry) +ret_str 

    	return ret_str



