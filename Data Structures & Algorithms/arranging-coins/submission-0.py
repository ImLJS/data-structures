class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 1
        res = 0

        while n-start>=0:
            res+=1
            n-=start
            start+=1
        
        return res