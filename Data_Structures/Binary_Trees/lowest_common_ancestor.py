import collections
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Notes:
            * When one node is a descendant of another, the higher node is the LCA
            * root is the default LCA
            * visiting each node should be the maximum time
            * algorithm should terminate when we traverse the second node
            * root, left, right. Keep a queue of possible nodes. If both children are fully traversed without a check found, 
              remove current node from queue
            * once the node is found, return the node. The trouble with recursion is that we have to wait until the processes we've started have returned
            * could see three options: 
            ** implementing top-town, passing in whether node has been found and current root
            **implementing level-order traversal in a stack, and then returning once the nodes are found
            **recursive solution that returns a call to itself unless the two are found (bottom up)
        """

        self.found_p = False
        self.found_q = False
        self.p =p
        self.q = q
        self.root_node_stack = collections.deque()
            
        self.checkForNodes(root)

        return self.root_node_stack.popleft()

        
    def checkForNodes(self, root:Optional['TreeNode']):

        def check_found_both(self):
            return self.found_p and self.found_q

        self.root_node_stack.appendleft(root)
        if self.p==root:
            self.found_p =True
            
        if self.q==root:
            self.found_q = True
        
        
        left_has_p = False
        left_has_q = False
        right_has_p =False
        right_has_q = False
        
        if not check_found_both(self) and root.left:
            left_has_p, left_has_q = self.checkForNodes(root.left)

        if not check_found_both(self) and root.right:
            right_has_p, right_has_q = self.checkForNodes(root.right)
            
        has_p = False
        has_q = False
        if self.p == root or right_has_p or left_has_p:
            has_p = True
        if self.q == root or right_has_q or left_has_q:
            has_q = True

        if  not (has_p and has_q):
            self.root_node_stack.popleft()

        return has_p, has_q