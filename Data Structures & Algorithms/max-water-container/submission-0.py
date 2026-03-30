class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights)-1
        maxWater = 0

        while L < R:
            maxWater = max(maxWater, min(heights[L],heights[R])*(R-L))
            if heights[L]<=heights[R]:
                L+=1
            else:
                R-=1
        
        return maxWater