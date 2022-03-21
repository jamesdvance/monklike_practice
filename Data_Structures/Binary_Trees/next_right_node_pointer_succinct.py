from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Need to group by order, and level
        # Level order, but using queue, and more succinct than my solution


        if not root:
            return root

        Q = deque([root])

        while Q:
            size = len(Q)

            for i in range(size): # iterate left to right
                node = Q.popleft() # FIFO


                if i < size -1: # don't add a next on the final node
                    node.next = Q[0] # 0 is the leftmost node

                if node.left:
                    Q.append(node.left)

                if node.right:
                    Q.append(node.right)

        return root 

