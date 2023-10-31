class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        from collections import Counter, defaultdict
        
        target_counts = Counter(t)
        
        counts = defaultdict(lambda: 0)
        
        l, r = 0, 0
        
        ans = " " * int(10e5)
        
        while r <= len(s):
            
            sub_str = s[l:r]
            
            if any(counts[k] < target_counts[k] for k in target_counts):
                
                r += 1
                
                if r <= len(s):
                    counts[s[r-1]] += 1
            else:
                
                if len(sub_str) == 0:
                    continue
                    
                if len(sub_str) < len(ans):
                    ans = sub_str
                
                counts[s[l]] -= 1
                l += 1
                
        if ans == " " * int(10e5):
            return ""
                
        return ans
            
