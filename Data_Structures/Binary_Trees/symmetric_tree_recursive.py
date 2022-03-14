# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not root.right and not root.left:
            return True
        
        if not root.right or not root.left:
            return False
        
        left_child =root.left
        right_child=root.right
        # Build array
        self.left_dict = {0:[left_child.val]}
        self.right_dict = {0:[right_child.val]}
        self.getChildren(left_child, 'left',1)
        self.getChildren(right_child, 'right',1)
        right_rev = self.right_dict
        #for lvl in list(right_rev.keys()):
        #    right_rev[lvl].reverse()
        
        print(self.left_dict)
        print(right_rev)
        if self.left_dict == right_rev:
            return True
        else:
            return False
    
    def getChildren(self, node:TreeNode,side='left', level=0)->list:
        lvl_dict = getattr(self, side+"_dict")
        if level not in lvl_dict:
            lvl_dict[level] = []
           

        if node.left and node.right:
                if side=='left':
                    # left first
                    lvl_dict[level].append([(node.val, node.left.val), (node.val, node.right.val)])
                    setattr(self, side+"_dict", lvl_dict)
                    self.getChildren(node.left,side,level+1)
                    self.getChildren(node.right, side, level+1)
                else:
                    lvl_dict[level].append([(node.val, node.right.val), (node.val, node.left.val)])
                    setattr(self, side+"_dict", lvl_dict)
                    self.getChildren(node.right,side,level+1)
                    self.getChildren(node.left, side, level+1)
                    
        elif node.right:
                if side=='left':
                    # left first
                    lvl_dict[level].append([(node.val,None), (node.val, node.right.val)])
                    setattr(self, side+"_dict", lvl_dict)
                    self.getChildren(node.right, side, level+1)
                else:
                    lvl_dict[level].append([(node.val, node.right.val), (node.val, None)])
                    setattr(self, side+"_dict", lvl_dict)
                    self.getChildren(node.right,side,level+1)
                    
        elif node.left:
                if side=='left':
                    # left first
                    lvl_dict[level].append([(node.val, node.left.val), (node.val, None)])                       
                    setattr(self, side+"_dict", lvl_dict)
                    self.getChildren(node.left, side, level+1)
                else:
                    lvl_dict[level].append([(node.val, None), (node.val, node.left.val)])
                    setattr(self, side+"_dict", lvl_dict)
                    self.getChildren(node.left,side,level+1)