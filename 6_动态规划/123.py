class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0

        for price in prices:
            new_buy1 = max(buy1, -price)
            new_sell1 = max(sell1, buy1 + price)
            new_buy2 = max(buy2, sell1 - price)
            new_sell2 = max(sell2, buy2 + price)
            
            buy1 = new_buy1
            sell1 = new_sell1
            buy2 = new_buy2
            sell2 = new_sell2
        
        return sell2