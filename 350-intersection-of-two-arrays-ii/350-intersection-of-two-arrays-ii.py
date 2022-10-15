class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        counts = {n: min(nums1.count(n), nums2.count(n)) for n in set(nums1)}
        
        elements = [[n] * counts[n] for n in counts]
            
        return [
            e 
            for sublist in elements
            for e in sublist
       ]