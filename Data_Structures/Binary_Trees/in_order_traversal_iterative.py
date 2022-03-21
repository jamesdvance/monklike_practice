
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Aproach:
        1. Create an empty stack
        2. Initialize current node
        3. Push current node to stack and set current to current.left until current is null
        4. If current is NULL and stack is not empty then pop top item from stack, print the popped item
        """

        current = root
        stack = []

        while True:
            if current is not None:
                stack.append(current)

                current = current.left

            elif(stack):
                current = stack.pop()
                print(current.val)

                current = current.right

            else: # stack is empty and no current 
                break 
