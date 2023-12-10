class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        from functools import cache
        
        @cache
        def foo(i):
            
            if i >= len(nums) - 1:
                return True
            
            if nums[i] == 0:
                return False
            
            return any(foo(i + x + 1) for x in reversed(range(nums[i])))
        
        return foo(0)
                