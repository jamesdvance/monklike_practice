# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self) -> None:
        self.ans = None


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # From the Leetcode solution

        
        def dfs(node)->bool:
            global ans

            if not node:
                return False
            
            l = dfs(node.left)
            r = dfs(node.right)

            mid = node.val == p.val or node.val == q.val

            if l + r + mid >= 2:
                self.ans = node

            return mid or l or r # found them somewhere in the stack
        
        dfs(root)
        return self.ans
            


            



# This implementation fails on the same use case
from queue import deque
from typing import Tuple, List
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 1. Traverse entire binary tree, adding parent. Save p and q with parent added in dictionary. 
        # 2. traverse up to root with q using parents. Create a 'visited' data structure
        # 3. Traverse upwards from p, as soon as reach a node not in visitors, return previous node. 

        # Traverse binary tree (iterative)

        pq = {"p":None, "q":None}
        stack = [root]
        visited = []

        parent = None
        while stack: 
            node = stack.pop()
            node.parent = parent
            visited.append(node)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

            if node.val == p.val:
                pq["p"]= p 

            if node.val == q.val:
                pq["q"] = q

            parent = node 
            
            if pq["q"] and pq["p"]:
                break

        q_visited = set([])
        while q.parent: 
            q_visited.add(q.val)
            q = q.parent

        q_visited.add(q.val) # add root node 

        while p.parent:
            if p.parent.val not in q_visited:
                return p 
            
            p = p.parent

        return p
            

             



# This has a bug, but works in most use cases
from queue import deque
from typing import Tuple, List
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # DFS, also returns a True/False
        
        def dfs(node, tgt)->Tuple[List[int], bool]:
            
            parent_list = []
            is_tgt = False
            
            if node.val == tgt.val:
                return [node.val], True
            
            if node.left:
                dfs_ans, dfs_tgt = dfs(node.left, tgt)
                if dfs_tgt:
                    return [node.val] + dfs_ans, dfs_tgt
                
            if node.right:
                dfs_ans, dfs_tgt = dfs(node.right, tgt)
                if dfs_tgt:
                    return [node.val] + dfs_ans, dfs_tgt
                
            return [node.val], False
        
        p_parents, _ = dfs(root, p)
        
        visited = set(p_parents)
        
        # level-order traversal
        
        que = deque([[root]])
        
        print(visited)
        
        if q.val in visited:
            return q
        
        while que:
            node_list = que.popleft()
            next_level = []
            cur_level = []
            unvisited = False
            
            for node in node_list:
                
                if node.val == q.val:
                    return node
                
                if node.val in visited:
                    cur_level.append(node)
                else:
                    unvisited = True
                
                if node.left: 
                    next_level.append(node.left)
                    
                if node.right:
                    next_level.append(node.right)
                    
            if unvisited:
                return cur_level[0]
        
            if next_level:
                que.append(next_level)
                
        return cur_level[-1]