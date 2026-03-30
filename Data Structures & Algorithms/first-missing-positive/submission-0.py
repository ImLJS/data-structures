class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mapping = Counter(nums)

        i = 1
        while True:
            if i not in mapping:
                return i
            i+=1
        