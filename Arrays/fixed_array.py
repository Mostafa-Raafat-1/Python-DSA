class FixedArray:
    def __init__(self, data: list):
        self.data=data
        self.capacity = len(data)
        self.size = 0
        for item in data:
            if item == None:
                break
            else:
                self.size +=1
    
        
    
    def get(self, index:int):
        return self.data[index]
    """
    Time Complexity = O(1)
    Space Complexity = O(1)
    """
    
    def set(self, index, value):
        if index >= self.size:
            return
        self.data[index] = value
    """
    Time Complexity = O(1)
    Space Complexity = O(1)
    """

    def insert_at(self, index, value):
        if index < 0 or index > self.size:
            return

        if self.size == self.capacity:
            return

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1
    
    """
    Time Complexity = O(n)
    Space Complexity = O(1)
    """
    
    def delete_at(self, index):
        if index >= self.size:
            return

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None
        self.size -= 1
            
    """
    Time Complexity = O(n)
    Space Complexity = O(1)
    """
            

fixed_array = FixedArray([0, 1, 2, None])
fixed_array.delete_at(0)
print(fixed_array.data)

