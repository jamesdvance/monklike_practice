"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Algorithm:
Iterate inorder, creating a monotonic increasing stack of size k
Once we reach size n-k, we pop the largest out as we go 

Finally, we join back the stack into a string and return

"1432219", k = 3

"""

class Solution:

	def removeKdigits(self, num:str, k:int)->str:
		monostack = []

		for n in num:
			while monostack and k and n < monostack[-1]:
				monostack.pop()
				k-=1

			monostack.append(n)

		monostack = monostack[:-k] if k else monostack
		ret_str = "".join(monostack).lstrip("0")
		return ret_str if ret_str else "0"




