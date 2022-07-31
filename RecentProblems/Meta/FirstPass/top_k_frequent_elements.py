"""
BucketSort Solution
"""
from collections import Counter 
class Solution:
	def topKFrequent(self, nums, k):
		bucket = [[] for _ in range(len(nums)+1)]
		for num, freq in Counter(nums).items():
			bucket[freq].append(num)
		bucket_long = [item for item_list in bucket for item in item_list]
		bucket_long.reverse()
		return bucket_long[:k]

"""
Heap SOlution
"""
from collections import Counter 
import heapq
class Solution:
	def topKFrequent(self, nums, k):
		count = Counter(nums)
		return heapq.nlargest(k, count.keys(), keys=count.get)
