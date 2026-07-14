class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 #buy
        maxP = 0
        right = 1 #sell
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit) # compare max profit and current profit
            else:
                left = right # update our buying position to this new price
            right += 1
        return maxP

            


        