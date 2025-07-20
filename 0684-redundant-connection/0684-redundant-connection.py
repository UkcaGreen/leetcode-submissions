class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parents = [None] * (len(edges)+1)

        def find_root(n):
            while parents[n]:
                n = parents[n]
            return n
        
        def union(u, v):
            root_u = find_root(u)
            root_v = find_root(v)

            if root_u != root_v:
                parents[root_u] = root_v
                return True
            else:
                return False

        for u, v in edges:
            if not union(u, v):
                return [u, v]