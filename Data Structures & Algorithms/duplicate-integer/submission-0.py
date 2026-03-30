class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        window = set()

        for n in nums:
            if n in window:
                return True
            window.add(n)
        return False