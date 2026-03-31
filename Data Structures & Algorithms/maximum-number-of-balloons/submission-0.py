class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = []

        target = "balloon"

        for char in target:
            res.append(text.count(char) // target.count(char))
        
        return min(res)