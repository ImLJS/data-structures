class MyQueue:

    def __init__(self):
        self.arr = deque([])

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        if self.arr:
            return self.arr.popleft()
        else:
            return -1
            
    def peek(self) -> int:
        if self.arr:
            return self.arr[0]
        else:
            return -1

    def empty(self) -> bool:
        return not self.arr
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()