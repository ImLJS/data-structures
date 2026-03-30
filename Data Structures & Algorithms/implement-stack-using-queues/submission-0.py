class MyStack:
    def __init__(self):
        self.arr = deque([])

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        if self.arr:
            return self.arr.pop()
        return None

    def top(self) -> int:
        if self.arr:
            return self.arr[-1]
        return None

    def empty(self) -> bool:
        return not self.arr
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()