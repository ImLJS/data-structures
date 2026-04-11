class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, cur_sum = 0,0
        min_size = float("inf")

        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_size = min(min_size, right-left+1)
                cur_sum-=nums[left]
                left+=1
            
        return min_size if min_size!=float("inf") else 0