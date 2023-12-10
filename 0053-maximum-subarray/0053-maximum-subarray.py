class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        mx = -float("inf")
        sm = 0
        
        for n in nums:
    
            if sm < 0:
                sm = 0
    
            sm += n
            
            mx = max(mx, sm)
        
        return mx