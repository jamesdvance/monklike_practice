"""
 There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
 You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 
"""

# Note - initial backtracking solution (below) is not efficient

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    	# 1. Build Adjacency list 
    	adj_list = defaultdict(list)
    	for course, pre_req in prerequisites:
    		adj_list[pre_req].append(course) # Ever course a course is a pre-req for


    	# 2. Iterate through each adjacency list. If any course includes itself, return False
    	def backtrack(course, path):
    		if path[course]:
    			return True 
    		path[course]=True 

    		cycle=False
    		for dep in adj_list[course]:
    			cycle = backtrack(dep, path)
    			if cycle:
    				break 

    		# have backtracked 
    		path[course]=False 
    		return cycle 

    	# 3. Call backtrack for every course in 0 -> numCourses
    	path = [False]*numCourses
    	for course_num in numCourses:
    		if backtrack(course,path):
    			return False 

    	return True



# PostOrder DFS
"""
Build on above, but eliminating visiting nodes multiple times in backtracking. Basically just memoization
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    	# 1. Build Adjacency list 
    	adj_list = defaultdict(list)
    	for course, pre_req in prerequisites:
    		adj_list[pre_req].append(course) # Ever course a course is a pre-req for

       	# 2. Iterate through each adjacency list. If any course includes itself, return False
    	def backtrack(course):
    		nonlocal path 
    		nonlocal checked
    		if checked[course]:
    			return False 

    		if path[course]:
    			return True 

    		path[course]=True
    		cycle=False
    		for dep in adj_list[course]:
    			cycle= backtrack(dep)
    			if cycle:
    				break 

    		path[course]=False 
    		checked[course]=True
    		return cycle 

    	path = [False]*numCourses
    	checked = [False]*numCourses
    	for i in range(numCourses):
    		if backtrack(i):
    			return False 

    	return True 

"""
Topological Sort
Faster than above in testing
O(E+V) time
O(E+V) space (adjacency list)
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    	order = []

    	adj_list = defaultdict(list)
    	indegree = [0]*numCourses

    	for course, pre_req in prerequisites:
    		adj_list[pre_req].append(course)
    		indegree[course]+=1 

    	# No indegrees - check 1 
    	q = deque([i for i in range(numCourses) if indegree[i]==0])
    	if not q:
    		return False 

    	while q:
    		course = q.popleft()
    		order.append(course)
    		for neighbor in adj_list[course]:
    			indegree[neighbor]-=1 
    			if indegree[neighbor]==0:
    				q.append(neighbor)

    	return len(order) == numCourses




