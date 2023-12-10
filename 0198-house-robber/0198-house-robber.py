class Solution:
    def rob(self, nums: List[int]) -> int:
        
        from functools import cache
        
        @cache
        def dfs(house_idx, is_prev_robbed=False):
            
            if house_idx == len(nums):
                return 0
            
            if is_prev_robbed:
                return dfs(house_idx + 1, False)
            else:
                return max(
                    dfs(house_idx + 1, True) + nums[house_idx],
                    dfs(house_idx + 1, False),
                )
            
        return dfs(0)