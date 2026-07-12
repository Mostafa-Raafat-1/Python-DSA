"""
Floyd's Cycle Detection Algorithm

Floyd's Cycle Detection (Tortoise and Hare) detects whether a
linked list contains a cycle using two pointers moving at
different speeds. If a cycle exists, this implementation also
finds and returns the node where the cycle begins.

Time Complexity
---------------
Cycle Detection     : O(n)
Find Cycle Entry    : O(n)

Space Complexity
----------------
O(1)

Technique
---------
- Uses a slow pointer that moves one step at a time.
- Uses a fast pointer that moves two steps at a time.
- If the pointers meet, reset one pointer to the head and move
  both one step at a time until they meet again.
- The second meeting point is the start of the cycle.
"""


from typing import Optional


class Node:
  def __init__(self,item):
    self.item = item
    self.next = None

def detect_cycle(head: Optional[Node]) -> Optional[Node]:
  slow = head
  fast = head
  
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
    if slow is fast:
      slow = head
      
      while slow is not fast:
        slow = slow.next
        fast = fast.next
      
      return slow
  
  return None