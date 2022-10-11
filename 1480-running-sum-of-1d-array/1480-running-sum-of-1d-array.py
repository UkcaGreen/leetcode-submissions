class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sm = 0
        return [sm := sm + n for n in nums]