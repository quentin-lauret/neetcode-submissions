class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        m = float('inf')
        profit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < m:
                m = prices[i - 1]
            if prices[i] - m > profit:
                profit = prices[i] - m 
        return profit
            