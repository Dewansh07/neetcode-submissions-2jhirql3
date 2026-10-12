class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = 0
        # r = 1
        # mprofit = 0
        # while r < len(prices):
        #     if prices[r]>prices[l]:
        #         profit = prices[r]- prices[l]
        #         mprofit = max(mprofit, profit)
        #     else:
        #         l = r
        #     r+=1
        # return mprofit
        buy = prices[0]
        profit = 0
        for sell in prices:
            if sell<buy:
                buy = sell
            else:
                profit = max(profit, sell-buy)
        return profit