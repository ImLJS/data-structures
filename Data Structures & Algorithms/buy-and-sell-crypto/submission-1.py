class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            cur_profit = prices[i]-buy
            profit = max(profit, cur_profit)
            buy = min(prices[i], buy)
        
        return profit