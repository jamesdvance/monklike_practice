import collections
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        """
        Approach:
            1. Traverse tree depth-first
            2. Return boolean if you encounter p or q
            3. LCA is node with p and q returned or either returned and the other equals the node
        
        Notes: this doesn't stop when it reaches an answer
        """

        def recurse_tree(current_node):

            if not current_node:
                return False 

            left = recurse_tree(current_node.left)

            right = recurse_tree(current_node.right)

            # is the current node p or q
            mid = current_node == p or current_node == q

            if mid + left + right >=2:
                self.ans = current_node 

            return mid or left or right 

        recurse_tree(root)

        return self.ans
