class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        for i in prices:
            if i < min_price:
                min_price = i
            profit = i - min_price
            max_profit = max(max_profit,profit)
        return max_profit 