class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        return descending[2] if len(descending := sorted(set(nums), reverse=True)) >= 3 else descending[0]