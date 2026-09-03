class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxDiff = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxDiff:
                maxDiff = price - minPrice
        return maxDiff