class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        The idea is that, the max profit would be achieved if prices[i] > prices[i-1].
        Therefore, we just sum the differences whenever prices[i] > prices[i-1].
        """
        max_profit = 0
        for i in range(1, len(prices), 1):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
