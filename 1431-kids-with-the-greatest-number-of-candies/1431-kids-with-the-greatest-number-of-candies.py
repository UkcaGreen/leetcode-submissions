class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        return [max(candies) <= c + extraCandies for c in candies]