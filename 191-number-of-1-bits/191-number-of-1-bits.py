class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(int(n) for n in list(bin(n)[2:]))