from copy import deepcopy
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_copy = deepcopy(points) #O(N)
        org_dist = [(point[0]**2+point[1]**2, point) for point in points_copy] #O(N)
        org_dist.sort(key=lambda x: x[0]) #O(NLogN)
        return [pair[1] for pair in org_dist][0:k] #O(N)


"""
Neetcode solution

Can avoid the full nlogn sorting in the solution above by using a min heap. 
Since we only need to return the first k items 

Heapify is an O(N) time algorithm. 
Popping from a heap is klogN
"""
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)
        res = []
        while k >0:
            dist,x,y =heapq.heappop(minHeap)
            res.append([x,y])
            k-=1

        return res