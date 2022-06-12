"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string 
and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Rephrase: Return length of longest substring that is not more  than k characters apart aka require more than k changes

Inputs: S, string, and k 

Examples: "AABBAACCA", 2 -> 9; "AABCDA", 2 -> 2; "AAACCDFEGDEEWDJKAD", 2 -> 4; "AAEFEABDACA", 2 -> 3
Edge cases: if len(s) <= k, len(s). if k ==0, then its the longest repeating string

Data structures: 
Sliding window, aka two pointers
Hash map containing strings as keys and list with:
	last index, current streak, how many k-edits are already done

Pseudo
loop through s
add character to hashmap with index
if character has already been seen, check if previous index longer than k distance. If so increment current streak
if not set current streak to one
check current streak against max
swap index for current
continue

I completely misunderstood the question.

Ex: "ABACDAGAHA",1 -> 3
"""

class Solution:

	def characterReplacement(self, s:str, k:int)->int:
		if len(s) <=k:
			return len(s)

		streaks = {}
	
		res =1
		for i,c in enumerate(s):
			if c in streaks:
				prev_idx = streaks[c][0]
				if i - prev_idx-1 > c[2]:
					streaks[c][0]=i 
					streaks[c][1]=1 
					streaks[c][2]=1
				else:
					streaks[c][0]=i 
					streaks[c][1]+=i - prev_idx
					streaks[c][2]+=i - prev_idx-1
					res=max(streaks[c][1],res)

			else:
				streaks[c] =[i,1,k-1]

			if i >=len(s)-1-k:
				for key, val in streaks.items():
					if key != c: # already incremented
						streaks[key][1]+=1
						res = max(streaks[key][1], res)

		return res


