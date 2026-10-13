class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP    
        # the 2 pointer approach -  we know/keep or assume l at low initially , and only update l if some values is lower the prices[l] means finding a better price as well as we keep the best/max profit updated/saved
        