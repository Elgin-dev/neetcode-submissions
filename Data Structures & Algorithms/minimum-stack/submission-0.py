from collections import deque

class MinStack:

    def __init__(self):
        self.container = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.container.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        removed = self.container.pop()

        if removed == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.container[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]