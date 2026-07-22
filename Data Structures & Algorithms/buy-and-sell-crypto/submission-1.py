class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = prices[0]

        for n in prices:
            if n < left:
                left = n
            profit = max(profit, n - left)
            
        return profit