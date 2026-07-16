"""
Queue Implementation (FIFO)

A queue is a linear data structure that follows the
First-In, First-Out (FIFO) principle. The first element
added to the queue is the first one removed.

This implementation uses a doubly linked list internally,
allowing constant-time insertion at the rear and removal
from the front.

Time Complexity
---------------
Enqueue          : O(1)
Dequeue          : O(1)
Peek             : O(1)
Is Empty         : O(1)
Length           : O(1)

Technique
---------
- Enqueue appends a new node to the tail of the linked list.
- Dequeue removes the head node and returns its value.
- Peek returns the front element without removing it.
- A size counter is maintained for constant-time length
  retrieval and efficient empty checks.
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

        if self.head is None:
            self.head = self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        if self.head is None:
            raise IndexError("pop from empty linked list")

        old_head = self.head

        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = old_head.next
            self.head.prev = None

        return old_head.item


class Queue:
    def __init__(self):
        self._items = DoublyLinkedList()
        self._size = 0

    def enqueue(self, item):
        self._items.append(item)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        self._size -= 1
        return self._items.pop_front()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")

        return self._items.head.item

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size
