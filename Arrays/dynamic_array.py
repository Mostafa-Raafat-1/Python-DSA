"""
Dynamic Array

A dynamic array is a resizable array that automatically increases
its capacity when it becomes full. This implementation starts with
a capacity of 1 and doubles its capacity whenever resizing is
required, ensuring efficient append operations.

Supported Operations
--------------------
Access      : O(1)
Append      : O(1) amortized
Insert      : O(n)
Delete      : O(n)
Pop         : O(1)
Resize      : O(n)

Implementation Details
----------------------
- Capacity doubles whenever the array becomes full.
- Existing elements are copied into the new array during resizing.
- Supports both positive and negative indexing for get(), insert(),
  and delete().
- Keeps track of both the current size and the allocated capacity.
"""


class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.data= [None] * self.capacity
        self.size = 0
    
    def append(self, value):
        if self.capacity == self.size:
            self._resize()
        self.data[self.size] = value
        self.size +=1
    
    def _resize(self):
        new_list = [None] * (self.capacity * 2)
        for i in range(self.size):
            new_list[i] = self.data[i]
        self.data = new_list
        self.capacity *= 2
        print(self.capacity)
    
    def get(self, index: int):
        if not (-self.size <= index < self.size):
            return
        
        return self.data[index]
    
    def pop(self):
        if self.size == 0:
            return
        
        element = self.data[self.size - 1]
        
        self.data[self.size - 1] = None
        self.size -=1
        
        return element
    
    def _convert_negative_index(self, index:int):
        return index + self.size

    def insert(self, index:int, value):
        is_negative_index = index < 0
        
        if index > self.size:
            return
        
        if is_negative_index and index * -1 > self.size + 1:
            return
        
        if self.size == self.capacity:
            self._resize()
            
        if is_negative_index:
            index = self._convert_negative_index(index=index)
        
        for i in range(self.size, index - 1, -1):
            self.data[i] = self.data[i- 1]
        
        self.data[index] = value
        self.size +=1
    
    def delete(self, index:int):
        is_negative_index = index < 0
        
        if index >= self.size:
            return
        
        if is_negative_index and index * -1 > self.size:
            return
        
        if is_negative_index:
            index = self._convert_negative_index(index=index)
        
        for i in range(index + 1, self.size):
            self.data[i - 1] = self.data[i]
        
        self.data[self.size - 1] = None
        
        self.size -=1
            
        


dynamic_array = DynamicArray()
dynamic_array.append(0)
dynamic_array.append(1)
dynamic_array.append(2)
dynamic_array.append(3)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)
dynamic_array.append(4)

print(dynamic_array.data)
print(dynamic_array.size)
"""
[1,2,3,4]
=>
[1,50,2,3,4]
---------------

"""
