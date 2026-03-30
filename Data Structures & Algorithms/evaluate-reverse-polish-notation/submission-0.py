class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque([])
        mapping = {"+", "-", "*", "/"}

        def operations(num1, nums2, op):
            match op:
                case "+":
                    return num1 + nums2
                case "-":
                    return num1 - nums2
                case "*":
                    return num1 * nums2
                case "/":
                    return int(num1 / nums2)
        
        for n in tokens:
            if n not in mapping:
                stack.append(int(n))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(operations(num1, num2, n))

        return stack[0]