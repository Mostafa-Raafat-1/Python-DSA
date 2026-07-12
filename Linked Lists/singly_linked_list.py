"""
Singly Linked List

A singly linked list is a linear data structure where each node
stores a value and a reference to the next node. Unlike arrays,
elements are not stored in contiguous memory, allowing efficient
insertions and deletions without shifting elements.

Supported Operations
--------------------
Append      : O(n)
Reverse     : O(n)
Traversal   : O(n)

Implementation Details
----------------------
- Each node stores a value and a pointer to the next node.
- The list maintains a reference only to the head node.
- Appending traverses to the last node before inserting.
- Reversal is performed iteratively using three pointers:
  previous, current, and after.
"""


class SinglyNode:
    def __init__(self, item):
        self.item = item
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, item):
        # create a node
        node = SinglyNode(item=item)
        
        # if list is empty:
        if self.head is None:
            # assign node to head
            self.head = node
        
        # else:
        else:
            current = self.head
            # find last node
            while True:
                if current.next:
                    current = current.next
                else:
                    break

            # change its next to the address of the new node
            current.next = node
    
    def reverse(self):
        if self.head is None:
            return
        
        # handle cases where the length is 0 or 1
        
        # set previous to first element
        previous = self.head
        after = self.head.next
        
        self.head.next = None
        
        # loop through each element starting from the second one till the last element:
        while after:
            # current = current.next
            current = after
            
            # save its next for later use
            after = current.next
            
            # set its next to previous
            current.next = previous
            
            # previous = current
            previous = current
            
        self.head = previous

    def print(self):
        current = self.head
        
        while current:
            print(current.item)
            current = current.next

linked_list = SinglyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.reverse()
linked_list.print()