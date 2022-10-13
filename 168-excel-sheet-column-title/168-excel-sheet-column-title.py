class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        x = columnNumber
        ans = []
        
        while x != 0:
            ans.append((x - 1) % 26)
            x = (x - 1) // 26
            
        if not ans:
            ans = [0]
            
        return "".join([self.int_to_ascii(n) for n in ans[::-1]])
    
    def int_to_ascii(self, n):
        return chr(65 + n)