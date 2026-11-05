# 122. Best Time to Buy and Sell Stock II
# Medium
# Topics
# premium lock icon
# Companies
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.
#
# Find and return the maximum profit you can achieve.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        max = 0

        for price in prices:
            if price < low:
                low = price
            current = price - low

            if current > max:
                max = current

        return max
