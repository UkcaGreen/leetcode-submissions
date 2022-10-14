class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = -1 if s and s[0] == "-" else 1
        s = s[1:] if s and s[0] in ["+", "-"] else s
        
        magnitude = ""
        for c in s:
            if c.isnumeric():
                magnitude += c
            else:
                break
        magnitude = int(magnitude) if magnitude else 0
        
        if -pow(2,31) > sign * magnitude:
            return -pow(2,31)
        if sign * magnitude > pow(2,31) - 1:
            return pow(2,31) - 1
        
        return sign * magnitude