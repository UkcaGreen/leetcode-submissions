class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import Counter, defaultdict
        
        groups = defaultdict(lambda: [])
        
        for s in strs:
            
            char_counts = [0] * 26
            
            for c in s:
                
                idx = ord(c) - ord("a")
        
                char_counts[idx] += 1
            
            groups[tuple(char_counts)].append(s)
        
        return groups.values()
            