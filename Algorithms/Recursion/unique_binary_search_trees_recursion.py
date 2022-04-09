# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate_trees(start, end)
            """ 
            Inputs:
            * Start - minimum value in tree / subtree
            * End - maximum value in tree / subtree
            """

            if start > end:
                return [None,] # Empty branch 

            all_trees = [] # all trees of the current key

            for i in range(start, end+1): #inclusive of n value
                left_trees = generate_trees(start, i-1) #create trees based on the next value in the range on the right

                right_trees = generate_trees(i+1,end) # create subtrees based on the next value on the left

                for l in left_trees:
                    for r in right_trees:
                        # Combine every combo of both subtrees
                        current_tree = TreeNode(val=i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees

        return generate_trees(1,n) if n else []



