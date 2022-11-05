class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        reversed_vowel_generator = (c for c in s[::-1] if c in vowels)
        chars = list(s)
        
        for i in range(len(chars)):
            if chars[i] in vowels:
                chars[i] = next(reversed_vowel_generator)
        
        return "".join(chars)