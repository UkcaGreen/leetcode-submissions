class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter
        
        counts = Counter(nums)
        
        return [e[0] for e in counts.most_common(k)]