class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [e for e in set(nums1) if min(nums1.count(e), nums2.count(e)) > 0]