class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for c in s:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1
            
        x = sum([v // 2 for v in counts.values()]) * 2
        
        return x if x == sum(counts.values()) else x + 1
                