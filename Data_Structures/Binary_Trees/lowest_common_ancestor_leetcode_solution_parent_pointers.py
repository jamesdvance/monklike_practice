class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Approach:
        1. Start for the root node and traverse the node (depth-first, so we use a stack)
        2. Until finding p and q, keep storing parent pointers in a dictionary
        3. Once we have p and q, get all ancestors for p using the parent dictionary and add a set called ancestors
        4. Traverse all ancestors for node q. If the ancestor is also in the set for p while traversing upwards, this is the LCA
        """

        stack = [root]

        parent = {root: None}

        while p not in parent or q not in parent: # need both to stop the loop

            node = stack.pop()

            if node.left:
                parent[node.left] = node 
                stack.append(node.left)

            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set() 

        while p: # find the set of ancestors until you get to the root
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q