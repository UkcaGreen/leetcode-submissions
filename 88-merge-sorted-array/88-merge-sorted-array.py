class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        
        nums1[-len(nums2):] = nums2
        nums1.sort()
            