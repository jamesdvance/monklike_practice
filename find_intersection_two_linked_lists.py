# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA=headA
        nodeB=headB
        if nodeB==nodeA:
            return nodeB
        
        nodeA.prev = ListNode()
        nodeB.prev = ListNode()

        while (nodeA and nodeA.next) or  (nodeB and nodeB.next):
            # NodeA
            if nodeA and nodeA.next:
                nodeA.list ='A'
                old_nodeA = nodeA
                nodeA = old_nodeA.next
                if hasattr(nodeA, 'prev'):
                    return nodeA
                else:
                    nodeA.prev = old_nodeA
                    
            else:
                termA = nodeA
                    
            if nodeB and nodeB.next:
                # NodeB
                nodeB.list = 'B'
                old_nodeB = nodeB
                nodeB = old_nodeB.next   
                if hasattr(nodeB, 'prev'):
                    return nodeB
                else:
                    nodeB.prev = old_nodeB
                    
            else:
                termB = nodeB
            
        return