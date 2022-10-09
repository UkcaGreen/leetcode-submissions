class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        itr = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            
            nums[itr] = nums[i]
            itr += 1
        
        return itr