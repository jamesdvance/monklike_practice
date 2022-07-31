"""
With Bucket Sort
O(4N) by my estimation
""" 


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    	if k==0:
    		return []

    	freq_arr = [[] for _ in range(len(nums)+1)]

    	counts = {}
    	for num in nums:
    		counts[num]=1+counts.get(num, 0)

    	for n, c in counts.items():
    		freq_arr[c].append(n)

    	res = []
    	for i in range(len(freq_arr)-1,0,-1):
    		for num in freq_arr[i]:
    			res.append(num)
    			if len(res)==k:
    				return res

"""
With Heap
O(Nlogk)
Space O(N+K)
"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    	if k==0:
    		return []

    	freq_arr = [[] for _ in range(len(nums)+1)]

    	counts = {}
    	for num in nums:
    		counts[num]=1+counts.get(num, 0)

    	return heapq.nlargest(k,counts.keys(), key=counts.get) # O(N)

