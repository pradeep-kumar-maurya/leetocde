class MinStack:
    def __init__(self):
        self.stack = []  # Stack to add and pop values
        self.top_index = -1  # index to refer the top element, pop element
        self.min_stack = []  # Stack to maintain the min elements based on the insertion and popping in self.stack

    def push(self, val: int) -> None:
        self.top_index += 1
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)  # first element of min_stack will be same as the first element of stack
        else:
            # If the val added to stack is <= min_stack[top-1] then add val to min_stack
            if val <= self.min_stack[self.top_index - 1]:
                self.min_stack.append(val)
            # Else, add min_stack[top-1] to min_stack[top] i.e. just append
            else:
                self.min_stack.append(self.min_stack[self.top_index - 1])

    def pop(self) -> None:
        # Pop from both the stacks i.e. stack and min_stack
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