"""
Substring With Largest Variance

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

Example 2:

Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.

Here's my buteforce solution, but this times out on Leetcode:
"""
from collections import Counter
class Solution:
    def largestVariance(self, s: str) -> int:
    	max_var = 0
    	len_s = len(s)
    	for i in range(len_s):
    		for j in range(i+1,len_s+1):
    			c = Counter(s[i:j])
    			max_var = max(max_var,
    				max(list(c.values()))-min(list(c.values())))

    	return max_var


"""
Looks likethis is dynamic programming (Kadane's) algorithm

Kadane's algorithm:
Initialize:
    max_so_far = INT_MIN
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far

Below are two solutions copied from the discussion

Should do 'Maximum Subarray' and 'Maximum Product Subarray' to prepare

"""


    def largestVariance(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        for a,b in itertools.permutations(counter,2): #N!
            max_subarray=0
            has_a,has_b = False,False
            remain_a,remain_b = counter[a],counter[b]
            for ch in s: #N**2
                if ch!=a and ch!=b:
                    continue
                if max_subarray<0 and remain_a!=0 and remain_b!=0:
                    max_subarray=0
                    has_a,has_b = False,False
                if ch==a: 
                    max_subarray+=1
                    remain_a-=1
                    has_a = True
                elif ch==b: 
                    max_subarray-=1
                    remain_b-=1
                    has_b = True
                if has_a and has_b:
                    res = max(res, max_subarray)
        return res



    def largestVariance(self, s: str) -> int:
        chr_idxs = defaultdict(lambda: [])
        for i,c in enumerate(s):
            chr_idxs[c].append(i)
        res = 0
        for a,b in itertools.combinations(chr_idxs,2):
            last_a,last_b=-1,-1 # at least one a one b
            prev_min,prev_max = defaultdict(int),defaultdict(int)
            cur = 0
            idxs = list(sorted(chr_idxs[a]+chr_idxs[b]))
            for ii,i in enumerate(idxs):
                if s[i]==a:
                    last_a=ii
                    cur+=1
                elif s[i]==b:
                    last_b=ii
                    cur-=1
                ii2 = min(last_a,last_b)
                if ii2>=0:
                    res = max(res, cur-prev_min[ii2-1], prev_max[ii2-1]-cur)
                prev_min[ii]=min(prev_min[ii-1],cur)
                prev_max[ii]=max(prev_max[ii-1],cur)
        return res