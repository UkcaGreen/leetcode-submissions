import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        
        # push
        
        if len(self.left) > 0 and num < self.left[0] * -1:
            
            heapq.heappush(self.left, num * -1)
        
        elif len(self.right) > 0 and num > self.right[0]:
            
            heapq.heappush(self.right, num)
        
        else:
            
            if len(self.right) > len(self.left):
                
                heapq.heappush(self.left, num * -1)
                
            elif len(self.left) > len(self.right):
                
                heapq.heappush(self.right, num)
                
            else:
                
                heapq.heappush(self.left, num * -1)
        
        # adjust
        
        if len(self.right) - len(self.left) == 2:
            
            heapq.heappush(self.left, heapq.heappop(self.right) * -1)
        
        elif len(self.right) - len(self.left) == -2:
            
            heapq.heappush(self.right, heapq.heappop(self.left) * -1)
        

    def findMedian(self) -> float:

        
        if len(self.right) == len(self.left):
            
            return (self.right[0] + self.left[0] * -1) / 2
        
        if len(self.right) > len(self.left):
            
            return self.right[0]
        
        if len(self.right) < len(self.left):
            
            return self.left[0] * -1
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()