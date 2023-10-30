class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        
        max_water_amount = 0
        
        while l < r:
            
            water_amount = (r - l) * min(height[l], height[r]) 
            max_water_amount = max(max_water_amount, water_amount)
            
            if height[l] < height[r]:
                l = l+1
            else:
                r = r-1
        
        return max_water_amount
        