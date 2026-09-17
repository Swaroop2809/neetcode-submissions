class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        profit=0
        for price in prices:
            min_price=min(min_price,price)
            current_profit=price-min_price
            profit=max(profit,current_profit)
        return profit