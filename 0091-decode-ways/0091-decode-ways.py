class Solution:
    def numDecodings(self, s: str) -> int:
        
        from functools import cache
        
        valid_patterns = {str(n) for n in range(1, 27)}
        
        @cache
        def dp(i):
            
            if i > len(s):
                return 0
            
            if i == len(s):
                return 1
            
            result = 0
            
            if s[i:i+1] in valid_patterns:
                result += dp(i+1)
            
            if s[i:i+2] in valid_patterns:
                result += dp(i+2)
            
            return result
        
        return dp(0)
                