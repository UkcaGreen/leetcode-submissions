class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        from collections import Counter, defaultdict
        
        target_counts = Counter(t)
        counts = defaultdict(lambda: 0)
        
        is_met = {k: False for k in target_counts}
        
        l, r = 0, 0
        
        ans = " " * int(10e5)
        
        while r <= len(s):
            
            sub_str = s[l:r]
            
            any(counts[k] < target_counts[k] for k in target_counts)
            
            if not all(is_met.values()):
                
                r += 1
                
                if r <= len(s):
                    
                    new_char = s[r-1]
                    
                    counts[new_char] += 1
                    
                    if new_char in target_counts and counts[new_char] >= target_counts[new_char]:
                        is_met[new_char] = True
            else:
                
                if len(sub_str) == 0:
                    continue
                    
                if len(sub_str) < len(ans):
                    ans = sub_str
                    
                old_char = s[l]
                
                counts[old_char] -= 1
                
                if old_char in target_counts and counts[old_char] < target_counts[old_char]:
                    is_met[old_char] = False
                
                l += 1
                
        if ans == " " * int(10e5):
            return ""
                
        return ans
            
