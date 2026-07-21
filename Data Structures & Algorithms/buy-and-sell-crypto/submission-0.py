class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        res = 0 

        for i in range(length):
            price_bought = prices[i]
            for j in range(i+1, length):
                price_sold = prices[j]
                profit = price_sold - price_bought 
                if profit < 1:
                    continue 
                else:
                    res = max(res, profit)
            
        return res
                

        