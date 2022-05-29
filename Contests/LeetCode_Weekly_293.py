"""
5234. Find Resultant Array After Removing Anagrams

You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.

In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, 
and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.

Return words after performing all operations. It can be shown that selecting the indices for each operation 
in any arbitrary order will lead to the same result.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using 
all the original letters exactly once. For example, "dacb" is an anagram of "abdc".

Basically check if any adjacent strings are anograms and if so delete the latter

Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]
"""


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
    	"delete from words inplace"

    	if len(words)==1:
    		return words

    	i = 1
    	while i < len(words):
    		prev = sorted(words[i-1])
    		word = sorted(words[i])

    		if prev == word:
    			words.pop(i)
    		else:
    			i+=1

    	return words

"""
6064. Maximum Consecutive Floors Without Special Floors

Alice manages a company and has rented some floors of a building as office space. Alice has decided some of these floors should be special floors, used for relaxation only.

You are given two integers bottom and top, which denote that Alice has rented all the floors from bottom to top (inclusive). You are also given the integer array special, where special[i] denotes a special floor that Alice has designated for relaxation.

Return the maximum number of consecutive floors without a special floor.

Input: bottom = 2, top = 9, special = [4,6]
Output: 3
Explanation: The following are the ranges (inclusive) of consecutive floors without a special floor:
- (2, 3) with a total amount of 2 floors.
- (5, 5) with a total amount of 1 floor.
- (7, 9) with a total amount of 3 floors.
Therefore, we return the maximum number which is 3 floors.

-----------------------------------------------------------

Thoughts
* Why can't I just iterate once from bottom to top and keep a counter that gets zeroed out when the floor is in special?
* If I want to be faster, could iterate through special, subtracting each from prev and last

"""

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
    	special.sort()
    	max_range = max(special[0]-bottom, top-special[len(special)-1])
    	for i in range(1,len(special)):
    		max_range = max(special[i]-special[i-1]-1,max_range)

    	return max_range

"""
6065. Largest Combination With Bitwise AND Greater Than Zero

The bitwise AND of an array nums is the bitwise AND of all integers in nums.

For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
Also, for nums = [7], the bitwise AND is 7.
You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. 
Each number in candidates may only be used once in each combination.

Return the size of the largest combination of candidates with a bitwise AND greater than 0.

"""
class Solution:
    def largestCombination(self, candidates: List[int]) -> int: