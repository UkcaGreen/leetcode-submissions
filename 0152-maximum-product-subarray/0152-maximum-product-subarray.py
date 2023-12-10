class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ans = max(nums)
        
        mx, mn = 1, 1
        
        for n in nums:
            
            if n == 0:
                mx, mn = 1, 1
                continue
            
            mx, mn = max(mx * n, mn * n, n), min(mx * n, mn * n, n)
            
            ans = max(ans, mx)
            
        return ans