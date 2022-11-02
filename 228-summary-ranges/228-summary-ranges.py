class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ans = [{nums[0]}]
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                ans[-1].add(nums[i+1])
            else:
                ans.append({nums[i+1]})
                
        return [f"{min(e)}->{max(e)}" if len(e) > 1 else f"{max(e)}" for e in ans]