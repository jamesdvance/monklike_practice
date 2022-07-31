# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
As you go, mark parent pointer.
Once you find the node, go k steps in every direction
"""
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        tgt_found = False
        stack = [(root, None)]
        # DFS
        while stack and not tgt_found:
            node, par = stack.pop()
            node.par = par
            if node.left:
                stack.append((node.left,node))
            if node.right:
                stack.append((node.right, node))

        # BFS
        ret_arr=[]
        q= deque([(target,0)])
        seen ={target}
        while q:
            node, d = q.popleft()
            if d==k:
                ret_arr.append(node.val)
            else:
                for neighbor in (node.left, node.right, node.par):
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        q.append((neighbor,d+1))

        return ret_arr
