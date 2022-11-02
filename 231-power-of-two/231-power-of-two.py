class Solution:
    def isPowerOfTwo(self, n: int) -> bool:    
        return any(n == (1 << i) for i in range(32))