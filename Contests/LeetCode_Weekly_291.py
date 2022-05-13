"""
Remove Digit From Number to Maximize Result
You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.
 
"""
class Solution:
	def removeDigit(self, number: str, digit: str) -> str:

		curMax =0
		for i in range(len(number)):
			n = number[i]
			if n == digit:
				curNum = int(number[0:i]+number[i+1:len(number)])
				if curNum > curMax:
					curMax = curNum

		return curMax

"""
6048. Minimum Consecutive Cards to Pick Up

You are given an integer array cards where cards[i] represents the value 
of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have 
a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.
"""

class Solution:
	def minimumCardPickup(self, cards: List[int]) -> int:
		"""
		The super simple solution is to have a dictionary with the index of the last index, and the shortest consecutive 
		pair so far
		"""
		longest_pick = len(cards)+1
		shortest_pick = longest_pick
		cards_picked = {}

		for i in range(len(cards)):
			card = cards[i]
			if card in cards_picked:
				if i - cards_picked[card] < shortest_pick:
					shortest_pick = i - cards_picked[card] +1 

			cards_picked[card] = i

		if shortest_pick == longest_pick:
			return -1 
		else:
			return shortest_pick


"""
6049. K Divisible Elements Subarrays
Given an integer array nums and two integers k and p, return the number of 
distinct subarrays which have at most k elements divisible by p.

Two arrays nums1 and nums2 are said to be distinct if:

They are of different lengths, or
There exists at least one index i where nums1[i] != nums2[i].
A subarray is defined as a non-empty contiguous sequence of elements in an array.
"""

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
    	"""
		1. It costs N time to iterate through and label. But can't because it doesn't solve the unique subarray
		2. The fact that we're counting unique reminds of recursion with memoization or a dictionary
		3. If we were to iterate through, how could determine that a num would no longer be part of any contigous subarray?
		4. If we have more than k divisible by p
		5. Should iterate through this once and turn into ones and zeros
    	"""
    	left = 0 
    	subs = 0
    	bin_nums = []
    	for num in nums:
    		bin_nums.append(1 if num%p == 0 else 0)
    	
    	for right in range(len(nums)):
    		if sum(nums[left:right]) <=k:
    			bin_nums+=1
    		else:
    			




