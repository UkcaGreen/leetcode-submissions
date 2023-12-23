class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        max_len = 0
        
        for i, _ in enumerate(s):
            
            span = s[0:i+1]
            
            if span == span[::-1]:
                max_len = len(span)
                
        return s[max_len:][::-1] + s
            