class Solution:
    def reverseWords(self, s: str) -> str:
        
        import re
        
        tokens = [t.strip() for t in re.split(r"\s+", s.strip())]
        
        return " ".join(tokens[::-1])