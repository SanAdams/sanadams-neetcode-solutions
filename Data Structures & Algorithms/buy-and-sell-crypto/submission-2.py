class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = len(prices) - 1
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = prices[j] - prices[i]
                print(j,i)
                max_profit = max(profit, max_profit)

        return max_profit