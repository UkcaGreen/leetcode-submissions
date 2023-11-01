class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0] * (n + 1)
        dp_idx = 0
        
        x = 1
        
        for i in range(1, n+1):
            
            if x * 2 == i:
                x = x * 2
                dp_idx = 0
                
            dp[i] = dp[dp_idx] + 1
            
            dp_idx += 1
            
        return dp
            