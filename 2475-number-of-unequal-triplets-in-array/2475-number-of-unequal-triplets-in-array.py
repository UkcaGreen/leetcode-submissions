class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        
        ans = 0
        
        for i, ni in enumerate(nums):
            for j, nj in enumerate(nums):
                for k, nk in enumerate(nums):
                    if i < j < k and ni != nj and nj != nk and nk != ni:
                        ans += 1
        
        return ans
                        
                    
                        
        