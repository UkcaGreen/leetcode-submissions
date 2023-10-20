class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        minimum = float("inf")
        
        for p in prices:
            
            minimum = min(minimum, p)
            
            profit = max(p - minimum, profit)
        
        return profit
            
            
            