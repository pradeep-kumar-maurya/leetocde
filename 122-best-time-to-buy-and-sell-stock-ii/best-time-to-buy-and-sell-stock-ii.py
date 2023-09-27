class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_stock = [0] * len(prices)
        sum = 0

        for i in range(len(prices)-1, -1, -1):
            if i == len(prices)-1:
                max_stock[i] = prices[i]
            elif prices[i] >= prices[i + 1]:
                max_stock[i] = prices[i]
            elif prices[i] < prices[i + 1]:
                max_stock[i] = prices[i + 1]

        for i in range(len(prices)):
            sum += max_stock[i] - prices[i]

        return sum
