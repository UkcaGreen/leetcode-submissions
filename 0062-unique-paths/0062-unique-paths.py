class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        from functools import cache
        
        ROWS, COLS = m, n
        
        @cache
        def dfs(r, c):
            
            if r >= ROWS or c >= COLS:
                return 0
            
            if r == ROWS-1 and c == COLS-1:
                return 1
            
            return dfs(r+1, c) + dfs(r, c+1)
        
        return dfs(0, 0)