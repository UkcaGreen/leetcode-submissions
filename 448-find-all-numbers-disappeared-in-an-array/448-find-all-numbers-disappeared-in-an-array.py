class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(list(range(1,len(nums) + 1))).difference(set(nums))