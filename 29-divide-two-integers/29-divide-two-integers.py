class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        total, count = 0, 0
        
        while abs(dividend) >= total + abs(divisor):
            t, c = abs(divisor), 1
            
            while abs(dividend) >= total + t:
                t <<= 1
                c <<= 1
                
            total += (t >> 1)
            count += (c >> 1)

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            count = -count
            
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        count = max(count, MIN_INT)
        count = min(count, MAX_INT) 
            
        return count