class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def dp(l, r):
            
            if l < 0 or r < 0 or l >= len(s) or r >= len(s):
                return 0
            
            if s[l] != s[r]:
                return 0
            
            return dp(l-1, r+1) + 1
            
        odd_ones, even_ones = 0, 0
            
        for i in range(len(s)):
            odd_ones += dp(i,i)
            
            if i > 0:
                odd_ones += dp(i-1, i)
                
        return odd_ones + even_ones