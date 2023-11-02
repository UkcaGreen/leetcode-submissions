class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            is_all_sorted = nums[l] <= nums[r]
            is_left_sorted = nums[l] <= nums[m]
            is_right_sorted = nums[r] >= nums[m]
            
            if is_all_sorted:
                
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            
            elif is_left_sorted:
                
                if nums[m] > target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
                    
            elif is_right_sorted:
                
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return l if l == r and nums[l] == target else -1
                    
                    
                    
                    