class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        itr = 1
        
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[itr] = nums[i+1]
                itr += 1
        
        return itr
        