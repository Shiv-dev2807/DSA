class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prev = max(prices)
        m = 0
        i = 0
        while  i< len(prices):
            if min_prev > prices[i]:
                min_prev = prices[i]
            
            a = prices[i] - min_prev
            
            if m == 0:
                m = a
            else:
                if m < a:
                    m = a
            i+=1
        
        return(m)