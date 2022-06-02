"""
 Merge Intervals

 Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
 and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

Rephrase: Condense given list of lists into intervals that all overlap

Input: list of integer lists: Output: list of integer lists

Examples: [[1,4],[4,5]]; [[1,3],[4,5];  [[1,3],[2,6],[3,4],[4,6],[1,18]]

Data structures:
List to return new intervals

Pseudo:
sort list by starting point of interval
iterate_over_each_interval.
if the starting point is greater than the ending point of the last interval in the returning list, append tothe list
if starting point is less than or equal to the ending point ofthelast interval +1 update the returned interval with the new ending point

Examples
[[1,4],[4,5]]
ret_list = [1,4]
ret_list = [1,5]

[[1,3],[4,5]]
ret_list = [[1,3]]
ret_list = [[1,5]]

[[1,3],[2,6],[3,4],[4,6],[1,18]]
sorted_list = [[1,3],[1,18],[2,6],[3,4],[4,6]]
ret_list [[1,3]]
ret_list [[1,18]]

[[1,3],[2,6],[3,4],[4,6],[1,18]]
sorted_list = [[1,3],[1,5],[2,6],[3,4],[4,6]]
ret_list [[1,3]]
ret_list [[1,5]]
ret_list = [[1,6]]
ret_list = [[]]
"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0]) # sorted in ascending order by first key 
        ret_list = [intervals[0]]
        for ivl in intervals[1:]:
            if ivl[0] > ret_list[-1][1]:
                ret_list.append(ivl)
            elif ivl[1] > ret_list[-1][1]:
                ret_list[-1][1] = ivl[1]

        return ret_list

"""
Leetcode Solution 1: Treat as a Graph

1. Represent graph as an adjacency list. Insert directed edges in both directions to simulate edges
2 Perform graph traversals from arbitrary unvisited nodes until all nodes have been visited. Stored visited nodes in a set as to not duplicate effort
3. Consider each connected component, merging its intervals by constructing a new interval with start being the minimum start value, and end being the maximum end value

Is basically brute force
"""
import collections
class Solution:
    def overlap(self,a,b):
        return a[0] <= b[1] and b[0] <= a[1]

    def buildGraph(self, intervals):
        graph = collections.defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    # building adjacency list
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)

        return graph 

    def mergeNodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]

    def getComponents(self, graph, intervals):
        visited = set()
        comp_number =0 
        nodes_in_comp = collections.defaultdict(list)

        def markComponentDFS(start):
            stack =[start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node]) # same as stack+=graph[node]

        for interval in intervals:
            if tuple(interval) not in visited:
                markComponentDFS(interval)
                comp_number+=1 

        return nodes_in_comp, comp_number 

    def merge(self, intervals:List[List[int]])->List[List[int]]:
        # Build adjancency list of all intervals
        graph = self.buildGraph(intervals)
        # Traverse all connected nodes for a given interval, building a dictionary of each overalpping intervals
        nodes_in_comp, number_of_comps = self.getComponents(graph, intervals)

        return [self.mergeNodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]
