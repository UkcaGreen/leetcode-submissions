class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0
        
        for i in range(len(flowerbed)):
            
            span = flowerbed[max(i-1, 0):i+2]
            
            if 1 not in span:
                flowerbed[i] = 1
                count += 1
        
        return count >= n