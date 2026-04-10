from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        target = len(nums)//3
        return [x for x in freq if freq[x]>target]