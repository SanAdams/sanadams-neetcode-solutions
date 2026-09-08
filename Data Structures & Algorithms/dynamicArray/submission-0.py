class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = capacity * [0]

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.array[self.size] = n
        self.size += 1
        
    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]
        
    def resize(self) -> None:
        new_capacity = 2 * len(self.array)
        resized_array = [0] * new_capacity
        
        for i in range(len(self.array)):
            resized_array[i] = self.array[i]

        self.capacity = new_capacity
        self.array = resized_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.array)