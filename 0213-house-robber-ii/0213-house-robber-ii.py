class Solution:
    def rob(self, nums: List[int]) -> int:
        
        from functools import cache
        
        @cache
        def dfs(house_idx, is_first_one_robbed, is_prev_robbed=False):
            
            if house_idx == len(nums):
                return 0
        
            if house_idx == 0:
                return max(
                    dfs(house_idx + 1, True, True) + nums[house_idx],
                    dfs(house_idx + 1, False, False),
                )
            
            if house_idx == len(nums) - 1:
                
                if is_first_one_robbed:
                    return 0
                
                if is_prev_robbed:
                    return dfs(house_idx + 1, is_first_one_robbed, False)
                else:
                    return max(
                        dfs(house_idx + 1, is_first_one_robbed, True) + nums[house_idx],
                        dfs(house_idx + 1, is_first_one_robbed, False),
                    )
                    
            
            if is_prev_robbed:
                return dfs(house_idx + 1, is_first_one_robbed, False)
            else:
                return max(
                    dfs(house_idx + 1, is_first_one_robbed, True) + nums[house_idx],
                    dfs(house_idx + 1, is_first_one_robbed, False),
                )
            
        return dfs(0, None)