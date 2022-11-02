class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        tokens = s.split()
        
        if len(tokens) != len(pattern):
            return False
        
        for i, e in enumerate(pattern):
            if e not in d:
                if tokens[i] in d.values():
                    return False
                d[e] = tokens[i]
            elif d[e] != tokens[i]:
                return False
        
        return True