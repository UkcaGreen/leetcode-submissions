class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        loc = {}
        
        ans = 0
        l = 0

        for r in range(len(s)):
            if s[r] in loc:
                l = max(l, loc[s[r]] + 1)
            loc[s[r]] = r
            
            ans = max(ans, r-l+1)
        
        return ans
                
