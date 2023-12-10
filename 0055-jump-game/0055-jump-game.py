class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        horizon = 0
        i = 0
        
        while horizon >= i:
            
            horizon = max(horizon, i+nums[i])
            
            if horizon >= len(nums) - 1:
                return True
            
            i += 1
        
        return False