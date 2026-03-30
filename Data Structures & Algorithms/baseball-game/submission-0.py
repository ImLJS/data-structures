class Solution:
    def calPoints(self, op: List[str]) -> int:
        stack = []

        for value in op:
            if value == '+':
                stack.append(stack[-1]+stack[-2])
            elif value == 'D':
                stack.append(stack[-1]*2)
            elif value == 'C':
                stack.pop()
            else:
                stack.append(int(value))
        
        return sum(stack)