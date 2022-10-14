class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        
        while n not in visited:
            visited.add(n)
            n = sum(pow(int(n), 2) for n in list(str(n)))
            
        return n == 1