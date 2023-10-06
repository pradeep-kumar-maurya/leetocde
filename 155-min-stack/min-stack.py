class MinStack:
    def __init__(self):
        self.stack = []
        self.top_index = -1
        self.min_stack = []

    def push(self, val: int) -> None:
        self.top_index += 1
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            if val <= self.min_stack[self.top_index - 1]:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[self.top_index - 1])

    def pop(self) -> None:
        self.stack.pop(self.top_index)
        self.min_stack.pop(self.top_index)
        self.top_index -= 1

    def top(self) -> int:
        return self.stack[self.top_index]

    def getMin(self) -> int:
        return self.min_stack[self.top_index]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()