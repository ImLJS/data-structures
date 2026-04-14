class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res = 0
        left = 0
        curSum, maxSum = 0, 0
        grumpVal = []
        
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res+=customers[i]
            
        satisfied = res

        for i in range(len(customers)-minutes+1):
            cur = 0
            for j in range(i, i+minutes):
                if grumpy[j]:
                    cur+=customers[j]
            
            res = max(res, satisfied+cur)
        
        return res
            

        
