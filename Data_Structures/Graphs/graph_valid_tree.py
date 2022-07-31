"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a 
list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two 
vertices are connected by exactly one path. 
In other words, any connected graph without simple cycles is a tree.”
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

    	# Exactly one path means n -1 edges 
    	if len(edges) != n-1:
    		return False
    	# No simple cycles - check with union find
    	uf = UnionFind(n)
    	for edge in edges:
    		if uf.connected(edge[0],edge[1]):
    			return False 
    		uf.union(edge[0], edge[1])

    	return True


class UnionFind:

	def __init__(self, size):
		self.root=[i for i in range(size)]
		self.rank=[1]*size

	def find(self, x):
		if self.root[x] ==x:
			return x

		self.root[x] = self.find(self.root[x])
		return self.root[x]

	def union(self,x,y):
		rootX = self.find(x)
		rootY = self.find(y)
		if rootX != rootY:
			if self.rank[rootX] > self.rank[rootY]:
				self.root[rootY] = self.root[rootX]
			elif self.rank[rootX] < self.rank[rootY]:
				self.root[rootX] = self.root[rootY]
			else:
				self.root[rootY] = self.root[rootX]
				self.rank[rootX]+=1 

	def connected(self,x,y):
		return self.find(x) == self.find(y)


