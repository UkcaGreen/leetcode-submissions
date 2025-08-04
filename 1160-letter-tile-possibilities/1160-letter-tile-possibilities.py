class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        counts = {c:0 for c in tiles}
        for c in tiles:
            counts[c] += 1

        ans = set()

        def bt(remaining_counts, curr_str):

            nonlocal ans

            if all(v == 0 for v in remaining_counts.values()):
                if curr_str:
                    ans.add(curr_str)
                return
            
            for c in set(remaining_counts):
                if remaining_counts[c] > 0:
                    remaining_counts[c] -= 1
                    bt(remaining_counts.copy(), curr_str + c)
                    bt(remaining_counts.copy(), curr_str)
                    remaining_counts[c] += 1

        bt(counts, "")

        return len(ans)