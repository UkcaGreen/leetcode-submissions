class Solution:
    def climbStairs(self, n: int) -> int:
        
        from functools import cache
        
        @cache
        def dfs(rest):
            
            if rest < 0:
                return 0
            
            if rest == 0:
                return 1
                
            return dfs(rest-1) + dfs(rest-2)
        
        return dfs(n)