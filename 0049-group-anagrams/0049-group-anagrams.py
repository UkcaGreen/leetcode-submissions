class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import Counter, defaultdict
        
        groups = defaultdict(lambda: [])
        
        
        for s in strs:
            
            groups[tuple(sorted(Counter(s).items()))].append(s)
            
        
        return groups.values()
            