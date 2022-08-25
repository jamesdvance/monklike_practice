

"""
2262. Total Appeal of A String

The appeal of a string is the number of distinct characters found in the string.

For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.
Given a string s, return the total appeal of all of its substrings.

A substring is a contiguous sequence of characters within a string.


Input: s = "abbca"
Output: 28
Explanation: The following are the substrings of "abbca":
- Substrings of length 1: "a", "b", "b", "c", "a" have an appeal of 1, 1, 1, 1, and 1 respectively. The sum is 5.
- Substrings of length 2: "ab", "bb", "bc", "ca" have an appeal of 2, 1, 2, and 2 respectively. The sum is 7.
- Substrings of length 3: "abb", "bbc", "bca" have an appeal of 2, 2, and 3 respectively. The sum is 7.
- Substrings of length 4: "abbc", "bbca" have an appeal of 3 and 3 respectively. The sum is 6.
- Substrings of length 5: "abbca" has an appeal of 3. The sum is 3.
The total sum is 5 + 7 + 7 + 6 + 3 = 28.

"""
class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        prev = defaultdict(lambda:-1)
        for i in range(n):
        	if i ==0:
        		dp[i]=1 
        	else:
        		# All unique characters is the all in the iteration before plus i new subarrays (must be counted for each subarray) minus all the ones counted already
        		dp[i]=dp[i-1] + i - prev[s[i]]

        	prev[s[i]] = i

        return sum(dp) # we can sum it 

# Same answer, just real simple and less space


class Solution:
    def appealSum(self, s: str) -> int:
    	cur, res = 0,0 
    	prev = defaultdict(lambda: -1)
    	for i,c in enumerate(s):
    		cur+= i - prev[c][-1]
    		res+=cur 
    		prev[c]=i 

    	return res 

# Another Solution, using combinatorics
"""
Each charaacter appears in (i+1) * (n-i) substrings. But it doesn't contribute
 to substrings on the left of it who already include that charater. 
 To exclude the previously counted substrings we subtract out the previous position of thecharacter
"""
class Solution:
    def appealSum(self, s: str) -> int:
    	res, n, prev = 0, len(s), defaultdict(lambda:-1)
    	for i, c in enumerate(s):
    		res += (i-prev[c]) *(n-i)
    		prev[c] =i 
    	return res 
