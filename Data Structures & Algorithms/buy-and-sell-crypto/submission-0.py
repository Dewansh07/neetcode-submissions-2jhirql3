class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxp = 0
        for sell in prices:
            # buy = prices[i]
            if sell<buy:
                buy = sell
            else:
                maxp = max(maxp, sell-buy)
        return maxp

