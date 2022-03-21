class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Need to group by order, and level
        # One opt is to have a dictionary property arranged by level
        # Root will always be followed by #
        # Inorder traversal makes the most sense
        # Being a perfect binary tree is important!
        # Another function makes sense to be able to pass in the level in a top-down way
        # SPACE: O[N+M+N]=~O[2N]; Time: O[N]
        if not root.left or root.right:
            return root.val

        levels = []
        def helper(root, level):
            if len(levels)==level:
                levels.append([])
                
            levels[level].append(node)
                
            if root.left:
                helper(root.left, level+1)
            if root.right:
                helper(root.right, level+1)
                
        helper(root, 0)
        
        # level order traversal finished
        for i in reversed(range(len(levels)-1)): # never gets to the node_level
            chi_levels = levels[i]
            par_levels = levels[i-1]
            for j in range(len(par_levels): # Par_levels should be 1/2 the size of chi_levels
                # Each list 
                par_levels[j]





