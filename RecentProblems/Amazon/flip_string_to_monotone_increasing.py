"""
926. Flip String to Monotone Increasing

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.

~~~~ Solve and here


Brute Force: 
Cycle through, flip all ones to zero in a copied array
cycle through again, flipping the last one to 
Cycle though n m times where m is the number of first zeros, seeing if leaving it in results in a properly sorted 
array or not 

Optimized (Looked at Solution):
Minmium

Start: 8:45
end: 9:00

"00110"
P=[0]
P=[0,0]
P=[0,0,0,1]
P=[0,0,0,1,2]
P=[0,0,0,1,2,2] vs 

ret_list = 
[ 0 + 5 - 0 - (5 - 0)] = [3]
[3, 0  + 5 - 1 - (5-0)] = [3,2]
[3,3,0 + 5 - 2 - (5-0)] = [3,3]

"01011"
P=[0,0,1,1,2,3]


n = 5
5 -2 =3

" How many 1's before index" to be flipped to 0 and how many 0s before index need to be fliiped to 1


"""



class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
    	P =[0]

    	for x in S: 
    		P.append(P[-1]+int(x)) # cumulative sum of the digits in X 


    	ret_list = []
    	for j in range(len(P)):
    		ret_list.append(P[j] + len(S)-j-(P[-1]-P[j]))

    	return min(ret_list)


