from functools import cache

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        
        @cache
        def util(x, y, z):

            assert x < y < z

            if y - 1 == x and y + 1 == z:
                return 0, 0

            mn, mx = float("inf"), -float("inf")
            
            for k in range(x+1,z):
                if k == y:
                    continue

                mn_z, mx_z = util(*sorted([x,y,k]))
                mn_x, mx_x = util(*sorted([k,y,z]))

                mn, mx = min(mn, mn_z, mn_x), max(mx, mx_z, mx_x)

            return mn + 1, mx + 1
        
        return util(*sorted([a, b, c]))



            