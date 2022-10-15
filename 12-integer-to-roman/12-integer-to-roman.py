class Solution:
    def intToRoman(self, num: int) -> str:
        int2roman = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M" 
        }
        
        ans = ""
        
        for n in sorted(int2roman.keys(), reverse=True):
            ans += int2roman[n] * (num // n)
            num = num % n
        
        ans = ans.replace("VIIII", "IX")
        ans = ans.replace("IIII", "IV")
        ans = ans.replace("LXXXX", "XC")
        ans = ans.replace("XXXX", "XL")
        ans = ans.replace("DCCCC", "CM")
        ans = ans.replace("CCCC", "CD")
            
        return ans