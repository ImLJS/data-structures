from collections import deque
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0]*len(temp)
        stack = deque([]) # [(temp, index)]

        for index, val in enumerate(temp):
            while stack and val > stack[-1][0]:
                temp, idx = stack.pop()
                res[idx] = index-idx
            stack.append((val, index))
        return res
        