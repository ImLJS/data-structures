class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquare(n):
            return sum([int(x)**2 for x in str(n)])
        
        memo = set([n])

        while True:
            n = sumSquare(n)

            if n == 1:
                return True
            
            if n in memo:
                return False
            
            memo.add(n)