class Solution:
    def reverseBits(self, n: int) -> int:
        
        ans, i = 0, 0
        
        while n > 0 or i < 32:
            
            digit = n % 2
            
            n = n >> 1
            ans = ans << 1
            
            ans += digit
            i += 1
            

            
        return ans