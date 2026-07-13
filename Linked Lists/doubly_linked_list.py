"""
Doubly Linked List

A doubly linked list is a linear data structure where each node
stores a value along with references to both the previous and
the next node. Unlike arrays, elements are not stored in
contiguous memory, allowing efficient insertions and deletions
without shifting elements. Bidirectional links also enable
forward and backward traversal.

Supported Operations
--------------------
Append            : O(1)
Prepend           : O(1)
Delete (by value) : O(n)
Forward Traversal : O(n)
Backward Traversal: O(n)

Implementation Details
----------------------
- Each node stores a value, a previous pointer, and a next pointer.
- The list maintains references to both the head and tail nodes.
- Appending and prepending run in constant time using the tail and
  head pointers.
- Deletion reconnects neighboring nodes by updating both previous
  and next references.
- Supports traversal from both the head and the tail.
"""


class DoublyNode:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        node = DoublyNode(item)

        if self.tail is None:
            self.head = self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def prepend(self, item):
        node = DoublyNode(item)
        
        if self.head is None:
            self.head = self.tail = node
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node

    def delete(self, item):
        current = self.head
        
        while current:
            if current.item == item:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                return

            current = current.next

    def print_forward(self):
        current = self.head
        
        while current:
            print(current.item)
            current = current.next

    def print_backward(self):
        current = self.tail
        
        while current:
            print(current.item)
            current = current.prev