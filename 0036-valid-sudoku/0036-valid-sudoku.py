class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        return self.check_cols(board) and self.check_rows(board) and self.check_boxes(board)
    
    def check_boxes(self, board):
        
        seen_dict = {(i,j):set() for i in range(3) for j in range(3)}
        
        for i in range(9):
            
            for j in range(9):

                if board[j][i] == ".":
                    continue

                if board[j][i] in seen_dict[(i//3,j//3)]:
                    return False
                
                seen_dict[(i//3,j//3)].add(board[j][i])
            
        return True
    
    def check_cols(self, board):
        
        for i in range(9):
            
            seen = set()
            
            for j in range(9):

                if board[j][i] == ".":
                    continue

                if board[j][i] in seen:
                    return False
                
                seen.add(board[j][i])
            
        return True
    
    def check_rows(self, board):
        
        for i in range(9):
            
            seen = set()
            
            for j in range(9):

                if board[i][j] == ".":
                    continue

                if board[i][j] in seen:
                    return False
                
                seen.add(board[i][j])
            
        return True