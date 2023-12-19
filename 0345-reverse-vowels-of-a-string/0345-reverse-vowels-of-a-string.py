class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vovels = "aeiouAEIOU"
        stack = []
        ans = ""
        
        for c in s:
            
            if c in vovels:
                stack.append(c)
        
        for c in s:
            
            if c in vovels:
                ans += stack.pop()
            else:
                ans += c
        
        return ans
            