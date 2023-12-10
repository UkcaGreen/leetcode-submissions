class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        from functools import cache
        
        @cache
        def dp(rest):
            
            if rest == "":
                return True
            
            result = False
            
            for w in wordDict:
            
                if rest.startswith(w):
                    result = result or dp(rest[len(w):])
            
            return result
        
        return dp(s)
            