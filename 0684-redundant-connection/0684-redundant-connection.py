class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        d = {}

        for u, v in edges:

            if u not in d:
                d[u] = {u}

            if v not in d:
                d[v] = {v}
            
            if d[v] != d[u]:
                merged_set = d[v] | d[u]
                k_to_update = [k for k in d if d[k] == d[v] or d[k] == d[u]]
                for k in k_to_update:
                    d[k] = merged_set

            else:
                return [u, v]

        return [0, 0]