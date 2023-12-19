class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        ans = ""
        
        for i, c in enumerate(word1):
            
            ans += c
            
            if i < len(word2):
                ans += word2[i]
        
        if i+1 < len(word2):
            ans += word2[i+1:]
            
        return ans
                