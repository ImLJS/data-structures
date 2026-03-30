class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for index, val in enumerate(nums):
            diff = target - val

            if diff in dic:
                ans = [index, dic[diff]]
                ans.sort()
                return ans

            dic[val] = index

