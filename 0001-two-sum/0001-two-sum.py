class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        wanted = set()
        
        for i, n in enumerate(nums):
            
            if n in wanted:
                return [nums.index(target - n), i]
            
            wanted.add(target - n)