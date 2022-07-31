"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.

"""
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    	dist = [] 
    	for i in range(k):
    		dist.append((-self.calc_distance(points[i],(0,0)),
    			i))
    	heapq.heapify(dist)
    	for i in range(k, len(points)):
    		loop_dist = -self.calc_distance(points[i], (0,0))
    		if dist[0][0] < loop_dist:
    			heapq.heappushpop(dist, (loop_dist, i))

    	return [points[i] for _, i in dist]

    def calc_distance(self, p1:list,p2:tuple)->float:
    	return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
