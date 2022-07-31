"""
1650. Lowest Common Ancestor of a Binary Tree III
Medium

956

30

Add to List

Share
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

 

Example 1:

Return lowest ancestor 
DFS - postorder

1. Navigate up towards the room from both nodes, one level at a time, building a list of nodes
When they both reach the root, check for overlap

If there is no overlap, or just return root 
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':


        p_set = set()
        q_set = set()

        p_node = p 
        q_node = q 

        while p_node.parent or q_node.parent:
            p_set.add(p_node)
            q_set.add(q_node)
            if p_node in q_set:
                return p_node

            if q_node in p_set:
                return q_node
            if p_node.parent:
                p_node = p_node.parent
            if q_node.parent:
                q_node = q_node.parent

        # Both at root 
        return q_node 

"""
Was correct. Another way to solve:
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        self.ans = None
        dfs(n1,n2):
            if n1.val == n2.val:
                self.ans = n1
                return 

            if n1.parent and n2.parent:
                dfs(n1.parent, n2.parent)
            elif n1.parent:
                dfs(n1.parent, n2)
            elif n2.parent:
                dfs(n1, n2.parent)

        dfs(p, q)
        return self.ans