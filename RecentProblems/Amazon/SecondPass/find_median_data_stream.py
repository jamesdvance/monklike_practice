# using two heaps
import heapq
class MedianFinder:

	def __init__(self):
		self.self.min_h = []
		self.self.max_h = []
		self.n = 0
		heapq.heapify(self.min_h)
		heapq.heapify(self.max_h)
		
	def addNum(self, num: int) -> None:
		if len(self.min_h) > self.max_h:
			while -1*self.min_h[0] > self.max_h[0] :
				val =heapq.heappop()
			heapq.heappush(self.max_h, -1*num)


		self.n+=1

	
	def findMedian(self) -> float:
		if n != 2 ==0:
			self.min_h[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Using heap