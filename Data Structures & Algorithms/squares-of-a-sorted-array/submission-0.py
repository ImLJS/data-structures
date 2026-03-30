class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [x**2 for x in nums]
        return sorted(arr)