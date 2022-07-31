import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def calc_dist(x,y):
            return math.sqrt(x**2+y**2)

        point_dist= []
        for i in range(k):
            point_dist.append(( -1*calc_dist(points[i][0],points[i][1]),i))

        heapq.heapify(point_dist)
        for i,point in enumerate(points[k:]):
            dist = -1*calc_dist(point[0],point[1])
            if dist > point_dist[0][0]:
                heapq.heappushpop(point_dist,(dist,i))
            
        return [points[i] for _,i in point_dist]

