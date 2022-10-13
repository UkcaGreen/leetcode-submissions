class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lines = [[] for _ in range(numRows)]
        
        i = 0
        update = 1
        for c in s:
            if i <= 0:
                update = 1
            if i >= numRows - 1:
                update = -1
            
            lines[i].append(c)
            
            i += update
            
        
        return ''.join([''.join(l) for l in lines])