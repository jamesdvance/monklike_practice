from collections import Counter 
import heapq
class Solution:
	# Bucket sort
	def topKFrequent(self, nums, k):

		bucket = [[] for _ in range(len(nums)+1)]
		count = Counter(nums)
		for key,v in count.items():
			bucket[v].append(key)

		bucket_long = [ i for item in bucket for i in item]
		bucket_long.reverse()
		return bucket_long[:k]
