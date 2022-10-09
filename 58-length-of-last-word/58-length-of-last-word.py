class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tokens = s.split()
        if not tokens:
            return 0
        return len(tokens[-1])
            