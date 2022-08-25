"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, 
return any of them. If it is impossible to finish all courses, return an empty array.


"""

"""
DFS / BAcktracking Solution
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:



"""
Topological Sort Solution
"""
from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    	result = []
    	# Edge cases
    	if not numCourses:
    		return [] 
    	if not prerequisites:
    		return [i for i in range(numCourses)]

    	# Adjacency list 
    	adj_list = defaultdict(list)
    	indegree = [0]*numCourses
    	for course, pre_req in prerequisites:
    		adj_list[pre_req].append(course)
    		indegree[course]+=1

    	q = deque([i for i in range(numCourses) if indegree[i]==0])
    	if not q:
    		return []

    	while q:
    		course = q.popleft()
    		result.append(course)
    		for neighbor in adj_list[course]:
    			indegree[neighbor]-=1

    			if indegree[neighbor]==0:
    				q.append(neighbor)


    	return result if len(result)==numCourses else []






