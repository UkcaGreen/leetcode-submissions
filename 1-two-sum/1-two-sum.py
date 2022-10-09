class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wanted = {}
        for i, num in enumerate(nums):
            if num in wanted:
                return i, wanted[num]
            wanted[target-num] = i