class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        from functools import cache
        
        @cache
        def dfs(i):
            
            if i >= len(nums):
                return 0
            
            result = 1
            
            for x in range(i+1, len(nums)):
                
                if nums[x] > nums[i]:
                    result = max(result, dfs(x) + 1)
            
            return result
        
        return max(dfs(i) for i in range(len(nums)))
                
        
        