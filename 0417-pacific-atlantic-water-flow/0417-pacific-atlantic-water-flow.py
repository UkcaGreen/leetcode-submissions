class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        
        def dfs(r, c, prev, visited):
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            
            if (r, c) in visited:
                return
            
            if heights[r][c] < prev:
                return
            
            visited.add((r,c))
            
            dfs(r+1, c, heights[r][c], visited)
            dfs(r-1, c, heights[r][c], visited)
            dfs(r, c+1, heights[r][c], visited)
            dfs(r, c-1, heights[r][c], visited)
            
        visited_pasific, visited_atlantic = set(), set()
        
        for r in range(ROWS):
            for c in range(COLS):
            
                if r == 0 or c == 0:
                    dfs(r, c, 0, visited_pasific)
            
                if r == ROWS-1 or c == COLS-1:
                    dfs(r, c, 0, visited_atlantic)
        
        return visited_pasific.intersection(visited_atlantic)
        
            
            