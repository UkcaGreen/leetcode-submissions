class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_lenght = min([len(s) for s in strs])
        
        prefix = ""
        
        for i in range(min_lenght):
            if len(set(s[i] for s in strs)) == 1:
                prefix += strs[0][i]
            else:
                break
        
        return prefix