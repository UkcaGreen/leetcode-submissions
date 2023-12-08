class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        count = 0
        
        def mark_island(r, c):
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            
            if grid[r][c] != "1":
                return

            if (r, c) in visited:
                return
            
            visited.add((r, c))
            
            mark_island(r+1, c)
            mark_island(r-1, c)
            mark_island(r, c+1)
            mark_island(r, c-1)
            
        for r in range(ROWS):
            for c in range(COLS):
                
                if (r, c) not in visited and grid[r][c] == "1":
                    mark_island(r, c)
                    count += 1
                    
        return count