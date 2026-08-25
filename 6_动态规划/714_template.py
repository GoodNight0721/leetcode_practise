class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]
        for price in prices[1:]:
            new_cash = max(cash, hold + price - fee)
            new_hold = max(hold, cash - price)

            cash = new_cash
            hold = new_hold
        
        return cash


