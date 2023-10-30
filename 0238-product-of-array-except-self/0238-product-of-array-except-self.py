class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:    
        
        from functools import reduce

        zero_count = nums.count(0)
        
        if zero_count > 1:
            return [0 for n in nums]
        
        non_zero_nums = [n for n in nums if n != 0]
        
        non_zero_product = 1
        
        for n in non_zero_nums:
            non_zero_product *= n
        
        if zero_count == 1:
            return [0 if n != 0 else non_zero_product for n in nums]
        
        return [non_zero_product // n for n in nums]
    

            
        