class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        l, r, max_range = 0, 0, 1
        
        while r < len(s) - 1:
            
            if s[r + 1] not in s[l:r + 1]:
                r += 1
                max_range = max(max_range, r + 1 - l)
            else:
                l += 1
        
        return max_range
                
            