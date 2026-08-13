class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        maxi = 0
        l, r = 0, 1

        while l < r and r < len(prices):
            profit = prices[r] - prices[l]
            maxi = max(maxi, profit)

            if prices[r] < prices[l]:
                l = r
                r += 1

            else:
                r += 1

        return maxi