class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [-prices[0]] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            new_buy = buy.copy()
            new_sell = sell.copy()
            for i in range(1, k + 1):
                new_buy[i] = max(buy[i], sell[i - 1] - price)
                new_sell[i] = max(sell[i], buy[i] + price)

                buy = new_buy
                sell = new_sell
        
        return sell[-1]