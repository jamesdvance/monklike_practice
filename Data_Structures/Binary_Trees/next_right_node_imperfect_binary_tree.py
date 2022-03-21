class Solution:

	def processChild(self, childNode, prev, leftmost):
		# if node doesn't exist, it just returns the childnode and leftmost
		if childNode:

			if prev:
				prev.next = childNode

			else:
				leftmost = childNode 

			prev = childNode 

		return prev, leftmost 


	def connect(self, root: Optional['Node'])->Optional['Node']:

		if not root:
			return root

		lefmost = root

		while leftmost:

			prev, curr = None, leftmost

			leftmost = None 

			while curr:

				prev, leftmost = self.processChild(curr.left, prev, leftmost)
				prev, leftmost = self.processChild(curr.right, prev, leftmost)

				curr = curr.next 

		return root 