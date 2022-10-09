class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(str(x)[::-1])
        return str(x)[::-1] == str(x)