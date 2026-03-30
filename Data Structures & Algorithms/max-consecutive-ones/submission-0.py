class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        R = 0
        max_window = 0
        window = []

        while R < len(nums):
            if nums[R] == 1:
                window.append(1)
                max_window = max(max_window, len(window))
            else:
                window = []
            R+=1
        return max_window