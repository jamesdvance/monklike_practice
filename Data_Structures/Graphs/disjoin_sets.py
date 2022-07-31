class UnionFind:
	"Uses QUICK FIND. Is O(N**2) overall complexity"
	def __init__(self, size):
		"O(N) to construct"
		self.root= [i for i in range(size)] # root array

	def find(self,x):
		""" Takes O(1) to get root of node """
		return self.root[x] # returns immediate parent of x 

	def union(self, x,y):
		""" Cycles through root array until finding rootY, 
		then sets its parent to parent of X 
		Takes O(N) to union two nodes
		"""
		rootX = self.find(x)
		rootY = self.find(y)
		if rootX != rootY:
			for i in range(len(self.root)):
				if self.root[i] == rootY:
					self.root[i] = rootX 

	def connected(self, x,y):
		"""Connected if share same parent
		Takes O(1) to check if connected
		"""
		return self.find(x) == self.find(y)


class UnionFind:
	"""Uses QUICK UNION
	Is generally more efficient than QUICK FIND 
	Is worst case O(N**2) overall complexity
	"""
	def __init__(self, size):
		""" O(N) to construct """
		self.root = [i for i in range(size)] # root array

	def find(self,x):
		""" Returns root node of set, x 
		O(N) to find root node
		"""
		while x != self.root[x] # root node is its own parent 
			x = self.root[x] # keep iterating until finding root 

		return x 

	def union(self, x, y):
		"""
		O(N) to union in worst case scenario. But depends on a structure 
		Overall complexity is <= N
		"""
		rootX = self.find(x) # find root of X 
		rootY = self.find(y) # find root of y
		if rootX != rootY:
			self.root[rootY] = rootX # set root of y to root of x 

	def connected(self, x, y):
		"""O(N) to find if connected"""
		"Connected if share same root "
		return self.find(x) == self.find(y)




class UnionFind:
	"""Uses UNION BY RANK
	Specifically orders root array by criteria
	Uses rank to choose parent node of certain criteria
	Store the 'height of a given vertex, and choose the root node of the vertex with greater height'
	"""
		def __init__(self,size):
			"O(N)"
			self.root = [i for i in range(size)]
			self.rank = [1] * size 

		def find(self, x):
			"O(LogN)"
			"Same root finding as QuickUnion"
			while x != self.root[x]
				x = self.root[x]

			return x 

		def union(self, x,y):
			"O(LogN)"
			rootX = self.find(x)
			rootY = self.find(y)
			if rootX != rootY:
				if self.rank[rootX] > self.rank[rootY]:
					self.root[rootY] = self.root[rootX]
				elif self.rank[rootX] < self.rank[RootY]:
					self.root[rootX]=rootY
				else: # if same 
					self.root[rootY] = rootX
					self.rank[rootX] +=1

		def connected(self, x, y):
			"O(LogN)"
			return self.find(x) == self.find(y)

class UnionFind:
	"""Uses PATH COMPRESSION OPTIMIZATION 
	After finding root node, update the parent node of all traversed elements 
	to their root node 
	When we search for root node of same element again, only need to traverse 
	two elemlents to find its root node. 
	Uses recursion to update the parent nodes of all traversed elements 
	Path compression optimizes the find function
	"""

	def __init__(self, size):
		"O(N)"
		self.root = [i for i in range(size)]

	def find(self,x):
		"O(LogN) avg time"
		if x == self.root[x]: # returns root
			return x 
		self.root[x]  = self.find(self.root[x]) # updates root of a given node 
		return self.root[x]

	def union(self, x, y):
		"Same as in QUICK UNION O(LogN) avg time"
		rootX = self.find(x)
		rootY = self.find(y)
		if rootX != rootY:
			self.root[rootY] = rootX

	def connected(self, x,y):
		"O(LogN) avg time"
		return self.find(x) == self.find(y)

class UnionFind:
	""" Uses Both PATH COMPRESSION and UNION BY RANK 

	"""

	def __init__(self, size):
		self.root = [i for i in range(size)]
		# initial rank is 1, because they start with no connections to other vertexes
		self.rank = [1]*size 

	def find(self, x):
		""" Uses Path Compression 
		is technically O(alpha(N))
		where alpha is the inverser ackerman function
		In practice, its assumed it is constant
		"""
		if x == self.root[x]:
			return x 
		self.root[x] = self.find(self.root[x])
		return self.root[x]

	def union(self,x,y):
		""" Uses union by rank
		is technically O(alpha(N))
		where alpha is the inverser ackerman function
		In practice, its assumed it is constant
		"""

		rootX = self.find(x)
		rootY = self.find(y)
		if rootX != rootY:
			if self.rank[rootX] > self.rank[rootY]:
				self.root[rootY] = self.root[rootX]
			elif self.rank[rootX] <self.rank[rootY]:
				self.root[rootX] = self.root[rootY]
			else:
				self.root[rootY] = self.root[rootX]
				self.rank[rootX]+=1

	def connected(self,x,y):
		"""
		is technically O(alpha(N))
		where alpha is the inverser ackerman function
		In practice, its assumed it is constant
		"""
		return self.find(x) == self.find(y)


	



