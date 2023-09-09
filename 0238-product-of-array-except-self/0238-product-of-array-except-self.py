class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:    
        
        zero_count = len([n for n in nums if n == 0])
        
        prod_of_all_nums = reduce(lambda a, b: a * b, nums)
        
        if zero_count == 0:
            return [prod_of_all_nums // n for n in nums]
        if zero_count == 1:
            prod_of_all_nums_except_zero = reduce(lambda a, b: a * b, [n for n in nums if n != 0])
            return [0 if n != 0 else prod_of_all_nums_except_zero for n in nums]
        if zero_count >= 2:
            return [0 for _ in nums]
            
        