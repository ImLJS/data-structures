from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = deque([0])
        maxRight = deque([0])
        maxLeftHeight = height[0]
        maxRightHeight = height[-1]
        res = 0

        for i in range(1,len(height)):
            maxLeft.append(maxLeftHeight)
            maxLeftHeight = max(maxLeftHeight, height[i])

        for i in range(len(height)-2,-1,-1):
            maxRight.appendleft(maxRightHeight)
            maxRightHeight = max(maxRightHeight, height[i])

        for i in range(len(height)):
            x = min(maxLeft[i],maxRight[i])-height[i]
            if x>0:
                res+=x
        
        return res
        