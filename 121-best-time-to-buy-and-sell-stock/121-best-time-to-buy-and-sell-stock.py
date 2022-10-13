class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        mx_list = [mx := max(mx, e) for e in reversed(prices)][::-1]
        
        mn = float("inf")
        mn_list = [mn := min(mn, e) for e in prices]
        
        profits = [mx_list[i] - mn_list[i] for i in range(len(prices))]
        
        return max(profits)
            