class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        no_zero = [n for n in nums if n != 0]
        zeros = [0] * (len(nums) - len(no_zero))
        ans = no_zero + zeros
        for i in range(len(nums)):
            nums[i] = ans[i]