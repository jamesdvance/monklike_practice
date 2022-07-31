"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

Start:2:03
Will end: 2:33

Rephrase: Basically, we need to confirm if we have a fully connected graph without a cycle? 
If that's it, the solution is below

O(E + V) time 
O(E + 4V) = O(E + V) space
"""
from collections import defaultdict
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseList = defaultdict(list) # directed adjacency list
        for relation in prerequisites:
            courseList[relation[1]].append(relation[0])

        # checked list (index = graph vertex)
        checked = [False] * numCourses
        path = [False] * numCourses

        for course in numCourses:
            if self.isCyclic(currCourse, courseList, checked, path):
                return False 

        return True

    def isCyclic(self, currCourse, courseList, checked, path):
        if checked[currCourse]:
            return False

        # if this path has already been marked, return True
        if path[currCourse]:
            return True 

        # mark we've seen this path before
        path[currCourse] = True 

        ret=False
        for child in courseList[currCourse]: # cycle through adjacency list
            ret = self.isCyclic(child, courseList,checked,path)
            if ret:
                break

        path[currCourse] = False #only wanted to check path for currCourse
        checked[currCourse] = True
        return ret 
