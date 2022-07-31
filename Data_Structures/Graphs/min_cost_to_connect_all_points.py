"""
Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
Kruskal's

[[2,-3],[-17,-8],[13,8],[-17,-15]] -> 53

[([2, -3], [-17, -8]), ([2, -3], [13, 8]), ([2, -3], [-17, -15]), ([-17, -8], [13, 8]), ([-17, -8], [-17, -15]), ([13, 8], [-17, -15])]


"""
from itertools import combinations
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        # create list of all edges in the graph and their weight
        edge_list = []
        for point1, point2 in combinations(points,2):
            dist = abs(point1[0]-point2[0])+abs(point1[1]-point2[1])
            edge_list.append([dist,[point1, point2]])

        edge_list.sort(key=lambda x:x[0])

        min_cost =0
        visited = set()
        edges= 0
        for edge in edge_list:
            point1 = tuple(edge[1][0])
            point2 = tuple(edge[1][1])
            if not (point1 in visited and point2 in visited):
                min_cost+=edge[0]
                edges+=1
                visited.add(point1)
                visited.add(point2)

            if edges == len(points)-1:
                break 

        return min_cost