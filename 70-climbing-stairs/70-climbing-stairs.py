class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def util(remaining_steps):
            if remaining_steps == 0 or remaining_steps == 1:
                return 1
            else:
                return util(remaining_steps - 2) + util(remaining_steps - 1)
            
        return util(n)