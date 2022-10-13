class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx, local_mx = -float("inf"), 0
        
        for i in range(len(nums)):
            local_mx = max(nums[i], local_mx + nums[i])
            mx = max(local_mx, mx)
            
        return mx