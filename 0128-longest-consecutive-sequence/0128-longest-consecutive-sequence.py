class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(list(set(nums)))
        
        mx = float("-inf")
        
        count = 1
        
        for i in range(1, len(nums)):
            
            if nums[i] - nums[i-1] == 1:
                count += 1
            else:
                mx = max(mx, count)
                count = 1
        
        return max(mx, count)
        
        