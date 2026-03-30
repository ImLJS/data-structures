class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        mapping = { 0: 1 }

        for n in nums:
            curSum+=n
            diff = curSum - k
            res += mapping.get(diff, 0)
            mapping[curSum] = 1 + mapping.get(curSum, 0)

        return res 