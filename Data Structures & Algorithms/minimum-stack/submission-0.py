from collections import deque
class MinStack:

    def __init__(self):
        self.arr = deque([])

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or min_val>val:
            min_val = val
        self.arr.append([val, min_val])

    def pop(self) -> None:
        if self.arr:
            return self.arr.pop()
        else:
            return None

    def top(self) -> int:
        if self.arr:
            return self.arr[-1][0]
        return None

    def getMin(self) -> int:
        if self.arr:
            return self.arr[-1][1]
        return None
