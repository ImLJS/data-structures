class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float("inf")
        L,R = 0,0
        cur_sum = 0

        while R<len(nums):
            cur_sum += nums[R]

            while cur_sum >= target:
                if cur_sum >= target:
                    min_size = min(min_size, R-L+1)
                cur_sum-=nums[L]
                L+=1
            R+=1
        return min_size if min_size!=float('inf') else 0