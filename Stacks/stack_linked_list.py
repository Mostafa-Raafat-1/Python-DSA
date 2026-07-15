"""
Stack (Linked List Implementation)

A stack is a linear data structure that follows the Last In,
First Out (LIFO) principle. This implementation uses a singly
linked list, where the head node represents the top of the stack,
allowing all operations to be performed in constant time.

Supported Operations
--------------------
Push        : O(1)
Pop         : O(1)
Peek        : O(1)
Is Empty    : O(1)

Implementation Details
----------------------
- Each node stores a value and a reference to the next node.
- The head node represents the top of the stack.
- Push inserts a new node at the head.
- Pop removes and returns the head node.
- Peek returns the head value without removing it.
- is_empty checks whether the head is None.
"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Stacks:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        self.head = ListNode(val=value, next=self.head)
    
    def pop(self):
        if self.head:
            value = self.head.val
            self.head = self.head.next
            return value

    def peek(self):
        if self.head:
            return self.head.val
    
    def is_empty(self) -> bool:
        return self.head is None