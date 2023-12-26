class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        asteroids = sorted(asteroids)
        
        for a in asteroids:
            
            if a > mass:
                return False
            
            mass += a
            
        return True