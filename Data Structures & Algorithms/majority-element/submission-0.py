from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans = [x for x in c if c[x]>len(nums)//2]
        return ans[0]
        