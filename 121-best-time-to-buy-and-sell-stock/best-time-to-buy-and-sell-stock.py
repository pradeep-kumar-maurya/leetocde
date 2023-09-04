class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ele = prices[len(prices)-1]
        max_stock_price = 0

        for i in range(len(prices)-1, -1, -1):
            if prices[i] >= max_ele:
                max_ele = prices[i]

            stock_price = max_ele - prices[i]

            if stock_price >= max_stock_price:
                max_stock_price = stock_price

        return max_stock_price
