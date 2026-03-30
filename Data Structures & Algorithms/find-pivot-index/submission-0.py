from collections import deque
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixLeft = deque([])
        prefixRight = deque([])

        total = 0
        for n in nums:
            total+=n
            prefixLeft.append(total)
        
        total = 0

        for i in range(len(nums)-1, -1, -1):
            total+=nums[i]
            prefixRight.appendleft(total)

        for i in range(len(nums)):
            if prefixLeft[i] == prefixRight[i]:
                return i
        
        return -1