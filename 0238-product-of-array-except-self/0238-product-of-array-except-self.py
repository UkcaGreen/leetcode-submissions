class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:    
        
        from collections import Counter
        from functools import reduce
        
        count = Counter(nums)
        
        if count[0] >= 2:
            return [0] * len(nums)
        
        product_of_non_zero_elements = reduce(lambda x, y: x * y, [e for e in nums if e != 0])
        
        if count[0] == 1:
            return [0 if e != 0 else product_of_non_zero_elements for e in nums ]
        
        if count[0] == 0:        
            return [product_of_non_zero_elements // e for e in nums]

    

            
        