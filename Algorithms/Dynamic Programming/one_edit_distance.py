

"""
IS an extension of Longest Common Subsequence

Edit Distance
(Levenshtein distance)

Minimum number of operations required to convert word1 into word2

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    	n = len(word1)
    	m = len(word2)

    	if n*m == 0:
    		return n+m

    	# array to store history
    	cache = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]

    	# 
    	for j in range(len(word2)+1):
    		cache[len(word1)][j] = len(word2)-j

    	for i in range(len(word1)+1):
    		cache[i][len(word2)] = len(word1)-i

    	for i in range(n -1, -1, -1):
    		for j in range(m-1-1,-1):
    			if word1[i] == word2[j]:
    				cache[i][j] = cache[i+1][j+1]
    			else:
    				cache[i][j] = 1+min(cache[i+1][j], # 
    					cache[i][j+1], 
    					cache[i+1][j+1])

    	

