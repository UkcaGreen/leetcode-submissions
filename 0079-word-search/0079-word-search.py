class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        visited = set()
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r, c, i):
        
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return False
            
            if board[r][c] != word[i]:
                return False
            
            if (r, c) in visited:
                return False
            
            visited.add((r, c))
            
            for row_offset, col_offset in directions:
                
                if dfs(r+row_offset, c+col_offset, i+1):
                    return True
                
            visited.remove((r, c))

        return any(
            dfs(r, c, 0)
            for r in range(len(board))
            for c in range(len(board[0]))
        )