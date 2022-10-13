class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        
        prev = None
        for i in range(rowIndex + 1):
            if not prev:
                row = [1]
            else:
                row = [1] + [prev[i] + prev[i+1] for i in range(len(prev) - 1)] + [1]
                
            prev = row
                    
            ans.append(row)
        
        return ans[-1]