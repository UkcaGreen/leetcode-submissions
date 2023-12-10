class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result = ""
        
        def dp(l, r):
            
            nonlocal result
            
            if l < 0 or r < 0 or l >= len(s) or r >= len(s):
                return
            
            if s[l] != s[r]:
                return
            
            substring = s[l:r+1]
            
            if len(substring) > len(result):
                
                result = substring
            
            dp(l-1, r+1)
            
        for i in range(len(s)):
            dp(i,i)
            
            if i > 0:
                dp(i-1, i)
                
        return result
                