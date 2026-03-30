class MinStack:

    def __init__(self):
        self.min_array = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if not self.min_array:
            self.min_array.append(val)
        else:
            self.min_array.append(min(self.min_array[-1], val))
            

    def pop(self) -> None:
        del self.min_stack[-1]
        del self.min_array[-1]
        

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.min_array[-1]
        
