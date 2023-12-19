class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        short_str = min(str1, str2, key=len)
        
        ans = ""
        
        for i in range(len(short_str)):
            
            slice = short_str[:i+1]
            
            if len(str1) % len(slice) != 0 or len(str2) % len(slice) != 0:
                continue
            
            if slice * int(len(str1) / len(slice)) == str1 and slice * int(len(str2) / len(slice)) == str2:
                ans = slice
        
        return ans
            
            