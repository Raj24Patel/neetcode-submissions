class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 

        maxprice = 0

        for r in range(1, len(prices)): #6
            if prices[l] < prices[r]:
                price = prices[r] - prices[l]
                maxprice = max(maxprice, price)
            else:
                l = r


        return maxprice
        