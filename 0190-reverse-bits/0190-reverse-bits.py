class Solution:
    def reverseBits(self, n: int) -> int:
        
        ans, i = 0, 0
        
        for i in range(32):
            
            digit = n & 1
            
            n = n >> 1
            ans = ans << 1
            
            ans |= digit
            

            
        return ans