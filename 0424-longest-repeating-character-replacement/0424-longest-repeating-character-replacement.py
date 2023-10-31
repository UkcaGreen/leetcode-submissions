class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counts = {chr(ord("A") + i): 0 for i in range(26)}
        
        l, r, longest = 0, 0, 0
        
        while r <= len(s):
            
            if k + max(counts.values()) >= len(s[l:r]):
                
                longest = max(len(s[l:r]), longest)
                
                r += 1
                
                if r <= len(s):
                    counts[s[r-1]] += 1
                
            else:
                
                if l <= r and l < len(s):
                    counts[s[l]] -= 1
                
                l += 1

                
        return longest