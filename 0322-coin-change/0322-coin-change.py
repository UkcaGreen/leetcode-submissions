class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins = sorted(list(set(coins)), reverse=True)
        
        from functools import cache
        
        @cache
        def dp(i, target):
            
            if target == 0:
                return 0
            
            if i >= len(coins) or target < 0:
                return float("inf")
            
            return min(
                dp(i+1, target),
                dp(i, target - coins[i]) + 1,
            )
            
        ans = dp(0, amount)
            
        return ans if ans != float("inf") else -1