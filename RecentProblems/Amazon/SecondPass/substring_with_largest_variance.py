"""
2272. Substring With Largest Variance

The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string.
 Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.

Steps:
1. iterate betwen every permutation of a,b
2.Then iterate over every individual string
3. Keep running subarray tally. If we've seen each char in a pair of chars, check if current var is the max 
"""
class Solution:
    def largestVariance(self, s: str) -> int:
    	counter = Counter(s) #O(N)
    	ans = 0 
    	# check every combination
    	for a,b in combinations(counter.keys(), 2):  # O N choose 2
    		has_a = False 
    		has_b = False 
    		a_left = counter[a]
    		b_left = counter[b]
    		subarr_var = 0 
    		for ch in s:
    			if ch not in (a,b):
    				continue
    			elif subarr_var < 0 and a_left != 0 and b_left != 0:
    				subarr_var =0 
    				has_a,has_b = False, False

    			if ch == a:
    				subarr_var+=1 
    				a_left-=1
    				has_a=True

    			if ch==b:
    				subarr_var-=1
    				b_left-=1 
    				has_b=True

    			if has_a and has_b:
    				ans = max(subarr_var, ans)

    	return ans



