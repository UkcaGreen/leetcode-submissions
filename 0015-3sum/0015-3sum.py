class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        nums = sorted(nums)
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                
                if nums[l] + nums[r] > -nums[i]:
                    r -= 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    ans.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    l += 1
        
        return ans
                