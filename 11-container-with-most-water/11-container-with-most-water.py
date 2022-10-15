class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        
        mx = -float("inf")
        while l < r:
            
            mx = max(mx, min(height[l], height[r]) * (r - l))
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return mx
        
            