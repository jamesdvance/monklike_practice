"""
Working LinkedList with tuples. Does not meet time requirements

"""

class MyLinkedList:

    def __init__(self):
        pass

    def get(self, index: int) -> int:
        if hasattr(self, 'head'):
            next_node = self.head
        else:
            return -1
        
        itr = 1
        while next_node[1] and itr <= index:
            next_node = getattr(self, str(next_node[1]))
            itr+=1
            
        return next_node[0]

    def addAtHead(self, val: int) -> None:
        if hasattr(self, 'head'):
            prev = self.head
            self.head = (val,str(prev[0]))
            setattr(self, str(prev[0]), prev)
        else:
            self.head = (val, None)

    def addAtTail(self, val: int) -> None:
        next_node = self.head
        
        itr = 1
        while next_node[1]:
            next_node = getattr(self, str(next_node[1]))
            itr+=1
        
        if itr == 1:
            setattr(self, 'head', (next_node[0], str(val)))
        else:
            setattr(self, str(next_node[0]), (next_node[0], str(val)))
        setattr(self, str(val), (val,None))

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            if index == 1:
                prev = self.head
                prev_label='head'
            else:
                prev_int = self.get(index-1)
                prev = getattr(self, str(prev_int))
                prev_label=str(prev[0])

            if prev[1]:
                setattr(self, str(val), (val, str(prev[1])))
            else:
                setattr(self, str(val), (val, None))
            
            setattr(self, prev_label, (prev[0], str(val)))

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head[1]:
                next_node = getattr(self, str(self.head[1]))
                setattr(self, 'head', next_node)
            else:
                del self.head
        
        else:
            if index == 1:
                prev = self.head
                prev_label ='head'
            else:
                prev_int = self.get(index-1)
                prev = getattr(self, str(prev_int))
                prev_label=str(prev_int)
        
            del_node_int = self.get(index)
            del_node = getattr(self, str(del_node_int))
            if del_node[1]:
                setattr(self, prev_label, (prev[0], str(del_node[1])))
            else:
                setattr(self, prev_label, (prev[0], None))

            
"""
Solution LinkedList (uses objects)
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        # index steps needed 
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length, 
        # the node will not be inserted.
        if index > self.size:
            return
        
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        
        self.size += 1
        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = pred.next
        pred.next = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # delete pred.next 
        pred.next = pred.next.next