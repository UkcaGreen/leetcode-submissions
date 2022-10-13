class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = []
        
        prev = None
        for i in range(numRows):
            if not prev:
                row = [1]
            else:
                row = [1] + [prev[i] + prev[i+1] for i in range(len(prev) - 1)] + [1]
                
            prev = row
                    
            ans.append(row)
        
        return ans