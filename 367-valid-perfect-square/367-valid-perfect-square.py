class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        l, r = 0, num//2
        
        while r >= l:
            
            mid = (l + r) // 2
            square = mid*mid
            
            if num == square:
                return True
            if num > square:
                l = mid + 1
            if num < square:
                r = mid - 1
        
        return False
            