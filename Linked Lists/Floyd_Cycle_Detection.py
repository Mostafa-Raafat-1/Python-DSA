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