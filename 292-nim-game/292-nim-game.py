class Solution:
    def canWinNim(self, n: int) -> bool:
        return int(bin(n)[2:][-2:])