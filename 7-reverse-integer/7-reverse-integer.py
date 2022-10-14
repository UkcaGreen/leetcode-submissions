class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        sign = x // abs(x)
        magnitude = int(str(abs(x)).strip("0")[::-1])
        
        mn, mx = -pow(2, 31), pow(2, 31) - 1
        
        if mn <= sign * magnitude <= mx:
            return sign * magnitude
        
        return 0
        