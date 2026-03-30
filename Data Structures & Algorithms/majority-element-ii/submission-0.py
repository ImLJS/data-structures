class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mapping = Counter(nums)
        major = len(nums)//3

        res = [x for x in mapping if mapping[x]>major]

        return res