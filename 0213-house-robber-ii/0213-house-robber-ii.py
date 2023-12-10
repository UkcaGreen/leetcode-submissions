class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        from functools import cache
        
        @cache
        def dfs(house_idx, last_idx, is_prev_robbed=False):
            
            if house_idx == last_idx + 1:
                return 0
            
            if is_prev_robbed:
                return dfs(house_idx + 1, last_idx, False)
            else:
                return max(
                    dfs(house_idx + 1, last_idx, True) + nums[house_idx],
                    dfs(house_idx + 1, last_idx, False),
                )
            
        return max(
            dfs(1, len(nums) - 1),
            dfs(0, len(nums) - 2),
        )