class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        numbers = [ord(c) - 64 for c in columnTitle][::-1]
        
        return sum(n * pow(26, i) for i, n in enumerate(numbers))