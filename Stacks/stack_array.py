"""
Stack (Array Implementation)

A stack is a linear data structure that follows the Last In,
First Out (LIFO) principle. This implementation uses Python's
built-in list as the underlying dynamic array, where the end of
the list represents the top of the stack.

Supported Operations
--------------------
Push        : O(1) amortized
Pop         : O(1)
Peek        : O(1)
Is Empty    : O(1)

Implementation Details
----------------------
- Elements are stored in a Python list.
- The end of the list represents the top of the stack.
- Push uses append() to add an element.
- Pop removes and returns the last element.
- Peek returns the last element without removing it.
- is_empty checks whether the list is empty.
"""


class Stacks:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def is_empty(self) -> bool:
        return len(self.items) == 0